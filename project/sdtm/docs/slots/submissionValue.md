

# Slot: submissionValue 


_CDISC submission value for the codelist_





URI: [cosmos_sdtm:slot/submissionValue](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/submissionValue)
Alias: submissionValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CodeList](../classes/CodeList.md) |  |  no  |






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
| self | cosmos_sdtm:submissionValue |
| native | cosmos_sdtm:submissionValue |




## LinkML Source

<details>
```yaml
name: submissionValue
description: CDISC submission value for the codelist
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: submissionValue
domain_of:
- CodeList
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>