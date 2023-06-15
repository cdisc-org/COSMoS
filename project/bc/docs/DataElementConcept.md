
# Class: DataElementConcept




URI: [https://www.cdisc.org/cosmos/1-0/DataElementConcept](https://www.cdisc.org/cosmos/1-0/DataElementConcept)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BiomedicalConcept]++-%20dataElementConcepts%200..*>[DataElementConcept&#124;conceptId:string;ncitCode:string%20%3F;href:uri%20%3F;shortName:string;dataType:DataElementConceptDataType;exampleSet:string%20*],[BiomedicalConcept])](https://yuml.me/diagram/nofunky;dir:TB/class/[BiomedicalConcept]++-%20dataElementConcepts%200..*>[DataElementConcept&#124;conceptId:string;ncitCode:string%20%3F;href:uri%20%3F;shortName:string;dataType:DataElementConceptDataType;exampleSet:string%20*],[BiomedicalConcept])

## Referenced by Class

 *  **None** *[dataElementConcepts](dataElementConcepts.md)*  <sub>0..\*</sub>  **[DataElementConcept](DataElementConcept.md)**

## Attributes


### Own

 * [DataElementConcept➞conceptId](DataElementConcept_conceptId.md)  <sub>1..1</sub>
     * Description: NCI C-code for the BC Data Element Concept
     * Range: [String](types/String.md)
 * [DataElementConcept➞ncitCode](DataElementConcept_ncitCode.md)  <sub>0..1</sub>
     * Description: An identifier for a Data Element Concept (DEC) which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
     * Range: [String](types/String.md)
 * [DataElementConcept➞href](DataElementConcept_href.md)  <sub>0..1</sub>
     * Description: Link to NCIt for the Data Element Concept
     * Range: [Uri](types/Uri.md)
 * [shortName](shortName.md)  <sub>1..1</sub>
     * Description: NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt
     * Range: [String](types/String.md)
 * [dataType](dataType.md)  <sub>1..1</sub>
     * Description: Data Type for the Data Element Concept
     * Range: [DataElementConceptDataType](DataElementConceptDataType.md)
 * [exampleSet](exampleSet.md)  <sub>0..\*</sub>
     * Description: Example values for the Data Element Concept
     * Range: [String](types/String.md)
