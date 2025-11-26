-- # Class: "SDTMGroup" Description: ""
--     * Slot: packageDate Description: Biomedical Concept package release date indicating when the BC package was published to production
--     * Slot: packageType Description: Package type (sdtm for SDTM Dataset Specializations)
--     * Slot: datasetSpecializationId Description: Identifier for SDTM Value Level Metadata group
--     * Slot: domain Description: Domain for the SDTM specialization group
--     * Slot: shortName Description: SDTM group short name which provides a user friendly and intuitive name for the vlm_group_id
--     * Slot: source Description: SDTM VLM Source which categorizes VLM groups by topic variable
--     * Slot: sdtmigStartVersion Description: The earliest SDTMIG version applicable to the BC dataset specialization
--     * Slot: sdtmigEndVersion Description: The last SDTMIG version that is applicable to the BC dataset specialization
--     * Slot: biomedicalConceptId Description: Biomedical Concept identifier foreign key
-- # Class: "SDTMVariable" Description: ""
--     * Slot: name Description: Variable included in the SDTM dataset specialization
--     * Slot: dataElementConceptId Description: Biomedical Concept Data Element Concept identifier foreign key
--     * Slot: isNonStandard Description: Flag that indicates if the variable is a non-standard variable
--     * Slot: subsetCodelist Description: Subset codelist short name
--     * Slot: role Description: SDTM variable role
--     * Slot: dataType Description: Variable data type
--     * Slot: length Description: Variable length
--     * Slot: format Description: Variable display format
--     * Slot: significantDigits Description: Variable significant_digits
--     * Slot: mandatoryVariable Description: Indicator that variable must be present within the SDTM group
--     * Slot: mandatoryValue Description: Indicator that variable must be populated within the SDTM group
--     * Slot: originType Description: Variable origin type (define-XML v21)
--     * Slot: originSource Description: Variable origin source (define-XML v21)
--     * Slot: comparator Description: Comparison operator for SDTM group variables included in VLM
--     * Slot: vlmTarget Description: Target variable for VLM
--     * Slot: SDTMGroup_datasetSpecializationId Description: Autocreated FK slot
--     * Slot: codelist_conceptId Description: Codelist
--     * Slot: assignedTerm_id Description: Assigned term
--     * Slot: relationship_id Description: Relationship between variables
-- # Class: "RelationShip" Description: ""
--     * Slot: id Description: 
--     * Slot: subject Description: Subject in a variable relationship
--     * Slot: linkingPhrase Description: Variable relationship descriptive linking phrase
--     * Slot: predicateTerm Description: Short variable relationship linking phrase for programming purposes
--     * Slot: object Description: Object in a variable relationship
-- # Class: "CodeList" Description: ""
--     * Slot: conceptId Description: C-code for a codelist in NCIt
--     * Slot: href Description: Link to NCIt for the codelist
--     * Slot: submissionValue Description: CDISC submission value for the codelist
-- # Class: "CodeListTerm" Description: ""
--     * Slot: id Description: 
--     * Slot: termId Description: C-code term in subset codelist
--     * Slot: termValue Description: Submision value of term in subset codelist
--     * Slot: SubsetCodeList_id Description: Autocreated FK slot
-- # Class: "SubsetCodeList" Description: ""
--     * Slot: id Description: 
--     * Slot: parentCodelist Description: Subset codelist parent codelist
--     * Slot: subsetShortName Description: Subset codelist short name
--     * Slot: subsetLabel Description: Subset codelist label
-- # Class: "AssignedTerm" Description: ""
--     * Slot: id Description: 
--     * Slot: conceptId Description: C-code for assigned term in NCIt or left blank when CDISC terminology does not apply
--     * Slot: value Description: Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value
-- # Class: "SDTMVariable_valueList" Description: ""
--     * Slot: SDTMVariable_name Description: Autocreated FK slot
--     * Slot: valueList Description: List of SDTM submission values used if subset codelist is not applicable

CREATE TABLE "SDTMGroup" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(4) NOT NULL, 
	"datasetSpecializationId" TEXT NOT NULL, 
	domain TEXT NOT NULL, 
	"shortName" TEXT NOT NULL, 
	source TEXT NOT NULL, 
	"sdtmigStartVersion" TEXT NOT NULL, 
	"sdtmigEndVersion" TEXT, 
	"biomedicalConceptId" TEXT, 
	PRIMARY KEY ("datasetSpecializationId")
);
CREATE TABLE "RelationShip" (
	id INTEGER NOT NULL, 
	subject TEXT NOT NULL, 
	"linkingPhrase" VARCHAR(101) NOT NULL, 
	"predicateTerm" VARCHAR(28) NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CodeList" (
	"conceptId" TEXT NOT NULL, 
	href TEXT, 
	"submissionValue" TEXT NOT NULL, 
	PRIMARY KEY ("conceptId")
);
CREATE TABLE "SubsetCodeList" (
	id INTEGER NOT NULL, 
	"parentCodelist" TEXT NOT NULL, 
	"subsetShortName" TEXT NOT NULL, 
	"subsetLabel" TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AssignedTerm" (
	id INTEGER NOT NULL, 
	"conceptId" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "SDTMVariable" (
	name TEXT NOT NULL, 
	"dataElementConceptId" TEXT, 
	"isNonStandard" BOOLEAN, 
	"subsetCodelist" TEXT, 
	role VARCHAR(10), 
	"dataType" VARCHAR(16), 
	length INTEGER, 
	format TEXT, 
	"significantDigits" INTEGER, 
	"mandatoryVariable" BOOLEAN, 
	"mandatoryValue" BOOLEAN, 
	"originType" VARCHAR(11), 
	"originSource" VARCHAR(12), 
	comparator VARCHAR(2), 
	"vlmTarget" BOOLEAN, 
	"SDTMGroup_datasetSpecializationId" TEXT, 
	"codelist_conceptId" TEXT, 
	"assignedTerm_id" INTEGER, 
	relationship_id INTEGER, 
	PRIMARY KEY (name), 
	FOREIGN KEY("SDTMGroup_datasetSpecializationId") REFERENCES "SDTMGroup" ("datasetSpecializationId"), 
	FOREIGN KEY("codelist_conceptId") REFERENCES "CodeList" ("conceptId"), 
	FOREIGN KEY("assignedTerm_id") REFERENCES "AssignedTerm" (id), 
	FOREIGN KEY(relationship_id) REFERENCES "RelationShip" (id)
);
CREATE TABLE "CodeListTerm" (
	id INTEGER NOT NULL, 
	"termId" TEXT NOT NULL, 
	"termValue" TEXT NOT NULL, 
	"SubsetCodeList_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SubsetCodeList_id") REFERENCES "SubsetCodeList" (id)
);
CREATE TABLE "SDTMVariable_valueList" (
	"SDTMVariable_name" TEXT, 
	"valueList" TEXT, 
	PRIMARY KEY ("SDTMVariable_name", "valueList"), 
	FOREIGN KEY("SDTMVariable_name") REFERENCES "SDTMVariable" (name)
);