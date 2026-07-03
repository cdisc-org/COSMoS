

# Slot: dataType 


_Item data type_





URI: [cosmos_crf:slot/dataType](https://www.cdisc.org/cosmos/crf_v1.0slot/dataType)
Alias: dataType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFItem](../classes/CRFItem.md) |  |  no  |






## Properties

* Range: [CRFItemDataTypeEnum](../enums/CRFItemDataTypeEnum.md)

* Required: True



## Aliases


* data_type


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:dataType |
| native | cosmos_crf:dataType |




## LinkML Source

<details>
```yaml
name: dataType
description: Item data type
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- data_type
rank: 1000
alias: dataType
domain_of:
- CRFItem
range: CRFItemDataTypeEnum
required: true

```
</details>