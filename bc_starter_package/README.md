# CDISC Biomedical Concepts Starter Package

<img src="../utilities/images/2023_Standards-Badges_v5.2-BCs.png" alt="Biomedical Concepts" width="150"/>

## Use cases

- [Users who want to create CDISC BCs and Dataset Specializations](README.md#usecase1)
- [Users who want to retrieve and use BCs and Dataset Specializations from the CDISC Library](README.md#usecase2)
- [Users who want to provide feedback on BCs and Dataset Specializations](README.md#usecase3)

## Use Case: Users who want to create CDISC BCs and Dataset Specializations<a id='usecase1'></a>

- [Biomedical Concepts Overview Training](doc/BC%20Overview%20Training.pdf)
- [High Level Biomedical Concept Process](doc/High%20Level%20Biomedical%20Concept%20Process.pdf)
- [BC Curation Principles and Completion Guidelines](doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx) (Excel spreadsheet)
- [BC DEC Templates](doc/BC%20DEC%20Templates.xlsx) (Excel spreadsheet)
- [BC Governance Process](doc/BC%20Governance%20Process.jpg)
- [Charter for COSMoS\_V1](doc/Charter%20for%20COSMOS_V1.pdf)
- [Charter for COSMoS\_V2](doc/Charter%20for%20COSMOS_V2.pdf)

## Use Case: Users who want to retrieve and use BCs and Dataset Specializations from the CDISC Library<a id='usecase2'></a>

- [Biomedical Concepts Overview Training](doc/BC%20Overview%20Training.pdf)

All technical documentation for CDISC Biomedical Concepts and Dataset Specialization, can be found in the CDISC [COSMoS GitHub repository](https://github.com/cdisc-org/COSMoS).

- Curation Excel files used for loading BCs and Dataset Specializations
- Data Models according to linkml specification and associated files
- OpenAPI definition of the API
- Utilities to generate YAML files from spreadsheet content
- YAML files generated from spreadsheet content
- Scripts to validate YAML files

Documentation for CDISC APIs can be found at [https://api.developer.library.cdisc.org/](https://api.developer.library.cdisc.org/).  Users should use their existing CDISC login credentials.   The latest release notes for the CDISC Biomedical Concepts and Dataset Specialization are at the [CDISC Wiki](https://wiki.cdisc.org/pages/viewpage.action?pageId=169412277).

The most current API endpoints for CDISC BCs and SDTM Dataset Specializations are available in API version 2. Version 1 has been superseded, and users should use version 2 when retrieving content.  

All API requests need to include the version as noted in the example below. If a user does not specify a version, a 404 API response code (Not Found) will be returned.  

 ` /cosmos/v2/mdr/bc/packages/2022-10-26/biomedicalconcepts/C64547 `

The SDTM Dataset Specializations can be considered pre-configured building blocks, from which end-users can select and configure to build Value Level Metadata, which is an important part of the metadata for their Define-XML.

This [paper](https://www.lexjansen.com/pharmasug/2023/SS/PharmaSUG-2023-SS-140.pdf) will show how SDTM Dataset Specializations can be used by the Open Source release of SAS Clinical Standards Toolkit (openCST) for the creation of Value Level Metadata in Define-XML v2.1 (slides and code at [GitHub](https://github.com/lexjansen/sas-papers/tree/master/pharmasug-2023) (PharmaSUG 2023) and [GitHub](https://github.com/lexjansen/CDISC_Interchange_US_2023) (CDISC US Interchange 2023).

## Use Case: Users who want to provide feedback on BCs and Dataset Specializations<a id='usecase3'></a>

- [Biomedical Concepts Overview Training](doc/BC%20Overview%20Training.pdf)
- [BC Governance Process](doc/BC%20Governance%20Process.jpg)

Give feedback or gain clarification on BC and Dataset Specialization content, data models, APIs

- [JIRA](https://wiki.cdisc.org/display/PUB/Biomedical+Concepts), our issue-tracking system

Refer to BC and Dataset Specialization Curation Principles and Guidelines to understand how  metadata is defined.

- [BC Curation Principles and Completion Guidelines](doc/BC%20Curation%20Principles%20and%20Completion%20GLs.xlsx)
