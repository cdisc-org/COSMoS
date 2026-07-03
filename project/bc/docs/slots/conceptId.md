

# Slot: conceptId 


_An identifier that uniquely represents an entity_





URI: [cosmos_bc:slot/conceptId](https://www.cdisc.org/cosmos/biomedical_concept_v1.0slot/conceptId)
Alias: conceptId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConcept](../classes/BiomedicalConcept.md) |  |  yes  |
| [DataElementConcept](../classes/DataElementConcept.md) |  |  yes  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_bc:conceptId |
| native | cosmos_bc:conceptId |




## LinkML Source

<details>
```yaml
name: conceptId
description: An identifier that uniquely represents an entity
from_schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0
rank: 1000
identifier: true
alias: conceptId
domain_of:
- BiomedicalConcept
- DataElementConcept
range: string
required: true
pattern: ^(C[0-9]+|NEW_[A-Z_]*[0-9]*)$

```
</details>