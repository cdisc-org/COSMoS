

# Slot: value 


_CDISC submission value for the CRF item_





URI: [cosmos_crf:slot/value](https://www.cdisc.org/cosmos/crf_v1.0slot/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PrepopulatedValue](../classes/PrepopulatedValue.md) |  |  yes  |
| [ListValue](../classes/ListValue.md) |  |  yes  |






## Properties

* Range: [String](../types/String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:value |
| native | cosmos_crf:value |




## LinkML Source

<details>
```yaml
name: value
description: CDISC submission value for the CRF item
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
rank: 1000
alias: value
domain_of:
- ListValue
- PrepopulatedValue
range: string

```
</details>