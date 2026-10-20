# How to add enums (or enum values) to the BC, SDTM and CRF models

Enums in COSMoS are defined **once**, in the LinkML schemas under `model/`. Everything else
(JSON Schema, Python/Pydantic classes, docs, the converters' validation cache) is derived from
those files. So the job is always: **edit the schema → refresh the cache → regenerate the
derived files → test**.

All commands assume you run from the **repository root** (`COSMoS/`) with the project venv
active (`.venv` on macOS/Linux, `venv` on Windows).

## Contents

- [1. Which file to edit](#1-which-file-to-edit)
- [2. Edit the schema](#2-edit-the-schema)
- [3. Refresh the enum cache](#3-refresh-the-enum-cache)
- [4. Regenerate the derived files](#4-regenerate-the-derived-files)
- [5. Test](#5-test)
- [6. Checklist](#6-checklist)
- [Which enums the Python converters actually check](#which-enums-the-python-converters-actually-check)
- [Known problems with regeneration on macOS/Linux](#known-problems-with-regeneration-on-macoslinux)

## 1. Which file to edit

| Model | Schema to edit (the only hand-edited file) | Enums defined there |
|-------|--------------------------------------------|---------------------|
| BC    | `model/cosmos_bc_model.yaml`   | `PackageTypeEnum`, `BiomedicalConceptResultScaleEnum`, `DataElementConceptDataTypeEnum` |
| SDTM  | `model/cosmos_sdtm_model.yaml` | `PackageTypeEnum`, `SDTMVariableDataTypeEnum`, `LinkingPhraseEnum`, `PredicateTermEnum`, `OriginTypeEnum`, `OriginSourceEnum`, `RoleEnum`, `ComparatorEnum` |
| CRF   | `model/cosmos_crf_model.yaml`  | `PackageTypeEnum`, `ImplementationOptionEnum`, `CRFItemDataTypeEnum`, `SelectionTypeEnum` |

Each file has an `enums:` section (BC ~line 142, SDTM ~line 270, CRF ~line 327). Find the enum
by name with `grep -n "Enum:" model/cosmos_<bc|sdtm|crf>_model.yaml`.

Rule of thumb for "which model?": use the model whose class owns the slot that uses the
enum. For example `linkingPhrase` and `predicateTerm` are slots of SDTM `RelationShip`, so
their enums live in the SDTM schema.

**Never hand-edit** the generated files: `model/*.json`, `*.md`, `*.yuml`, `*.svg`, or anything
under `project/{bc,sdtm,crf}/`. They are overwritten on regeneration.

## 2. Edit the schema

### Add a value to an existing enum

Add a new key under `permissible_values:`. Order does not matter functionally; new values are
conventionally appended at the end of the list.

```yaml
  LinkingPhraseEnum:
    permissible_values:
      ...
      is the value for the parameter in:
      my new linking phrase in:          # <- new value; text is exactly what appears in the spreadsheet
```

- The key is the literal permissible value, so spelling, case, spaces and punctuation must
  match what curators type in the spreadsheets. Values with spaces or `/` need no quotes in
  this file's existing style (see `is identifier for treatment label/kit ...`), but a value
  containing `:`, `#`, a leading `-`, or other YAML-special characters must be quoted.
- A bare key with nothing after the colon is the file's normal style. Optional extras, used by
  some enums, are `title:`, `description:` and `meaning:` (e.g. `meaning: NCIT:C25936` in
  `OriginSourceEnum`). Follow the style of the enum you are editing.
- Do not use tabs. Indent with two spaces, matching neighbours.

### Add a brand-new enum

1. Add it under `enums:` in the right schema:

   ```yaml
     MyNewEnum:
       permissible_values:
         ValueOne:
         ValueTwo:
   ```
2. Point a slot at it with `range:`, in the same file's `slots:` section:

   ```yaml
     myNewSlot:
       description: ...
       range: MyNewEnum
   ```
3. Attach the slot to a class (`slots:` list on the class, or `slot_usage`) — otherwise the
   enum is defined but unused.
4. Name it `<Something>Enum`. The Python cache strips the `Enum` suffix, so the converters look
   it up as `"Something"`.
5. A new enum is only **checked by the converters** if code calls
   `exists_enum_term(enum_index, "Something", value)`. That is a change under
   `scripts/cosmoslib/` (and tests) — see
   [Which enums the Python converters actually check](#which-enums-the-python-converters-actually-check).
   Adding the schema entry alone does not make the converters validate the new enum.

## 3. Refresh the enum cache

The converters and validators read enum values from a cache file
(`utilities/data/linkml_enums.json`, gitignored), **not** from the schema directly. If the
cache is stale, spreadsheets that use your new value will be flagged as invalid.

```bash
python scripts/refresh_enums.py
```

This reads all three schemas, merges enums by name (minus the `Enum` suffix) and rewrites the
cache. It is fast and needs no network. Re-run it on every machine that runs the converters
after the schema change is pulled — the cache is not committed.

## 4. Regenerate the derived files

The regeneration scripts are **Windows batch files** that expect a `venv` with `linkml`
installed. Run the one for each schema you changed (from the repo root):

```
scripts\cosmos_bc_model_generate.cmd
scripts\cosmos_sdtm_model_generate.cmd
scripts\cosmos_crf_model_generate.cmd
```

Each runs, in order: `gen-json-schema`, `create_svg.py`, `gen-erdiagram`, `gen-yuml`,
`gen-plantuml`, `gen-doc`, `gen-python`, `gen-python-api`, `gen-pydantic`.

Files that actually change when you only add enum values:

| Generator | Output |
|-----------|--------|
| `gen-json-schema` | `model/cosmos_<m>_model.json` |
| `gen-python` | `project/<m>/cosmos_<m>_model.py` |
| `gen-pydantic` | `project/<m>/cosmos_<m>_model_pydantic.py` |
| `gen-doc` | `project/<m>/docs/enums/<Name>Enum.md` (and `slots/`, `classes/` if a slot or class changed) |

The diagrams (`.svg`, `.yuml`, `.md`, plantuml) and `cosmos_<m>_model_api.py` do not list
enum values, so they change only if you added a new enum **and** a new slot/class. After
regenerating, run `git diff --stat` — for a value-only change you should see roughly those four
kinds of files and nothing else. A large unrelated diff means the tool versions differ from
the ones used for the committed files (see below).

## 5. Test

```bash
pytest tests/unit/test_enums.py          # cache/index logic
pytest                                   # full suite incl. golden-file regression tests
python scripts/validate_yaml.py -y yaml/<release>/sdtm -s model/cosmos_sdtm_model.yaml -c SDTMGroup
```

`validate_yaml.py` takes `-c BiomedicalConcept`, `SDTMGroup` or `CRFGroup` with the matching
schema; use the one for the model you changed. If you added a
value because curators need it, re-run the relevant converter on their spreadsheet
(`scripts/convert_<bc|sdtm|crf>_xlsx2yaml.py --manifest ...`) and confirm the "invalid enum"
issues for that value are gone.

If you add a new enum that the converters check, add a unit case in
`tests/unit/test_<bc|sdtm>_converter.py`.

## 6. Checklist

1. [ ] Identify the model (BC / SDTM / CRF) and the enum; confirm the exact value text with the requester.
2. [ ] Edit `model/cosmos_<m>_model.yaml` (new value, or new enum + `range:` slot + class attachment).
3. [ ] `python scripts/refresh_enums.py`
4. [ ] Run `scripts\cosmos_<m>_model_generate.cmd` (Windows), or the macOS/Linux workaround below.
5. [ ] `git diff --stat` — only the expected generated files changed.
6. [ ] `pytest`, and re-run the converter/validator on the spreadsheet that needed the value.
7. [ ] Commit the schema **and** the regenerated files together, so `model/*.yaml` and
   `model/*.json` / `project/*` never disagree.
8. [ ] Tell the team to re-run `python scripts/refresh_enums.py` (the cache is gitignored).

## Which enums the Python converters actually check

Only these enum names are looked up by the code today (`exists_enum_term(...)` in
`scripts/cosmoslib/`). Value changes to these take effect in validation after step 3:

| Cache key | Schema | Checked in |
|-----------|--------|------------|
| `BiomedicalConceptResultScale`, `DataElementConceptDataType` | BC | `bc_converter.py` |
| `SDTMVariableDataType`, `Role`, `OriginType`, `OriginSource`, `Comparator`, `LinkingPhrase`, `PredicateTerm` | SDTM | `sdtm_converter.py` |

The CRF converter (`crf_converter.py`) does **not** check any enum, so a CRF enum change is
schema/derived-files only. `PackageType`, `ImplementationOption`, `CRFItemDataType` and
`SelectionType` are likewise not checked by converters.

Note the cache merges same-named enums across schemas: `PackageTypeEnum` exists in all three,
and the single `PackageType` key holds `bc`, `crf` and `sdtm`. Don't reuse an enum name across
schemas unless you want that merge.

## Known problems with regeneration on macOS/Linux

The `.cmd` scripts are the supported route. If you must regenerate on a Mac, a recent `linkml`
behaves differently from the version that produced the committed files (observed on
2026-10-20 with the repo's `.venv`):

- `gen-json-schema` and `gen-python` work and produce a clean, minimal diff. Use them.
- `gen-pydantic` errors (`--meta auto` rejected) and `gen-python-api` is not installed. Because
  the scripts redirect with `>`, a failed command **leaves an empty file** — run
  `git checkout -- <file>` to restore it, then hand-add the new enum members to
  `project/<m>/cosmos_<m>_model_pydantic.py` (follow the existing pattern: a snake_case
  attribute equal to the value text). `_api.py` does not list enum values; leave it alone.
- `gen-doc` rewrites ~80 unrelated doc files (changed URI lines etc.). Revert the churn
  (`git checkout -- project/<m>/docs`) and hand-add rows to `project/<m>/docs/enums/<Name>Enum.md`.
- `create_svg.py` uses the yUML web service, which now stamps "PLEASE MIGRATE" on the diagram.
  Revert any `.svg` it touches (`git checkout -- model/*.svg`); enum values are not drawn
  anyway.

Preferably have the Windows regeneration done by someone with the pinned toolchain, and
review `git diff --stat` before committing.
