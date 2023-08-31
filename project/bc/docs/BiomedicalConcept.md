
# Class: BiomedicalConcept




URI: [cosmos:BiomedicalConcept](https://www.cdisc.org/cosmos/1-0BiomedicalConcept)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataElementConcept],[Coding],[DataElementConcept]<dataElementConcepts%200..*-++[BiomedicalConcept&#124;conceptId:string;ncitCode:string%20%3F;href:uri%20%3F;packageDate:date;packageType:BiomedicalConceptPackageTypeEnum;categories:string%20%2B;parentConceptId:string%20%3F;shortName:string;synonyms:string%20*;resultScales:BiomedicalConceptResultScaleEnum%20*;definition:string],[Coding]<coding%200..*-++[BiomedicalConcept])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataElementConcept],[Coding],[DataElementConcept]<dataElementConcepts%200..*-++[BiomedicalConcept&#124;conceptId:string;ncitCode:string%20%3F;href:uri%20%3F;packageDate:date;packageType:BiomedicalConceptPackageTypeEnum;categories:string%20%2B;parentConceptId:string%20%3F;shortName:string;synonyms:string%20*;resultScales:BiomedicalConceptResultScaleEnum%20*;definition:string],[Coding]<coding%200..*-++[BiomedicalConcept])

## Referenced by Class


## Attributes


### Own

 * [BiomedicalConcept➞conceptId](BiomedicalConcept_conceptId.md)  <sub>1..1</sub>
     * Description: A unique identifier for a Biomedical Concept which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
     * Range: [String](types/String.md)
 * [BiomedicalConcept➞ncitCode](BiomedicalConcept_ncitCode.md)  <sub>0..1</sub>
     * Description: NCIt C-code for the Biomedical Concept
     * Range: [String](types/String.md)
 * [BiomedicalConcept➞href](BiomedicalConcept_href.md)  <sub>0..1</sub>
     * Description: URI link to NCIt for the Biomedical Concept; blank if  concept is not available in NCIt
     * Range: [Uri](types/Uri.md)
 * [packageDate](packageDate.md)  <sub>1..1</sub>
     * Description: Biomedical Concept package release date indicating when the BC package was published to production
     * Range: [Date](types/Date.md)
 * [packageType](packageType.md)  <sub>1..1</sub>
     * Description: Package type (bc for Biomedical Concepts)
     * Range: [BiomedicalConceptPackageTypeEnum](BiomedicalConceptPackageTypeEnum.md)
 * [categories](categories.md)  <sub>1..\*</sub>
     * Description: Biomedical Concept category for the faciliation of API search and extract
     * Range: [String](types/String.md)
 * [parentConceptId](parentConceptId.md)  <sub>0..1</sub>
     * Description: C-code for the parent concept in the NCIt hiearchy; blank if concept is not available in NCIt
     * Range: [String](types/String.md)
 * [shortName](shortName.md)  <sub>1..1</sub>
     * Description: NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt
     * Range: [String](types/String.md)
 * [synonyms](synonyms.md)  <sub>0..\*</sub>
     * Description: Biomedical Concept synonym equivalent to BC short name for the facilitation of API search and extraction
     * Range: [String](types/String.md)
 * [resultScales](resultScales.md)  <sub>0..\*</sub>
     * Description: Scale of measurement for the Biomedical Concept result
     * Range: [BiomedicalConceptResultScaleEnum](BiomedicalConceptResultScaleEnum.md)
 * [definition](definition.md)  <sub>1..1</sub>
     * Description: NCIt definition for the Biomedical Concept; provisional defintion if concept is not available in NCIt
     * Range: [String](types/String.md)
 * [coding](coding.md)  <sub>0..\*</sub>
     * Range: [Coding](Coding.md)
 * [dataElementConcepts](dataElementConcepts.md)  <sub>0..\*</sub>
     * Description: Data Element Concept
     * Range: [DataElementConcept](DataElementConcept.md)
