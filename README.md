# CDISC Conceptual and Operational Standards Metadata (COSMoS)

This repository contains working files to implement Biomedical Concepts and Dataset Specializations in the CDISC Library:

- **curation**
  - Spreadsheets that were used for initial loading of BCs and SDTM Specializations.

- **model**
  - Model files (cosmos_bc_model.yaml and cosmos_sdtm_bc_model.yaml) according to the [linkml](https://linkml.io/linkml/) specification.
    It also contains several other files auto generated from the model:
    - cosmos_bc_model.json amd cosmos_sdtm_bc_model.json:
    JSON schema files describing the machine-readable YAML files
    - cosmos_bc_model.svg, cosmos_bc_model.yuml, cosmos_sdtm_bc_model.svg, cosmos_sdtm_bc_model.yuml:
    Entity diagrams
    - cosmos_bc_model.py, cosmos_sdtm_bc_model.py:
    Python models

- **openapi**
  - OpenAPI definition of the API (cosmos.yaml)

- **utilities**
  - Utilities to generate YAML files from the curation spreadsheets

- **yaml**
  - YAML files generated from the curation spreadsheets
  - Scripts to validate the YAML files
