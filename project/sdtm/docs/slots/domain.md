

# Slot: domain 


_Domain for the SDTM specialization group_





URI: [cosmos_sdtm:slot/domain](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/domain)
Alias: domain

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMGroup](../classes/SDTMGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:domain |
| native | cosmos_sdtm:domain |




## LinkML Source

<details>
```yaml
name: domain
description: Domain for the SDTM specialization group
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: domain
domain_of:
- SDTMGroup
range: string
required: true

```
</details>