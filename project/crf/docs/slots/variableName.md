

# Slot: variableName 


_Variable name of the CRF item for which data are being collected._





URI: [cosmos_crf:slot/variableName](https://www.cdisc.org/cosmos/crf_v1.0slot/variableName)
Alias: variableName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CRFItem](../classes/CRFItem.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^[A-Z][A-Z0-9_]*$`



## Aliases


* variable_name


## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:variableName |
| native | cosmos_crf:variableName |




## LinkML Source

<details>
```yaml
name: variableName
description: Variable name of the CRF item for which data are being collected.
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
aliases:
- variable_name
rank: 1000
alias: variableName
domain_of:
- CRFItem
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>