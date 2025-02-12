-- # Class: "BiomedicalConcept" Description: ""
--     * Slot: packageDate Description: Biomedical Concept package release date indicating when the BC package was published to production
--     * Slot: packageType Description: Package type (bc for Biomedical Concepts)
--     * Slot: conceptId Description: A unique identifier for a Biomedical Concept which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
--     * Slot: ncitCode Description: NCIt C-code for the Biomedical Concept
--     * Slot: href Description: URI link to NCIt for the Biomedical Concept; blank if  concept is not available in NCIt
--     * Slot: parentConceptId Description: C-code for the parent concept in the NCIt hiearchy; blank if concept is not available in NCIt
--     * Slot: shortName Description: NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt
--     * Slot: definition Description: NCIt definition for the Biomedical Concept; provisional defintion if concept is not available in NCIt
-- # Class: "Coding" Description: ""
--     * Slot: id Description: 
--     * Slot: code Description: Synonym concept for the Biomedical Concept as defined in a code system
--     * Slot: system Description: Identifies the code system for the synonym concept. The URL of the code system should be used if it exists
--     * Slot: systemName Description: Human-readable name for the code system
--     * Slot: BiomedicalConcept_conceptId Description: Autocreated FK slot
-- # Class: "DataElementConcept" Description: ""
--     * Slot: conceptId Description: An identifier for a Data Element Concept (DEC) which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
--     * Slot: ncitCode Description: NCI C-code for the BC Data Element Concept
--     * Slot: href Description: Link to NCIt for the Data Element Concept
--     * Slot: shortName Description: NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt
--     * Slot: dataType Description: Data Type for the Data Element Concept
--     * Slot: BiomedicalConcept_conceptId Description: Autocreated FK slot
-- # Class: "BiomedicalConcept_categories" Description: ""
--     * Slot: BiomedicalConcept_conceptId Description: Autocreated FK slot
--     * Slot: categories Description: Biomedical Concept category for the faciliation of API search and extract
-- # Class: "BiomedicalConcept_synonyms" Description: ""
--     * Slot: BiomedicalConcept_conceptId Description: Autocreated FK slot
--     * Slot: synonyms Description: Biomedical Concept synonym equivalent to BC short name for the facilitation of API search and extraction
-- # Class: "BiomedicalConcept_resultScales" Description: ""
--     * Slot: BiomedicalConcept_conceptId Description: Autocreated FK slot
--     * Slot: resultScales Description: Scale of measurement for the Biomedical Concept result
-- # Class: "DataElementConcept_exampleSet" Description: ""
--     * Slot: DataElementConcept_conceptId Description: Autocreated FK slot
--     * Slot: exampleSet Description: Example values for the Data Element Concept

CREATE TABLE "BiomedicalConcept" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(2) NOT NULL, 
	"conceptId" TEXT NOT NULL, 
	"ncitCode" TEXT, 
	href TEXT, 
	"parentConceptId" TEXT, 
	"shortName" TEXT NOT NULL, 
	definition TEXT NOT NULL, 
	PRIMARY KEY ("conceptId")
);
CREATE TABLE "Coding" (
	id INTEGER NOT NULL, 
	code TEXT NOT NULL, 
	system TEXT NOT NULL, 
	"systemName" TEXT, 
	"BiomedicalConcept_conceptId" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("BiomedicalConcept_conceptId") REFERENCES "BiomedicalConcept" ("conceptId")
);
CREATE TABLE "DataElementConcept" (
	"conceptId" TEXT NOT NULL, 
	"ncitCode" TEXT, 
	href TEXT, 
	"shortName" TEXT NOT NULL, 
	"dataType" VARCHAR(8) NOT NULL, 
	"BiomedicalConcept_conceptId" TEXT, 
	PRIMARY KEY ("conceptId"), 
	FOREIGN KEY("BiomedicalConcept_conceptId") REFERENCES "BiomedicalConcept" ("conceptId")
);
CREATE TABLE "BiomedicalConcept_categories" (
	"BiomedicalConcept_conceptId" TEXT, 
	categories TEXT NOT NULL, 
	PRIMARY KEY ("BiomedicalConcept_conceptId", categories), 
	FOREIGN KEY("BiomedicalConcept_conceptId") REFERENCES "BiomedicalConcept" ("conceptId")
);
CREATE TABLE "BiomedicalConcept_synonyms" (
	"BiomedicalConcept_conceptId" TEXT, 
	synonyms TEXT, 
	PRIMARY KEY ("BiomedicalConcept_conceptId", synonyms), 
	FOREIGN KEY("BiomedicalConcept_conceptId") REFERENCES "BiomedicalConcept" ("conceptId")
);
CREATE TABLE "BiomedicalConcept_resultScales" (
	"BiomedicalConcept_conceptId" TEXT, 
	"resultScales" VARCHAR(12), 
	PRIMARY KEY ("BiomedicalConcept_conceptId", "resultScales"), 
	FOREIGN KEY("BiomedicalConcept_conceptId") REFERENCES "BiomedicalConcept" ("conceptId")
);
CREATE TABLE "DataElementConcept_exampleSet" (
	"DataElementConcept_conceptId" TEXT, 
	"exampleSet" TEXT, 
	PRIMARY KEY ("DataElementConcept_conceptId", "exampleSet"), 
	FOREIGN KEY("DataElementConcept_conceptId") REFERENCES "DataElementConcept" ("conceptId")
);