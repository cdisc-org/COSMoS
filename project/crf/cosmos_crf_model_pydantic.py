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


linkml_meta = LinkMLMeta({'default_prefix': 'cosmos_crf',
     'default_range': 'string',
     'id': 'https://www.cdisc.org/cosmos/crf_v1.0',
     'imports': ['linkml:types'],
     'name': 'COSMoS-Biomedical-Concepts-CRF-Schema',
     'prefixes': {'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'cosmos_crf': {'prefix_prefix': 'cosmos_crf',
                                 'prefix_reference': 'https://www.cdisc.org/cosmos/crf_v1.0'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': '../model/cosmos_crf_model.yaml'} )

class PackageTypeEnum(str, Enum):
    crf = "crf"


class ImplementationOptionEnum(str, Enum):
    Normalized = "Normalized"
    Denormalized = "Denormalized"


class CRFItemDataTypeEnum(str, Enum):
    decimal = "decimal"
    float = "float"
    integer = "integer"
    text = "text"
    date = "date"
    time = "time"


class SelectionTypeEnum(str, Enum):
    Multiple = "Multiple"
    Single = "Single"



class CRFGroup(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/crf_v1.0', 'tree_root': True})

    packageDate: date = Field(default=..., description="""Biomedical Concept package release date indicating when the BC package was published to production""", json_schema_extra = { "linkml_meta": {'alias': 'packageDate', 'aliases': ['package_date'], 'domain_of': ['CRFGroup']} })
    packageType: PackageTypeEnum = Field(default=..., description="""Package type for CRF specializations (crf)""", json_schema_extra = { "linkml_meta": {'alias': 'packageType', 'aliases': ['package_type'], 'domain_of': ['CRFGroup']} })
    crfSpecializationId: str = Field(default=..., description="""Identifier for CRF specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'crfSpecializationId',
         'aliases': ['crf_group_id'],
         'domain_of': ['CRFGroup']} })
    shortName: str = Field(default=..., description="""Short name which provides a user friendly and intuitive name for the CRF group""", json_schema_extra = { "linkml_meta": {'alias': 'shortName', 'aliases': ['short_name'], 'domain_of': ['CRFGroup']} })
    standard: str = Field(default=..., description="""Standard for the CRF specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'standard', 'aliases': ['standard'], 'domain_of': ['CRFGroup']} })
    standardStartVersion: str = Field(default=..., description="""The earliest CRF IG version applicable to the CRF specialization""", json_schema_extra = { "linkml_meta": {'alias': 'standardStartVersion',
         'aliases': ['standard_start_version'],
         'domain_of': ['CRFGroup']} })
    standardEndVersion: Optional[str] = Field(default=None, description="""The last CRF IG version that is applicable to the CRF specialization""", json_schema_extra = { "linkml_meta": {'alias': 'standardEndVersion',
         'aliases': ['standard_end_version'],
         'domain_of': ['CRFGroup']} })
    implementationOption: Optional[ImplementationOptionEnum] = Field(default=None, description="""Implementation option for the CRF specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'implementationOption',
         'aliases': ['implementation_option'],
         'domain_of': ['CRFGroup']} })
    scenario: Optional[str] = Field(default=None, description="""Scenario for the CRF specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'scenario', 'aliases': ['scenario'], 'domain_of': ['CRFGroup']} })
    categories: Optional[list[str]] = Field(default=None, description="""CRF Dataset Specialization category for the faciliation of API search and extract""", json_schema_extra = { "linkml_meta": {'alias': 'categories', 'domain_of': ['CRFGroup']} })
    domain: Optional[str] = Field(default=None, description="""Domain for the CRF specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['CRFGroup']} })
    biomedicalConceptId: Optional[str] = Field(default=None, description="""Biomedical Concept identifier foreign key""", json_schema_extra = { "linkml_meta": {'alias': 'biomedicalConceptId',
         'aliases': ['bc_id'],
         'domain_of': ['CRFGroup'],
         'recommended': True} })
    sdtmDatasetSpecializationId: Optional[str] = Field(default=None, description="""Identifier for SDTM Dataset Specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmDatasetSpecializationId',
         'aliases': ['vlm_group_id'],
         'domain_of': ['CRFGroup']} })
    items: list[CRFItem] = Field(default=..., description="""Items included in the CRF specialization""", json_schema_extra = { "linkml_meta": {'alias': 'items', 'domain_of': ['CRFGroup']} })

    @field_validator('crfSpecializationId')
    def pattern_crfSpecializationId(cls, v):
        pattern=re.compile(r"^[A-Z][A-Z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid crfSpecializationId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid crfSpecializationId format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('biomedicalConceptId')
    def pattern_biomedicalConceptId(cls, v):
        pattern=re.compile(r"^(C[0-9]+|NEW_[A-Z]*[0-9]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid biomedicalConceptId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid biomedicalConceptId format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sdtmDatasetSpecializationId')
    def pattern_sdtmDatasetSpecializationId(cls, v):
        pattern=re.compile(r"^[A-Z][A-Z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sdtmDatasetSpecializationId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sdtmDatasetSpecializationId format: {v}"
            raise ValueError(err_msg)
        return v


class CRFItem(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/crf_v1.0'})

    name: str = Field(default=..., description="""Item name as it appears on the CRF instrument""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'aliases': ['crf_item'], 'domain_of': ['CRFItem']} })
    variableName: str = Field(default=..., description="""Variable name of the CRF item for which data are being collected.""", json_schema_extra = { "linkml_meta": {'alias': 'variableName',
         'aliases': ['variable_name'],
         'domain_of': ['CRFItem']} })
    dataElementConceptId: Optional[str] = Field(default=None, description="""Biomedical Concept Data Element Concept identifier foreign key""", json_schema_extra = { "linkml_meta": {'alias': 'dataElementConceptId',
         'aliases': ['dec_id'],
         'domain_of': ['CRFItem']} })
    questionText: Optional[str] = Field(default=None, description="""Item question text""", json_schema_extra = { "linkml_meta": {'alias': 'questionText',
         'aliases': ['question_text'],
         'domain_of': ['CRFItem']} })
    prompt: Optional[str] = Field(default=None, description="""Item prompt""", json_schema_extra = { "linkml_meta": {'alias': 'prompt', 'aliases': ['prompt'], 'domain_of': ['CRFItem']} })
    completionInstructions: Optional[str] = Field(default=None, description="""Item completion instructions""", json_schema_extra = { "linkml_meta": {'alias': 'completionInstructions',
         'aliases': ['completion_instructions'],
         'domain_of': ['CRFItem']} })
    orderNumber: int = Field(default=..., description="""Item order number""", json_schema_extra = { "linkml_meta": {'alias': 'orderNumber', 'aliases': ['order_number'], 'domain_of': ['CRFItem']} })
    mandatoryVariable: bool = Field(default=..., description="""Indicator that the item must be present within the CRF group""", json_schema_extra = { "linkml_meta": {'alias': 'mandatoryVariable',
         'aliases': ['mandatory_variable'],
         'domain_of': ['CRFItem']} })
    dataType: CRFItemDataTypeEnum = Field(default=..., description="""Item data type""", json_schema_extra = { "linkml_meta": {'alias': 'dataType', 'aliases': ['data_type'], 'domain_of': ['CRFItem']} })
    length: Optional[int] = Field(default=None, description="""Item length""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'length', 'aliases': ['length'], 'domain_of': ['CRFItem']} })
    significantDigits: Optional[int] = Field(default=None, description="""Item significant_digits""", json_schema_extra = { "linkml_meta": {'alias': 'significantDigits',
         'aliases': ['significant_digits'],
         'domain_of': ['CRFItem']} })
    displayHidden: Optional[bool] = Field(default=None, description="""Indicator that the item is hidden from the user""", json_schema_extra = { "linkml_meta": {'alias': 'displayHidden',
         'aliases': ['display_hidden'],
         'domain_of': ['CRFItem']} })
    derivedVariable: Optional[bool] = Field(default=None, description="""Indicator that variable is derived""", json_schema_extra = { "linkml_meta": {'alias': 'derivedVariable', 'domain_of': ['CRFItem']} })
    derivationDescription: Optional[str] = Field(default=None, description="""Description of the derivation. Required when derivedVariable is true.""", json_schema_extra = { "linkml_meta": {'alias': 'derivationDescription', 'domain_of': ['CRFItem']} })
    codelist: Optional[CodeList] = Field(default=None, description="""Codelist""", json_schema_extra = { "linkml_meta": {'alias': 'codelist', 'domain_of': ['CRFItem']} })
    valueList: Optional[list[ListValue]] = Field(default=None, description="""A set of values for a CRF item""", json_schema_extra = { "linkml_meta": {'alias': 'valueList', 'domain_of': ['CRFItem']} })
    selectionType: Optional[SelectionTypeEnum] = Field(default=None, description="""Type of selection used for set-up of the CRF instrument""", json_schema_extra = { "linkml_meta": {'alias': 'selectionType',
         'aliases': ['selection_type'],
         'domain_of': ['CRFItem']} })
    prepopulatedValue: Optional[PrepopulatedValue] = Field(default=None, description="""Pre-populated value for the CRF instrument""", json_schema_extra = { "linkml_meta": {'alias': 'prepopulatedValue', 'domain_of': ['CRFItem']} })
    sdtmTarget: Optional[SDTMTarget] = Field(default=None, description="""SDTM target variables for CRF item variable""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmTarget', 'domain_of': ['CRFItem']} })

    @field_validator('name')
    def pattern_name(cls, v):
        pattern=re.compile(r"^[A-Z][A-Z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('variableName')
    def pattern_variableName(cls, v):
        pattern=re.compile(r"^[A-Z][A-Z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid variableName format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid variableName format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('dataElementConceptId')
    def pattern_dataElementConceptId(cls, v):
        pattern=re.compile(r"^(C[0-9]+|NEW_[A-Z]*[0-9]*)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid dataElementConceptId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid dataElementConceptId format: {v}"
            raise ValueError(err_msg)
        return v


class ListValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/crf_v1.0',
         'slot_usage': {'displayValue': {'aliases': ['value_display_list'],
                                         'description': 'CDISC submission value for '
                                                        'the CRF item',
                                         'name': 'displayValue',
                                         'required': True},
                        'value': {'aliases': ['value_list'],
                                  'description': 'User-friendly display value for the '
                                                 'CRF item',
                                  'name': 'value',
                                  'required': False}}})

    displayValue: str = Field(default=..., description="""CDISC submission value for the CRF item""", json_schema_extra = { "linkml_meta": {'alias': 'displayValue',
         'aliases': ['value_display_list'],
         'domain_of': ['ListValue']} })
    value: Optional[str] = Field(default=None, description="""User-friendly display value for the CRF item""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'aliases': ['value_list'],
         'domain_of': ['ListValue', 'PrepopulatedValue']} })


class PrepopulatedValue(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/crf_v1.0',
         'slot_usage': {'conceptId': {'aliases': ['prepopulated_code'],
                                      'description': 'C-code for pre-populated term in '
                                                     'NCIt',
                                      'name': 'conceptId',
                                      'required': False},
                        'value': {'aliases': ['prepopulated_term'],
                                  'description': 'Submission value for pre-populated '
                                                 'term in NCIt',
                                  'name': 'value',
                                  'required': True}}})

    value: str = Field(default=..., description="""Submission value for pre-populated term in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'value',
         'aliases': ['prepopulated_term'],
         'domain_of': ['ListValue', 'PrepopulatedValue']} })
    conceptId: Optional[str] = Field(default=None, description="""C-code for pre-populated term in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'conceptId',
         'aliases': ['prepopulated_code'],
         'domain_of': ['PrepopulatedValue', 'CodeList']} })

    @field_validator('conceptId')
    def pattern_conceptId(cls, v):
        pattern=re.compile(r"^(C[0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid conceptId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid conceptId format: {v}"
            raise ValueError(err_msg)
        return v


class CodeList(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/crf_v1.0',
         'slot_usage': {'conceptId': {'aliases': ['codelist'],
                                      'description': 'C-code for codelist in NCIt',
                                      'name': 'conceptId'},
                        'href': {'aliases': ['codelist_uri'],
                                 'description': 'Link to NCIt for the codelist',
                                 'name': 'href'},
                        'submissionValue': {'aliases': ['codelist_submission_value'],
                                            'description': 'CDISC submission value for '
                                                           'the codelist',
                                            'name': 'submissionValue',
                                            'required': True}}})

    submissionValue: str = Field(default=..., description="""CDISC submission value for the codelist""", json_schema_extra = { "linkml_meta": {'alias': 'submissionValue',
         'aliases': ['codelist_submission_value'],
         'domain_of': ['CodeList']} })
    conceptId: Optional[str] = Field(default=None, description="""C-code for codelist in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'conceptId',
         'aliases': ['codelist'],
         'domain_of': ['PrepopulatedValue', 'CodeList']} })
    href: Optional[str] = Field(default=None, description="""Link to NCIt for the codelist""", json_schema_extra = { "linkml_meta": {'alias': 'href', 'aliases': ['codelist_uri'], 'domain_of': ['CodeList']} })

    @field_validator('submissionValue')
    def pattern_submissionValue(cls, v):
        pattern=re.compile(r"^[A-Z][A-Z0-9_]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid submissionValue format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid submissionValue format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('conceptId')
    def pattern_conceptId(cls, v):
        pattern=re.compile(r"^(C[0-9]+)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid conceptId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid conceptId format: {v}"
            raise ValueError(err_msg)
        return v


class SDTMTarget(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/crf_v1.0'})

    sdtmAnnotation: Optional[str] = Field(default=None, description="""Annotation of the SDTM target in the CRF instrument""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmAnnotation',
         'aliases': ['sdtm_annotation'],
         'domain_of': ['SDTMTarget'],
         'recommended': True} })
    sdtmVariables: Optional[list[str]] = Field(default=None, description="""SDTM target variable for CRF item variable""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmVariables',
         'aliases': ['sdtm_target_variable'],
         'domain_of': ['SDTMTarget']} })
    sdtmTargetMapping: Optional[str] = Field(default=None, description="""Rule for mapping from CRF item to SDTM target variable.""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmTargetMapping',
         'aliases': ['sdtm_mapping'],
         'domain_of': ['SDTMTarget']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CRFGroup.model_rebuild()
CRFItem.model_rebuild()
ListValue.model_rebuild()
PrepopulatedValue.model_rebuild()
CodeList.model_rebuild()
SDTMTarget.model_rebuild()

