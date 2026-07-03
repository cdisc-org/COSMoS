

# Slot: name 


_Item name as it appears on the CRF instrument_





URI: [cosmos_crf:slot/name](https://www.cdisc.org/cosmos/crf_v1.0slot/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFItem](../classes/CRFItem.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^[A-Z][A-Z0-9_]*$`



## Aliases


* crf_item


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:name |
| native | cosmos_crf:name |




## LinkML Source

<details>
```yaml
name: name
description: Item name as it appears on the CRF instrument
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- crf_item
rank: 1000
identifier: true
alias: name
domain_of:
- CRFItem
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>