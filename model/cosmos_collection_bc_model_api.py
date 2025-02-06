
import logging
from dataclasses import dataclass
from linkml_runtime_api.query.queryengine import QueryEngine
from linkml_runtime_api.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_runtime_api.query.queryengine import MatchExpression

from .COSMoS-Biomedical-Concepts-Collection-Schema import *

@dataclass
class COSMoS-Biomedical-Concepts-Collection-SchemaAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # DataCollectionItem methods
    # --
    def fetch_DataCollectionItem(self, id_value: str) -> DataCollectionItem:
        """
        Retrieves an instance of `DataCollectionItem` via a primary key

        :param id_value:
        :return: DataCollectionItem with matching ID
        """
        q = FetchById(id=id_value, target_class=DataCollectionItem.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DataCollectionItem(self,
             name: Union[str, MatchExpression] = None,
             variableName: Union[str, MatchExpression] = None,
             dataElementConceptId: Union[str, MatchExpression] = None,
             questionText: Union[str, MatchExpression] = None,
             prompt: Union[str, MatchExpression] = None,
             orderNumber: Union[str, MatchExpression] = None,
             mandatoryVariable: Union[str, MatchExpression] = None,
             dataType: Union[str, MatchExpression] = None,
             length: Union[str, MatchExpression] = None,
             significantDigits: Union[str, MatchExpression] = None,
             displayHidden: Union[str, MatchExpression] = None,
             codelist: Union[str, MatchExpression] = None,
             valueList: Union[str, MatchExpression] = None,
             listType: Union[str, MatchExpression] = None,
             prepopulatedValue: Union[str, MatchExpression] = None,
             sdtmTarget: Union[str, MatchExpression] = None,
             sdtmAnnotation: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DataCollectionItem]:
        """
        Queries for instances of `DataCollectionItem`

        :param name: Item name as it appears on the collection instrument
        :param variableName: Variable name of the collection item for which data are being collected.
        :param dataElementConceptId: Biomedical Concept Data Element Concept identifier foreign key
        :param questionText: Item question text
        :param prompt: Item prompt
        :param orderNumber: Item order number
        :param mandatoryVariable: Indicator that the item must be present within the data collection group
        :param dataType: Item data type
        :param length: Item length
        :param significantDigits: Item significant_digits
        :param displayHidden: Indicator that the item is hidden from the user
        :param codelist: Codelist
        :param valueList: A set of values for a data collection item
        :param listType: Type of list used for set-up of the data collection instrument
        :param prepopulatedValue: Pre-populated value for the data collection instrument
        :param sdtmTarget: SDTM target variables for data collection item variable
        :param sdtmAnnotation: Annotation of the SDTM target in the data collection instrument
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DataCollectionItem.class_name,
                                                 
                                                 name=name,
                                                 
                                                 variableName=variableName,
                                                 
                                                 dataElementConceptId=dataElementConceptId,
                                                 
                                                 questionText=questionText,
                                                 
                                                 prompt=prompt,
                                                 
                                                 orderNumber=orderNumber,
                                                 
                                                 mandatoryVariable=mandatoryVariable,
                                                 
                                                 dataType=dataType,
                                                 
                                                 length=length,
                                                 
                                                 significantDigits=significantDigits,
                                                 
                                                 displayHidden=displayHidden,
                                                 
                                                 codelist=codelist,
                                                 
                                                 valueList=valueList,
                                                 
                                                 listType=listType,
                                                 
                                                 prepopulatedValue=prepopulatedValue,
                                                 
                                                 sdtmTarget=sdtmTarget,
                                                 
                                                 sdtmAnnotation=sdtmAnnotation,
                                                 
                                                 _extra=_extra)
        return results
    

