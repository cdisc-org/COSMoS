-- # Class: "DataCollectionGroup" Description: ""
--     * Slot: packageDate Description: Biomedical Concept package release date indicating when the BC package was published to production
--     * Slot: packageType Description: Package type for data collection specializations (collection)
--     * Slot: collectionSpecializationId Description: Identifier for data collection specialization group
--     * Slot: shortName Description: Short name which provides a user friendly and intuitive name for the data collection group
--     * Slot: standard Description: Standard for the data collection specialization group
--     * Slot: standardStartVersion Description: The earliest data collection IG version applicable to the collection specialization
--     * Slot: standardEndVersion Description: The last data collection IG version that is applicable to the collection specialization
--     * Slot: domain Description: Domain for the data collection specialization group
--     * Slot: biomedicalConceptId Description: Biomedical Concept identifier foreign key
--     * Slot: sdtmDatasetSpecializationId Description: Identifier for SDTM Dataset Specialization group
-- # Class: "DataCollectionItem" Description: ""
--     * Slot: name Description: Item included in the data collection dataset specialization
--     * Slot: dataElementConceptId Description: Biomedical Concept Data Element Concept identifier foreign key
--     * Slot: isNonStandard Description: Flag that indicates if the variable is a non-standard variable
--     * Slot: dataCollectionInstrumentItem Description: Item included in the data collection dataset specialization used for eCSR set-up
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
--     * Slot: prepopulatedValue_id Description: Pre-populated value for the data collection instrument
--     * Slot: codelist_id Description: Codelist
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
--     * Slot: sdtmVariable Description: SDTM target variable for data collection item variable
--     * Slot: sdtmAnnotation Description: Annotation of the SDTM target in the data collection instrument
--     * Slot: sdtmTargetMapping Description: Rule for mapping from data collection item to SDTM target variable.
--     * Slot: DataCollectionItem_name Description: Autocreated FK slot

CREATE TABLE "DataCollectionGroup" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(10) NOT NULL, 
	"collectionSpecializationId" TEXT NOT NULL, 
	"shortName" TEXT NOT NULL, 
	standard TEXT NOT NULL, 
	"standardStartVersion" TEXT NOT NULL, 
	"standardEndVersion" TEXT, 
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
CREATE TABLE "DataCollectionItem" (
	name TEXT NOT NULL, 
	"dataElementConceptId" TEXT, 
	"isNonStandard" BOOLEAN, 
	"dataCollectionInstrumentItem" TEXT NOT NULL, 
	"questionText" TEXT NOT NULL, 
	prompt TEXT, 
	"orderNumber" INTEGER NOT NULL, 
	"mandatoryVariable" BOOLEAN NOT NULL, 
	"dataType" VARCHAR(7) NOT NULL, 
	length INTEGER, 
	"significantDigits" INTEGER, 
	"displayHidden" BOOLEAN, 
	"listType" VARCHAR(19), 
	"DataCollectionGroup_collectionSpecializationId" TEXT, 
	"prepopulatedValue_id" INTEGER, 
	codelist_id INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("DataCollectionGroup_collectionSpecializationId") REFERENCES "DataCollectionGroup" ("collectionSpecializationId"), 
	FOREIGN KEY("prepopulatedValue_id") REFERENCES "PrepopulatedValue" (id), 
	FOREIGN KEY(codelist_id) REFERENCES "CodeList" (id)
);
CREATE TABLE "ListValue" (
	id INTEGER NOT NULL, 
	"displayValue" TEXT NOT NULL, 
	value TEXT, 
	"DataCollectionItem_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataCollectionItem_name") REFERENCES "DataCollectionItem" (name)
);
CREATE TABLE "SDTMTarget" (
	id INTEGER NOT NULL, 
	"sdtmVariable" TEXT NOT NULL, 
	"sdtmAnnotation" TEXT, 
	"sdtmTargetMapping" TEXT, 
	"DataCollectionItem_name" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("DataCollectionItem_name") REFERENCES "DataCollectionItem" (name)
);