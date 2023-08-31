
# Class: Coding




URI: [cosmos:Coding](https://www.cdisc.org/cosmos/1-0Coding)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BiomedicalConcept]++-%20coding%200..*>[Coding&#124;code:string;system:string;systemName:string%20%3F],[BiomedicalConcept])](https://yuml.me/diagram/nofunky;dir:TB/class/[BiomedicalConcept]++-%20coding%200..*>[Coding&#124;code:string;system:string;systemName:string%20%3F],[BiomedicalConcept])

## Referenced by Class

 *  **None** *[coding](coding.md)*  <sub>0..\*</sub>  **[Coding](Coding.md)**

## Attributes


### Own

 * [code](code.md)  <sub>1..1</sub>
     * Description: Synonym concept for the Biomedical Concept as defined in a code system
     * Range: [String](types/String.md)
 * [system](system.md)  <sub>1..1</sub>
     * Description: Identifies the code system for the synonym concept The URL of the code system should be used if it exists
     * Range: [String](types/String.md)
 * [systemName](systemName.md)  <sub>0..1</sub>
     * Description: Human-readable name for the code system
     * Range: [String](types/String.md)
