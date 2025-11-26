
import logging
from dataclasses import dataclass
from linkml_dataops.query.queryengine import QueryEngine
from linkml_dataops.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_dataops.query.queryengine import MatchExpression

from .COSMoS-Biomedical-Concepts-CRF-Schema import *

@dataclass
class COSMoS-Biomedical-Concepts-CRF-SchemaAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # CRFItem methods
    # --
    def fetch_CRFItem(self, id_value: str) -> CRFItem:
        """
        Retrieves an instance of `CRFItem` via a primary key

        :param id_value:
        :return: CRFItem with matching ID
        """
        q = FetchById(id=id_value, target_class=CRFItem.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CRFItem(self,
             name: Union[str, MatchExpression] = None,
             variableName: Union[str, MatchExpression] = None,
             dataElementConceptId: Union[str, MatchExpression] = None,
             questionText: Union[str, MatchExpression] = None,
             prompt: Union[str, MatchExpression] = None,
             completionInstructions: Union[str, MatchExpression] = None,
             orderNumber: Union[str, MatchExpression] = None,
             mandatoryVariable: Union[str, MatchExpression] = None,
             dataType: Union[str, MatchExpression] = None,
             length: Union[str, MatchExpression] = None,
             significantDigits: Union[str, MatchExpression] = None,
             displayHidden: Union[str, MatchExpression] = None,
             derivedVariable: Union[str, MatchExpression] = None,
             derivationDescription: Union[str, MatchExpression] = None,
             codelist: Union[str, MatchExpression] = None,
             valueList: Union[str, MatchExpression] = None,
             selectionType: Union[str, MatchExpression] = None,
             prepopulatedValue: Union[str, MatchExpression] = None,
             sdtmTarget: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CRFItem]:
        """
        Queries for instances of `CRFItem`

        :param name: Item name as it appears on the CRF instrument
        :param variableName: Variable name of the CRF item for which data are being collected.
        :param dataElementConceptId: Biomedical Concept Data Element Concept identifier foreign key
        :param questionText: Item question text
        :param prompt: Item prompt
        :param completionInstructions: Item completion instructions
        :param orderNumber: Item order number
        :param mandatoryVariable: Indicator that the item must be present within the CRF group
        :param dataType: Item data type
        :param length: Item length
        :param significantDigits: Item significant_digits
        :param displayHidden: Indicator that the item is hidden from the user
        :param derivedVariable: Indicator that variable is derived
        :param derivationDescription: Description of the derivation. Required when derivedVariable is true.
        :param codelist: Codelist
        :param valueList: A set of values for a CRF item
        :param selectionType: Type of selection used for set-up of the CRF instrument
        :param prepopulatedValue: Pre-populated value for the CRF instrument
        :param sdtmTarget: SDTM target variables for CRF item variable
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CRFItem.class_name,
                                                 
                                                 name=name,
                                                 
                                                 variableName=variableName,
                                                 
                                                 dataElementConceptId=dataElementConceptId,
                                                 
                                                 questionText=questionText,
                                                 
                                                 prompt=prompt,
                                                 
                                                 completionInstructions=completionInstructions,
                                                 
                                                 orderNumber=orderNumber,
                                                 
                                                 mandatoryVariable=mandatoryVariable,
                                                 
                                                 dataType=dataType,
                                                 
                                                 length=length,
                                                 
                                                 significantDigits=significantDigits,
                                                 
                                                 displayHidden=displayHidden,
                                                 
                                                 derivedVariable=derivedVariable,
                                                 
                                                 derivationDescription=derivationDescription,
                                                 
                                                 codelist=codelist,
                                                 
                                                 valueList=valueList,
                                                 
                                                 selectionType=selectionType,
                                                 
                                                 prepopulatedValue=prepopulatedValue,
                                                 
                                                 sdtmTarget=sdtmTarget,
                                                 
                                                 _extra=_extra)
        return results
    

