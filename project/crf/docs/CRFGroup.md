
# Class: CRFGroup



URI: [cosmos_crf:CRFGroup](https://www.cdisc.org/cosmos/crf_v1.0CRFGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CRFItem],[CRFItem]<items%201..*-++[CRFGroup&#124;packageDate:date;packageType:PackageTypeEnum;crfSpecializationId:string;shortName:string;standard:string;standardStartVersion:string;standardEndVersion:string%20%3F;implementationOption:ImplementationOptionEnum%20%3F;scenario:string%20%3F;categories:string%20*;domain:string%20%3F;biomedicalConceptId:string%20%3F;sdtmDatasetSpecializationId:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[CRFItem],[CRFItem]<items%201..*-++[CRFGroup&#124;packageDate:date;packageType:PackageTypeEnum;crfSpecializationId:string;shortName:string;standard:string;standardStartVersion:string;standardEndVersion:string%20%3F;implementationOption:ImplementationOptionEnum%20%3F;scenario:string%20%3F;categories:string%20*;domain:string%20%3F;biomedicalConceptId:string%20%3F;sdtmDatasetSpecializationId:string%20%3F])

## Attributes


### Own

 * [packageDate](packageDate.md)  <sub>1..1</sub>
     * Description: Biomedical Concept package release date indicating when the BC package was published to production
     * Range: [Date](types/Date.md)
 * [packageType](packageType.md)  <sub>1..1</sub>
     * Description: Package type for CRF specializations (crf)
     * Range: [PackageTypeEnum](PackageTypeEnum.md)
 * [crfSpecializationId](crfSpecializationId.md)  <sub>1..1</sub>
     * Description: Identifier for CRF specialization group
     * Range: [String](types/String.md)
 * [shortName](shortName.md)  <sub>1..1</sub>
     * Description: Short name which provides a user friendly and intuitive name for the CRF group
     * Range: [String](types/String.md)
 * [standard](standard.md)  <sub>1..1</sub>
     * Description: Standard for the CRF specialization group
     * Range: [String](types/String.md)
 * [standardStartVersion](standardStartVersion.md)  <sub>1..1</sub>
     * Description: The earliest CRF IG version applicable to the CRF specialization
     * Range: [String](types/String.md)
 * [standardEndVersion](standardEndVersion.md)  <sub>0..1</sub>
     * Description: The last CRF IG version that is applicable to the CRF specialization
     * Range: [String](types/String.md)
 * [implementationOption](implementationOption.md)  <sub>0..1</sub>
     * Description: Implementation option for the CRF specialization group
     * Range: [ImplementationOptionEnum](ImplementationOptionEnum.md)
 * [scenario](scenario.md)  <sub>0..1</sub>
     * Description: Scenario for the CRF specialization group
     * Range: [String](types/String.md)
 * [categories](categories.md)  <sub>0..\*</sub>
     * Description: CRF Dataset Specialization category for the faciliation of API search and extract
     * Range: [String](types/String.md)
 * [domain](domain.md)  <sub>0..1</sub>
     * Description: Domain for the CRF specialization group
     * Range: [String](types/String.md)
 * [biomedicalConceptId](biomedicalConceptId.md)  <sub>0..1</sub>
     * Description: Biomedical Concept identifier foreign key
     * Range: [String](types/String.md)
 * [sdtmDatasetSpecializationId](sdtmDatasetSpecializationId.md)  <sub>0..1</sub>
     * Description: Identifier for SDTM Dataset Specialization group
     * Range: [String](types/String.md)
 * [items](items.md)  <sub>1..\*</sub>
     * Description: Items included in the CRF specialization
     * Range: [CRFItem](CRFItem.md)
