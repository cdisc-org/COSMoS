
import logging
from dataclasses import dataclass
from linkml_dataops.query.queryengine import QueryEngine
from linkml_dataops.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_dataops.query.queryengine import MatchExpression

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
             dataElementConceptId: Union[str, MatchExpression] = None,
             isNonStandard: Union[str, MatchExpression] = None,
             eCRFItem: Union[str, MatchExpression] = None,
             questionText: Union[str, MatchExpression] = None,
             prompt: Union[str, MatchExpression] = None,
             orderNumber: Union[str, MatchExpression] = None,
             codelist: Union[str, MatchExpression] = None,
             valueList: Union[str, MatchExpression] = None,
             listStyle: Union[str, MatchExpression] = None,
             prepopulatedValue: Union[str, MatchExpression] = None,
             displayHidden: Union[str, MatchExpression] = None,
             dataType: Union[str, MatchExpression] = None,
             length: Union[str, MatchExpression] = None,
             significantDigits: Union[str, MatchExpression] = None,
             mandatoryVariable: Union[str, MatchExpression] = None,
             sdtmTarget: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DataCollectionItem]:
        """
        Queries for instances of `DataCollectionItem`

        :param name: Item included in the data collection dataset specialization
        :param dataElementConceptId: Biomedical Concept Data Element Concept identifier foreign key
        :param isNonStandard: Flag that indicates if the variable is a non-standard variable
        :param eCRFItem: Variable included in the data collection dataset specialization used for eCSR set-up
        :param questionText: Data collection item question text
        :param prompt: Data collection item prompt
        :param orderNumber: Data collection item order number
        :param codelist: Codelist
        :param valueList: A set of valid CDISC submission values for a data collection item
        :param listStyle: Type of list used for eCRF set-up
        :param prepopulatedValue: Pre-populated value on a CRF
        :param displayHidden: Indicator that the item is hidden from the user
        :param dataType: Item data type
        :param length: Variable length
        :param significantDigits: Variable significant_digits
        :param mandatoryVariable: Indicator that the item must be present within the data collection group
        :param sdtmTarget: SDTM target variables for data collection item variable
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DataCollectionItem.class_name,
                                                 
                                                 name=name,
                                                 
                                                 dataElementConceptId=dataElementConceptId,
                                                 
                                                 isNonStandard=isNonStandard,
                                                 
                                                 eCRFItem=eCRFItem,
                                                 
                                                 questionText=questionText,
                                                 
                                                 prompt=prompt,
                                                 
                                                 orderNumber=orderNumber,
                                                 
                                                 codelist=codelist,
                                                 
                                                 valueList=valueList,
                                                 
                                                 listStyle=listStyle,
                                                 
                                                 prepopulatedValue=prepopulatedValue,
                                                 
                                                 displayHidden=displayHidden,
                                                 
                                                 dataType=dataType,
                                                 
                                                 length=length,
                                                 
                                                 significantDigits=significantDigits,
                                                 
                                                 mandatoryVariable=mandatoryVariable,
                                                 
                                                 sdtmTarget=sdtmTarget,
                                                 
                                                 _extra=_extra)
        return results
    

