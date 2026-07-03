

# Slot: packageDate 


_Biomedical Concept package release date indicating when the BC package was published to production_





URI: [cosmos_sdtm:slot/packageDate](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/packageDate)
Alias: packageDate

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMGroup](../classes/SDTMGroup.md) |  |  no  |






## Properties

* Range: [Date](../types/Date.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:packageDate |
| native | cosmos_sdtm:packageDate |




## LinkML Source

<details>
```yaml
name: packageDate
description: Biomedical Concept package release date indicating when the BC package
  was published to production
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: packageDate
domain_of:
- SDTMGroup
range: date
required: true

```
</details>