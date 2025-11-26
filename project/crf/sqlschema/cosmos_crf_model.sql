-- # Class: "CRFGroup" Description: ""
--     * Slot: packageDate Description: Biomedical Concept package release date indicating when the BC package was published to production
--     * Slot: packageType Description: Package type for CRF specializations (crf)
--     * Slot: crfSpecializationId Description: Identifier for CRF specialization group
--     * Slot: shortName Description: Short name which provides a user friendly and intuitive name for the CRF group
--     * Slot: standard Description: Standard for the CRF specialization group
--     * Slot: standardStartVersion Description: The earliest CRF IG version applicable to the CRF specialization
--     * Slot: standardEndVersion Description: The last CRF IG version that is applicable to the CRF specialization
--     * Slot: implementationOption Description: Implementation option for the CRF specialization group
--     * Slot: scenario Description: Scenario for the CRF specialization group
--     * Slot: domain Description: Domain for the CRF specialization group
--     * Slot: biomedicalConceptId Description: Biomedical Concept identifier foreign key
--     * Slot: sdtmDatasetSpecializationId Description: Identifier for SDTM Dataset Specialization group
-- # Class: "CRFItem" Description: ""
--     * Slot: name Description: Item name as it appears on the CRF instrument
--     * Slot: variableName Description: Variable name of the CRF item for which data are being collected.
--     * Slot: dataElementConceptId Description: Biomedical Concept Data Element Concept identifier foreign key
--     * Slot: questionText Description: Item question text
--     * Slot: prompt Description: Item prompt
--     * Slot: completionInstructions Description: Item completion instructions
--     * Slot: orderNumber Description: Item order number
--     * Slot: mandatoryVariable Description: Indicator that the item must be present within the CRF group
--     * Slot: dataType Description: Item data type
--     * Slot: length Description: Item length
--     * Slot: significantDigits Description: Item significant_digits
--     * Slot: displayHidden Description: Indicator that the item is hidden from the user
--     * Slot: derivedVariable Description: Indicator that variable is derived
--     * Slot: derivationDescription Description: Description of the derivation. Required when derivedVariable is true.
--     * Slot: selectionType Description: Type of selection used for set-up of the CRF instrument
--     * Slot: CRFGroup_crfSpecializationId Description: Autocreated FK slot
--     * Slot: codelist_id Description: Codelist
--     * Slot: prepopulatedValue_id Description: Pre-populated value for the CRF instrument
--     * Slot: sdtmTarget_id Description: SDTM target variables for CRF item variable
-- # Class: "ListValue" Description: ""
--     * Slot: id Description: 
--     * Slot: displayValue Description: CDISC submission value for the CRF item
--     * Slot: value Description: User-friendly display value for the CRF item
--     * Slot: CRFItem_name Description: Autocreated FK slot
-- # Class: "PrepopulatedValue" Description: ""
--     * Slot: id Description: 
--     * Slot: value Description: Submission value for pre-populated term in NCIt
--     * Slot: conceptId Description: C-code for pre-populated term in NCIt
-- # Class: "CodeList" Description: ""
--     * Slot: id Description: 
--     * Slot: submissionValue Description: CDISC submission value for the codelist
--     * Slot: conceptId Description: C-code for codelist in NCIt
--     * Slot: href Description: Link to NCIt for the codelist
-- # Class: "SDTMTarget" Description: ""
--     * Slot: id Description: 
--     * Slot: sdtmAnnotation Description: Annotation of the SDTM target in the CRF instrument
--     * Slot: sdtmTargetMapping Description: Rule for mapping from CRF item to SDTM target variable.
-- # Class: "CRFGroup_categories" Description: ""
--     * Slot: CRFGroup_crfSpecializationId Description: Autocreated FK slot
--     * Slot: categories Description: CRF Dataset Specialization category for the faciliation of API search and extract
-- # Class: "SDTMTarget_sdtmVariables" Description: ""
--     * Slot: SDTMTarget_id Description: Autocreated FK slot
--     * Slot: sdtmVariables Description: SDTM target variable for CRF item variable

CREATE TABLE "CRFGroup" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(3) NOT NULL, 
	"crfSpecializationId" TEXT NOT NULL, 
	"shortName" TEXT NOT NULL, 
	standard TEXT NOT NULL, 
	"standardStartVersion" TEXT NOT NULL, 
	"standardEndVersion" TEXT, 
	"implementationOption" VARCHAR(12), 
	scenario TEXT, 
	domain TEXT, 
	"biomedicalConceptId" TEXT, 
	"sdtmDatasetSpecializationId" TEXT, 
	PRIMARY KEY ("crfSpecializationId")
);
CREATE TABLE "PrepopulatedValue" (
	id INTEGER NOT NULL, 
	value TEXT NOT NULL, 
	"conceptId" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CodeList" (
	id INTEGER NOT NULL, 
	"submissionValue" TEXT NOT NULL, 
	"conceptId" TEXT, 
	href TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SDTMTarget" (
	id INTEGER NOT NULL, 
	"sdtmAnnotation" TEXT, 
	"sdtmTargetMapping" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CRFItem" (
	name TEXT NOT NULL, 
	"variableName" TEXT NOT NULL, 
	"dataElementConceptId" TEXT, 
	"questionText" TEXT, 
	prompt TEXT, 
	"completionInstructions" TEXT, 
	"orderNumber" INTEGER NOT NULL, 
	"mandatoryVariable" BOOLEAN NOT NULL, 
	"dataType" VARCHAR(7) NOT NULL, 
	length INTEGER, 
	"significantDigits" INTEGER, 
	"displayHidden" BOOLEAN, 
	"derivedVariable" BOOLEAN, 
	"derivationDescription" TEXT, 
	"selectionType" VARCHAR(8), 
	"CRFGroup_crfSpecializationId" TEXT, 
	codelist_id INTEGER, 
	"prepopulatedValue_id" INTEGER, 
	"sdtmTarget_id" INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("CRFGroup_crfSpecializationId") REFERENCES "CRFGroup" ("crfSpecializationId"), 
	FOREIGN KEY(codelist_id) REFERENCES "CodeList" (id), 
	FOREIGN KEY("prepopulatedValue_id") REFERENCES "PrepopulatedValue" (id), 
	FOREIGN KEY("sdtmTarget_id") REFERENCES "SDTMTarget" (id)
);
CREATE TABLE "CRFGroup_categories" (
	"CRFGroup_crfSpecializationId" TEXT, 
	categories TEXT, 
	PRIMARY KEY ("CRFGroup_crfSpecializationId", categories), 
	FOREIGN KEY("CRFGroup_crfSpecializationId") REFERENCES "CRFGroup" ("crfSpecializationId")
);
CREATE TABLE "SDTMTarget_sdtmVariables" (
	"SDTMTarget_id" INTEGER, 
	"sdtmVariables" TEXT, 
	PRIMARY KEY ("SDTMTarget_id", "sdtmVariables"), 
	FOREIGN KEY("SDTMTarget_id") REFERENCES "SDTMTarget" (id)
);
CREATE TABLE "ListValue" (
	id INTEGER NOT NULL, 
	"displayValue" TEXT NOT NULL, 
	value TEXT, 
	"CRFItem_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("CRFItem_name") REFERENCES "CRFItem" (name)
);