

# Slot: system 


_Identifies the code system for the synonym concept. The URL of the code system should be used if it exists_





URI: [cosmos_bc:slot/system](https://www.cdisc.org/cosmos/biomedical_concept_v1.0slot/system)
Alias: system

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Coding](../classes/Coding.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_bc:system |
| native | cosmos_bc:system |




## LinkML Source

<details>
```yaml
name: system
description: Identifies the code system for the synonym concept. The URL of the code
  system should be used if it exists
from_schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0
rank: 1000
alias: system
domain_of:
- Coding
range: string
required: true

```
</details>