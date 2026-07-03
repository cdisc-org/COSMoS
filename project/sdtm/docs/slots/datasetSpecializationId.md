

# Slot: datasetSpecializationId 


_Identifier for SDTM Value Level Metadata group_





URI: [cosmos_sdtm:slot/datasetSpecializationId](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/datasetSpecializationId)
Alias: datasetSpecializationId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMGroup](../classes/SDTMGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^[A-Z][A-Z0-9_]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:datasetSpecializationId |
| native | cosmos_sdtm:datasetSpecializationId |




## LinkML Source

<details>
```yaml
name: datasetSpecializationId
description: Identifier for SDTM Value Level Metadata group
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
identifier: true
alias: datasetSpecializationId
domain_of:
- SDTMGroup
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>