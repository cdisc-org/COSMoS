

# Slot: ncitCode 


_NCIt code_





URI: [cosmos_bc:slot/ncitCode](https://www.cdisc.org/cosmos/biomedical_concept_v1.0slot/ncitCode)
Alias: ncitCode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConcept](../classes/BiomedicalConcept.md) |  |  yes  |
| [DataElementConcept](../classes/DataElementConcept.md) |  |  yes  |






## Properties

* Range: [String](../types/String.md)

* Regex pattern: `^(C[0-9]+)$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_bc:ncitCode |
| native | cosmos_bc:ncitCode |




## LinkML Source

<details>
```yaml
name: ncitCode
description: NCIt code
from_schema: https://www.cdisc.org/cosmos/biomedical_concept_v1.0
rank: 1000
alias: ncitCode
domain_of:
- BiomedicalConcept
- DataElementConcept
range: string
pattern: ^(C[0-9]+)$

```
</details>