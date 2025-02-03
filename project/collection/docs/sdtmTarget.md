
# Class: SDTMTarget



URI: [cosmos_collection:SDTMTarget](https://www.cdisc.org/cosmos/collection_v1.0SDTMTarget)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem]++-%20sdtmTarget%200..*>[SDTMTarget&#124;sdtmVariable:string;sdtmAnnotation:string%20%3F;sdtmTargetMapping:string%20%3F],[DataCollectionItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem]++-%20sdtmTarget%200..*>[SDTMTarget&#124;sdtmVariable:string;sdtmAnnotation:string%20%3F;sdtmTargetMapping:string%20%3F],[DataCollectionItem])

## Referenced by Class

 *  **None** *[sdtmTarget](sdtmTarget.md)*  <sub>0..\*</sub>  **[SDTMTarget](SDTMTarget.md)**

## Attributes


### Own

 * [sdtmVariable](sdtmVariable.md)  <sub>1..1</sub>
     * Description: SDTM target variable for data collection item variable
     * Range: [String](types/String.md)
 * [sdtmAnnotation](sdtmAnnotation.md)  <sub>0..1</sub>
     * Description: Annotation of the SDTM target in the data collection instrument
     * Range: [String](types/String.md)
 * [sdtmTargetMapping](sdtmTargetMapping.md)  <sub>0..1</sub>
     * Description: Rule for mapping from data collection item to SDTM target variable.
     * Range: [String](types/String.md)
