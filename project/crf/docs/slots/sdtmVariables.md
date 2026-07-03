

# Slot: sdtmVariables 


_SDTM target variable for CRF item variable_





URI: [cosmos_crf:slot/sdtmVariables](https://www.cdisc.org/cosmos/crf_v1.0slot/sdtmVariables)
Alias: sdtmVariables

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMTarget](../classes/SDTMTarget.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Multivalued: True



## Aliases


* sdtm_target_variable


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:sdtmVariables |
| native | cosmos_crf:sdtmVariables |




## LinkML Source

<details>
```yaml
name: sdtmVariables
description: SDTM target variable for CRF item variable
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- sdtm_target_variable
rank: 1000
alias: sdtmVariables
domain_of:
- SDTMTarget
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>