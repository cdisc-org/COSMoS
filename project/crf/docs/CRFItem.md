
# Class: CRFItem



URI: [cosmos_crf:CRFItem](https://www.cdisc.org/cosmos/crf_v1.0CRFItem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMTarget],[PrepopulatedValue],[ListValue],[CodeList],[SDTMTarget]<sdtmTarget%200..1-++[CRFItem&#124;name:string;variableName:string;dataElementConceptId:string%20%3F;questionText:string%20%3F;prompt:string%20%3F;completionInstructions:string%20%3F;orderNumber:integer;mandatoryVariable:boolean;dataType:CRFItemDataTypeEnum;length:integer%20%3F;significantDigits:integer%20%3F;displayHidden:boolean%20%3F;derivedVariable:boolean%20%3F;derivationDescription:string%20%3F;selectionType:SelectionTypeEnum%20%3F],[PrepopulatedValue]<prepopulatedValue%200..1-++[CRFItem],[ListValue]<valueList%200..*-++[CRFItem],[CodeList]<codelist%200..1-++[CRFItem],[CRFGroup]++-%20items%201..*>[CRFItem],[CRFGroup])](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMTarget],[PrepopulatedValue],[ListValue],[CodeList],[SDTMTarget]<sdtmTarget%200..1-++[CRFItem&#124;name:string;variableName:string;dataElementConceptId:string%20%3F;questionText:string%20%3F;prompt:string%20%3F;completionInstructions:string%20%3F;orderNumber:integer;mandatoryVariable:boolean;dataType:CRFItemDataTypeEnum;length:integer%20%3F;significantDigits:integer%20%3F;displayHidden:boolean%20%3F;derivedVariable:boolean%20%3F;derivationDescription:string%20%3F;selectionType:SelectionTypeEnum%20%3F],[PrepopulatedValue]<prepopulatedValue%200..1-++[CRFItem],[ListValue]<valueList%200..*-++[CRFItem],[CodeList]<codelist%200..1-++[CRFItem],[CRFGroup]++-%20items%201..*>[CRFItem],[CRFGroup])

## Referenced by Class

 *  **None** *[items](items.md)*  <sub>1..\*</sub>  **[CRFItem](CRFItem.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Description: Item name as it appears on the CRF instrument
     * Range: [String](types/String.md)
 * [variableName](variableName.md)  <sub>1..1</sub>
     * Description: Variable name of the CRF item for which data are being collected.
     * Range: [String](types/String.md)
 * [dataElementConceptId](dataElementConceptId.md)  <sub>0..1</sub>
     * Description: Biomedical Concept Data Element Concept identifier foreign key
     * Range: [String](types/String.md)
 * [questionText](questionText.md)  <sub>0..1</sub>
     * Description: Item question text
     * Range: [String](types/String.md)
 * [prompt](prompt.md)  <sub>0..1</sub>
     * Description: Item prompt
     * Range: [String](types/String.md)
 * [completionInstructions](completionInstructions.md)  <sub>0..1</sub>
     * Description: Item completion instructions
     * Range: [String](types/String.md)
 * [orderNumber](orderNumber.md)  <sub>1..1</sub>
     * Description: Item order number
     * Range: [Integer](types/Integer.md)
 * [mandatoryVariable](mandatoryVariable.md)  <sub>1..1</sub>
     * Description: Indicator that the item must be present within the CRF group
     * Range: [Boolean](types/Boolean.md)
 * [dataType](dataType.md)  <sub>1..1</sub>
     * Description: Item data type
     * Range: [CRFItemDataTypeEnum](CRFItemDataTypeEnum.md)
 * [length](length.md)  <sub>0..1</sub>
     * Description: Item length
     * Range: [Integer](types/Integer.md)
 * [significantDigits](significantDigits.md)  <sub>0..1</sub>
     * Description: Item significant_digits
     * Range: [Integer](types/Integer.md)
 * [displayHidden](displayHidden.md)  <sub>0..1</sub>
     * Description: Indicator that the item is hidden from the user
     * Range: [Boolean](types/Boolean.md)
 * [derivedVariable](derivedVariable.md)  <sub>0..1</sub>
     * Description: Indicator that variable is derived
     * Range: [Boolean](types/Boolean.md)
 * [derivationDescription](derivationDescription.md)  <sub>0..1</sub>
     * Description: Description of the derivation. Required when derivedVariable is true.
     * Range: [String](types/String.md)
 * [codelist](codelist.md)  <sub>0..1</sub>
     * Description: Codelist
     * Range: [CodeList](CodeList.md)
 * [valueList](valueList.md)  <sub>0..\*</sub>
     * Description: A set of values for a CRF item
     * Range: [ListValue](ListValue.md)
 * [selectionType](selectionType.md)  <sub>0..1</sub>
     * Description: Type of selection used for set-up of the CRF instrument
     * Range: [SelectionTypeEnum](SelectionTypeEnum.md)
 * [prepopulatedValue](prepopulatedValue.md)  <sub>0..1</sub>
     * Description: Pre-populated value for the CRF instrument
     * Range: [PrepopulatedValue](PrepopulatedValue.md)
 * [sdtmTarget](sdtmTarget.md)  <sub>0..1</sub>
     * Description: SDTM target variables for CRF item variable
     * Range: [SDTMTarget](SDTMTarget.md)
