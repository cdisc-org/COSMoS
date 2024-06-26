
import logging
from dataclasses import dataclass
from linkml_runtime_api.query.queryengine import QueryEngine
from linkml_runtime_api.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_runtime_api.query.queryengine import MatchExpression

from .COSMoS-Biomedical-Concepts-Schema import *

@dataclass
class COSMoS-Biomedical-Concepts-SchemaAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # CDASHVariable methods
    # --
    def fetch_CDASHVariable(self, id_value: str) -> CDASHVariable:
        """
        Retrieves an instance of `CDASHVariable` via a primary key

        :param id_value:
        :return: CDASHVariable with matching ID
        """
        q = FetchById(id=id_value, target_class=CDASHVariable.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CDASHVariable(self,
             name: Union[str, MatchExpression] = None,
             questionText: Union[str, MatchExpression] = None,
             dataElementConceptId: Union[str, MatchExpression] = None,
             prompt: Union[str, MatchExpression] = None,
             codelist: Union[str, MatchExpression] = None,
             subsetCodelist: Union[str, MatchExpression] = None,
             valueList: Union[str, MatchExpression] = None,
             valueDisplayList: Union[str, MatchExpression] = None,
             prepopulatedValue: Union[str, MatchExpression] = None,
             relationship: Union[str, MatchExpression] = None,
             dataType: Union[str, MatchExpression] = None,
             length: Union[str, MatchExpression] = None,
             significantDigits: Union[str, MatchExpression] = None,
             cdashigCore: Union[str, MatchExpression] = None,
             sdtmTarget: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CDASHVariable]:
        """
        Queries for instances of `CDASHVariable`

        :param name: Variable included in the CDASH dataset specialization
        :param questionText: CDASH variable question text
        :param dataElementConceptId: Biomedical Concept Data Element Concept idenfifier foreign key
        :param prompt: CDASH variable prompt
        :param codelist: Codelist
        :param subsetCodelist: Subset codelist short name
        :param valueList: A set of valid CDISC submission values for a CDASH variable
        :param valueDisplayList: A set of valid user-friendly CDISC submission values for a CDASH variable
        :param prepopulatedValue: Pre-populated value on a CRF
        :param relationship: None
        :param dataType: Variable data type
        :param length: Variable length
        :param significantDigits: Variable significant_digits
        :param cdashigCore: Rule for inclusion of a variable within a dataset including 'Hightly Recommended', 'Required/Conditional', and 'Optional'
        :param sdtmTarget: None
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CDASHVariable.class_name,
                                                 
                                                 name=name,
                                                 
                                                 questionText=questionText,
                                                 
                                                 dataElementConceptId=dataElementConceptId,
                                                 
                                                 prompt=prompt,
                                                 
                                                 codelist=codelist,
                                                 
                                                 subsetCodelist=subsetCodelist,
                                                 
                                                 valueList=valueList,
                                                 
                                                 valueDisplayList=valueDisplayList,
                                                 
                                                 prepopulatedValue=prepopulatedValue,
                                                 
                                                 relationship=relationship,
                                                 
                                                 dataType=dataType,
                                                 
                                                 length=length,
                                                 
                                                 significantDigits=significantDigits,
                                                 
                                                 cdashigCore=cdashigCore,
                                                 
                                                 sdtmTarget=sdtmTarget,
                                                 
                                                 _extra=_extra)
        return results
    

