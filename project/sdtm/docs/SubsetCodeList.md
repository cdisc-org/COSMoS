
# Class: SubsetCodeList




URI: [cosmos:SubsetCodeList](https://www.cdisc.org/cosmos/1-0SubsetCodeList)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CodeListTerm]<codelistTerm%201..*-++[SubsetCodeList&#124;parentCodelist:string;subsetShortName:string;subsetLabel:string],[CodeListTerm])](https://yuml.me/diagram/nofunky;dir:TB/class/[CodeListTerm]<codelistTerm%201..*-++[SubsetCodeList&#124;parentCodelist:string;subsetShortName:string;subsetLabel:string],[CodeListTerm])

## Attributes


### Own

 * [parentCodelist](parentCodelist.md)  <sub>1..1</sub>
     * Description: Subset codelist parent codelist
     * Range: [String](types/String.md)
 * [subsetShortName](subsetShortName.md)  <sub>1..1</sub>
     * Description: Subset codelist short name
     * Range: [String](types/String.md)
 * [subsetLabel](subsetLabel.md)  <sub>1..1</sub>
     * Description: Subset codelist label
     * Range: [String](types/String.md)
 * [codelistTerm](codelistTerm.md)  <sub>1..\*</sub>
     * Range: [CodeListTerm](CodeListTerm.md)
