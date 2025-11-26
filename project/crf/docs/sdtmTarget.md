
# Class: SDTMTarget



URI: [cosmos_crf:SDTMTarget](https://www.cdisc.org/cosmos/crf_v1.0SDTMTarget)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CRFItem]++-%20sdtmTarget%200..1>[SDTMTarget&#124;sdtmAnnotation:string%20%3F;sdtmVariables:string%20*;sdtmTargetMapping:string%20%3F],[CRFItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[CRFItem]++-%20sdtmTarget%200..1>[SDTMTarget&#124;sdtmAnnotation:string%20%3F;sdtmVariables:string%20*;sdtmTargetMapping:string%20%3F],[CRFItem])

## Referenced by Class

 *  **None** *[sdtmTarget](sdtmTarget.md)*  <sub>0..1</sub>  **[SDTMTarget](SDTMTarget.md)**

## Attributes


### Own

 * [sdtmAnnotation](sdtmAnnotation.md)  <sub>0..1</sub>
     * Description: Annotation of the SDTM target in the CRF instrument
     * Range: [String](types/String.md)
 * [sdtmVariables](sdtmVariables.md)  <sub>0..\*</sub>
     * Description: SDTM target variable for CRF item variable
     * Range: [String](types/String.md)
 * [sdtmTargetMapping](sdtmTargetMapping.md)  <sub>0..1</sub>
     * Description: Rule for mapping from CRF item to SDTM target variable.
     * Range: [String](types/String.md)
