```mermaid
erDiagram
CRFGroup {
    date packageDate  
    PackageTypeEnum packageType  
    string crfSpecializationId  
    string shortName  
    string standard  
    string standardStartVersion  
    string standardEndVersion  
    ImplementationOptionEnum implementationOption  
    string scenario  
    stringList categories  
    string domain  
    string biomedicalConceptId  
    string sdtmDatasetSpecializationId  
}
CRFItem {
    string name  
    string variableName  
    string dataElementConceptId  
    string questionText  
    string prompt  
    string completionInstructions  
    integer orderNumber  
    boolean mandatoryVariable  
    CRFItemDataTypeEnum dataType  
    integer length  
    integer significantDigits  
    boolean displayHidden  
    boolean derivedVariable  
    string derivationDescription  
    SelectionTypeEnum selectionType  
}
ListValue {
    string displayValue  
    string value  
}
PrepopulatedValue {
    string value  
    string conceptId  
}
CodeList {
    string submissionValue  
    string conceptId  
    uri href  
}
SDTMTarget {
    string sdtmAnnotation  
    stringList sdtmVariables  
    string sdtmTargetMapping  
}

CRFGroup ||--}| CRFItem : "items"
CRFItem ||--|o CodeList : "codelist"
CRFItem ||--}o ListValue : "valueList"
CRFItem ||--|o PrepopulatedValue : "prepopulatedValue"
CRFItem ||--|o SDTMTarget : "sdtmTarget"

```

