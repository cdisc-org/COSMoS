
import logging
from dataclasses import dataclass
from linkml_dataops.query.queryengine import QueryEngine
from linkml_dataops.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_dataops.query.queryengine import MatchExpression

from .COSMoS-Biomedical-Concepts-Schema import *

@dataclass
class COSMoS-Biomedical-Concepts-SchemaAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # SDTMVariable methods
    # --
    def fetch_SDTMVariable(self, id_value: str) -> SDTMVariable:
        """
        Retrieves an instance of `SDTMVariable` via a primary key

        :param id_value:
        :return: SDTMVariable with matching ID
        """
        q = FetchById(id=id_value, target_class=SDTMVariable.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_SDTMVariable(self,
             name: Union[str, MatchExpression] = None,
             dataElementConceptId: Union[str, MatchExpression] = None,
             isNonStandard: Union[str, MatchExpression] = None,
             codelist: Union[str, MatchExpression] = None,
             subsetCodelist: Union[str, MatchExpression] = None,
             valueList: Union[str, MatchExpression] = None,
             assignedTerm: Union[str, MatchExpression] = None,
             role: Union[str, MatchExpression] = None,
             relationship: Union[str, MatchExpression] = None,
             dataType: Union[str, MatchExpression] = None,
             length: Union[str, MatchExpression] = None,
             format: Union[str, MatchExpression] = None,
             significantDigits: Union[str, MatchExpression] = None,
             mandatoryVariable: Union[str, MatchExpression] = None,
             mandatoryValue: Union[str, MatchExpression] = None,
             originType: Union[str, MatchExpression] = None,
             originSource: Union[str, MatchExpression] = None,
             comparator: Union[str, MatchExpression] = None,
             vlmTarget: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[SDTMVariable]:
        """
        Queries for instances of `SDTMVariable`

        :param name: Variable included in the SDTM dataset specialization
        :param dataElementConceptId: Biomedical Concept Data Element Concept identifier foreign key
        :param isNonStandard: Flag that indicates if the variable is a non-standard variable
        :param codelist: Codelist
        :param subsetCodelist: Subset codelist short name
        :param valueList: List of SDTM submission values used if subset codelist is not applicable
        :param assignedTerm: None
        :param role: SDTM variable role
        :param relationship: None
        :param dataType: Variable data type
        :param length: Variable length
        :param format: Variable display format
        :param significantDigits: Variable significant_digits
        :param mandatoryVariable: Indicator that variable must be present within the SDTM group
        :param mandatoryValue: Indicator that variable must be populated within the SDTM group
        :param originType: Variable origin type (define-XML v21)
        :param originSource: Variable origin source (define-XML v21)
        :param comparator: Comparison operator for SDTM group variables included in VLM
        :param vlmTarget: Target variable for VLM
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(SDTMVariable.class_name,
                                                 
                                                 name=name,
                                                 
                                                 dataElementConceptId=dataElementConceptId,
                                                 
                                                 isNonStandard=isNonStandard,
                                                 
                                                 codelist=codelist,
                                                 
                                                 subsetCodelist=subsetCodelist,
                                                 
                                                 valueList=valueList,
                                                 
                                                 assignedTerm=assignedTerm,
                                                 
                                                 role=role,
                                                 
                                                 relationship=relationship,
                                                 
                                                 dataType=dataType,
                                                 
                                                 length=length,
                                                 
                                                 format=format,
                                                 
                                                 significantDigits=significantDigits,
                                                 
                                                 mandatoryVariable=mandatoryVariable,
                                                 
                                                 mandatoryValue=mandatoryValue,
                                                 
                                                 originType=originType,
                                                 
                                                 originSource=originSource,
                                                 
                                                 comparator=comparator,
                                                 
                                                 vlmTarget=vlmTarget,
                                                 
                                                 _extra=_extra)
        return results
    

