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
    Dict,
    List,
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
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cosmos_sdtm',
     'default_range': 'string',
     'id': 'https://www.cdisc.org/cosmos/sdtm_v1.0',
     'imports': ['linkml:types'],
     'name': 'COSMoS-Biomedical-Concepts-SDTM-Schema',
     'prefixes': {'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'cosmos_sdtm': {'prefix_prefix': 'cosmos_sdtm',
                                  'prefix_reference': 'https://www.cdisc.org/cosmos/sdtm_v1.0/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'}},
     'source_file': '../model/cosmos_sdtm_bc_model.yaml'} )

class PackageTypeEnum(str, Enum):
    sdtm = "sdtm"


class SDTMVariableDataTypeEnum(str, Enum):
    datetime = "datetime"
    durationDatetime = "durationDatetime"
    float = "float"
    integer = "integer"
    text = "text"


class LinkingPhraseEnum(str, Enum):
    assesses_seriousness_of = "assesses seriousness of"
    assesses_the_severity_of = "assesses the severity of"
    associates_the_tumor_identified_in = "associates the tumor identified in"
    decodes_the_value_in = "decodes the value in"
    describes_actions_taken = "describes actions taken"
    describes_relationship_of = "describes relationship of"
    describes_the_outcome_of = "describes the outcome of"
    further_describes_the_test_in = "further describes the test in"
    further_specifies_the_anatomical_location_in = "further specifies the anatomical location in"
    groups_tumor_assessments_used_in_overall_response_identified_by = "groups tumor assessments used in overall response identified by"
    groups_values_in = "groups values in"
    groups_within_an_individual_subject_values_in = "groups, within an individual subject, values in"
    identifies_a_pattern_of = "identifies a pattern of"
    identifies_an_observation_described_by = "identifies an observation described by"
    identifies_overall_response_supported_by_tumor_assessments_identified_by = "identifies overall response supported by tumor assessments identified by"
    identifies_the_image_from_the_procedure_in = "identifies the image from the procedure in"
    identifies_the_tumor_found_by_the_test_in = "identifies the tumor found by the test in"
    indicates_occurrence_of_the_value_in = "indicates occurrence of the value in"
    indicates_pre_specification_of_the_value_in = "indicates pre-specification of the value in"
    indicates_severity_of = "indicates severity of"
    indicates_the_previous_irradiation_status_of_the_tumor_identified_by = "indicates the previous irradiation status of the tumor identified by"
    indicates_the_progression_status_of_the_previous_irradiated_tumor_identified_by = "indicates the progression status of the previous irradiated tumor identified by"
    is_a_dictionary_derived_term_for_the_value_in = "is a dictionary-derived term for the value in"
    is_a_dictionary_derived_class_code_for_the_value_in = "is a dictionary-derived class code for the value in"
    is_a_dictionary_derived_class_name_for_the_value_in = "is a dictionary-derived class name for the value in"
    is_decoded_by_the_value_in = "is decoded by the value in"
    is_original_text_for = "is original text for"
    is_the_administered_amount_of_the_treatment_in = "is the administered amount of the treatment in"
    is_the_administration_anatomical_location_for_the_treatment_in = "is the administration anatomical location for the treatment in"
    is_the_aspect_of_the_event_used_to_define_the_date_in = "is the aspect of the event used to define the date in"
    is_the_clinical_significance_interpretation_for = "is the clinical significance interpretation for"
    is_the_code_for_the_value_in = "is the code for the value in"
    is_the_dictionary_code_for_the_test_in = "is the dictionary code for the test in"
    is_the_dictionary_derived_term_for_the_value_in = "is the dictionary-derived term for the value in"
    is_the_dictionary_derived_class_code_for_the_value_in = "is the dictionary-derived class code for the value in"
    is_the_dictionary_derived_class_name_for_the_value_in = "is the dictionary-derived class name for the value in"
    is_the_duration_for = "is the duration for"
    is_the_end_date_for = "is the end date for"
    is_the_epoch_of_the_performance_of_the_test_in = "is the epoch of the performance of the test in"
    is_the_frequency_of_administration_of_the_amount_in = "is the frequency of administration of the amount in"
    is_the_identifier_for_the_source_data_used_in_the_performance_of_the_test_in = "is the identifier for the source data used in the performance of the test in"
    is_the_material_type_of_the_subject_of_the_activity_in = "is the material type of the subject of the activity in"
    is_the_medical_condition_that_is_the_reason_for_the_treatment_in = "is the medical condition that is the reason for the treatment in"
    is_the_method_for_the_test_in = "is the method for the test in"
    is_the_part_of_the_body_through_which_is_administered_the_treatment_in = "is the part of the body through which is administered the treatment in"
    is_the_physical_form_of_the_product_in = "is the physical form of the product in"
    is_the_result_of_the_test_in = "is the result of the test in"
    is_the_role_of_the_assessor_who_performed_the_test_in = "is the role of the assessor who performed the test in"
    is_the_specimen_tested_in = "is the specimen tested in"
    is_the_start_date_for = "is the start date for"
    is_the_subject_position_during_performance_of_the_test_in = "is the subject position during performance of the test in"
    is_the_subjectAPOSTROPHEs_fasting_status_during_the_performance_of_the_test_in = "is the subject's fasting status during the performance of the test in"
    is_the_unit_for_the_value_in = "is the unit for the value in"
    is_the_unit_for = "is the unit for"
    specifies_the_anatomical_location_in = "specifies the anatomical location in"
    specifies_the_anatomical_location_of = "specifies the anatomical location of"
    specifies_the_anatomical_location_of_the_performance_of_the_test_in = "specifies the anatomical location of the performance of the test in"
    specifies_the_severity_of = "specifies the severity of"
    values_are_grouped_by = "values are grouped by"
    was_the_subject_position_during_performance_of_the_test_in = "was the subject position during performance of the test in"
    identifies_the_reference_used_in_the_genomic_test_in = "identifies the reference used in the genomic test in"
    indicates_heritability_of_the_genetic_variant_in = "indicates heritability of the genetic variant in"
    is_an_identifier_for_a_published_reference_for_the_genetic_variant_in = "is an identifier for a published reference for the genetic variant in"
    is_an_identifier_for_the_copy_on_one_of_two_homologous_chromosones_of_the_genetic_variant_in = "is an identifier for the copy, on one of two homologous chromosones, of the genetic variant in"
    is_an_identifier_for_the_genetic_sequence_of_the_genetic_entity_represented_by = "is an identifier for the genetic sequence of the genetic entity represented by"
    is_the_chromosome_that_is_the_position_of_the_result_in = "is the chromosome that is the position of the result in"
    is_the_clinical_trial_or_treatment_setting_for = "is the clinical trial or treatment setting for"
    is_the_date_of_occurrence = "is the date of occurrence"
    is_the_date_of_occurrence_for = "is the date of occurrence for"
    is_the_intended_disease_outcome_for = "is the intended disease outcome for"
    is_the_method_of_secondary_analysis_of_results_in = "is the method of secondary analysis of results in"
    is_the_numeric_location_within_a_chromosone_genetic_entity_or_genetic_sub_region_of_the_result_in = "is the numeric location, within a chromosone, genetic entity, or genetic sub-region, of the result in"
    is_the_symbol_for_the_genomic_entity_that_is_the_position_of_the_result_in = "is the symbol for the genomic entity that is the position of the result in"
    is_the_type_of_genomic_entity_that_is_the_position_of_the_result_in = "is the type of genomic entity that is the position of the result in"
    is_the_genetic_sub_location_of_the_result_in = "is the genetic sub-location of the result in"
    is_the_object_of_the_observation_in = "is the object of the observation in"
    is_an_identifier_for_the_evaluator_with_the_role_in = "is an identifier for the evaluator with the role in"
    is_the_severity_of_the_toxicity_in = "is the severity of the toxicity in"
    is_a_grouping_of_values_in = "is a grouping of values in"
    is_the_textual_description_of_the_intended_dose_regimen_for = "is the textual description of the intended dose regimen for"
    is_the_reason_for_stopping_administration_of = "is the reason for stopping administration of"


class PredicateTermEnum(str, Enum):
    ASSESSES = "ASSESSES"
    CLASSIFIES = "CLASSIFIES"
    DECODES = "DECODES"
    DESCRIBES = "DESCRIBES"
    GROUPS = "GROUPS"
    GROUPS_BY = "GROUPS_BY"
    IDENTIFIES = "IDENTIFIES"
    IDENTIFIES_OBSERVATION = "IDENTIFIES_OBSERVATION"
    IDENTIFIES_PRODUCT_IN = "IDENTIFIES_PRODUCT_IN"
    IDENTIFIES_TUMOR_IN = "IDENTIFIES_TUMOR_IN"
    INDICATES = "INDICATES"
    IS_ATTRIBUTE_FOR = "IS_ATTRIBUTE_FOR"
    IS_DECODED_BY = "IS_DECODED_BY"
    IS_DERIVED_FROM = "IS_DERIVED_FROM"
    IS_EPOCH_OF = "IS_EPOCH_OF"
    IS_GROUPED_BY = "IS_GROUPED_BY"
    IS_INDICATOR_FOR = "IS_INDICATOR_FOR"
    IS_ORIGINAL_TEXT_FOR = "IS_ORIGINAL_TEXT_FOR"
    IS_POSITION_FOR = "IS_POSITION_FOR"
    IS_REASON_FOR = "IS_REASON_FOR"
    IS_RESULT_OF = "IS_RESULT_OF"
    IS_SPECIMEN_TESTED_IN = "IS_SPECIMEN_TESTED_IN"
    IS_SUBJECT_STATE_FOR = "IS_SUBJECT_STATE_FOR"
    IS_TIMING_FOR = "IS_TIMING_FOR"
    IS_UNIT_FOR = "IS_UNIT_FOR"
    PERFORMED = "PERFORMED"
    PERFORMS = "PERFORMS"
    QUALIFIES = "QUALIFIES"
    SPECIFIES = "SPECIFIES"


class OriginTypeEnum(str, Enum):
    """
    Terminology relevant to the origin type for datasets in the Define-XML document.
    """
    # A value that is derived through designation, such as values from a look up table or a label on a CRF.
    Assigned = "Assigned"
    # A value that is actually observed and recorded by a person or obtained by an instrument.
    Collected = "Collected"
    # A value that is calculated by an algorithm or reproducible rule, and which is dependent upon other data values.
    Derived = "Derived"
    # A value that is copied from a variable in another dataset.
    Predecessor = "Predecessor"
    # A value that is included as part of the study protocol.
    Protocol = "Protocol"


class OriginSourceEnum(str, Enum):
    """
    Terminology relevant to the origin source for datasets in the Define-XML document.
    """
    # A person responsible for the conduct of the clinical trial at a trial site. If a trial is conducted by a team of individuals at the trial site, the investigator is the responsible leader of the team and may be called the principal investigator.
    Investigator = "Investigator"
    # An individual, company, institution, or organization that takes responsibility for the initiation, management, and/or financing of a clinical study. [After ICH E6, WHO, 21 CFR 50.3 (e), and after IDMP]
    Sponsor = "Sponsor"
    # An individual who is observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study.
    Subject = "Subject"
    # A person or agency that promotes or exchanges goods or services for money. (NCI)
    Vendor = "Vendor"


class RoleEnum(str, Enum):
    Identifier = "Identifier"
    Qualifier = "Qualifier"
    Timing = "Timing"
    Topic = "Topic"


class ComparatorEnum(str, Enum):
    EQ = "EQ"
    IN = "IN"



class SDTMGroup(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0', 'tree_root': True})

    packageDate: date = Field(default=..., description="""Biomedical Concept package release date indicating when the BC package was published to production""", json_schema_extra = { "linkml_meta": {'alias': 'packageDate', 'domain_of': ['SDTMGroup']} })
    packageType: PackageTypeEnum = Field(default=..., description="""Package type (sdtm for SDTM Dataset Specializations)""", json_schema_extra = { "linkml_meta": {'alias': 'packageType', 'domain_of': ['SDTMGroup']} })
    datasetSpecializationId: str = Field(default=..., description="""Identifier for SDTM Value Level Metadata group""", json_schema_extra = { "linkml_meta": {'alias': 'datasetSpecializationId', 'domain_of': ['SDTMGroup']} })
    domain: str = Field(default=..., description="""Domain for the SDTM specialization group""", json_schema_extra = { "linkml_meta": {'alias': 'domain', 'domain_of': ['SDTMGroup']} })
    shortName: str = Field(default=..., description="""SDTM group short name which provides a user friendly and intuitive name for the vlm_group_id""", json_schema_extra = { "linkml_meta": {'alias': 'shortName', 'domain_of': ['SDTMGroup']} })
    source: str = Field(default=..., description="""SDTM VLM Source which categorizes VLM groups by topic variable""", json_schema_extra = { "linkml_meta": {'alias': 'source', 'domain_of': ['SDTMGroup']} })
    sdtmigStartVersion: str = Field(default=..., description="""The earliest SDTMIG version applicable to the BC dataset specialization""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmigStartVersion', 'domain_of': ['SDTMGroup']} })
    sdtmigEndVersion: Optional[str] = Field(default=None, description="""The last SDTMIG version that is applicable to the BC dataset specialization""", json_schema_extra = { "linkml_meta": {'alias': 'sdtmigEndVersion', 'domain_of': ['SDTMGroup']} })
    biomedicalConceptId: Optional[str] = Field(default=None, description="""Biomedical Concept identifier foreign key""", json_schema_extra = { "linkml_meta": {'alias': 'biomedicalConceptId',
         'domain_of': ['SDTMGroup'],
         'recommended': True} })
    variables: List[SDTMVariable] = Field(default=..., description="""Variable included in the SDTM dataset specialization""", json_schema_extra = { "linkml_meta": {'alias': 'variables', 'domain_of': ['SDTMGroup']} })

    @field_validator('biomedicalConceptId')
    def pattern_biomedicalConceptId(cls, v):
        pattern=re.compile(r"^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid biomedicalConceptId format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid biomedicalConceptId format: {v}")
        return v


class SDTMVariable(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0'})

    name: str = Field(default=..., description="""Variable included in the SDTM dataset specialization""", json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['SDTMVariable']} })
    dataElementConceptId: Optional[str] = Field(default=None, description="""Biomedical Concept Data Element Concept identifier foreign key""", json_schema_extra = { "linkml_meta": {'alias': 'dataElementConceptId', 'domain_of': ['SDTMVariable']} })
    isNonStandard: Optional[bool] = Field(default=None, description="""Flag that indicates if the variable is a non-standard variable""", json_schema_extra = { "linkml_meta": {'alias': 'isNonStandard', 'domain_of': ['SDTMVariable']} })
    codelist: Optional[CodeList] = Field(default=None, description="""Codelist""", json_schema_extra = { "linkml_meta": {'alias': 'codelist', 'domain_of': ['SDTMVariable']} })
    subsetCodelist: Optional[str] = Field(default=None, description="""Subset codelist short name""", json_schema_extra = { "linkml_meta": {'alias': 'subsetCodelist', 'domain_of': ['SDTMVariable']} })
    valueList: Optional[List[str]] = Field(default=None, description="""List of SDTM submission values used if subset codelist is not applicable""", json_schema_extra = { "linkml_meta": {'alias': 'valueList', 'domain_of': ['SDTMVariable']} })
    assignedTerm: Optional[AssignedTerm] = Field(default=None, description="""Assigned term""", json_schema_extra = { "linkml_meta": {'alias': 'assignedTerm', 'domain_of': ['SDTMVariable']} })
    role: Optional[RoleEnum] = Field(default=None, description="""SDTM variable role""", json_schema_extra = { "linkml_meta": {'alias': 'role', 'domain_of': ['SDTMVariable']} })
    relationship: Optional[RelationShip] = Field(default=None, description="""Relationship between variables""", json_schema_extra = { "linkml_meta": {'alias': 'relationship', 'domain_of': ['SDTMVariable']} })
    dataType: Optional[SDTMVariableDataTypeEnum] = Field(default=None, description="""Variable data type""", json_schema_extra = { "linkml_meta": {'alias': 'dataType', 'domain_of': ['SDTMVariable']} })
    length: Optional[int] = Field(default=None, description="""Variable length""", ge=1, json_schema_extra = { "linkml_meta": {'alias': 'length', 'domain_of': ['SDTMVariable']} })
    format: Optional[str] = Field(default=None, description="""Variable display format""", json_schema_extra = { "linkml_meta": {'alias': 'format', 'domain_of': ['SDTMVariable']} })
    significantDigits: Optional[int] = Field(default=None, description="""Variable significant_digits""", json_schema_extra = { "linkml_meta": {'alias': 'significantDigits', 'domain_of': ['SDTMVariable']} })
    mandatoryVariable: Optional[bool] = Field(default=None, description="""Indicator that variable must be present within the SDTM group""", json_schema_extra = { "linkml_meta": {'alias': 'mandatoryVariable', 'domain_of': ['SDTMVariable']} })
    mandatoryValue: Optional[bool] = Field(default=None, description="""Indicator that variable must be populated within the SDTM group""", json_schema_extra = { "linkml_meta": {'alias': 'mandatoryValue', 'domain_of': ['SDTMVariable']} })
    originType: Optional[OriginTypeEnum] = Field(default=None, description="""Variable origin type (define-XML v21)""", json_schema_extra = { "linkml_meta": {'alias': 'originType', 'domain_of': ['SDTMVariable']} })
    originSource: Optional[OriginSourceEnum] = Field(default=None, description="""Variable origin source (define-XML v21)""", json_schema_extra = { "linkml_meta": {'alias': 'originSource', 'domain_of': ['SDTMVariable']} })
    comparator: Optional[ComparatorEnum] = Field(default=None, description="""Comparison operator for SDTM group variables included in VLM""", json_schema_extra = { "linkml_meta": {'alias': 'comparator', 'domain_of': ['SDTMVariable']} })
    vlmTarget: Optional[bool] = Field(default=None, description="""Target variable for VLM""", json_schema_extra = { "linkml_meta": {'alias': 'vlmTarget', 'domain_of': ['SDTMVariable']} })

    @field_validator('dataElementConceptId')
    def pattern_dataElementConceptId(cls, v):
        pattern=re.compile(r"^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid dataElementConceptId format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid dataElementConceptId format: {v}")
        return v


class RelationShip(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0'})

    subject: str = Field(default=..., description="""Subject in a variable relationship""", json_schema_extra = { "linkml_meta": {'alias': 'subject', 'domain_of': ['RelationShip']} })
    linkingPhrase: LinkingPhraseEnum = Field(default=..., description="""Variable relationship descriptive linking phrase""", json_schema_extra = { "linkml_meta": {'alias': 'linkingPhrase', 'domain_of': ['RelationShip']} })
    predicateTerm: PredicateTermEnum = Field(default=..., description="""Short variable relationship linking phrase for programming purposes""", json_schema_extra = { "linkml_meta": {'alias': 'predicateTerm', 'domain_of': ['RelationShip']} })
    object: str = Field(default=..., description="""Object in a variable relationship""", json_schema_extra = { "linkml_meta": {'alias': 'object', 'domain_of': ['RelationShip']} })


class CodeList(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0'})

    conceptId: str = Field(default=..., description="""C-code for a codelist in NCIt""", json_schema_extra = { "linkml_meta": {'alias': 'conceptId', 'domain_of': ['CodeList', 'AssignedTerm']} })
    href: Optional[str] = Field(default=None, description="""Link to NCIt for the codelist""", json_schema_extra = { "linkml_meta": {'alias': 'href', 'domain_of': ['CodeList']} })
    submissionValue: str = Field(default=..., description="""CDISC submission value for the codelist""", json_schema_extra = { "linkml_meta": {'alias': 'submissionValue', 'domain_of': ['CodeList']} })

    @field_validator('conceptId')
    def pattern_conceptId(cls, v):
        pattern=re.compile(r"^(C[0123456789]+)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid conceptId format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid conceptId format: {v}")
        return v


class CodeListTerm(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0'})

    termId: str = Field(default=..., description="""C-code term in subset codelist""", json_schema_extra = { "linkml_meta": {'alias': 'termId', 'domain_of': ['CodeListTerm']} })
    termValue: str = Field(default=..., description="""Submision value of term in subset codelist""", json_schema_extra = { "linkml_meta": {'alias': 'termValue', 'domain_of': ['CodeListTerm']} })

    @field_validator('termId')
    def pattern_termId(cls, v):
        pattern=re.compile(r"^(C[0123456789]+)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid termId format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid termId format: {v}")
        return v


class SubsetCodeList(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0'})

    parentCodelist: str = Field(default=..., description="""Subset codelist parent codelist""", json_schema_extra = { "linkml_meta": {'alias': 'parentCodelist', 'domain_of': ['SubsetCodeList']} })
    subsetShortName: str = Field(default=..., description="""Subset codelist short name""", json_schema_extra = { "linkml_meta": {'alias': 'subsetShortName', 'domain_of': ['SubsetCodeList']} })
    subsetLabel: str = Field(default=..., description="""Subset codelist label""", json_schema_extra = { "linkml_meta": {'alias': 'subsetLabel', 'domain_of': ['SubsetCodeList']} })
    codelistTerm: List[CodeListTerm] = Field(default=..., description="""Term in subset codelist""", json_schema_extra = { "linkml_meta": {'alias': 'codelistTerm', 'domain_of': ['SubsetCodeList']} })


class AssignedTerm(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://www.cdisc.org/cosmos/sdtm_v1.0'})

    conceptId: Optional[str] = Field(default=None, description="""C-code for assigned term in NCIt or left blank when CDISC terminology does not apply""", json_schema_extra = { "linkml_meta": {'alias': 'conceptId', 'domain_of': ['CodeList', 'AssignedTerm']} })
    value: str = Field(default=..., description="""Submission value for assigned term in NCIt if it exists, or an assigned value which will be the default value""", json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['AssignedTerm']} })

    @field_validator('conceptId')
    def pattern_conceptId(cls, v):
        pattern=re.compile(r"^(C[0123456789]+)$")
        if isinstance(v,list):
            for element in v:
                if isinstance(v, str) and not pattern.match(element):
                    raise ValueError(f"Invalid conceptId format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid conceptId format: {v}")
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SDTMGroup.model_rebuild()
SDTMVariable.model_rebuild()
RelationShip.model_rebuild()
CodeList.model_rebuild()
CodeListTerm.model_rebuild()
SubsetCodeList.model_rebuild()
AssignedTerm.model_rebuild()

