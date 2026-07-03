

# Slot: variables 


_Variable included in the SDTM dataset specialization_





URI: [cosmos_sdtm:slot/variables](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/variables)
Alias: variables

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMGroup](../classes/SDTMGroup.md) |  |  no  |






## Properties

* Range: [SDTMVariable](../classes/SDTMVariable.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:variables |
| native | cosmos_sdtm:variables |




## LinkML Source

<details>
```yaml
name: variables
description: Variable included in the SDTM dataset specialization
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: variables
domain_of:
- SDTMGroup
range: SDTMVariable
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>