-- # Class: "DataCollectionGroup" Description: ""
--     * Slot: packageDate Description: Biomedical Concept package release date indicating when the BC package was published to production
--     * Slot: packageType Description: Package type for data collection specializations (collection)
--     * Slot: collectionSpecializationId Description: Identifier for data collection specialization group
--     * Slot: shortName Description: Short name which provides a user friendly and intuitive name for the data collection group
--     * Slot: standard Description: Standard for the data collection specialization group
--     * Slot: standardStartVersion Description: The earliest data collection IG version applicable to the collection specialization
--     * Slot: standardEndVersion Description: The last data collection IG version that is applicable to the collection specialization
--     * Slot: implementationOption Description: Implementation option for the data collection specialization group
--     * Slot: scenario Description: Scenario for the data collection specialization group
--     * Slot: domain Description: Domain for the data collection specialization group
--     * Slot: biomedicalConceptId Description: Biomedical Concept identifier foreign key
--     * Slot: sdtmDatasetSpecializationId Description: Identifier for SDTM Dataset Specialization group
-- # Class: "DataCollectionItem" Description: ""
--     * Slot: name Description: Item name as it appears on the collection instrument
--     * Slot: variableName Description: Variable name of the collection item for which data are being collected.
--     * Slot: dataElementConceptId Description: Biomedical Concept Data Element Concept identifier foreign key
--     * Slot: questionText Description: Item question text
--     * Slot: prompt Description: Item prompt
--     * Slot: orderNumber Description: Item order number
--     * Slot: mandatoryVariable Description: Indicator that the item must be present within the data collection group
--     * Slot: dataType Description: Item data type
--     * Slot: length Description: Item length
--     * Slot: significantDigits Description: Item significant_digits
--     * Slot: displayHidden Description: Indicator that the item is hidden from the user
--     * Slot: listType Description: Type of list used for set-up of the data collection instrument
--     * Slot: DataCollectionGroup_collectionSpecializationId Description: Autocreated FK slot
--     * Slot: codelist_id Description: Codelist
--     * Slot: prepopulatedValue_id Description: Pre-populated value for the data collection instrument
--     * Slot: sdtmTarget_id Description: SDTM target variables for data collection item variable
-- # Class: "ListValue" Description: ""
--     * Slot: id Description: 
--     * Slot: displayValue Description: CDISC submission value for the data collection item
--     * Slot: value Description: User-friendly display value for the data collection item
--     * Slot: DataCollectionItem_name Description: Autocreated FK slot
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
--     * Slot: sdtmAnnotation Description: Annotation of the SDTM target in the data collection instrument
--     * Slot: sdtmTargetMapping Description: Rule for mapping from data collection item to SDTM target variable.
-- # Class: "SDTMTarget_sdtmVariable" Description: ""
--     * Slot: SDTMTarget_id Description: Autocreated FK slot
--     * Slot: sdtmVariable Description: SDTM target variable for data collection item variable

CREATE TABLE "DataCollectionGroup" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(10) NOT NULL, 
	"collectionSpecializationId" TEXT NOT NULL, 
	"shortName" TEXT NOT NULL, 
	standard TEXT NOT NULL, 
	"standardStartVersion" TEXT NOT NULL, 
	"standardEndVersion" TEXT, 
	"implementationOption" VARCHAR(10), 
	scenario TEXT, 
	domain TEXT, 
	"biomedicalConceptId" TEXT, 
	"sdtmDatasetSpecializationId" TEXT NOT NULL, 
	PRIMARY KEY ("collectionSpecializationId")
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
CREATE TABLE "DataCollectionItem" (
	name TEXT NOT NULL, 
	"variableName" TEXT NOT NULL, 
	"dataElementConceptId" TEXT, 
	"questionText" TEXT, 
	prompt TEXT, 
	"orderNumber" INTEGER NOT NULL, 
	"mandatoryVariable" BOOLEAN NOT NULL, 
	"dataType" VARCHAR(7) NOT NULL, 
	length INTEGER, 
	"significantDigits" INTEGER, 
	"displayHidden" BOOLEAN, 
	"listType" VARCHAR(19), 
	"DataCollectionGroup_collectionSpecializationId" TEXT, 
	codelist_id INTEGER, 
	"prepopulatedValue_id" INTEGER, 
	"sdtmTarget_id" INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("DataCollectionGroup_collectionSpecializationId") REFERENCES "DataCollectionGroup" ("collectionSpecializationId"), 
	FOREIGN KEY(codelist_id) REFERENCES "CodeList" (id), 
	FOREIGN KEY("prepopulatedValue_id") REFERENCES "PrepopulatedValue" (id), 
	FOREIGN KEY("sdtmTarget_id") REFERENCES "SDTMTarget" (id)
);
CREATE TABLE "SDTMTarget_sdtmVariable" (
	"SDTMTarget_id" INTEGER, 
	"sdtmVariable" TEXT NOT NULL, 
	PRIMARY KEY ("SDTMTarget_id", "sdtmVariable"), 
	FOREIGN KEY("SDTMTarget_id") REFERENCES "SDTMTarget" (id)
);
CREATE TABLE "ListValue" (
	id INTEGER NOT NULL, 
	"displayValue" TEXT NOT NULL, 
	value TEXT, 
	"DataCollectionItem_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataCollectionItem_name") REFERENCES "DataCollectionItem" (name)
);