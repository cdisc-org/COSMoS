

# Slot: items 


_Items included in the CRF specialization_





URI: [cosmos_crf:slot/items](https://www.cdisc.org/cosmos/crf_v1.0slot/items)
Alias: items

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFGroup](../classes/CRFGroup.md) |  |  no  |






## Properties

* Range: [CRFItem](../classes/CRFItem.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:items |
| native | cosmos_crf:items |




## LinkML Source

<details>
```yaml
name: items
description: Items included in the CRF specialization
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
rank: 1000
alias: items
domain_of:
- CRFGroup
range: CRFItem
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>