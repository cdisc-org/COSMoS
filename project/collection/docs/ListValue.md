
# Class: ListValue



URI: [cosmos_collection:ListValue](https://www.cdisc.org/cosmos/collection_v1.0ListValue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem]++-%20valueList%200..*>[ListValue&#124;displayValue:string;value:string%20%3F],[DataCollectionItem])](https://yuml.me/diagram/nofunky;dir:TB/class/[DataCollectionItem]++-%20valueList%200..*>[ListValue&#124;displayValue:string;value:string%20%3F],[DataCollectionItem])

## Referenced by Class

 *  **None** *[valueList](valueList.md)*  <sub>0..\*</sub>  **[ListValue](ListValue.md)**

## Attributes


### Own

 * [ListValue➞displayValue](ListValue_displayValue.md)  <sub>1..1</sub>
     * Description: CDISC submission value for the data collection item
     * Range: [String](types/String.md)
 * [ListValue➞value](ListValue_value.md)  <sub>0..1</sub>
     * Description: User-friendly display value for the data collection item
     * Range: [String](types/String.md)
