# Enum: OriginSourceEnum 




_Terminology relevant to the origin source for datasets in the Define-XML document._



URI: [cosmos_sdtm:enum/OriginSourceEnum](https://www.cdisc.org/cosmos/sdtm_v1.0/enum/OriginSourceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Investigator | NCIT:C25936 | A person responsible for the conduct of the clinical trial at a trial site. If a trial is conducted by a team of individuals at the trial site, the investigator is the responsible leader of the team and may be called the principal investigator. |
| Sponsor | NCIT:C70793 | An individual, company, institution, or organization that takes responsibility for the initiation, management, and/or financing of a clinical study. [After ICH E6, WHO, 21 CFR 50.3 (e), and after IDMP] |
| Subject | NCIT:C41189 | An individual who is observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study. |
| Vendor | NCIT:C68608 | A person or agency that promotes or exchanges goods or services for money. (NCI) |




## Slots

| Name | Description |
| ---  | --- |
| [originSource](../slots/originSource.md) | Variable origin source (define-XML v21) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://www.cdisc.org/cosmos/sdtm_v1.0






## LinkML Source

<details>
```yaml
name: OriginSourceEnum
description: Terminology relevant to the origin source for datasets in the Define-XML
  document.
from_schema: https://www.cdisc.org/cosmos/sdtm_v1.0
rank: 1000
code_set: NCIT:C170450
permissible_values:
  Investigator:
    text: Investigator
    description: A person responsible for the conduct of the clinical trial at a trial
      site. If a trial is conducted by a team of individuals at the trial site, the
      investigator is the responsible leader of the team and may be called the principal
      investigator.
    meaning: NCIT:C25936
  Sponsor:
    text: Sponsor
    description: An individual, company, institution, or organization that takes responsibility
      for the initiation, management, and/or financing of a clinical study. [After
      ICH E6, WHO, 21 CFR 50.3 (e), and after IDMP]
    meaning: NCIT:C70793
  Subject:
    text: Subject
    description: An individual who is observed, analyzed, examined, investigated,
      experimented upon, or/and treated in the course of a particular study.
    meaning: NCIT:C41189
  Vendor:
    text: Vendor
    description: A person or agency that promotes or exchanges goods or services for
      money. (NCI)
    meaning: NCIT:C68608

```
</details>