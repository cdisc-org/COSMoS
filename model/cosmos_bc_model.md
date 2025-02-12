```mermaid
erDiagram
BiomedicalConcept {
    date packageDate  
    PackageTypeEnum packageType  
    string conceptId  
    string ncitCode  
    uri href  
    string parentConceptId  
    stringList categories  
    string shortName  
    stringList synonyms  
    BiomedicalConceptResultScaleEnumList resultScales  
    string definition  
}
Coding {
    string code  
    string system  
    string systemName  
}
DataElementConcept {
    string conceptId  
    string ncitCode  
    uri href  
    string shortName  
    DataElementConceptDataTypeEnum dataType  
    stringList exampleSet  
}

BiomedicalConcept ||--}o Coding : "coding"
BiomedicalConcept ||--}o DataElementConcept : "dataElementConcepts"

```

