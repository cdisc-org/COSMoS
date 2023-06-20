
# Class: SDTMGroup




URI: [cosmos:SDTMGroup](https://www.cdisc.org/cosmos/1-0SDTMGroup)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable],[SDTMVariable]<variables%200..*-++[SDTMGroup&#124;packageDate:date;packageType:SDTMDatasetSpecializationPackageType;domain:string;shortName:string;datasetSpecializationId:string;source:string;sdtmigStartVersion:string;sdtmigEndVersion:string%20%3F;biomedicalConceptId:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable],[SDTMVariable]<variables%200..*-++[SDTMGroup&#124;packageDate:date;packageType:SDTMDatasetSpecializationPackageType;domain:string;shortName:string;datasetSpecializationId:string;source:string;sdtmigStartVersion:string;sdtmigEndVersion:string%20%3F;biomedicalConceptId:string%20%3F])

## Attributes


### Own

 * [packageDate](packageDate.md)  <sub>1..1</sub>
     * Description: Biomedical Concept package release date indicating when the BC package was published to production
     * Range: [Date](types/Date.md)
 * [packageType](packageType.md)  <sub>1..1</sub>
     * Description: Package type (sdtm for SDTM Dataset Specializations)
     * Range: [SDTMDatasetSpecializationPackageType](SDTMDatasetSpecializationPackageType.md)
 * [domain](domain.md)  <sub>1..1</sub>
     * Description: Domain for the SDTM specialization group
     * Range: [String](types/String.md)
 * [shortName](shortName.md)  <sub>1..1</sub>
     * Description: SDTM group short name which provides a user friendly and intuitive name for the vlm_group_id
     * Range: [String](types/String.md)
 * [datasetSpecializationId](datasetSpecializationId.md)  <sub>1..1</sub>
     * Description: Identifier for SDTM Value Level Metadata group
     * Range: [String](types/String.md)
 * [source](source.md)  <sub>1..1</sub>
     * Description: SDTM VLM Source which categorizes VLM groups by topic variable
     * Range: [String](types/String.md)
 * [sdtmigStartVersion](sdtmigStartVersion.md)  <sub>1..1</sub>
     * Description: The earliest SDTMIG version applicable to the BC dataset specialization
     * Range: [String](types/String.md)
 * [sdtmigEndVersion](sdtmigEndVersion.md)  <sub>0..1</sub>
     * Description: The last SDTMIG version that is applicable to the BC dataset specialization
     * Range: [String](types/String.md)
 * [biomedicalConceptId](biomedicalConceptId.md)  <sub>0..1</sub>
     * Description: Biomedical Concept identifier
     * Range: [String](types/String.md)
 * [variables](variables.md)  <sub>0..\*</sub>
     * Description: Variable included in the SDTM dataset specialization
     * Range: [SDTMVariable](SDTMVariable.md)
