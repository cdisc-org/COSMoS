from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cosmos_bc',
     'default_range': 'string',
     'id': 'https://www.cdisc.org/cosmos/biomedical_concept_v1.0',
     'imports': ['linkml:types'],
     'name': 'COSMoS-Biomedical-Concepts-Schema',
     'prefixes': {'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'cosmos_bc': {'prefix_prefix': 'cosmos_bc',
                                'prefix_reference': 'https://www.cdisc.org/cosmos/biomedical_concept_v1.0'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': '../model/cosmos_bc_model.yaml'} )

class PackageTypeEnum(str, Enum):
    bc = "bc"


class BiomedicalConceptResultScaleEnum(str, Enum):
    Ordinal = "Ordinal"
    Narrative = "Narrative"
    Nominal = "Nominal"
    Quantitative = "Quantitative"
    Temporal = "Temporal"


class DataElementConceptDataTypeEnum(str, Enum):
    boolean = "boolean"
    date = "date"
    datetime = "datetime"
    decimal = "decimal"
    duration = "duration"
    integer = "integer"
    string = "string"
    uri = "uri"



class BiomedicalConcept(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/biomedical_concept_v1.0',
         'slot_usage': {'conceptId': {'description': 'A unique identifier for a '
                                                     'Biomedical Concept which will be '
                                                     'assigned as the NCIt code if it '
                                                     'exists or a placeholder '
                                                     'identifier if the concept is not '
                                                     'yet available in NCIt',
                                      'name': 'conceptId'},
                        'href': {'description': 'URI link to NCIt for the Biomedical '
                                                'Concept; blank if  concept is not '
                                                'available in NCIt',
                                 'name': 'href'},
                        'ncitCode': {'description': 'NCIt C-code for the Biomedical '
                                                    'Concept',
                                     'name': 'ncitCode'}},
         'tree_root': True})

    packageDate: date = Field(default=..., description="""Biomedical Concept package release date indicating when the BC package was published to production""", json_schema_extra = { "linkml_meta": {'alias': 'packageDate', 'domain_of': ['BiomedicalConcept']} })
    packageType: PackageTypeEnum = Field(default=..., description="""Package type (bc for Biomedical Concepts)""", json_schema_extra = { "linkml_meta": {'alias': 'packageType', 'domain_of': ['BiomedicalConcept']} })
    conceptId: str = Field(default=..., description="""A unique identifier for a Biomedical Concept which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'conceptId', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    ncitCode: Optional[str] = Field(default=None, description="""NCIt C-code for the Biomedical Concept""", json_schema_extra = { "linkml_meta": {'alias': 'ncitCode', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    href: Optional[str] = Field(default=None, description="""URI link to NCIt for the Biomedical Concept; blank if  concept is not available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'href', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    parentConceptId: Optional[str] = Field(default=None, description="""C-code for the parent concept in the NCIt hiearchy; blank if concept is not available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'parentConceptId', 'domain_of': ['BiomedicalConcept']} })
    categories: list[str] = Field(default=..., description="""Biomedical Concept category for the faciliation of API search and extract""", json_schema_extra = { "linkml_meta": {'alias': 'categories', 'domain_of': ['BiomedicalConcept']} })
    shortName: str = Field(default=..., description="""NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'shortName', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    synonyms: Optional[list[str]] = Field(default=None, description="""Biomedical Concept synonym equivalent to BC short name for the facilitation of API search and extraction""", json_schema_extra = { "linkml_meta": {'alias': 'synonyms', 'domain_of': ['BiomedicalConcept']} })
    resultScales: Optional[list[BiomedicalConceptResultScaleEnum]] = Field(default=None, description="""Scale of measurement for the Biomedical Concept result""", json_schema_extra = { "linkml_meta": {'alias': 'resultScales', 'domain_of': ['BiomedicalConcept']} })
    definition: str = Field(default=..., description="""NCIt definition for the Biomedical Concept; provisional defintion if concept is not available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'definition', 'domain_of': ['BiomedicalConcept']} })
    coding: Optional[list[Coding]] = Field(default=None, description="""Coding for the Biomedical Concept""", json_schema_extra = { "linkml_meta": {'alias': 'coding', 'domain_of': ['BiomedicalConcept']} })
    dataElementConcepts: Optional[list[DataElementConcept]] = Field(default=None, description="""Data Element Concept""", json_schema_extra = { "linkml_meta": {'alias': 'dataElementConcepts', 'domain_of': ['BiomedicalConcept']} })

    @field_validator('conceptId')
    def pattern_conceptId(cls, v):
        pattern=re.compile(r"^(C[0-9]+|NEW_[A-Z]*[0-9]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid conceptId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid conceptId format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ncitCode')
    def pattern_ncitCode(cls, v):
        pattern=re.compile(r"^(C[0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ncitCode format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ncitCode format: {v}"
            raise ValueError(err_msg)
        return v


class Coding(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/biomedical_concept_v1.0'})

    code: str = Field(default=..., description="""Synonym concept for the Biomedical Concept as defined in a code system""", json_schema_extra = { "linkml_meta": {'alias': 'code', 'domain_of': ['Coding']} })
    system: str = Field(default=..., description="""Identifies the code system for the synonym concept. The URL of the code system should be used if it exists""", json_schema_extra = { "linkml_meta": {'alias': 'system', 'domain_of': ['Coding']} })
    systemName: Optional[str] = Field(default=None, description="""Human-readable name for the code system""", json_schema_extra = { "linkml_meta": {'alias': 'systemName', 'domain_of': ['Coding']} })


class DataElementConcept(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/biomedical_concept_v1.0',
         'slot_usage': {'conceptId': {'description': 'An identifier for a Data Element '
                                                     'Concept (DEC) which will be '
                                                     'assigned as the NCIt code if it '
                                                     'exists or a placeholder '
                                                     'identifier if the concept is not '
                                                     'yet available in NCIt',
                                      'name': 'conceptId'},
                        'href': {'description': 'Link to NCIt for the Data Element '
                                                'Concept',
                                 'name': 'href'},
                        'ncitCode': {'description': 'NCI C-code for the BC Data '
                                                    'Element Concept',
                                     'name': 'ncitCode'}}})

    conceptId: str = Field(default=..., description="""An identifier for a Data Element Concept (DEC) which will be assigned as the NCIt code if it exists or a placeholder identifier if the concept is not yet available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'conceptId', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    ncitCode: Optional[str] = Field(default=None, description="""NCI C-code for the BC Data Element Concept""", json_schema_extra = { "linkml_meta": {'alias': 'ncitCode', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    href: Optional[str] = Field(default=None, description="""Link to NCIt for the Data Element Concept""", json_schema_extra = { "linkml_meta": {'alias': 'href', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    shortName: str = Field(default=..., description="""NCI Preferred Name for the concept; provisional name will be used if concept is not available in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'shortName', 'domain_of': ['BiomedicalConcept', 'DataElementConcept']} })
    dataType: DataElementConceptDataTypeEnum = Field(default=..., description="""Data Type for the Data Element Concept""", json_schema_extra = { "linkml_meta": {'alias': 'dataType', 'domain_of': ['DataElementConcept']} })
    exampleSet: Optional[list[str]] = Field(default=None, description="""Example values for the Data Element Concept""", json_schema_extra = { "linkml_meta": {'alias': 'exampleSet', 'domain_of': ['DataElementConcept']} })

    @field_validator('conceptId')
    def pattern_conceptId(cls, v):
        pattern=re.compile(r"^(C[0-9]+|NEW_[A-Z]*[0-9]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid conceptId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid conceptId format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('ncitCode')
    def pattern_ncitCode(cls, v):
        pattern=re.compile(r"^(C[0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid ncitCode format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid ncitCode format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
BiomedicalConcept.model_rebuild()
Coding.model_rebuild()
DataElementConcept.model_rebuild()

