

CREATE TABLE "AssignedTerm" (
	"conceptId" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("conceptId", value)
);

CREATE TABLE "CodeList" (
	"conceptId" TEXT NOT NULL, 
	href TEXT, 
	"submissionValue" TEXT NOT NULL, 
	PRIMARY KEY ("conceptId")
);

CREATE TABLE "CodeListTerm" (
	"termId" TEXT NOT NULL, 
	"termValue" TEXT NOT NULL, 
	PRIMARY KEY ("termId", "termValue")
);

CREATE TABLE "RelationShip" (
	subject TEXT NOT NULL, 
	"linkingPhrase" VARCHAR(101) NOT NULL, 
	"predicateTerm" VARCHAR(22) NOT NULL, 
	object TEXT NOT NULL, 
	PRIMARY KEY (subject, "linkingPhrase", "predicateTerm", object)
);

CREATE TABLE "SDTMGroup" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(4) NOT NULL, 
	domain TEXT NOT NULL, 
	"shortName" TEXT NOT NULL, 
	"datasetSpecializationId" TEXT NOT NULL, 
	source TEXT NOT NULL, 
	"sdtmigStartVersion" TEXT NOT NULL, 
	"sdtmigEndVersion" TEXT, 
	"biomedicalConceptId" TEXT, 
	PRIMARY KEY ("datasetSpecializationId")
);

CREATE TABLE "SubsetCodeList" (
	"parentCodelist" TEXT NOT NULL, 
	"subsetShortName" TEXT NOT NULL, 
	"subsetLabel" TEXT NOT NULL, 
	"codelistTerm" TEXT NOT NULL, 
	PRIMARY KEY ("parentCodelist", "subsetShortName", "subsetLabel", "codelistTerm")
);

CREATE TABLE "SDTMVariable" (
	name TEXT NOT NULL, 
	"dataElementConceptId" TEXT, 
	"isNonStandard" BOOLEAN, 
	codelist TEXT, 
	"subsetCodelist" TEXT, 
	"assignedTerm" TEXT, 
	role VARCHAR(10), 
	relationship TEXT, 
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
	PRIMARY KEY (name), 
	FOREIGN KEY(codelist) REFERENCES "CodeList" ("conceptId"), 
	FOREIGN KEY("SDTMGroup_datasetSpecializationId") REFERENCES "SDTMGroup" ("datasetSpecializationId")
);

CREATE TABLE "SDTMVariable_valueList" (
	backref_id TEXT, 
	"valueList" TEXT, 
	PRIMARY KEY (backref_id, "valueList"), 
	FOREIGN KEY(backref_id) REFERENCES "SDTMVariable" (name)
);
