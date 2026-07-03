

# Slot: submissionValue 


_CDISC submission value_





URI: [cosmos_crf:slot/submissionValue](https://www.cdisc.org/cosmos/crf_v1.0slot/submissionValue)
Alias: submissionValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CodeList](../classes/CodeList.md) |  |  yes  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^[A-Z][A-Z0-9_]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/crf_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_crf:submissionValue |
| native | cosmos_crf:submissionValue |




## LinkML Source

<details>
```yaml
name: submissionValue
description: CDISC submission value
from_schema: https://www.cdisc.org/cosmos/crf_v1.0
rank: 1000
alias: submissionValue
domain_of:
- CodeList
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>