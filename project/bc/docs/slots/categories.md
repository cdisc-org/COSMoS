

# Slot: categories 


_Biomedical Concept category for the faciliation of API search and extract_





URI: [cosmos_bc:slot/categories](https://www.cdisc.org/cosmos/biomedical_concept_v1.0slot/categories)
Alias: categories

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConcept](../classes/BiomedicalConcept.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_bc:categories |
| native | cosmos_bc:categories |




## LinkML Source

<details>
```yaml
name: categories
description: Biomedical Concept category for the faciliation of API search and extract
from_schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0
rank: 1000
alias: categories
domain_of:
- BiomedicalConcept
range: string
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>