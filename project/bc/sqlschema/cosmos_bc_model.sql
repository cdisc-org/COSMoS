

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
	code TEXT NOT NULL, 
	system TEXT NOT NULL, 
	"systemName" TEXT, 
	"BiomedicalConcept_conceptId" TEXT, 
	PRIMARY KEY (code, system, "systemName", "BiomedicalConcept_conceptId"), 
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
	backref_id TEXT, 
	categories TEXT NOT NULL, 
	PRIMARY KEY (backref_id, categories), 
	FOREIGN KEY(backref_id) REFERENCES "BiomedicalConcept" ("conceptId")
);

CREATE TABLE "BiomedicalConcept_synonyms" (
	backref_id TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (backref_id, synonyms), 
	FOREIGN KEY(backref_id) REFERENCES "BiomedicalConcept" ("conceptId")
);

CREATE TABLE "BiomedicalConcept_resultScales" (
	backref_id TEXT, 
	"resultScales" VARCHAR(12), 
	PRIMARY KEY (backref_id, "resultScales"), 
	FOREIGN KEY(backref_id) REFERENCES "BiomedicalConcept" ("conceptId")
);

CREATE TABLE "DataElementConcept_exampleSet" (
	backref_id TEXT, 
	"exampleSet" TEXT, 
	PRIMARY KEY (backref_id, "exampleSet"), 
	FOREIGN KEY(backref_id) REFERENCES "DataElementConcept" ("conceptId")
);
