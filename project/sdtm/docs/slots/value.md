

# Slot: value 


_Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value_





URI: [cosmos_sdtm:slot/value](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/value)
Alias: value

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssignedTerm](../classes/AssignedTerm.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:value |
| native | cosmos_sdtm:value |




## LinkML Source

<details>
```yaml
name: value
description: Submission value for assigned term in NCIt if it exists, or an assigned
  value which will be the default value
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: value
owner: AssignedTerm
domain_of:
- AssignedTerm
range: string
required: true

```
</details>