
# Class: CodeList




URI: [cosmos:CodeList](https://www.cdisc.org/cosmos/1-0CodeList)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable]++-%20codelist%200..1>[CodeList&#124;conceptId:string;href:uri%20%3F;submissionValue:string],[SDTMVariable])](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable]++-%20codelist%200..1>[CodeList&#124;conceptId:string;href:uri%20%3F;submissionValue:string],[SDTMVariable])

## Referenced by Class

 *  **None** *[codelist](codelist.md)*  <sub>0..1</sub>  **[CodeList](CodeList.md)**

## Attributes


### Own

 * [conceptId](conceptId.md)  <sub>1..1</sub>
     * Description: C-code for a codelist in NCIt
     * Range: [String](types/String.md)
 * [href](href.md)  <sub>0..1</sub>
     * Description: Link to NCIt for the codelist
     * Range: [Uri](types/Uri.md)
 * [submissionValue](submissionValue.md)  <sub>1..1</sub>
     * Description: CDISC submission value for the codelist
     * Range: [String](types/String.md)
