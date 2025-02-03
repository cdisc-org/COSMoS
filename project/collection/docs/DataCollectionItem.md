
# Class: DataCollectionItem



URI: [cosmos_collection:DataCollectionItem](https://www.cdisc.org/cosmos/collection_v1.0DataCollectionItem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMTarget],[PrepopulatedValue],[ListValue],[SDTMTarget]<sdtmTarget%200..*-++[DataCollectionItem&#124;name:string;dataElementConceptId:string%20%3F;isNonStandard:boolean%20%3F;dataCollectionInstrumentItem:string;questionText:string;prompt:string%20%3F;orderNumber:integer;mandatoryVariable:boolean;dataType:CollectionItemDataTypeEnum;length:integer%20%3F;significantDigits:integer%20%3F;displayHidden:boolean%20%3F;listType:ListTypeEnum%20%3F],[CodeList]<codelist%200..1-++[DataCollectionItem],[PrepopulatedValue]<prepopulatedValue%200..1-++[DataCollectionItem],[ListValue]<valueList%200..*-++[DataCollectionItem],[DataCollectionGroup]++-%20items%201..*>[DataCollectionItem],[DataCollectionGroup],[CodeList])](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMTarget],[PrepopulatedValue],[ListValue],[SDTMTarget]<sdtmTarget%200..*-++[DataCollectionItem&#124;name:string;dataElementConceptId:string%20%3F;isNonStandard:boolean%20%3F;dataCollectionInstrumentItem:string;questionText:string;prompt:string%20%3F;orderNumber:integer;mandatoryVariable:boolean;dataType:CollectionItemDataTypeEnum;length:integer%20%3F;significantDigits:integer%20%3F;displayHidden:boolean%20%3F;listType:ListTypeEnum%20%3F],[CodeList]<codelist%200..1-++[DataCollectionItem],[PrepopulatedValue]<prepopulatedValue%200..1-++[DataCollectionItem],[ListValue]<valueList%200..*-++[DataCollectionItem],[DataCollectionGroup]++-%20items%201..*>[DataCollectionItem],[DataCollectionGroup],[CodeList])

## Referenced by Class

 *  **None** *[items](items.md)*  <sub>1..\*</sub>  **[DataCollectionItem](DataCollectionItem.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Description: Item included in the data collection dataset specialization
     * Range: [String](types/String.md)
 * [dataElementConceptId](dataElementConceptId.md)  <sub>0..1</sub>
     * Description: Biomedical Concept Data Element Concept identifier foreign key
     * Range: [String](types/String.md)
 * [isNonStandard](isNonStandard.md)  <sub>0..1</sub>
     * Description: Flag that indicates if the variable is a non-standard variable
     * Range: [Boolean](types/Boolean.md)
 * [dataCollectionInstrumentItem](dataCollectionInstrumentItem.md)  <sub>1..1</sub>
     * Description: Item included in the data collection dataset specialization used for eCSR set-up
     * Range: [String](types/String.md)
 * [questionText](questionText.md)  <sub>1..1</sub>
     * Description: Item question text
     * Range: [String](types/String.md)
 * [prompt](prompt.md)  <sub>0..1</sub>
     * Description: Item prompt
     * Range: [String](types/String.md)
 * [orderNumber](orderNumber.md)  <sub>1..1</sub>
     * Description: Item order number
     * Range: [Integer](types/Integer.md)
 * [mandatoryVariable](mandatoryVariable.md)  <sub>1..1</sub>
     * Description: Indicator that the item must be present within the data collection group
     * Range: [Boolean](types/Boolean.md)
 * [dataType](dataType.md)  <sub>1..1</sub>
     * Description: Item data type
     * Range: [CollectionItemDataTypeEnum](CollectionItemDataTypeEnum.md)
 * [length](length.md)  <sub>0..1</sub>
     * Description: Item length
     * Range: [Integer](types/Integer.md)
 * [significantDigits](significantDigits.md)  <sub>0..1</sub>
     * Description: Item significant_digits
     * Range: [Integer](types/Integer.md)
 * [displayHidden](displayHidden.md)  <sub>0..1</sub>
     * Description: Indicator that the item is hidden from the user
     * Range: [Boolean](types/Boolean.md)
 * [valueList](valueList.md)  <sub>0..\*</sub>
     * Description: A set of values for a data collection item
     * Range: [ListValue](ListValue.md)
 * [listType](listType.md)  <sub>0..1</sub>
     * Description: Type of list used for set-up of the data collection instrument
     * Range: [ListTypeEnum](ListTypeEnum.md)
 * [prepopulatedValue](prepopulatedValue.md)  <sub>0..1</sub>
     * Description: Pre-populated value for the data collection instrument
     * Range: [PrepopulatedValue](PrepopulatedValue.md)
 * [codelist](codelist.md)  <sub>0..1</sub>
     * Description: Codelist
     * Range: [CodeList](CodeList.md)
 * [sdtmTarget](sdtmTarget.md)  <sub>0..\*</sub>
     * Description: SDTM target variables for data collection item variable
     * Range: [SDTMTarget](SDTMTarget.md)
