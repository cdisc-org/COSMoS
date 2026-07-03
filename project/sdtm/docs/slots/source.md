

# Slot: source 


_SDTM VLM Source which categorizes VLM groups by topic variable_





URI: [cosmos_sdtm:slot/source](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/source)
Alias: source

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SDTMGroup](../classes/SDTMGroup.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:source |
| native | cosmos_sdtm:source |




## LinkML Source

<details>
```yaml
name: source
description: SDTM VLM Source which categorizes VLM groups by topic variable
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: source
domain_of:
- SDTMGroup
range: string
required: true

```
</details>