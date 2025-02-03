
# Class: CodeList



URI: [cosmos_collection:CodeList](https://www.cdisc.org/cosmos/collection_v1.0CodeList)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem]++-%20codelist%200..1>[CodeList&#124;submissionValue:string;conceptId:string%20%3F;href:uri%20%3F],[DataCollectionItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem]++-%20codelist%200..1>[CodeList&#124;submissionValue:string;conceptId:string%20%3F;href:uri%20%3F],[DataCollectionItem])

## Referenced by Class

 *  **None** *[codelist](codelist.md)*  <sub>0..1</sub>  **[CodeList](CodeList.md)**

## Attributes


### Own

 * [CodeList➞submissionValue](CodeList_submissionValue.md)  <sub>1..1</sub>
     * Description: CDISC submission value for the codelist
     * Range: [String](types/String.md)
 * [CodeList➞conceptId](CodeList_conceptId.md)  <sub>0..1</sub>
     * Description: C-code for codelist in NCIt
     * Range: [String](types/String.md)
 * [CodeList➞href](CodeList_href.md)  <sub>0..1</sub>
     * Description: Link to NCIt for the codelist
     * Range: [Uri](types/Uri.md)
