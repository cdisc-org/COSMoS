
# COSMoS-Biomedical-Concepts-CRF-Schema


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [CRFGroup](CRFGroup.md)
 * [CRFItem](CRFItem.md)
 * [CodeList](CodeList.md)
 * [ListValue](ListValue.md)
 * [PrepopulatedValue](PrepopulatedValue.md)
 * [SDTMTarget](SDTMTarget.md)

### Mixins


### Slots

 * [biomedicalConceptId](biomedicalConceptId.md) - Biomedical Concept identifier foreign key
 * [categories](categories.md) - CRF Dataset Specialization category for the faciliation of API search and extract
 * [codelist](codelist.md) - Codelist
 * [completionInstructions](completionInstructions.md) - Item completion instructions
 * [conceptId](conceptId.md) - C-code for codelist or term in NCIt
     * [CodeList➞conceptId](CodeList_conceptId.md) - C-code for codelist in NCIt
     * [PrepopulatedValue➞conceptId](PrepopulatedValue_conceptId.md) - C-code for pre-populated term in NCIt
 * [crfSpecializationId](crfSpecializationId.md) - Identifier for CRF specialization group
 * [dataElementConceptId](dataElementConceptId.md) - Biomedical Concept Data Element Concept identifier foreign key
 * [dataType](dataType.md) - Item data type
 * [derivationDescription](derivationDescription.md) - Description of the derivation. Required when derivedVariable is true.
 * [derivedVariable](derivedVariable.md) - Indicator that variable is derived
 * [displayHidden](displayHidden.md) - Indicator that the item is hidden from the user
 * [displayValue](displayValue.md) - User-friendly display value for the CRF item
     * [ListValue➞displayValue](ListValue_displayValue.md) - CDISC submission value for the CRF item
 * [domain](domain.md) - Domain for the CRF specialization group
 * [href](href.md) - Link to NCIt for the codelist or term
     * [CodeList➞href](CodeList_href.md) - Link to NCIt for the codelist
 * [implementationOption](implementationOption.md) - Implementation option for the CRF specialization group
 * [items](items.md) - Items included in the CRF specialization
 * [length](length.md) - Item length
 * [mandatoryVariable](mandatoryVariable.md) - Indicator that the item must be present within the CRF group
 * [name](name.md) - Item name as it appears on the CRF instrument
 * [orderNumber](orderNumber.md) - Item order number
 * [packageDate](packageDate.md) - Biomedical Concept package release date indicating when the BC package was published to production
 * [packageType](packageType.md) - Package type for CRF specializations (crf)
 * [prepopulatedValue](prepopulatedValue.md) - Pre-populated value for the CRF instrument
 * [prompt](prompt.md) - Item prompt
 * [questionText](questionText.md) - Item question text
 * [scenario](scenario.md) - Scenario for the CRF specialization group
 * [sdtmAnnotation](sdtmAnnotation.md) - Annotation of the SDTM target in the CRF instrument
 * [sdtmDatasetSpecializationId](sdtmDatasetSpecializationId.md) - Identifier for SDTM Dataset Specialization group
 * [sdtmTarget](sdtmTarget.md) - SDTM target variables for CRF item variable
 * [sdtmTargetMapping](sdtmTargetMapping.md) - Rule for mapping from CRF item to SDTM target variable.
 * [sdtmVariables](sdtmVariables.md) - SDTM target variable for CRF item variable
 * [selectionType](selectionType.md) - Type of selection used for set-up of the CRF instrument
 * [shortName](shortName.md) - Short name which provides a user friendly and intuitive name for the CRF group
 * [significantDigits](significantDigits.md) - Item significant_digits
 * [standard](standard.md) - Standard for the CRF specialization group
 * [standardEndVersion](standardEndVersion.md) - The last CRF IG version that is applicable to the CRF specialization
 * [standardStartVersion](standardStartVersion.md) - The earliest CRF IG version applicable to the CRF specialization
 * [submissionValue](submissionValue.md) - CDISC submission value
     * [CodeList➞submissionValue](CodeList_submissionValue.md) - CDISC submission value for the codelist
 * [value](value.md) - CDISC submission value for the CRF item
     * [ListValue➞value](ListValue_value.md) - User-friendly display value for the CRF item
     * [PrepopulatedValue➞value](PrepopulatedValue_value.md) - Submission value for pre-populated term in NCIt
 * [valueList](valueList.md) - A set of values for a CRF item
 * [variableName](variableName.md) - Variable name of the CRF item for which data are being collected.

### Enums

 * [CRFItemDataTypeEnum](CRFItemDataTypeEnum.md)
 * [ImplementationOptionEnum](ImplementationOptionEnum.md)
 * [PackageTypeEnum](PackageTypeEnum.md)
 * [SelectionTypeEnum](SelectionTypeEnum.md)

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
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
