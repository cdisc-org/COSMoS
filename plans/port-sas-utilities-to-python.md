# Port `utilities/*.sas` to Python

## Context

COSMoS currently validates and converts curation Excel spreadsheets into per-record YAML
(`curation/packageNN/*.xlsx` → `yaml/<release>/{bc,sdtm,crf}/*.yaml`) using 27 SAS files (~7,100
lines) under `utilities/`. This SAS toolchain requires a Windows SAS installation with SAS/ACCESS to
PC Files, a Python-via-MAS bridge for embedded NCIt lookups, and hand-edited comment blocks in the
driver scripts for every new release — none of which is portable or maintainable long-term, and none
of it has any test coverage. The goal is a full, faithful Python port of this entire pipeline (drivers,
macros, and the reference-data-refresh utilities) that fits this repo's existing `scripts/` conventions,
so future releases can be converted/validated without SAS at all.

Decisions already made with the user:
- **Scope**: port everything — all 9 top-level drivers, all 17 macros, including DHT/draft variants,
  `convert_latest_xlsx2yaml.sas`, the 3 reference-data-refresh utilities, and the JSON round-trip macros.
- **Live API calls** (NCI EVS + CDISC Library): replicate them, with local caching so a conversion run
  doesn't hit the network per-row.
- **Issue reporting**: a structured CSV/XLSX issues file (same columns as the SAS `*_ISSUE` templates)
  plus a console severity-count summary — not a full HTML+Excel report replica.
- **Manifest layer**: adopt a small YAML manifest per release/domain as the single source of truth for
  which workbook/range/package params to convert, shared by converters and validators (replacing the
  SAS pattern of hand-edited comment blocks duplicated across driver and validator scripts).
- **Known SAS bugs**: fix the CRF `completionIinstructions` field-name typo and the
  `convert_crf_xlsx2yaml.sas` `&folder.2` output-path bug; preserve the SDTM `comparator=""`
  auto-clearing side effect exactly (it's load-bearing for golden-file fidelity).

## Architecture

### New shared package: `scripts/cosmoslib/`

```
scripts/cosmoslib/
  manifest.py            # release manifest schema + loader (see Manifests below)
  excel_reader.py        # named-range xlsx reading (replaces readexcel.sas + get_excel_sheets.sas)
  yaml_writer.py          # hand-rolled ordered YAML line emitter (see YAML fidelity below)
  issues.py                # IssueLog accumulator + CSV/XLSX writer + severity summary
  templates.py              # BC/SDTM/CRF issue-record column schemas (replaces create_template.sas)
  naming.py                  # output filename/path helpers, release-folder conventions
  enums.py                    # LinkML enum lookup via linkml_runtime.SchemaView
  cdisc_library_cache.py        # codelist/term lookup cache wrapping CDISCLibraryClient
  ncievs_cache.py                 # NCI EVS lookup cache, extends scripts/ncievs_client.py
  relations_cache.py                # linking-phrase/predicate-term lookup cache
  subset_codelists.py                # get_subset_codelists.sas port
  hierarchy.py                        # create_hierarchy.sas + util_gettree.sas ports (library-only)
  json_roundtrip.py                    # read_bc/sdtm/crf_from_json.sas ports
  bc_converter.py                        # generate_yaml_from_bc.sas port
  sdtm_converter.py                       # generate_yaml_from_sdtm.sas port
  crf_converter.py                         # generate_yaml_from_crf.sas port
  validators/
    common.py                              # shared cross-workbook checks (unresolved refs, dupes, retired-BC, encoding scan)
    sdtm.py                                # SDTM-specific checks, built on common.py
    crf.py                                 # CRF-specific checks, built on common.py + sdtm.py
```

Top-level driver scripts stay flat in `scripts/`, matching existing conventions (argparse via
`set_cmd_line_args()`, `main()` + `if __name__ == "__main__":`, `logging` module per the
`check_concept_status.py` precedent since these scripts are validation-heavy, `os.path` not `pathlib`,
no type hints, module-level docstring):

```
scripts/convert_bc_xlsx2yaml.py
scripts/convert_sdtm_xlsx2yaml.py
scripts/convert_crf_xlsx2yaml.py
scripts/convert_latest_xlsx2yaml.py
scripts/validate_spreadsheet_sdtm.py
scripts/validate_spreadsheet_crf.py
scripts/refresh_codelists.py
scripts/refresh_enums.py
scripts/refresh_sdtm_relations.py
scripts/dump_bc_from_json.py     # thin CLI wrapper over json_roundtrip.py
scripts/dump_sdtm_from_json.py
scripts/dump_crf_from_json.py
utilities/manifests/{bc,sdtm,crf}/<release>.yaml
```

`create_hierarchy.sas`/`util_gettree.sas` become library functions only in `hierarchy.py` (no current
caller in the SAS code, no CLI needed). `varexist.sas` and `check_reg_keys.sas` are **not ported** —
superseded by native Python attribute/column checks and a SAS/Windows-Excel-driver concern with no
Python equivalent, respectively; note this explicitly in code comments rather than silently dropping them.

### Manifests

One YAML file per release per domain, e.g. `utilities/manifests/sdtm/20260714_r18.yaml`, listing exactly
the `generate_yaml_from_*` call parameters currently hand-coded in the (only) uncommented block of each
SAS driver: `excel_file`, `range`, `type`, `package`, `override_package_date`, `out_folder`, plus
domain-specific params (`subsetsDS`/`check_relationships` for SDTM). Converters and validators both load
manifests; validators additionally load every manifest across the release history (mirroring
`validate_spreadsheet_sdtm.sas`'s union-of-packages-1-through-18 approach) to build the full referential
corpus. Building the initial manifests for the current active release (r18) and the DHT/draft variants
requires transcribing the currently-uncommented blocks from the three `convert_*_xlsx2yaml.sas` files —
this is manual, one-time transcription work, done in Phase 1.

### YAML fidelity — hand-rolled writer, not `yaml.safe_dump`

Existing YAML files (e.g. `yaml/20260714_r18/sdtm/sdtm_pasi03headscaling.yaml`) have fixed non-alphabetical
field order and a conditional quoting rule (quote a string if it contains `"`, `:`, or `-`) that
`yaml.safe_dump` cannot reproduce without a fully custom `Dumper`. Build a small `YamlWriter` line-emitter
class (justified exception to the "no classes" convention, same rationale as the existing `NCIEVSClient`)
with methods for scalar/always-quoted-scalar/block-key/list-scalar/list-quoted lines, and a shared
`needs_quoting(value)` helper centralizing the `"` / `:` / `-` predicate used ~8 times across the SAS
macros. Golden-file tests (see Verification) confirm this reproduces already-published YAML exactly.

### Reference-data caching

Cached lookups live under `utilities/data/*.json` (already the SAS `libname data` convention, already on
disk). Three caches are populated by dedicated **refresh scripts** and consumed **read-only** by
converters/validators:

| Cache file | Populated by | Consumed by |
|---|---|---|
| `sdtm_latest_codelist_package.json` (+ cdash/ddf/protocol variants) | `refresh_codelists.py` | SDTM/CRF converters, validators |
| `linkml_enums.json` | `refresh_enums.py` (via `SchemaView(model/cosmos_*_model.yaml).all_enums()` — cleaner than the SAS approach of parsing generated JSON-schema files, no dependency on a prior Windows-only regeneration step) | BC/SDTM converters |
| `sdtm_linkingphrases_predterms.json`, `sdtm_predicateterms.json`, `sdtm_linkingphrases.json` | `refresh_sdtm_relations.py` (slowest refresh — crawls every published SDTM specialization) | SDTM converter/validator |

The **NCI EVS cache** (`ncievs_cache.json`) is different: it's a read-through cache populated lazily by
the converters themselves during a run (keyed `f"{function}:{ncit_code}"`), since NCit lookups are keyed
by whatever codes appear in curation, not enumerable ahead of time like codelist packages. Every
converter/validator script gets `--no-cache` and `--refresh-cache` flags. Cache files carry a
`_meta.fetched_at` timestamp; scripts print (don't fail on) a staleness warning past a configurable
threshold.

**Case-sensitivity note**: the CDISC Library codelist cache index must stay case-sensitive (terms are
stored exactly as the API returns them); only fold case at the two specific call sites that intentionally
do a second, case-insensitive probe to detect `*_WRONG_CASE` issues. A case-folded index would silently
disable that check.

## Script-to-script mapping

| SAS source | Python script | Notes |
|---|---|---|
| `convert_bc_xlsx2yaml.sas` + `_dht` variant | `convert_bc_xlsx2yaml.py --manifest <path>` | One script; DHT variant is just a different manifest file |
| `convert_sdtm_xlsx2yaml.sas` + `_dht` variant | `convert_sdtm_xlsx2yaml.py --manifest <path>` | Same reasoning |
| `convert_crf_xlsx2yaml.sas` | `convert_crf_xlsx2yaml.py --manifest <path>` | No DHT variant exists for CRF |
| `convert_latest_xlsx2yaml.sas` | `convert_latest_xlsx2yaml.py --domain {bc,sdtm} --release <name>` | Simplify: determine "already produced" ids by listing filenames already in `yaml/<release>/{bc,sdtm}/` instead of re-reading a draft workbook — same result, one less redundant Excel read |
| `validate_spreadsheet_sdtm.sas` + `_dht` | `validate_spreadsheet_sdtm.py --manifests <glob>` | Collapses ~800 lines of hand-listed `%ReadExcel` calls to "load these manifests" |
| `validate_spreadsheet_crf.sas` | `validate_spreadsheet_crf.py` | Separate script, but built on shared `validators/common.py` + `sdtm.py` (today's SAS is a near-duplicate copy-paste of the SDTM validator plus CRF checks — the port shares the logic instead of copying it) |
| `get_latest_codelists_api.sas` | `refresh_codelists.py` | |
| `get_latest_enums_linkml.sas` | `refresh_enums.py` | |
| `get_latest_relations_sdtm_api.sas` | `refresh_sdtm_relations.py` | Slowest — never bundle into an implicit "refresh all" default |
| `create_hierarchy.sas`, `util_gettree.sas` | `cosmoslib/hierarchy.py` (library only) | No current caller |
| `read_bc/sdtm/crf_from_json.sas` | `cosmoslib/json_roundtrip.py` + thin `dump_*_from_json.py` CLIs | Used for ad hoc round-trip verification against the live API |

## Phased delivery order

Front-loading the riskiest/most novel logic (YAML formatting fidelity, the manifest abstraction, the
BC/SDTM group-boundary state machine):

1. **Foundation** — `excel_reader.py`, `yaml_writer.py` (+ golden-file tests against real checked-in
   YAML), `issues.py`, `templates.py`, `naming.py`, `manifest.py`, and hand-transcribe the r18/DHT/draft
   manifests from the currently-active SAS driver blocks.
2. **BC reference data** — `enums.py` + `refresh_enums.py`, `ncievs_cache.py` extending `NCIEVSClient`.
3. **BC converter** — `bc_converter.py` (including the `lag()`-based group-boundary state machine, ported
   as an explicit per-group state object, not a pandas groupby shortcut — see Verification for why this
   distinction matters) + `convert_bc_xlsx2yaml.py`.
4. **SDTM reference data** — `cdisc_library_cache.py` + `refresh_codelists.py`, `relations_cache.py` +
   `refresh_sdtm_relations.py`, `subset_codelists.py`. Independent of Phase 3; can run in parallel if
   staffed.
5. **SDTM converter** — `sdtm_converter.py` (the largest, most rule-dense macro — ~35 distinct validation
   checks, subset-codelist merge, relationship checks, regex-driven mandatory-variable rules) +
   `convert_sdtm_xlsx2yaml.py`. Longest phase; the comparator auto-clear quirk gets an explicit unit test
   here, not just eyeballing.
6. **CRF converter** — `crf_converter.py` + `convert_crf_xlsx2yaml.py`. Reuses Phase 4's codelist cache.
   Apply the two approved fixes here (`completionInstructions` spelling, `yaml/<folder>/crf` path).
7. **Cross-spreadsheet validators** — `validators/common.py`/`sdtm.py`/`crf.py`,
   `validate_spreadsheet_sdtm.py`, `validate_spreadsheet_crf.py`. Consumes manifests from Phases 3/5/6, so
   this phase is comparatively low-risk — the payoff of the manifest layer lands here.
8. **Delta regeneration + refresh polish + JSON round-trip wrappers** — `convert_latest_xlsx2yaml.py`,
   any retry/backoff polish on the refresh scripts, remaining manifest files, `dump_*_from_json.py`.

## Subtle behaviors to preserve or fix

- **Group-boundary detection**: SAS's `lag()` on the group-id column advances every row regardless of
  branch; the "new group" reset only fires when `prev_group_id != group_id`. Port as an explicit state
  object over an already-sorted iterator (sort by `(group_id, order)` first) — not a pandas `groupby`
  shortcut, which doesn't reproduce the header-only-first-row edge case where a group's header block and
  its first child item can land on different rows.
- **`comparator=""` auto-clear** (approved: preserve exactly) — the `WHERECLAUSE_UNEXPECTED` rule for
  `*TEST`-suffix variables mutates `comparator` as a side effect of logging the issue, and that mutation
  is visible in the emitted YAML. Port this in the same order: log issue, then clear, then emit.
- **`completionIinstructions` typo** (approved: fix) — emit `completionInstructions` matching the LinkML
  schema.
- **CRF folder path `&folder.2`** (approved: fix) — emit to `yaml/<folder>/crf`, matching the bc/sdtm
  convention.
- **Issue-type string typos** (`"DEC_SHORTNAME MISMATCH_OR_MISSING"`, `"QUESTION_TEXT_PROMPT_BOTH_NOT MISSING"`
  — space instead of underscore, confirmed via grep to have no other consumer in the repo) — fix these;
  they're log-text-only with no payload effect.
- **CRF term-case-checking asymmetry** — SDTM validates both exact-case and upcased term lookups
  (`*_WRONG_CASE` checks); CRF has no equivalent fallback. This looks like an unintentional omission
  rather than a deliberate difference, but changes which `issue_type` curators see — flag it in a code
  comment (`# SAS-QUIRK(flagged-for-SME)`) and leave CRF as-is (no `WRONG_CASE` check) until a CDISC SME
  weighs in, rather than unilaterally adding new validation behavior.
- **Hardcoded Windows path separators** (`\` in `outname=catt(...)` calls) — fix, use `os.path.join`.
- Tag every preserve/fix decision inline with a one-line comment (`# SAS-QUIRK(preserved|fixed): ... (see
  utilities/.../<file>.sas:<line>)`) so `grep -rn "SAS-QUIRK"` gives a complete audit trail.

## Verification strategy

No automated tests exist in this repo today (`verify_cosmos_data.py`'s bare `assert`s are the closest
precedent) and SAS isn't available to regenerate fresh comparison output — verification relies on
diffing against already-published files.

- **Golden-file regression** (`tests/regression/test_convert_xlsx2yaml.py`, marked `@pytest.mark.golden`):
  primary fixture is `curation/package18/R18_BC_PASI_FREDRIKSSON.xlsx` (tabs `BC_PASI_FREDRIKSSON` /
  `SDTM_PASI_FREDRIKSSON`) against the 17 BC + 16 SDTM files already in `yaml/20260714_r18/{bc,sdtm}/`
  (confirmed present). Assert `yaml.safe_load(generated) == yaml.safe_load(golden)` (dict-equality, not
  byte-diff — SAS's `$YN.` boolean formatting leaves a cosmetic trailing space that's semantically
  irrelevant) and assert the generated file set matches exactly (catches group-boundary regressions). No
  committed non-draft CRF golden fixture exists yet (`yaml/20260714_r18` has no `crf/` folder) — use a
  `_draft` CRF package as a lower-confidence fixture with a caveat, or get SME sign-off on one first.
- **Unit tests per validation rule** (`tests/unit/test_rules_{bc,sdtm,crf}.py`): split each
  `%add2issues_*` call site into a pure function `rule_xxx(row, lookups) -> Issue | None`, tested
  table-driven with "should trigger"/"should NOT trigger" cases against small in-memory
  dicts/dataclasses — no xlsx, no network. Give the `prxmatch`-suffix rules (TEST/TESTCD/ORRES/STRESC
  etc.) extra boundary-case coverage (near-miss prefixes), since off-by-one suffix-length bugs are the
  most likely porting error in that rule family.
- **Mocking live APIs**: CDISC Library codelist/relations data is fetched once upfront into plain
  objects that downstream code takes as arguments — unit tests never need network mocking for these; an
  optional `responses`-based integration test with hand-maintained JSON fixtures
  (`tests/fixtures/cdisc_library/*.json`) covers the fetch-then-validate path, gated behind a `--live`
  marker for real-API re-verification. NCI EVS lookups are per-row — inject a thin `NCitClient` so unit
  tests substitute a dict-backed fake, reserving `responses` mocking for a handful of "parses the real
  response shape" tests against saved real payloads (`tests/fixtures/ncit/*.json`).
- **Manual checklist** (non-automatable): (1) run the BC converter with the real `NCitClient` against the
  package18 fixture and confirm zero unexpected retired-concept/definition-mismatch issues, consistent
  with the fact that this is already-published data; (2) run the cross-workbook validators against the
  full corpus (all 18 packages + both `export/*_latest.xlsx` files) and confirm zero unresolved-reference/
  duplicate/retired-BC hits, expecting a small number of true-positive character-encoding hits to triage;
  (3) hand-compare a CRF `_draft` conversion against `yaml/20251231_draft/crf` and `yaml/20260630_draft/crf`
  noting the lower-confidence caveat; (4) after any full regeneration, run the existing
  `scripts/validate_yaml.py` and `scripts/verify_cosmos_data.py -e prod` as independent cross-checks.
- **New dev dependencies**: add a separate `requirements-dev.txt` (not folded into `requirements.txt`)
  with `pytest` and `responses` (preferred over `requests-mock`/`vcrpy` — matches the existing plain
  `requests`-based style and keeps hand-maintained, PR-reviewable JSON fixtures instead of opaque
  cassettes). Update the "no automated test suite" line in `CLAUDE.md` once this lands.

## Files to create/modify

- New package `scripts/cosmoslib/` (all files listed under Architecture above).
- New scripts listed under Script-to-script mapping, in `scripts/`.
- New `utilities/manifests/{bc,sdtm,crf}/*.yaml`.
- New `tests/regression/` and `tests/unit/` with fixtures under `tests/fixtures/`.
- New `requirements-dev.txt`.
- Update `requirements.txt` if any new runtime deps are needed (e.g. `linkml_runtime` if not already
  transitively available via `linkml`).
- Update root `CLAUDE.md` once tests exist, to reflect the new commands and drop the "no test suite"
  statement.
- No existing SAS files are modified or deleted — the Python port lives alongside `utilities/*.sas`
  until the team is ready to retire the SAS pipeline.
