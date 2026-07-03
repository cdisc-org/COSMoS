

# Slot: crfSpecializationId 


_Identifier for CRF specialization group_





URI: [cosmos_crf:slot/crfSpecializationId](https://www.cdisc.org/cosmos/crf_v1.0slot/crfSpecializationId)
Alias: crfSpecializationId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFGroup](../classes/CRFGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^[A-Z][A-Z0-9_]*$`



## Aliases


* crf_group_id


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:crfSpecializationId |
| native | cosmos_crf:crfSpecializationId |




## LinkML Source

<details>
```yaml
name: crfSpecializationId
description: Identifier for CRF specialization group
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- crf_group_id
rank: 1000
identifier: true
alias: crfSpecializationId
domain_of:
- CRFGroup
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>