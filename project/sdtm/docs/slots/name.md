

# Slot: name 


_Variable included in the SDTM dataset specialization_





URI: [cosmos_sdtm:slot/name](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/name)
Alias: name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMVariable](../classes/SDTMVariable.md) |  |  no  |






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
| self | cosmos_sdtm:name |
| native | cosmos_sdtm:name |




## LinkML Source

<details>
```yaml
name: name
description: Variable included in the SDTM dataset specialization
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
identifier: true
alias: name
domain_of:
- SDTMVariable
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>