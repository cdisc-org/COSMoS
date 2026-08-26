# How to use the Python conversion pipeline

This is a full, faithful Python port of the SAS toolchain under `utilities/` — the scripts
that validate curation Excel spreadsheets and convert them into the per-record YAML under
`yaml/<release>/{bc,sdtm,crf}/`. It requires no Windows, no SAS installation, and no
SAS-via-Python (MAS) bridge. It reads the same curation spreadsheets the SAS scripts read
and produces byte-for-byte-equivalent YAML (verified with golden-file regression tests
against already-published output).

The SAS files are **not modified or removed** by this port — both toolchains work side by
side today. This guide covers the Python side only.

All commands below assume you run from the **repository root** (`COSMoS/`), since every
script's default paths (manifests, caches, curation files, output folders) are relative to
it.

## Contents

- [Setup](#setup)
- [The pipeline, in order](#the-pipeline-in-order)
- [Manifests: the single source of truth for what gets converted](#manifests-the-single-source-of-truth-for-what-gets-converted)
- [Script reference](#script-reference)
- [Caveats and preserved SAS quirks](#caveats-and-preserved-sas-quirks)
- [Best practices](#best-practices)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Setup

```bash
# From the repo root, in a Python 3.10+ virtual environment
pip install -r requirements.txt          # runtime deps (pandas, openpyxl, linkml, cdisc-library-client, ...)
pip install -r requirements-dev.txt      # + pytest, responses (only needed to run the test suite)
```

Two live services are involved, and their credentials come from environment variables
(typically via a gitignored `.env` file, loaded the same way the pre-existing
`create_cosmos_*_excel.py` / `verify_cosmos_data.py` scripts already do):

| Variable | Used by | Required for |
|---|---|---|
| `CDISC_LIBRARY_API_KEY` / `CDISC_LIBRARY_API_URL` | `refresh_codelists.py`, `refresh_sdtm_relations.py`, `dump_bc_from_json.py --id`, `dump_sdtm_from_json.py --id` | Production CDISC Library API |
| `CDISC_LIBRARY_API_KEY_DEV` / `CDISC_LIBRARY_API_URL_DEV` | same scripts, with `-e dev` | Dev CDISC Library API |

**NCI EVS (`ncievs_client.py` / `ncievs_cache.py`) needs no API key** — it's a public
endpoint (`api-evsrest.nci.nih.gov`). Only the CDISC Library calls above need credentials.

If a script needs credentials that aren't set, it prints a clear error and exits — it never
fails halfway through with a confusing traceback.

## The pipeline, in order

Running everything from scratch for a release follows this order. Skip steps whose output
is already fresh enough for your purposes (see [Best practices](#best-practices)).

```
1. Refresh reference-data caches   (once per day/session, not once per conversion)
   scripts/refresh_enums.py
   scripts/refresh_codelists.py
   scripts/refresh_sdtm_relations.py     (slow - see caveats)

2. Convert curation spreadsheets -> YAML, per domain
   scripts/convert_bc_xlsx2yaml.py    --manifest utilities/manifests/bc/<release>.yaml
   scripts/convert_sdtm_xlsx2yaml.py  --manifest utilities/manifests/sdtm/<release>.yaml
   scripts/convert_crf_xlsx2yaml.py   --manifest utilities/manifests/crf/<release>.yaml

3. Validate across the whole corpus (BC <-> SDTM <-> CRF cross-references)
   scripts/validate_spreadsheet_sdtm.py
   scripts/validate_spreadsheet_crf.py

4. (Optional) Regenerate the full "latest" export corpus, or a delta against one release
   scripts/convert_latest_xlsx2yaml.py --domain bc   [--release <release>]
   scripts/convert_latest_xlsx2yaml.py --domain sdtm [--release <release>]

5. (Optional, ad hoc) Round-trip a single record against the live API for spot-checking
   scripts/dump_bc_from_json.py / dump_sdtm_from_json.py / dump_crf_from_json.py
```

Steps 2 and 3 both read the caches step 1 builds — run step 1 first, or the converters and
validators will each print an error naming the missing cache file and the refresh script
that builds it, and exit without touching anything.

### Step 1: refresh reference-data caches

These populate `utilities/data/*.json` (gitignored — every developer/CI run builds their
own copy). Converters and validators read them **read-only**; nothing under `scripts/`
ever calls the live API mid-conversion except the NCI EVS lookups described below.

```bash
python scripts/refresh_enums.py
python scripts/refresh_codelists.py
python scripts/refresh_sdtm_relations.py
```

`refresh_sdtm_relations.py` is the slow one — it crawls **every** published SDTM dataset
specialization one at a time (the plan calls it out explicitly as "the slowest refresh in
the pipeline"). Don't bundle it into a habitual "refresh everything" alias; run it
deliberately, only when the SDTM relationship corpus (linking phrases / predicate terms)
actually needs updating. `refresh_enums.py` and `refresh_codelists.py` are fast by
comparison (a handful of API calls each).

The **NCI EVS cache** (`utilities/data/ncievs_cache.json`) is different from the three
above: it is *not* built by a refresh script. It's a read-through cache populated lazily,
one code at a time, by the BC/latest converters themselves as they run (since NCit codes
are keyed by whatever appears in curation, not enumerable ahead of time). It persists
across runs automatically.

### Step 2: convert curation spreadsheets to YAML

```bash
python scripts/convert_bc_xlsx2yaml.py   --manifest utilities/manifests/bc/20260714_r18.yaml
python scripts/convert_sdtm_xlsx2yaml.py --manifest utilities/manifests/sdtm/20260714_r18.yaml
python scripts/convert_crf_xlsx2yaml.py  --manifest utilities/manifests/crf/20260630_draft.yaml
```

Each converts every job listed in the manifest and writes one YAML file per BC/SDTM
specialization/CRF item group to the manifest's `out_folder`. Each also writes a
structured issues report — see [Issues reports](#issues-reports) below — and prints a
console severity-count summary when it finishes.

There is no separate `_dht` script — point `--manifest` at
`utilities/manifests/{bc,sdtm}/dht_test.yaml` instead of writing a second script.

### Step 3: validate across the whole corpus

```bash
python scripts/validate_spreadsheet_sdtm.py
python scripts/validate_spreadsheet_crf.py
```

Run **after** step 2 for the release(s) you care about — the validators build their
referential corpus from whatever manifests exist under `utilities/manifests/{bc,sdtm,crf}/`
(by default, *all* of them — see `--manifests`/`--bc-manifests`/`--sdtm-manifests` in the
[script reference](#script-reference) to narrow that), merged with the already-published
`export/*_latest.xlsx` corpus. They check for:

- BC `parent_bc_id` references that don't resolve to a real `bc_id`
- SDTM/CRF `bc_id`/`dec_id` references that don't resolve to a real BC/DEC
- CRF `vlm_group_id` references that don't resolve to a real SDTM specialization
- Duplicate BC/SDTM/CRF records
- SDTM/CRF records pointing at a retired BC
- Curated cells containing control characters or disallowed high-byte characters

None of these checks require live network access — everything is read from the curation
spreadsheets and the `export/*_latest.xlsx` files already in the repo.

### Step 4 (optional): "latest" delta regeneration

```bash
python scripts/convert_latest_xlsx2yaml.py --domain bc   --release 20260714_r18
python scripts/convert_latest_xlsx2yaml.py --domain sdtm --release 20260714_r18
```

Regenerates YAML from the published `export/cdisc_*_latest.xlsx` corpus rather than a
specific release's curation files. This is a maintenance/backfill tool, not part of the
normal per-release flow:

- **Without `--release`**: regenerates the *entire* latest export into `yaml/latest/<domain>/`.
  Only do this deliberately (e.g. after a schema or converter change) — it's a full corpus
  run, comparable in scale to steps 1–3 combined, and touches every already-published
  record.
- **With `--release <name>`**: excludes every id already produced under
  `yaml/<name>/<domain>/` and writes to `yaml/latest_test/<domain>/` instead — a dry-run
  area to review before touching the real `yaml/latest/` folder.

### Step 5 (optional): round-trip a single record

```bash
python scripts/dump_bc_from_json.py   --id C191040 --out /tmp/bc.csv
python scripts/dump_sdtm_from_json.py --id PASI03HEADSCALING
python scripts/dump_crf_from_json.py  --json-file path/to/crf_record.json
```

Fetches (BC/SDTM only — no live CRF endpoint exists yet) or reads one record and flattens
it into the same row shape as the curation spreadsheets, printed as CSV (to `--out` or
stdout). This is a diagnostic tool for spot-checking a specific record against what's
published live, not something any converter or validator calls.

## Manifests: the single source of truth for what gets converted

A manifest (`utilities/manifests/{bc,sdtm,crf}/<release>.yaml`) is the Python pipeline's
replacement for SAS's hand-edited, commented-out per-release blocks at the top of
`convert_{bc,sdtm,crf}_xlsx2yaml.sas`. One file per release per domain:

```yaml
release: "20260714_r18"
domain: sdtm
package: "20260714"
override_package_date: "2026-07-14"
out_folder: yaml/20260714_r18/sdtm
check_relationships: true
subsets_source:
  file: curation/package06/BC_Package_R6_LZZT.xlsx
  range: "Subset Codelist Example"
jobs:
  - excel_file: curation/package18/R18_SDTM_IS_MAST7.xlsx
    range: SDTM_IS
    type: is
```

Top-level keys (`package`, `override_package_date`, `out_folder`, `select`,
`subsets_source`, `check_relationships`) are defaults every job inherits; a job can
override any of them individually. Currently checked in:

| Manifest | Covers |
|---|---|
| `utilities/manifests/bc/20260714_r18.yaml` | The active BC release |
| `utilities/manifests/sdtm/20260714_r18.yaml` | The active SDTM release |
| `utilities/manifests/crf/20260630_draft.yaml` | The current CRF draft package |
| `utilities/manifests/bc/dht_test.yaml`, `sdtm/dht_test.yaml` | The DHT test package |

**To convert a new release**: copy the block that's currently uncommented at the bottom of
the corresponding `utilities/convert_*_xlsx2yaml.sas` file into a new manifest (one `jobs`
entry per `%generate_yaml_from_*(...)` call), point `--manifest` at it, and run. There is
no need to touch any Python source to add a release.

Only the *active* release per domain has a manifest today — earlier packages' driver
blocks are commented out in the SAS source and were never transcribed (see
[Caveats](#caveats-and-preserved-sas-quirks)). The validators don't need them: they merge
whatever manifests exist with the already-published `export/*_latest.xlsx` corpus instead.

## Script reference

All scripts support `-h`/`--help` for the authoritative, up-to-date flag list. Defaults
below assume you're running from the repo root.

### Refresh scripts

| Script | Key flags | Notes |
|---|---|---|
| `refresh_enums.py` | `-s/--schema` (default: the 3 `model/cosmos_*_model.yaml` files), `-o/--out-file` (default `utilities/data/linkml_enums.json`) | No API key needed — reads the LinkML schemas directly |
| `refresh_codelists.py` | `-e/--env` (`prod`\|`dev`) | Writes 4 files: `utilities/data/{sdtm,cdash,ddf,protocol}_latest_codelist_package.json`. One family failing doesn't stop the others. |
| `refresh_sdtm_relations.py` | `-e/--env`, `-v/--api-version` (default `v2`) | Writes `utilities/data/sdtm_{linkingphrases_predterms,predicateterms,linkingphrases}.json`. One specialization failing doesn't stop the crawl. |

### Converters

| Script | Required | Key optional flags | Notes |
|---|---|---|---|
| `convert_bc_xlsx2yaml.py` | `-m/--manifest` | `--enum-cache`, `--ncievs-cache`, `--no-cache`, `--refresh-cache`, `--issues-out` | |
| `convert_sdtm_xlsx2yaml.py` | `-m/--manifest` | `--enum-cache`, `--codelist-cache`, `--linkingphrases-predterms-cache`, `--predicateterms-cache`, `--issues-out` | |
| `convert_crf_xlsx2yaml.py` | `-m/--manifest` | `--codelist-cache`, `--issues-out` | No `--enum-cache` — the CRF macro never validates against a LinkML enum in the SAS source either |
| `convert_latest_xlsx2yaml.py` | `--domain {bc,sdtm}` | `--release`, plus the same cache flags as the two converters above | See [step 4](#step-4-optional-latest-delta-regeneration) |

`--no-cache` disables the NCI EVS cache entirely for that run (always hits the live API,
caches nothing). `--refresh-cache` ignores what's cached and re-fetches every lookup,
still updating the cache file. Neither flag affects the *emitted YAML* — only the BC
converter's issue-log checks (retired-concept status, short-name/definition mismatches)
depend on NCI EVS at all; SDTM/CRF term-mismatch checks depend on the codelist caches the
same way. **Every field written to the generated YAML comes straight from the curation
workbook** — none of it depends on a live lookup.

### Validators

| Script | Key flags | Notes |
|---|---|---|
| `validate_spreadsheet_sdtm.py` | `--manifests`, `--bc-manifests` (globs, default `utilities/manifests/{sdtm,bc}/*.yaml`), `--bc-latest-file/-range`, `--sdtm-latest-file/-range`, `--subsets-file/-range`, `--distinct-parent-check`, `--no-suppress-retired`, `--high-byte-max` (default `159`), `--issues-out` | |
| `validate_spreadsheet_crf.py` | `--manifests`, `--bc-manifests`, `--sdtm-manifests` (globs), `--bc-latest-file/-range`, `--sdtm-latest-file/-range`, `--distinct-parent-check`, `--high-byte-max` (default `255`), `--issues-out` | No `--subsets-*` (CRF doesn't merge subset codelists) |

The `--distinct-parent-check`, `--no-suppress-retired`, and `--high-byte-max 255` flags on
`validate_spreadsheet_sdtm.py` reproduce `validate_spreadsheet_sdtm_dht.sas`'s three real
behavioral differences from the main SAS validator — pass them together when validating a
DHT package.

### Round-trip dump scripts

| Script | Input | Notes |
|---|---|---|
| `dump_bc_from_json.py` | `--id <conceptId>` (live fetch) **or** `--json-file <path>` | `-v/--api-version` (default `v2`), `--out` |
| `dump_sdtm_from_json.py` | `--id <datasetSpecializationId>` **or** `--json-file <path>` | same |
| `dump_crf_from_json.py` | `--json-file <path>` **only** | No `--id` — no live CRF specialization endpoint exists in `cdisc_library_client` yet |

### Issues reports

Every converter and validator writes a CSV + XLSX pair under `utilities/reports/`
(gitignored) plus a console severity-count summary, e.g.:

```
Found 9 issue(s):
  WARNING: 9
```

Default report paths follow `utilities/reports/<script>_issues[_<release>].{csv,xlsx}` —
override with `--issues-out <path-without-extension>` on any script that produces one.
**An issue in the report is not necessarily a bug in your data** — see
[Caveats](#caveats-and-preserved-sas-quirks) below for known, preserved SAS quirks that
surface as findings.

## Caveats and preserved SAS quirks

This is a **faithful** port — it deliberately reproduces several SAS behaviors that look
like bugs, because changing them would silently diverge from already-published data. Two
were explicitly approved and fixed (noted below); everything else quirky is preserved and
documented in code as `# SAS-QUIRK(preserved): ...` or `# SAS-QUIRK(fixed): ...` comments —
`grep -rn "SAS-QUIRK" scripts/` for the full audit trail.

- **`comparator=""` auto-clear (preserved)** — a `*TEST`-suffixed SDTM variable with a
  `comparator` value logs a `WHERECLAUSE_UNEXPECTED` issue *and then clears the
  comparator as a side effect*, in that order. The cleared (blank) value, not the original,
  is what ends up in the emitted YAML.
- **Group-boundary quirks (preserved)** — the BC converter's `dataElementConcepts:` list
  header prints only if checked within the group's first *two* rows; SDTM/CRF are even
  stricter (first row only). If neither of a BC group's first two rows (or an SDTM/CRF
  group's first row) carries the relevant child field, the list header never prints for
  that group at all, even if a later row has one.
- **Asymmetric quoting** — several fields (BC DEC `shortName`, SDTM `domain`/`source`,
  href lines) are emitted unquoted even when they contain characters (`-`, `:`) that other,
  similar fields *do* quote. This is intentional fidelity to the SAS source's actual,
  inconsistent `put` statements, confirmed line-by-line against already-published YAML.
- **`completionInstructions` (fixed)** — SAS emits the misspelled `completionIinstructions`;
  this port emits the corrected spelling.
- **CRF output path (fixed)** — the SAS driver's `&folder.2` macro reference is an apparent
  typo producing a nonexistent folder; the CRF manifest uses the standard
  `yaml/<folder>/crf` path instead.
- **Case-sensitive Excel range lookups, dropped blank columns** — the Python Excel reader
  matches sheet names case-*insensitively* (like the Windows driver SAS used) and silently
  drops columns with a blank header (an openpyxl used-range artifact) — both were real gaps
  found and fixed during this port, not present in the original SAS.
- **Validator asymmetries between SDTM and CRF (preserved, not "fixed")** — the SDTM
  validator suppresses two checks when the row's *own* `short_name` is tagged `[RETIRED]`;
  the CRF validator has no such suppression. The CRF duplicate-record check groups by
  `standard`, not `domain`. Both match the SAS source exactly.
- **Live-API dependency for issue detail, not YAML content** — as noted above, the emitted
  YAML never depends on a live lookup; only the *issues* (mismatch/retired-concept/wrong-
  case checks) do. Running with `--no-cache` or a stale cache changes what issues get
  flagged, never what YAML gets written.
- **No CI, no automated SAS comparison** — there is no SAS installation available anywhere
  in this port's development or CI story. Fidelity was established once, by diffing
  generated output against already-published YAML (see [Testing](#testing)) — there's no
  ongoing mechanism that would catch a *future* SAS-side change silently diverging from the
  Python port. If the SAS macros change, the Python port needs a matching manual update.
- **`refresh_sdtm_relations.py` is slow** — see [Step 1](#step-1-refresh-reference-data-caches).
- **CRF has no live API endpoint** — `cdisc_library_client.CDISCLibraryClient` has no CRF
  specialization method (CRF is still draft-only upstream). `dump_crf_from_json.py` and the
  CRF converter/validator's corpus-building only ever read local curation files, never a
  live "latest" CRF export.
- **Only the active release per domain has a manifest** — see
  [Manifests](#manifests-the-single-source-of-truth-for-what-gets-converted). The
  validators compensate for the missing historical manifests by merging against
  `export/*_latest.xlsx`, which already represents the full historical corpus.

## Best practices

- **Run refresh scripts on a schedule, not per-conversion.** The caches they build are
  meant to be reused across many converter/validator runs in a session. Re-running
  `refresh_sdtm_relations.py` before every single `convert_sdtm_xlsx2yaml.py` invocation
  wastes the slowest part of the pipeline for no benefit — the SDTM relationship corpus
  doesn't change from run to run.
- **Use `--refresh-cache` sparingly, and `--no-cache` only for one-off debugging.** Both
  bypass the whole point of caching (avoiding a live network round-trip per curated code).
  Prefer just re-running `refresh_*.py` when you specifically know upstream data changed.
- **Never hand-edit anything under `yaml/`, `utilities/data/`, `utilities/reports/`, or
  `utilities/manifests/*/latest*.yaml`.** All are either build output or, in the manifest
  case, meant to be edited by copying a SAS block, not by hand-crafting YAML from scratch.
- **Treat the issues report as the thing to read, not the console summary.** The console
  only gives severity counts; the CSV/XLSX has the `_excel_file_`/`_tab_`/identifier columns
  you need to actually locate and fix a curation problem.
- **When adding a new release's manifest, transcribe from the SAS source, don't
  freehand it.** Copy the currently-uncommented `%generate_yaml_from_*` block from the
  corresponding `.sas` file line-by-line into `jobs:` entries — this is exactly what the
  four checked-in manifests were built from, and keeps the manifest an accurate mirror of
  what SAS would have run.
- **Prefer the stub-client pattern from the test suite when scripting something new.** If
  you're writing a one-off script that calls `convert_bc_job`/`convert_sdtm_job`/
  `convert_crf_job` directly, you very likely don't need a real `NCIEVSCache`/
  `CodelistIndex`/`RelationsIndex` unless you specifically care about the issues log — see
  `tests/regression/test_convert_xlsx2yaml.py`'s `_StubNCIEVS`/`_StubCodelistIndex`/
  `_StubRelationsIndex` for the pattern (every YAML field comes from curation, not from
  these lookups).

## Testing

```bash
pytest              # whole suite: unit + golden-file regression tests
pytest -m golden     # only the golden-file regression tests
pytest tests/unit    # only unit tests
flake8               # lint (max line length 120, max complexity 10 - see .flake8)
```

- **Golden-file regression tests** (`tests/regression/test_convert_xlsx2yaml.py`, marked
  `@pytest.mark.golden`) run each converter against a real curation workbook and assert the
  result is dict-equal (via `yaml.safe_load`, not a byte-diff) to what's already published
  under `yaml/20260714_r18/` and `yaml/20260630_draft/crf/`. These are the strongest
  fidelity evidence in the repo — they run with no network access at all (stub NCI
  EVS/codelist/relations clients), since none of the YAML content depends on a live lookup.
- **Unit tests** (`tests/unit/`) cover individual converter blocks, validator checks, cache
  classes, and helpers against small synthetic in-memory data — no Excel or network I/O.
- **No automated SAS-comparison or live-API test exists** (see
  [Caveats](#caveats-and-preserved-sas-quirks)) — the `live` marker in `pytest.ini` is
  reserved for future use but no test currently uses it.
- **When changing a converter or validator**, run the full suite (`pytest`) before and
  after your change — a golden-file test failing means your change diverged from
  already-published data, which is exactly the failure mode these tests exist to catch.
- **When adding a new manifest or curation fixture**, consider whether it's worth a new
  golden-file test (if real already-published YAML exists to diff against) or a synthetic
  unit test (if you're testing a branch the existing fixtures don't exercise) — see any
  existing `tests/unit/test_{bc,sdtm,crf}_converter.py` for the pattern (a `_FakeJob`, a
  `_FakeCodelistIndex`/`_FakeRelationsIndex`, and `patch("cosmoslib.X.read_named_range", ...)`
  to avoid touching real files).

## Troubleshooting

| Symptom | Likely cause / fix |
|---|---|
| `Cache <path> not found - run scripts/refresh_*.py first.` | Run the named refresh script; see [Step 1](#step-1-refresh-reference-data-caches) |
| `Please set the CDISC_LIBRARY_API_KEY and CDISC_LIBRARY_API_URL environment variables.` | Set them (or the `_DEV` pair with `-e dev`) — see [Setup](#setup) |
| `KeyError: "Named range/sheet '...' not found in ..."` | The manifest's `range` doesn't match any sheet/defined-name in that workbook (case-insensitively) — check the workbook, or that the file wasn't renamed/moved since the manifest was written |
| A `pd.concat`/`InvalidIndexError` when running a validator | Almost certainly a workbook with blank-header trailing columns clashing with a real column; this was fixed once in `excel_reader.py` for `R18_BC_SDTM_SC.xlsx` — if you see it again on a *new* workbook, the same fix (drop blank-header columns) should already cover it, so look for a genuinely duplicate real header name instead |
| `refresh_sdtm_relations.py` takes a very long time | Expected — see [Caveats](#caveats-and-preserved-sas-quirks). It logs progress every 100 specializations; let it finish, or interrupt it (no partial cache is written until it completes) |
| A golden-file test fails after a converter change | Your change diverged from already-published output — either it's an unintended regression (fix the change) or you've knowingly changed emitted behavior (update the golden fixture's expectations *and* get sign-off, since these files are the fidelity contract with SAS) |
