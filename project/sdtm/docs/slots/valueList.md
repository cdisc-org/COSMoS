

# Slot: valueList 


_List of SDTM submission values used if subset codelist is not applicable_





URI: [cosmos_sdtm:slot/valueList](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/valueList)
Alias: valueList

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMVariable](../classes/SDTMVariable.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:valueList |
| native | cosmos_sdtm:valueList |




## LinkML Source

<details>
```yaml
name: valueList
description: List of SDTM submission values used if subset codelist is not applicable
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: valueList
domain_of:
- SDTMVariable
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>