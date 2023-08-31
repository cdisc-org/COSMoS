
# Class: AssignedTerm




URI: [cosmos:AssignedTerm](https://www.cdisc.org/cosmos/1-0AssignedTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable]++-%20assignedTerm%200..1>[AssignedTerm&#124;conceptId:string%20%3F;value:string],[SDTMVariable])](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable]++-%20assignedTerm%200..1>[AssignedTerm&#124;conceptId:string%20%3F;value:string],[SDTMVariable])

## Referenced by Class

 *  **None** *[assignedTerm](assignedTerm.md)*  <sub>0..1</sub>  **[AssignedTerm](AssignedTerm.md)**

## Attributes


### Own

 * [➞conceptId](assignedTerm__conceptId.md)  <sub>0..1</sub>
     * Description: C-code for assigned term in NCIt or left blank when CDISC terminology does not apply
     * Range: [String](types/String.md)
 * [➞value](assignedTerm__value.md)  <sub>1..1</sub>
     * Description: Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value
     * Range: [String](types/String.md)
