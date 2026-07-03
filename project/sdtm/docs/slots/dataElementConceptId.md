

# Slot: dataElementConceptId 


_Biomedical Concept Data Element Concept identifier foreign key_





URI: [cosmos_sdtm:slot/dataElementConceptId](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/dataElementConceptId)
Alias: dataElementConceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMVariable](../classes/SDTMVariable.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Regex pattern: `^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:dataElementConceptId |
| native | cosmos_sdtm:dataElementConceptId |




## LinkML Source

<details>
```yaml
name: dataElementConceptId
description: Biomedical Concept Data Element Concept identifier foreign key
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: dataElementConceptId
domain_of:
- SDTMVariable
range: string
pattern: ^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$

```
</details>