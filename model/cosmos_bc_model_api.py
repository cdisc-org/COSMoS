
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
    # Coding methods
    # --
    def fetch_Coding(self, id_value: str) -> Coding:
        """
        Retrieves an instance of `Coding` via a primary key

        :param id_value:
        :return: Coding with matching ID
        """
        q = FetchById(id=id_value, target_class=Coding.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Coding(self,
             code: Union[str, MatchExpression] = None,
             system: Union[str, MatchExpression] = None,
             systemName: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Coding]:
        """
        Queries for instances of `Coding`

        :param code: Synonym concept for the Biomedical Concept as defined in a code system
        :param system: Identifies the code system for the synonym concept. The URL of the code system should be used if it exists
        :param systemName: Human-readable name for the code system
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Coding.class_name,
                                                 
                                                 code=code,
                                                 
                                                 system=system,
                                                 
                                                 systemName=systemName,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DataElementConcept methods
    # --
    def fetch_DataElementConcept(self, id_value: str) -> DataElementConcept:
        """
        Retrieves an instance of `DataElementConcept` via a primary key

        :param id_value:
        :return: DataElementConcept with matching ID
        """
        q = FetchById(id=id_value, target_class=DataElementConcept.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DataElementConcept(self,
             conceptId: Union[str, MatchExpression] = None,
             ncitCode: Union[str, MatchExpression] = None,
             href: Union[str, MatchExpression] = None,
             shortName: Union[str, MatchExpression] = None,
             dataType: Union[str, MatchExpression] = None,
             exampleSet: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DataElementConcept]:
        """
        Queries for instances of `DataElementConcept`

        :param conceptId: An identifier for a Data Element Concept (DEC) which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt
        :param ncitCode: NCI C-code for the BC Data Element Concept
        :param href: Link to NCIt for the Data Element Concept
        :param shortName: NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt
        :param dataType: Data Type for the Data Element Concept
        :param exampleSet: Example values for the Data Element Concept
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DataElementConcept.class_name,
                                                 
                                                 conceptId=conceptId,
                                                 
                                                 ncitCode=ncitCode,
                                                 
                                                 href=href,
                                                 
                                                 shortName=shortName,
                                                 
                                                 dataType=dataType,
                                                 
                                                 exampleSet=exampleSet,
                                                 
                                                 _extra=_extra)
        return results
    

