

# Slot: conceptId 


_C-code for a codelist in NCIt_





URI: [cosmos_sdtm:slot/conceptId](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/conceptId)
Alias: conceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssignedTerm](../classes/AssignedTerm.md) |  |  no  |
| [CodeList](../classes/CodeList.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^(C[0-9]+|CNEW)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:conceptId |
| native | cosmos_sdtm:conceptId |




## LinkML Source

<details>
```yaml
name: conceptId
description: C-code for a codelist in NCIt
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
identifier: true
alias: conceptId
domain_of:
- CodeList
- AssignedTerm
range: string
required: true
pattern: ^(C[0-9]+|CNEW)$

```
</details>