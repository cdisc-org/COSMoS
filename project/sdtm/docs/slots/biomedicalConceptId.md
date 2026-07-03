

# Slot: biomedicalConceptId 


_Biomedical Concept identifier foreign key_





URI: [cosmos_sdtm:slot/biomedicalConceptId](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/biomedicalConceptId)
Alias: biomedicalConceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMGroup](../classes/SDTMGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Recommended: True

* Regex pattern: `^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:biomedicalConceptId |
| native | cosmos_sdtm:biomedicalConceptId |




## LinkML Source

<details>
```yaml
name: biomedicalConceptId
description: Biomedical Concept identifier foreign key
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: biomedicalConceptId
domain_of:
- SDTMGroup
range: string
recommended: true
pattern: ^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$

```
</details>