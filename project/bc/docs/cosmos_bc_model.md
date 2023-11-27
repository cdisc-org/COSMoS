
# COSMoS-Biomedical-Concepts-Schema


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [BiomedicalConcept](BiomedicalConcept.md)
 * [Coding](Coding.md)
 * [DataElementConcept](DataElementConcept.md)

### Mixins


### Slots

 * [categories](categories.md) - Biomedical Concept category for the faciliation of API search and extract
 * [code](code.md) - Synonym concept for the Biomedical Concept as defined in a code system
 * [coding](coding.md)
 * [conceptId](conceptId.md) - An identifier that uniquely represents an entity
     * [BiomedicalConcept➞conceptId](BiomedicalConcept_conceptId.md) - A unique identifier for a Biomedical Concept which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
     * [DataElementConcept➞conceptId](DataElementConcept_conceptId.md) - An identifier for a Data Element Concept (DEC) which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
 * [dataElementConcepts](dataElementConcepts.md) - Data Element Concept
 * [dataType](dataType.md) - Data Type for the Data Element Concept
 * [definition](definition.md) - NCIt definition for the Biomedical Concept; provisional defintion if concept is not available in NCIt
 * [exampleSet](exampleSet.md) - Example values for the Data Element Concept
 * [href](href.md)
     * [BiomedicalConcept➞href](BiomedicalConcept_href.md) - URI link to NCIt for the Biomedical Concept; blank if  concept is not available in NCIt
     * [DataElementConcept➞href](DataElementConcept_href.md) - Link to NCIt for the Data Element Concept
 * [ncitCode](ncitCode.md) - NCIt code
     * [BiomedicalConcept➞ncitCode](BiomedicalConcept_ncitCode.md) - NCIt C-code for the Biomedical Concept
     * [DataElementConcept➞ncitCode](DataElementConcept_ncitCode.md) - NCI C-code for the BC Data Element Concept
 * [packageDate](packageDate.md) - Biomedical Concept package release date indicating when the BC package was published to production
 * [packageType](packageType.md) - Package type (bc for Biomedical Concepts)
 * [parentConceptId](parentConceptId.md) - C-code for the parent concept in the NCIt hiearchy; blank if concept is not available in NCIt
 * [resultScales](resultScales.md) - Scale of measurement for the Biomedical Concept result
 * [shortName](shortName.md) - NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt
 * [synonyms](synonyms.md) - Biomedical Concept synonym equivalent to BC short name for the facilitation of API search and extraction
 * [system](system.md) - Identifies the code system for the synonym concept. The URL of the code system should be used if it exists
 * [systemName](systemName.md) - Human-readable name for the code system

### Enums

 * [BiomedicalConceptPackageTypeEnum](BiomedicalConceptPackageTypeEnum.md)
 * [BiomedicalConceptResultScaleEnum](BiomedicalConceptResultScaleEnum.md)
 * [DataElementConceptDataTypeEnum](DataElementConceptDataTypeEnum.md)

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
