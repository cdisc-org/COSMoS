# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

COSMoS (CDISC Conceptual and Operational Standards Metadata Services) is the working repository for
CDISC Biomedical Concepts (BCs), SDTM Dataset Specializations, and CRF Specializations. It holds the
LinkML data model, curation spreadsheets, generated YAML/Excel/CSV artifacts, and the scripts/macros
that move data between those forms. Most of the repository is generated or curated data (spreadsheets,
YAML, diagrams), not application code — treat files under `curation/`, `export/`, `yaml/`, and the
generated files under `model/`/`project/` as build output or source data, not hand-edited code, unless
a task specifically concerns their content.

## Data pipeline (the "big picture")

Understanding the flow between directories is more important than any single file:

1. **Curation** — Subject-matter experts author/edit Excel spreadsheets in `curation/packageNN/`
   (published packages) or `curation/draft/` (work in progress, not yet validated or loaded).
2. **Conversion & validation** — `utilities/*.sas` (e.g. `validate_spreadsheet_sdtm.sas`,
   `convert_bc_xlsx2yaml.sas`) and the shared macros in `utilities/macros/` validate the curation
   spreadsheets and convert them into YAML, written to `yaml/<release>/{bc,sdtm,crf}/` (release folders
   are named `YYYYMMDD_rN`, e.g. `yaml/20260714_r18/`). A full, faithful Python port of this SAS
   pipeline now lives under `scripts/` (drivers) and `scripts/cosmoslib/` (shared library) — see
   "Python pipeline" under Commands below. Both toolchains read the same curation spreadsheets and
   produce byte-for-byte-equivalent YAML (verified via golden-file regression tests); the SAS files are
   unmodified and still work, kept side by side until the team is ready to retire them.
3. **Schema validation** — `scripts/validate_yaml.py` validates those YAML files against the canonical
   LinkML schema in `model/` using the `linkml` validator.
4. **Excel/CSV regeneration** — `scripts/create_cosmos_bc_excel.py`, `create_cosmos_sdtm_excel.py`, and
   `create_cosmos_crf_excel.py` build the polished "latest" spreadsheets/CSVs in `export/`, sourcing data
   either from local YAML (`-s YAML`) or directly from the live CDISC Library API (`-s API` /
   `-s APIDEV`).
5. **Model regeneration** — `model/cosmos_bc_model.yaml`, `cosmos_sdtm_model.yaml`, and
   `cosmos_crf_model.yaml` are the canonical LinkML schemas. The `scripts/cosmos_*_model_generate.cmd`
   batch scripts (Windows only) regenerate everything derived from them: JSON Schema, SVG/yUML diagrams,
   Markdown ER docs, and Python/Pydantic classes under `model/` and `project/{bc,sdtm,crf}/`.
6. **Live API checks** — `scripts/verify_cosmos_data.py` and `scripts/check_concept_status.py` call the
   CDISC Library API (and NCI EVS for concept status) to sanity-check package counts and flag retired
   NCIt concepts referenced by BCs/DECs.

When asked to trace or fix "why does this BC/SDTM value look wrong," follow this pipeline in order —
the root cause is usually in the curation spreadsheet or the LinkML schema, not in the generated
YAML/Excel/CSV downstream of it.

## Commands

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Lint (flake8, config in `.flake8`: max line length 120, max complexity 10):

```bash
flake8
```

Validate YAML against the LinkML schema:

```bash
python scripts/validate_yaml.py -y yaml/20260714_r18/bc -s model/cosmos_bc_model.yaml -c BiomedicalConcept
python scripts/validate_yaml.py -y yaml/20260714_r18/sdtm -s model/cosmos_sdtm_model.yaml -c SDTMGroup
python scripts/validate_yaml.py -y yaml/20251231_draft/bc -s model/cosmos_crf_model.yaml -c CRFGroup
```

Regenerate an export spreadsheet from YAML or the live API:

```bash
python scripts/create_cosmos_bc_excel.py -s YAML -y yaml/20260714_r18/bc -o curation/draft/cdisc_biomedical_concepts_r18_draft.xlsx -d 2026-07-14
python scripts/create_cosmos_bc_excel.py -s API -o export/cdisc_biomedical_concepts_latest.xlsx -d 2026-07-14
```

(`create_cosmos_sdtm_excel.py` and `create_cosmos_crf_excel.py` share the same `-s/-y/-o/-d` interface.)
`-s` accepts `API` (production), `APIDEV` (dev environment), or `YAML` (local files via `-y`).

Check for retired NCIt concepts referenced by curated BCs/DECs:

```bash
python scripts/check_concept_status.py
```

Sanity-check API package/record counts against expected values (edit `RESPONSE_DATA` in the script when a
new package is released):

```bash
python scripts/verify_cosmos_data.py -e dev
python scripts/verify_cosmos_data.py -e prod
```

Regenerate model artifacts (JSON Schema, diagrams, Python/Pydantic) from a LinkML schema — Windows-only,
requires a `venv` with `linkml` installed and its `gen-*` console scripts on `PATH`:

```
scripts\cosmos_bc_model_generate.cmd
scripts\cosmos_sdtm_model_generate.cmd
scripts\cosmos_crf_model_generate.cmd
```

Build the documentation site (mkdocs, sources from `project/docs`, outputs to `docs/`):

```bash
mkdocs build
mkdocs serve
```

### Python pipeline (port of the SAS scripts)

Install dev dependencies (adds `pytest`/`responses` on top of `requirements.txt`):

```bash
pip install -r requirements-dev.txt
```

Run the test suite (golden-file regression tests diff generated output against already-published
YAML under `yaml/`; unit tests cover individual converter/validator rules):

```bash
pytest
```

Refresh the reference-data caches under `utilities/data/*.json` (gitignored; each converter/validator
reads them read-only and errors out with instructions if missing):

```bash
python scripts/refresh_enums.py
python scripts/refresh_codelists.py
python scripts/refresh_sdtm_relations.py    # slowest refresh, crawls every published SDTM specialization
```

Convert curation spreadsheets to YAML, using a release manifest (`utilities/manifests/{bc,sdtm,crf}/*.yaml`)
in place of SAS's hand-edited per-release comment blocks:

```bash
python scripts/convert_bc_xlsx2yaml.py --manifest utilities/manifests/bc/20260714_r18.yaml
python scripts/convert_sdtm_xlsx2yaml.py --manifest utilities/manifests/sdtm/20260714_r18.yaml
python scripts/convert_crf_xlsx2yaml.py --manifest utilities/manifests/crf/20260630_draft.yaml
python scripts/convert_latest_xlsx2yaml.py --domain bc --release 20260714_r18   # or --domain sdtm
```

Run the cross-workbook validators (unresolved BC/DEC/SDTM references, duplicates, retired-BC pointers,
character-coding issues):

```bash
python scripts/validate_spreadsheet_sdtm.py
python scripts/validate_spreadsheet_crf.py
```

Every driver script writes a structured issues report (`utilities/reports/*_issues_<release>.{csv,xlsx}`,
gitignored) plus a console severity-count summary, and accepts `-h`/`--help` for its full flag list
(cache paths, `--no-cache`/`--refresh-cache`, DHT-variant flags on the validators, etc).

`verify_cosmos_data.py` and `validate_yaml.py` are the two other things in this repo close to tests
(both run manually, outside `pytest`); there is no CI workflow.

## Environment variables

Scripts that call the CDISC Library API read credentials from the environment (typically via a
gitignored `.env` file loaded with `python-dotenv`):

- `CDISC_LIBRARY_API_KEY` / `CDISC_LIBRARY_API_URL` — production
- `CDISC_LIBRARY_API_KEY_DEV` / `CDISC_LIBRARY_API_URL_DEV` — dev environment

## Working with the LinkML schemas

- `model/cosmos_bc_model.yaml` defines `BiomedicalConcept` (tree root), `DataElementConcept`, and
  `Coding`. `model/cosmos_sdtm_model.yaml` and `model/cosmos_crf_model.yaml` follow the analogous
  pattern for SDTM Dataset Specializations and CRF Specializations respectively.
- `model/.linkmllint.yaml` extends the `recommended` lint config, disables `standard_naming`, and
  enforces `tree_root_class` as an error — keep new classes conformant with that.
- Every generated artifact under `model/` (`.json`, `.svg`, `.yuml`, `.md`) and `project/{bc,sdtm,crf}/`
  is derived from the corresponding `.yaml` schema — edit the schema and regenerate, never hand-edit the
  generated files.
