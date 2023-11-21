
# Class: RelationShip




URI: [cosmos:RelationShip](https://www.cdisc.org/cosmos/1-0RelationShip)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable]++-%20relationship%200..1>[RelationShip&#124;subject:string;linkingPhrase:LinkingPhraseEnum;predicateTerm:PredicateTermEnum;object:string],[SDTMVariable])](https://yuml.me/diagram/nofunky;dir:TB/class/[SDTMVariable]++-%20relationship%200..1>[RelationShip&#124;subject:string;linkingPhrase:LinkingPhraseEnum;predicateTerm:PredicateTermEnum;object:string],[SDTMVariable])

## Referenced by Class

 *  **None** *[relationship](relationship.md)*  <sub>0..1</sub>  **[RelationShip](RelationShip.md)**

## Attributes


### Own

 * [subject](subject.md)  <sub>1..1</sub>
     * Description: Subject in a variable relationship
     * Range: [String](types/String.md)
 * [linkingPhrase](linkingPhrase.md)  <sub>1..1</sub>
     * Description: Variable relationship descriptive linking phrase
     * Range: [LinkingPhraseEnum](LinkingPhraseEnum.md)
 * [predicateTerm](predicateTerm.md)  <sub>1..1</sub>
     * Description: Short variable relationship linking phrase for programming purposes
     * Range: [PredicateTermEnum](PredicateTermEnum.md)
 * [object](object.md)  <sub>1..1</sub>
     * Description: Object in a variable relationship
     * Range: [String](types/String.md)
