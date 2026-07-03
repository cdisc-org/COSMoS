

# Slot: packageDate 


_Biomedical Concept package release date indicating when the BC package was published to production_





URI: [cosmos_crf:slot/packageDate](https://www.cdisc.org/cosmos/crf_v1.0slot/packageDate)
Alias: packageDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFGroup](../classes/CRFGroup.md) |  |  no  |






## Properties

* Range: [Date](../types/Date.md)

* Required: True



## Aliases


* package_date


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:packageDate |
| native | cosmos_crf:packageDate |




## LinkML Source

<details>
```yaml
name: packageDate
description: Biomedical Concept package release date indicating when the BC package
  was published to production
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- package_date
rank: 1000
alias: packageDate
domain_of:
- CRFGroup
range: date
required: true

```
</details>