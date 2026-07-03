

# Slot: dataElementConceptId 


_Biomedical Concept Data Element Concept identifier foreign key_





URI: [cosmos_crf:slot/dataElementConceptId](https://www.cdisc.org/cosmos/crf_v1.0slot/dataElementConceptId)
Alias: dataElementConceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFItem](../classes/CRFItem.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Regex pattern: `^(C[0-9]+|NEW_[A-Z]*[0-9]*)$`



## Aliases


* dec_id


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:dataElementConceptId |
| native | cosmos_crf:dataElementConceptId |




## LinkML Source

<details>
```yaml
name: dataElementConceptId
description: Biomedical Concept Data Element Concept identifier foreign key
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- dec_id
rank: 1000
alias: dataElementConceptId
domain_of:
- CRFItem
range: string
pattern: ^(C[0-9]+|NEW_[A-Z]*[0-9]*)$

```
</details>