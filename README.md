# CDISC Conceptual and Operational Standards Metadata (COSMoS)

This repository contains working files to implement Biomedical Concepts and Dataset Specializations in the CDISC Library:

- **curation**
  Spreadsheets that were used for loading of BCs and SDTM Specializations.

- **curation/draft**
  This folder contains draft curation spreadsheets that are still work in progress.
  The content in these draft spreadsheets is neither validated nor loaded in the CDISC Library.

- **model**
  Model files (cosmos_bc_model.yaml and cosmos_sdtm_bc_model.yaml) according to the [linkml](https://linkml.io/linkml/) specification.
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

## License

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) ![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-blue.svg)

### Code & Scripts

This project is using the [MIT](http://www.opensource.org/licenses/MIT "The MIT License | Open Source Initiative") license (see [`LICENSE`](LICENSE)) for code and scripts.

### Content

The content files like documentation and minutes are released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). This does not include trademark permissions.

## Re-use

When you re-use the source, keep or copy the license information also in the source code files. When you re-use the source in proprietary software or distribute binaries (derived or underived), copy additionally the license text to a third-party-licenses file or similar.

When you want to re-use and refer to the content, please do so like the following:

> Content based on [COSMoS (GitHub)](https://github.com/cdisc-org/COSMoS) used under the [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) license.
