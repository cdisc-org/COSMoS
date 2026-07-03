

# Slot: termId 


_C-code term in subset codelist_





URI: [cosmos_sdtm:slot/termId](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/termId)
Alias: termId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CodeListTerm](../classes/CodeListTerm.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^(C[0-9]+)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:termId |
| native | cosmos_sdtm:termId |




## LinkML Source

<details>
```yaml
name: termId
description: C-code term in subset codelist
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: termId
domain_of:
- CodeListTerm
range: string
required: true
pattern: ^(C[0-9]+)$

```
</details>