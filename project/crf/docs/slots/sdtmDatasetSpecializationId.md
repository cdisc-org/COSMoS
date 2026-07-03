

# Slot: sdtmDatasetSpecializationId 


_Identifier for SDTM Dataset Specialization group_





URI: [cosmos_crf:slot/sdtmDatasetSpecializationId](https://www.cdisc.org/cosmos/crf_v1.0slot/sdtmDatasetSpecializationId)
Alias: sdtmDatasetSpecializationId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFGroup](../classes/CRFGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Regex pattern: `^[A-Z][A-Z0-9_]*$`



## Aliases


* vlm_group_id


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:sdtmDatasetSpecializationId |
| native | cosmos_crf:sdtmDatasetSpecializationId |




## LinkML Source

<details>
```yaml
name: sdtmDatasetSpecializationId
description: Identifier for SDTM Dataset Specialization group
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- vlm_group_id
rank: 1000
alias: sdtmDatasetSpecializationId
domain_of:
- CRFGroup
range: string
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>