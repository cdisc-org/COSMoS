

# Slot: parentCodelist 


_Subset codelist parent codelist_





URI: [cosmos_sdtm:slot/parentCodelist](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/parentCodelist)
Alias: parentCodelist

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubsetCodeList](../classes/SubsetCodeList.md) |  |  no  |






## Properties

* Range: [String](../types/String.md)

* Required: True

* Regex pattern: `^C[0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:parentCodelist |
| native | cosmos_sdtm:parentCodelist |




## LinkML Source

<details>
```yaml
name: parentCodelist
description: Subset codelist parent codelist
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: parentCodelist
domain_of:
- SubsetCodeList
range: string
required: true
pattern: ^C[0-9]+$

```
</details>