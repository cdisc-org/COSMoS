# Enum: OriginTypeEnum 




_Terminology relevant to the origin type for datasets in the Define-XML document._



URI: [cosmos_sdtm:enum/OriginTypeEnum](https://www.cdisc.org/cosmos/sdtm_v1.0/enum/OriginTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Assigned | NCIT:C170547 | A value that is derived through designation, such as values from a look up table or a label on a CRF. |
| Collected | NCIT:C170548 | A value that is actually observed and recorded by a person or obtained by an instrument. |
| Derived | NCIT:C170549 | A value that is calculated by an algorithm or reproducible rule, and which is dependent upon other data values. |
| Predecessor | NCIT:C170550 | A value that is copied from a variable in another dataset. |
| Protocol | NCIT:C170551 | A value that is included as part of the study protocol. |




## Slots

| Name | Description |
| ---  | --- |
| [originType](../slots/originType.md) | Variable origin type (define-XML v21) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0






## LinkML Source

<details>
```yaml
name: OriginTypeEnum
description: Terminology relevant to the origin type for datasets in the Define-XML
  document.
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
code_set: NCIT:C170449
permissible_values:
  Assigned:
    text: Assigned
    description: A value that is derived through designation, such as values from
      a look up table or a label on a CRF.
    meaning: NCIT:C170547
  Collected:
    text: Collected
    description: A value that is actually observed and recorded by a person or obtained
      by an instrument.
    meaning: NCIT:C170548
  Derived:
    text: Derived
    description: A value that is calculated by an algorithm or reproducible rule,
      and which is dependent upon other data values.
    meaning: NCIT:C170549
  Predecessor:
    text: Predecessor
    description: A value that is copied from a variable in another dataset.
    meaning: NCIT:C170550
  Protocol:
    text: Protocol
    description: A value that is included as part of the study protocol.
    meaning: NCIT:C170551

```
</details>