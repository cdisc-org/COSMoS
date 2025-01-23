```mermaid
erDiagram
DataCollectionGroup {
    date packageDate  
    PackageTypeEnum packageType  
    string datasetSpecializationId  
    string standard  
    string domain  
    string shortName  
    string collectionigStartVersion  
    string collectionigEndVersion  
    string biomedicalConceptId  
    string sdtmDatasetSpecializationId  
}
DataCollectionItem {
    string name  
    string dataElementConceptId  
    boolean isNonStandard  
    string eCRFItem  
    string questionText  
    string prompt  
    integer orderNumber  
    ListTypeEnum listStyle  
    boolean displayHidden  
    CollectionItemDataTypeEnum dataType  
    integer length  
    integer significantDigits  
    boolean mandatoryVariable  
    CDASHIGCore cdashigCore  
}
CodeList {
    string conceptId  
    uri href  
    string submissionValue  
}
ListValue {
    string value  
    string displayValue  
}
PrepopulatedValue {
    string conceptId  
    string value  
}
SDTMTarget {
    string sdtmVariable  
    string sdtmAnnotation  
    string sdtmTargetMapping  
}

DataCollectionGroup ||--}| DataCollectionItem : "items"
DataCollectionItem ||--|o CodeList : "codelist"
DataCollectionItem ||--}o ListValue : "valueList"
DataCollectionItem ||--|o PrepopulatedValue : "prepopulatedValue"
DataCollectionItem ||--}o SDTMTarget : "sdtmTarget"

```

