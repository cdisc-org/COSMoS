

# Slot: mandatoryVariable 


_Indicator that the item must be present within the CRF group_





URI: [cosmos_crf:slot/mandatoryVariable](https://www.cdisc.org/cosmos/crf_v1.0slot/mandatoryVariable)
Alias: mandatoryVariable

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFItem](../classes/CRFItem.md) |  |  no  |






## Properties

* Range: [Boolean](../types/Boolean.md)

* Required: True



## Aliases


* mandatory_variable


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:mandatoryVariable |
| native | cosmos_crf:mandatoryVariable |




## LinkML Source

<details>
```yaml
name: mandatoryVariable
description: Indicator that the item must be present within the CRF group
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- mandatory_variable
rank: 1000
alias: mandatoryVariable
domain_of:
- CRFItem
range: boolean
required: true

```
</details>