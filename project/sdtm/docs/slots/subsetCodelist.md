

# Slot: subsetCodelist 


_Subset codelist short name_





URI: [cosmos_sdtm:slot/subsetCodelist](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/subsetCodelist)
Alias: subsetCodelist

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMVariable](../classes/SDTMVariable.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Regex pattern: `^[A-Z][A-Z0-9_]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:subsetCodelist |
| native | cosmos_sdtm:subsetCodelist |




## LinkML Source

<details>
```yaml
name: subsetCodelist
description: Subset codelist short name
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: subsetCodelist
domain_of:
- SDTMVariable
range: string
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>