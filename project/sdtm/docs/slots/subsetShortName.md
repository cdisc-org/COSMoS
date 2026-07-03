

# Slot: subsetShortName 


_Subset codelist short name_





URI: [cosmos_sdtm:slot/subsetShortName](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/subsetShortName)
Alias: subsetShortName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubsetCodeList](../classes/SubsetCodeList.md) |  |  no  |






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
| self | cosmos_sdtm:subsetShortName |
| native | cosmos_sdtm:subsetShortName |




## LinkML Source

<details>
```yaml
name: subsetShortName
description: Subset codelist short name
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: subsetShortName
domain_of:
- SubsetCodeList
range: string
required: true
pattern: ^[A-Z][A-Z0-9_]*$

```
</details>