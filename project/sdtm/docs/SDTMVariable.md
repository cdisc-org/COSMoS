
# Class: SDTMVariable




URI: [cosmos:SDTMVariable](https://www.cdisc.org/cosmos/1-0SDTMVariable)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationShip]<relationship%200..1-++[SDTMVariable&#124;name:string;dataElementConceptId:string%20%3F;isNonStandard:boolean%20%3F;subsetCodelist:string%20%3F;valueList:string%20*;role:RoleEnum%20%3F;dataType:SDTMVariableDataTypeEnum%20%3F;length:integer%20%3F;format:string%20%3F;significantDigits:integer%20%3F;mandatoryVariable:boolean%20%3F;mandatoryValue:boolean%20%3F;originType:OriginTypeEnum%20%3F;originSource:OriginSourceEnum%20%3F;comparator:ComparatorEnum%20%3F;vlmTarget:boolean%20%3F],[AssignedTerm]<assignedTerm%200..1-++[SDTMVariable],[CodeList]<codelist%200..1-++[SDTMVariable],[SDTMGroup]++-%20variables%200..*>[SDTMVariable],[SDTMGroup],[RelationShip],[CodeList],[AssignedTerm])](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationShip]<relationship%200..1-++[SDTMVariable&#124;name:string;dataElementConceptId:string%20%3F;isNonStandard:boolean%20%3F;subsetCodelist:string%20%3F;valueList:string%20*;role:RoleEnum%20%3F;dataType:SDTMVariableDataTypeEnum%20%3F;length:integer%20%3F;format:string%20%3F;significantDigits:integer%20%3F;mandatoryVariable:boolean%20%3F;mandatoryValue:boolean%20%3F;originType:OriginTypeEnum%20%3F;originSource:OriginSourceEnum%20%3F;comparator:ComparatorEnum%20%3F;vlmTarget:boolean%20%3F],[AssignedTerm]<assignedTerm%200..1-++[SDTMVariable],[CodeList]<codelist%200..1-++[SDTMVariable],[SDTMGroup]++-%20variables%200..*>[SDTMVariable],[SDTMGroup],[RelationShip],[CodeList],[AssignedTerm])

## Referenced by Class

 *  **None** *[variables](variables.md)*  <sub>0..\*</sub>  **[SDTMVariable](SDTMVariable.md)**

## Attributes


### Own

 * [name](name.md)  <sub>1..1</sub>
     * Description: Variable included in the SDTM dataset specialization
     * Range: [String](types/String.md)
 * [dataElementConceptId](dataElementConceptId.md)  <sub>0..1</sub>
     * Description: Biomedical Concept Data Element Concept identifier foreign key
     * Range: [String](types/String.md)
 * [isNonStandard](isNonStandard.md)  <sub>0..1</sub>
     * Description: Flag that indicates if the variable is a non-standard variable
     * Range: [Boolean](types/Boolean.md)
 * [codelist](codelist.md)  <sub>0..1</sub>
     * Description: Codelist
     * Range: [CodeList](CodeList.md)
 * [subsetCodelist](subsetCodelist.md)  <sub>0..1</sub>
     * Description: Subset codelist short name
     * Range: [String](types/String.md)
 * [valueList](valueList.md)  <sub>0..\*</sub>
     * Description: List of SDTM submission values used if subset codelist is not applicable
     * Range: [String](types/String.md)
 * [assignedTerm](assignedTerm.md)  <sub>0..1</sub>
     * Range: [AssignedTerm](AssignedTerm.md)
 * [role](role.md)  <sub>0..1</sub>
     * Description: SDTM variable role
     * Range: [RoleEnum](RoleEnum.md)
 * [relationship](relationship.md)  <sub>0..1</sub>
     * Range: [RelationShip](RelationShip.md)
 * [dataType](dataType.md)  <sub>0..1</sub>
     * Description: Variable data type
     * Range: [SDTMVariableDataTypeEnum](SDTMVariableDataTypeEnum.md)
 * [length](length.md)  <sub>0..1</sub>
     * Description: Variable length
     * Range: [Integer](types/Integer.md)
 * [format](format.md)  <sub>0..1</sub>
     * Description: Variable display format
     * Range: [String](types/String.md)
 * [significantDigits](significantDigits.md)  <sub>0..1</sub>
     * Description: Variable significant_digits
     * Range: [Integer](types/Integer.md)
 * [mandatoryVariable](mandatoryVariable.md)  <sub>0..1</sub>
     * Description: Indicator that variable must be present within the SDTM group
     * Range: [Boolean](types/Boolean.md)
 * [mandatoryValue](mandatoryValue.md)  <sub>0..1</sub>
     * Description: Indicator that variable must be populated within the SDTM group
     * Range: [Boolean](types/Boolean.md)
 * [originType](originType.md)  <sub>0..1</sub>
     * Description: Variable origin type (define-XML v21)
     * Range: [OriginTypeEnum](OriginTypeEnum.md)
 * [originSource](originSource.md)  <sub>0..1</sub>
     * Description: Variable origin source (define-XML v21)
     * Range: [OriginSourceEnum](OriginSourceEnum.md)
 * [comparator](comparator.md)  <sub>0..1</sub>
     * Description: Comparison operator for SDTM group variables included in VLM
     * Range: [ComparatorEnum](ComparatorEnum.md)
 * [vlmTarget](vlmTarget.md)  <sub>0..1</sub>
     * Description: Target variable for VLM
     * Range: [Boolean](types/Boolean.md)
