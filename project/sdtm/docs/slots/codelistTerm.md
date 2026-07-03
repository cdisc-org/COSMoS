

# Slot: codelistTerm 


_Term in subset codelist_





URI: [cosmos_sdtm:slot/codelistTerm](https://www.cdisc.org/cosmos/sdtm_v1.0/slot/codelistTerm)
Alias: codelistTerm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubsetCodeList](../classes/SubsetCodeList.md) |  |  no  |






## Properties

* Range: [CodeListTerm](../classes/CodeListTerm.md)

* Multivalued: True

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:codelistTerm |
| native | cosmos_sdtm:codelistTerm |




## LinkML Source

<details>
```yaml
name: codelistTerm
description: Term in subset codelist
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
alias: codelistTerm
domain_of:
- SubsetCodeList
range: CodeListTerm
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>