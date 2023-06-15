
# COSMoS-Biomedical-Concepts-Schema


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [AssignedTerm](AssignedTerm.md)
 * [CodeList](CodeList.md)
 * [CodeListTerm](CodeListTerm.md)
 * [RelationShip](RelationShip.md)
 * [SDTMGroup](SDTMGroup.md)
 * [SDTMVariable](SDTMVariable.md)
 * [SubsetCodeList](SubsetCodeList.md)

### Mixins


### Slots

 * [assignedTerm](assignedTerm.md)
 * [➞conceptId](assignedTerm__conceptId.md) - C-code for assigned term in NCIt or left blank when CDISC terminology does not apply
 * [➞value](assignedTerm__value.md) - Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value
 * [biomedicalConceptId](biomedicalConceptId.md) - Biomedical Concept identifier
 * [codelist](codelist.md) - Codelist
 * [codelistTerm](codelistTerm.md)
 * [comparator](comparator.md) - Comparison operator for SDTM group variables included in VLM
 * [conceptId](conceptId.md) - C-code for a codelist in NCIt
 * [dataElementConceptId](dataElementConceptId.md) - Biomedical Concept Data Element Concept idenfifier foreign key
 * [dataType](dataType.md) - Variable data type
 * [datasetSpecializationId](datasetSpecializationId.md) - Identifier for SDTM Value Level Metadata group
 * [domain](domain.md) - Domain for the SDTM specialization group
 * [format](format.md) - Variable display format
 * [href](href.md) - Link to NCIt for the codelist
 * [isNonStandard](isNonStandard.md) - Flag that indicates if the variable is a non-standard variable
 * [length](length.md) - Variable length
 * [linkingPhrase](linkingPhrase.md) - Variable relationship descriptive linking phrase
 * [mandatoryValue](mandatoryValue.md) - Indicator that variable must be populated within the SDTM group
 * [mandatoryVariable](mandatoryVariable.md) - Indicator that variable must be present within the SDTM group
 * [name](name.md) - Variable included in the SDTM dataset specialization
 * [object](object.md) - Object in a variable relationship
 * [originSource](originSource.md) - Variable origin source (define-XML v21)
 * [originType](originType.md) - Variable origin type (define-XML v21)
 * [packageDate](packageDate.md) - Biomedical Concept package release date indicating when the BC package was published to production
 * [packageType](packageType.md) - Package type (sdtm for SDTM Dataset Specializations)
 * [parentCodelist](parentCodelist.md) - Subset codelist parent codelist
 * [predicateTerm](predicateTerm.md) - Short variable relatio ship linking phrase for programming purposes
 * [relationship](relationship.md)
 * [role](role.md) - SDTM variable role
 * [sdtmigEndVersion](sdtmigEndVersion.md) - The last SDTMIG version that is applicable to the BC dataset specialization
 * [sdtmigStartVersion](sdtmigStartVersion.md) - The earliest SDTMIG version applicable to the BC dataset specialization
 * [shortName](shortName.md) - SDTM group short name which provides a user friendly and intuitive name for the vlm_group_id
 * [significantDigits](significantDigits.md) - Variable significant_digits
 * [source](source.md) - SDTM VLM Source which categorizes VLM groups by topic variable
 * [subject](subject.md) - Subject in a variable relationship
 * [submissionValue](submissionValue.md) - CDISC submission value for the codelist
 * [subsetCodelist](subsetCodelist.md) - Subset codelist short name
 * [subsetLabel](subsetLabel.md) - Subset codelist label
 * [subsetShortName](subsetShortName.md) - Subset codelist short name
 * [termId](termId.md) - C-code term in subset codelist
 * [termValue](termValue.md) - Submision value of term in subset codelist
 * [valueList](valueList.md) - List of SDTM submission values used if subset codelist is not applicable
 * [variables](variables.md) - Variable included in the SDTM dataset specialization
 * [vlmTarget](vlmTarget.md) - Target variable for VLM

### Enums

 * [Comparator](Comparator.md)
 * [LinkingPhrase](LinkingPhrase.md)
 * [OriginSource](OriginSource.md)
 * [OriginType](OriginType.md)
 * [PredicateTerm](PredicateTerm.md)
 * [Role](Role.md)
 * [SDTMDatasetSpecializationPackageType](SDTMDatasetSpecializationPackageType.md)
 * [SDTMVariableDataType](SDTMVariableDataType.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
