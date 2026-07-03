

# Slot: valueList 


_A set of values for a CRF item_





URI: [cosmos_crf:slot/valueList](https://www.cdisc.org/cosmos/crf_v1.0slot/valueList)
Alias: valueList

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFItem](../classes/CRFItem.md) |  |  no  |






## Properties

* Range: [ListValue](../classes/ListValue.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:valueList |
| native | cosmos_crf:valueList |




## LinkML Source

<details>
```yaml
name: valueList
description: A set of values for a CRF item
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
rank: 1000
alias: valueList
domain_of:
- CRFItem
range: ListValue
multivalued: true
inlined: true
inlined_as_list: true

```
</details>