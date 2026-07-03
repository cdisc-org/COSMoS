

# Slot: conceptId 


_C-code for codelist or term in NCIt_





URI: [cosmos_crf:slot/conceptId](https://www.cdisc.org/cosmos/crf_v1.0slot/conceptId)
Alias: conceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrepopulatedValue](../classes/PrepopulatedValue.md) |  |  yes  |
| [CodeList](../classes/CodeList.md) |  |  yes  |






## Properties

* Range: [String](../types/String.md)

* Regex pattern: `^(C[0-9]+)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:conceptId |
| native | cosmos_crf:conceptId |




## LinkML Source

<details>
```yaml
name: conceptId
description: C-code for codelist or term in NCIt
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
rank: 1000
alias: conceptId
domain_of:
- PrepopulatedValue
- CodeList
range: string
pattern: ^(C[0-9]+)$

```
</details>