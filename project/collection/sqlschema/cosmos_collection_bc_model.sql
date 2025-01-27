

CREATE TABLE "CodeList" (
	"conceptId" TEXT NOT NULL, 
	href TEXT, 
	"submissionValue" TEXT NOT NULL, 
	PRIMARY KEY ("conceptId")
);

CREATE TABLE "DataCollectionGroup" (
	"packageDate" DATE NOT NULL, 
	"packageType" VARCHAR(10) NOT NULL, 
	"datasetSpecializationId" TEXT NOT NULL, 
	standard TEXT NOT NULL, 
	"standardStartVersion" TEXT NOT NULL, 
	"standardEndVersion" TEXT, 
	domain TEXT, 
	"shortName" TEXT NOT NULL, 
	"biomedicalConceptId" TEXT, 
	"sdtmDatasetSpecializationId" TEXT, 
	PRIMARY KEY ("datasetSpecializationId")
);

CREATE TABLE "PrepopulatedValue" (
	"conceptId" TEXT, 
	value TEXT NOT NULL, 
	PRIMARY KEY ("conceptId", value)
);

CREATE TABLE "DataCollectionItem" (
	name TEXT NOT NULL, 
	"dataElementConceptId" TEXT, 
	"isNonStandard" BOOLEAN, 
	"eCRFItem" TEXT NOT NULL, 
	"questionText" TEXT, 
	prompt TEXT, 
	"orderNumber" INTEGER NOT NULL, 
	codelist TEXT, 
	"listStyle" VARCHAR(19), 
	"prepopulatedValue" TEXT, 
	"displayHidden" BOOLEAN, 
	"dataType" VARCHAR(7) NOT NULL, 
	length INTEGER, 
	"significantDigits" INTEGER, 
	"mandatoryVariable" BOOLEAN NOT NULL, 
	"DataCollectionGroup_datasetSpecializationId" TEXT, 
	PRIMARY KEY (name), 
	FOREIGN KEY(codelist) REFERENCES "CodeList" ("conceptId"), 
	FOREIGN KEY("DataCollectionGroup_datasetSpecializationId") REFERENCES "DataCollectionGroup" ("datasetSpecializationId")
);

CREATE TABLE "ListValue" (
	value TEXT, 
	"displayValue" TEXT NOT NULL, 
	"DataCollectionItem_name" TEXT, 
	PRIMARY KEY (value, "displayValue", "DataCollectionItem_name"), 
	FOREIGN KEY("DataCollectionItem_name") REFERENCES "DataCollectionItem" (name)
);

CREATE TABLE "SDTMTarget" (
	"sdtmVariable" TEXT NOT NULL, 
	"sdtmAnnotation" TEXT, 
	"sdtmTargetMapping" TEXT NOT NULL, 
	"DataCollectionItem_name" TEXT, 
	PRIMARY KEY ("sdtmVariable", "sdtmAnnotation", "sdtmTargetMapping", "DataCollectionItem_name"), 
	FOREIGN KEY("DataCollectionItem_name") REFERENCES "DataCollectionItem" (name)
);
