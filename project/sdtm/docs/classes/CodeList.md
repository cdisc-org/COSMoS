

# Class: CodeList 



URI: [cosmos_sdtm:class/CodeList](https://www.cdisc.org/cosmos/sdtm_v1.0/class/CodeList)


```mermaid
erDiagram
CodeList {
    string conceptId  
    uri href  
    string submissionValue  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [conceptId](../slots/conceptId.md) | 1 <br/> [String](../types/String.md) | C-code for a codelist in NCIt | direct |
| [href](../slots/href.md) | 0..1 <br/> [Uri](../types/Uri.md) | Link to NCIt for the codelist | direct |
| [submissionValue](../slots/submissionValue.md) | 1 <br/> [String](../types/String.md) | CDISC submission value for the codelist | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SDTMVariable](../classes/SDTMVariable.md) | [codelist](../slots/codelist.md) | range | [CodeList](../classes/CodeList.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cosmos_sdtm:CodeList |
| native | cosmos_sdtm:CodeList |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CodeList
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
slots:
- conceptId
- href
- submissionValue

```
</details>

### Induced

<details>
```yaml
name: CodeList
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
attributes:
  conceptId:
    name: conceptId
    description: C-code for a codelist in NCIt
    from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
    rank: 1000
    identifier: true
    alias: conceptId
    owner: CodeList
    domain_of:
    - CodeList
    - AssignedTerm
    range: string
    required: true
    pattern: ^(C[0-9]+|CNEW)$
  href:
    name: href
    description: Link to NCIt for the codelist
    from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
    rank: 1000
    alias: href
    owner: CodeList
    domain_of:
    - CodeList
    range: uri
    required: false
  submissionValue:
    name: submissionValue
    description: CDISC submission value for the codelist
    from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
    rank: 1000
    alias: submissionValue
    owner: CodeList
    domain_of:
    - CodeList
    range: string
    required: true
    pattern: ^[A-Z][A-Z0-9_]*$

```
</details>