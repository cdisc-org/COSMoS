

# Slot: biomedicalConceptId 


_Biomedical Concept identifier foreign key_





URI: [cosmos_crf:slot/biomedicalConceptId](https://www.cdisc.org/cosmos/crf_v1.0slot/biomedicalConceptId)
Alias: biomedicalConceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFGroup](../classes/CRFGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Recommended: True

* Regex pattern: `^(C[0-9]+|NEW_[A-Z]*[0-9]*)$`



## Aliases


* bc_id


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:biomedicalConceptId |
| native | cosmos_crf:biomedicalConceptId |




## LinkML Source

<details>
```yaml
name: biomedicalConceptId
description: Biomedical Concept identifier foreign key
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- bc_id
rank: 1000
alias: biomedicalConceptId
domain_of:
- CRFGroup
range: string
recommended: true
pattern: ^(C[0-9]+|NEW_[A-Z]*[0-9]*)$

```
</details>