

# Slot: packageType 


_Package type for CRF specializations (crf)_





URI: [cosmos_crf:slot/packageType](https://www.cdisc.org/cosmos/crf_v1.0slot/packageType)
Alias: packageType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFGroup](../classes/CRFGroup.md) |  |  no  |






## Properties

* Range: [PackageTypeEnum](../enums/PackageTypeEnum.md)

* Required: True



## Aliases


* package_type


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:packageType |
| native | cosmos_crf:packageType |




## LinkML Source

<details>
```yaml
name: packageType
description: Package type for CRF specializations (crf)
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- package_type
rank: 1000
alias: packageType
domain_of:
- CRFGroup
range: PackageTypeEnum
required: true

```
</details>