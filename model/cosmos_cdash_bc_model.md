```mermaid
erDiagram
CDASHGroup {
    date packageDate  
    CDASHDatasetSpecializationPackageType packageType  
    string domain  
    string shortName  
    CDASHScenario scenario  
    string datasetSpecializationId  
    string cdashigStartVersion  
    string cdashigEndVersion  
    string biomedicalConceptId  
}
CDASHVariable {
    string name  
    string questionText  
    string dataElementConceptId  
    string prompt  
    string subsetCodelist  
    stringList valueList  
    stringList valueDisplayList  
    string prepopulatedValue  
    CDASHVariableDataType dataType  
    integer length  
    integer significantDigits  
    CDASHIGCore cdashigCore  
}
SDTMTarget {
    string sdtmTargetVariable  
    string sdtmTargetMapping  
    string sdtmTargetGroup  
}
RelationShip {
    string subject  
    LinkingPhrase linkingPhrase  
    PredicateTerm predicateTerm  
    string object  
}
CodeList {
    string conceptId  
    uri href  
    string submissionValue  
}

CDASHGroup ||--}o CDASHVariable : "variables"
CDASHVariable ||--|o CodeList : "codelist"
CDASHVariable ||--|o RelationShip : "relationship"
CDASHVariable ||--|o SDTMTarget : "sdtmTarget"

```

