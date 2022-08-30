# Auto generated from cosmos_sdtm_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-30T12:01:55
# Schema: COSMoS-Biomedical-Concepts-Schema
#
# id: https://www.cdisc.org/cosmos/1-0
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://www.cdisc.org/cosmos/1-0/')


# Types

# Class references
class SDTMGroupVlmGroupId(extended_str):
    pass


class SDTMVariableName(extended_str):
    pass


class CodeListConceptId(extended_str):
    pass


@dataclass
class SDTMGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SDTMGroup"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMGroup")

    vlm_group_id: Union[str, SDTMGroupVlmGroupId] = None
    package_date: Union[str, XSDDate] = None
    domain: str = None
    group_short_name: str = None
    vlm_source: str = None
    sdtmig_start_version: str = None
    sdtmig_end_version: Optional[str] = None
    biomedical_concept_id: Optional[str] = None
    sdtm_variables: Optional[Union[Dict[Union[str, SDTMVariableName], Union[dict, "SDTMVariable"]], List[Union[dict, "SDTMVariable"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.vlm_group_id):
            self.MissingRequiredField("vlm_group_id")
        if not isinstance(self.vlm_group_id, SDTMGroupVlmGroupId):
            self.vlm_group_id = SDTMGroupVlmGroupId(self.vlm_group_id)

        if self._is_empty(self.package_date):
            self.MissingRequiredField("package_date")
        if not isinstance(self.package_date, XSDDate):
            self.package_date = XSDDate(self.package_date)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self._is_empty(self.group_short_name):
            self.MissingRequiredField("group_short_name")
        if not isinstance(self.group_short_name, str):
            self.group_short_name = str(self.group_short_name)

        if self._is_empty(self.vlm_source):
            self.MissingRequiredField("vlm_source")
        if not isinstance(self.vlm_source, str):
            self.vlm_source = str(self.vlm_source)

        if self._is_empty(self.sdtmig_start_version):
            self.MissingRequiredField("sdtmig_start_version")
        if not isinstance(self.sdtmig_start_version, str):
            self.sdtmig_start_version = str(self.sdtmig_start_version)

        if self.sdtmig_end_version is not None and not isinstance(self.sdtmig_end_version, str):
            self.sdtmig_end_version = str(self.sdtmig_end_version)

        if self.biomedical_concept_id is not None and not isinstance(self.biomedical_concept_id, str):
            self.biomedical_concept_id = str(self.biomedical_concept_id)

        self._normalize_inlined_as_list(slot_name="sdtm_variables", slot_type=SDTMVariable, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class SDTMVariable(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMVariable")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SDTMVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMVariable")

    name: Union[str, SDTMVariableName] = None
    biomedical_concept_dec_id: Optional[str] = None
    nsv_flag: Optional[Union[bool, Bool]] = None
    codelist: Optional[Union[str, CodeListConceptId]] = None
    subset_codelist: Optional[str] = None
    value_list: Optional[Union[str, List[str]]] = empty_list()
    assigned_term: Optional[Union[dict, "AssignedTerm"]] = None
    role: Optional[str] = None
    relationship: Optional[Union[dict, "RelationShip"]] = None
    data_type: Optional[Union[str, "SDTMVariableDataType"]] = None
    length: Optional[int] = None
    format: Optional[str] = None
    significant_digits: Optional[int] = None
    mandatory_variable: Optional[Union[bool, Bool]] = None
    mandatory_value: Optional[Union[bool, Bool]] = None
    origin_type: Optional[Union[str, "OriginType"]] = None
    origin_source: Optional[Union[str, "OriginSource"]] = None
    comparator: Optional[Union[str, "Comparator"]] = None
    vlm_target: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SDTMVariableName):
            self.name = SDTMVariableName(self.name)

        if self.biomedical_concept_dec_id is not None and not isinstance(self.biomedical_concept_dec_id, str):
            self.biomedical_concept_dec_id = str(self.biomedical_concept_dec_id)

        if self.nsv_flag is not None and not isinstance(self.nsv_flag, Bool):
            self.nsv_flag = Bool(self.nsv_flag)

        if self.codelist is not None and not isinstance(self.codelist, CodeListConceptId):
            self.codelist = CodeListConceptId(self.codelist)

        if self.subset_codelist is not None and not isinstance(self.subset_codelist, str):
            self.subset_codelist = str(self.subset_codelist)

        if not isinstance(self.value_list, list):
            self.value_list = [self.value_list] if self.value_list is not None else []
        self.value_list = [v if isinstance(v, str) else str(v) for v in self.value_list]

        if self.assigned_term is not None and not isinstance(self.assigned_term, AssignedTerm):
            self.assigned_term = AssignedTerm(**as_dict(self.assigned_term))

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.relationship is not None and not isinstance(self.relationship, RelationShip):
            self.relationship = RelationShip(**as_dict(self.relationship))

        if self.data_type is not None and not isinstance(self.data_type, SDTMVariableDataType):
            self.data_type = SDTMVariableDataType(self.data_type)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.significant_digits is not None and not isinstance(self.significant_digits, int):
            self.significant_digits = int(self.significant_digits)

        if self.mandatory_variable is not None and not isinstance(self.mandatory_variable, Bool):
            self.mandatory_variable = Bool(self.mandatory_variable)

        if self.mandatory_value is not None and not isinstance(self.mandatory_value, Bool):
            self.mandatory_value = Bool(self.mandatory_value)

        if self.origin_type is not None and not isinstance(self.origin_type, OriginType):
            self.origin_type = OriginType(self.origin_type)

        if self.origin_source is not None and not isinstance(self.origin_source, OriginSource):
            self.origin_source = OriginSource(self.origin_source)

        if self.comparator is not None and not isinstance(self.comparator, Comparator):
            self.comparator = Comparator(self.comparator)

        if self.vlm_target is not None and not isinstance(self.vlm_target, Bool):
            self.vlm_target = Bool(self.vlm_target)

        super().__post_init__(**kwargs)


@dataclass
class RelationShip(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/RelationShip")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RelationShip"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/RelationShip")

    subject: str = None
    linking_phrase: Union[str, "LinkingPhrase"] = None
    predicate_term: Union[str, "PredicateTerm"] = None
    object: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.linking_phrase):
            self.MissingRequiredField("linking_phrase")
        if not isinstance(self.linking_phrase, LinkingPhrase):
            self.linking_phrase = LinkingPhrase(self.linking_phrase)

        if self._is_empty(self.predicate_term):
            self.MissingRequiredField("predicate_term")
        if not isinstance(self.predicate_term, PredicateTerm):
            self.predicate_term = PredicateTerm(self.predicate_term)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CodeList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CodeList")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CodeList"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CodeList")

    concept_id: Union[str, CodeListConceptId] = None
    submission_value: str = None
    concept_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, CodeListConceptId):
            self.concept_id = CodeListConceptId(self.concept_id)

        if self._is_empty(self.submission_value):
            self.MissingRequiredField("submission_value")
        if not isinstance(self.submission_value, str):
            self.submission_value = str(self.submission_value)

        if self.concept_uri is not None and not isinstance(self.concept_uri, URI):
            self.concept_uri = URI(self.concept_uri)

        super().__post_init__(**kwargs)


@dataclass
class CodeListTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CodeListTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CodeListTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CodeListTerm")

    term_id: str = None
    term_value: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.term_id):
            self.MissingRequiredField("term_id")
        if not isinstance(self.term_id, str):
            self.term_id = str(self.term_id)

        if self._is_empty(self.term_value):
            self.MissingRequiredField("term_value")
        if not isinstance(self.term_value, str):
            self.term_value = str(self.term_value)

        super().__post_init__(**kwargs)


@dataclass
class SubsetCodeList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SubsetCodeList")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SubsetCodeList"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SubsetCodeList")

    parent_codelist: str = None
    subset_short_name: str = None
    subset_label: str = None
    codelist_term: Union[Union[dict, CodeListTerm], List[Union[dict, CodeListTerm]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.parent_codelist):
            self.MissingRequiredField("parent_codelist")
        if not isinstance(self.parent_codelist, str):
            self.parent_codelist = str(self.parent_codelist)

        if self._is_empty(self.subset_short_name):
            self.MissingRequiredField("subset_short_name")
        if not isinstance(self.subset_short_name, str):
            self.subset_short_name = str(self.subset_short_name)

        if self._is_empty(self.subset_label):
            self.MissingRequiredField("subset_label")
        if not isinstance(self.subset_label, str):
            self.subset_label = str(self.subset_label)

        if self._is_empty(self.codelist_term):
            self.MissingRequiredField("codelist_term")
        if not isinstance(self.codelist_term, list):
            self.codelist_term = [self.codelist_term] if self.codelist_term is not None else []
        self.codelist_term = [v if isinstance(v, CodeListTerm) else CodeListTerm(**as_dict(v)) for v in self.codelist_term]

        super().__post_init__(**kwargs)


@dataclass
class AssignedTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/AssignedTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AssignedTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/AssignedTerm")

    value: str = None
    code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.code is not None and not isinstance(self.code, str):
            self.code = str(self.code)

        super().__post_init__(**kwargs)


# Enumerations
class SDTMVariableDataType(EnumDefinitionImpl):

    float = PermissibleValue(text="float")
    integer = PermissibleValue(text="integer")
    text = PermissibleValue(text="text")

    _defn = EnumDefinition(
        name="SDTMVariableDataType",
    )

class LinkingPhrase(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LinkingPhrase",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "decodes the value in",
                PermissibleValue(text="decodes the value in") )
        setattr(cls, "is decoded by the value in",
                PermissibleValue(text="is decoded by the value in") )
        setattr(cls, "groups values in",
                PermissibleValue(text="groups values in") )
        setattr(cls, "is the subject position during performance of the test in",
                PermissibleValue(text="is the subject position during performance of the test in") )
        setattr(cls, "is the result of the test in",
                PermissibleValue(text="is the result of the test in") )
        setattr(cls, "is the unit for the value in",
                PermissibleValue(text="is the unit for the value in") )
        setattr(cls, "is the specimen tested in",
                PermissibleValue(text="is the specimen tested in") )
        setattr(cls, "specifies the anatomical location of the performance of the test in",
                PermissibleValue(text="specifies the anatomical location of the performance of the test in") )
        setattr(cls, "further specifies the anatomical location in",
                PermissibleValue(text="further specifies the anatomical location in") )
        setattr(cls, "is the method for the test in",
                PermissibleValue(text="is the method for the test in") )
        setattr(cls, "is the subject's fasting status during the performance of the test in",
                PermissibleValue(text="is the subject's fasting status during the performance of the test in") )
        setattr(cls, "identifies an observation described by",
                PermissibleValue(text="identifies an observation described by") )
        setattr(cls, "is the dictionary code for the test in",
                PermissibleValue(text="is the dictionary code for the test in") )

class PredicateTerm(EnumDefinitionImpl):

    DECODES = PermissibleValue(text="DECODES")
    IS_DECODED_BY = PermissibleValue(text="IS_DECODED_BY")
    GROUPS = PermissibleValue(text="GROUPS")
    IS_SUBJECT_STATE_FOR = PermissibleValue(text="IS_SUBJECT_STATE_FOR")
    IS_RESULT_OF = PermissibleValue(text="IS_RESULT_OF")
    IS_UNIT_FOR = PermissibleValue(text="IS_UNIT_FOR")
    IDENTIFIES_OBSERVATION = PermissibleValue(text="IDENTIFIES_OBSERVATION")
    IS_SPECIMEN_TESTED_IN = PermissibleValue(text="IS_SPECIMEN_TESTED_IN")
    SPECIFIES = PermissibleValue(text="SPECIFIES")
    CODES = PermissibleValue(text="CODES")

    _defn = EnumDefinition(
        name="PredicateTerm",
    )

class OriginType(EnumDefinitionImpl):

    Assigned = PermissibleValue(text="Assigned")
    Collected = PermissibleValue(text="Collected")
    Derived = PermissibleValue(text="Derived")
    Predecessor = PermissibleValue(text="Predecessor")
    Protocol = PermissibleValue(text="Protocol")

    _defn = EnumDefinition(
        name="OriginType",
    )

class OriginSource(EnumDefinitionImpl):

    Investigator = PermissibleValue(text="Investigator")
    Sponsor = PermissibleValue(text="Sponsor")
    Subject = PermissibleValue(text="Subject")
    Vendor = PermissibleValue(text="Vendor")

    _defn = EnumDefinition(
        name="OriginSource",
    )

class Role(EnumDefinitionImpl):

    Topic = PermissibleValue(text="Topic")
    Qualifier = PermissibleValue(text="Qualifier")

    _defn = EnumDefinition(
        name="Role",
    )

class Comparator(EnumDefinitionImpl):

    EQ = PermissibleValue(text="EQ")
    IN = PermissibleValue(text="IN")

    _defn = EnumDefinition(
        name="Comparator",
    )

# Slots
class slots:
    pass

slots.package_date = Slot(uri=DEFAULT_.package_date, name="package_date", curie=DEFAULT_.curie('package_date'),
                   model_uri=DEFAULT_.package_date, domain=None, range=Union[str, XSDDate])

slots.domain = Slot(uri=DEFAULT_.domain, name="domain", curie=DEFAULT_.curie('domain'),
                   model_uri=DEFAULT_.domain, domain=None, range=str)

slots.vlm_group_id = Slot(uri=DEFAULT_.vlm_group_id, name="vlm_group_id", curie=DEFAULT_.curie('vlm_group_id'),
                   model_uri=DEFAULT_.vlm_group_id, domain=None, range=URIRef)

slots.vlm_source = Slot(uri=DEFAULT_.vlm_source, name="vlm_source", curie=DEFAULT_.curie('vlm_source'),
                   model_uri=DEFAULT_.vlm_source, domain=None, range=str)

slots.group_short_name = Slot(uri=DEFAULT_.group_short_name, name="group_short_name", curie=DEFAULT_.curie('group_short_name'),
                   model_uri=DEFAULT_.group_short_name, domain=None, range=str)

slots.sdtmig_start_version = Slot(uri=DEFAULT_.sdtmig_start_version, name="sdtmig_start_version", curie=DEFAULT_.curie('sdtmig_start_version'),
                   model_uri=DEFAULT_.sdtmig_start_version, domain=None, range=str)

slots.sdtmig_end_version = Slot(uri=DEFAULT_.sdtmig_end_version, name="sdtmig_end_version", curie=DEFAULT_.curie('sdtmig_end_version'),
                   model_uri=DEFAULT_.sdtmig_end_version, domain=None, range=Optional[str])

slots.biomedical_concept_id = Slot(uri=DEFAULT_.biomedical_concept_id, name="biomedical_concept_id", curie=DEFAULT_.curie('biomedical_concept_id'),
                   model_uri=DEFAULT_.biomedical_concept_id, domain=None, range=Optional[str])

slots.sdtm_variables = Slot(uri=DEFAULT_.sdtm_variables, name="sdtm_variables", curie=DEFAULT_.curie('sdtm_variables'),
                   model_uri=DEFAULT_.sdtm_variables, domain=None, range=Optional[Union[Dict[Union[str, SDTMVariableName], Union[dict, SDTMVariable]], List[Union[dict, SDTMVariable]]]])

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=URIRef)

slots.biomedical_concept_dec_id = Slot(uri=DEFAULT_.biomedical_concept_dec_id, name="biomedical_concept_dec_id", curie=DEFAULT_.curie('biomedical_concept_dec_id'),
                   model_uri=DEFAULT_.biomedical_concept_dec_id, domain=None, range=Optional[str])

slots.nsv_flag = Slot(uri=DEFAULT_.nsv_flag, name="nsv_flag", curie=DEFAULT_.curie('nsv_flag'),
                   model_uri=DEFAULT_.nsv_flag, domain=None, range=Optional[Union[bool, Bool]])

slots.codelist = Slot(uri=DEFAULT_.codelist, name="codelist", curie=DEFAULT_.curie('codelist'),
                   model_uri=DEFAULT_.codelist, domain=None, range=Optional[Union[str, CodeListConceptId]])

slots.subset_codelist = Slot(uri=DEFAULT_.subset_codelist, name="subset_codelist", curie=DEFAULT_.curie('subset_codelist'),
                   model_uri=DEFAULT_.subset_codelist, domain=None, range=Optional[str])

slots.concept_id = Slot(uri=DEFAULT_.concept_id, name="concept_id", curie=DEFAULT_.curie('concept_id'),
                   model_uri=DEFAULT_.concept_id, domain=None, range=URIRef)

slots.concept_uri = Slot(uri=DEFAULT_.concept_uri, name="concept_uri", curie=DEFAULT_.curie('concept_uri'),
                   model_uri=DEFAULT_.concept_uri, domain=None, range=Optional[Union[str, URI]])

slots.submission_value = Slot(uri=DEFAULT_.submission_value, name="submission_value", curie=DEFAULT_.curie('submission_value'),
                   model_uri=DEFAULT_.submission_value, domain=None, range=str)

slots.parent_codelist = Slot(uri=DEFAULT_.parent_codelist, name="parent_codelist", curie=DEFAULT_.curie('parent_codelist'),
                   model_uri=DEFAULT_.parent_codelist, domain=None, range=str)

slots.subset_short_name = Slot(uri=DEFAULT_.subset_short_name, name="subset_short_name", curie=DEFAULT_.curie('subset_short_name'),
                   model_uri=DEFAULT_.subset_short_name, domain=None, range=str)

slots.subset_label = Slot(uri=DEFAULT_.subset_label, name="subset_label", curie=DEFAULT_.curie('subset_label'),
                   model_uri=DEFAULT_.subset_label, domain=None, range=str)

slots.codelist_term = Slot(uri=DEFAULT_.codelist_term, name="codelist_term", curie=DEFAULT_.curie('codelist_term'),
                   model_uri=DEFAULT_.codelist_term, domain=None, range=Union[Union[dict, CodeListTerm], List[Union[dict, CodeListTerm]]])

slots.term_id = Slot(uri=DEFAULT_.term_id, name="term_id", curie=DEFAULT_.curie('term_id'),
                   model_uri=DEFAULT_.term_id, domain=None, range=str)

slots.term_value = Slot(uri=DEFAULT_.term_value, name="term_value", curie=DEFAULT_.curie('term_value'),
                   model_uri=DEFAULT_.term_value, domain=None, range=str)

slots.value_list = Slot(uri=DEFAULT_.value_list, name="value_list", curie=DEFAULT_.curie('value_list'),
                   model_uri=DEFAULT_.value_list, domain=None, range=Optional[Union[str, List[str]]])

slots.assigned_term = Slot(uri=DEFAULT_.assigned_term, name="assigned_term", curie=DEFAULT_.curie('assigned_term'),
                   model_uri=DEFAULT_.assigned_term, domain=None, range=Optional[Union[dict, AssignedTerm]])

slots.code = Slot(uri=DEFAULT_.code, name="code", curie=DEFAULT_.curie('code'),
                   model_uri=DEFAULT_.code, domain=None, range=Optional[str])

slots.value = Slot(uri=DEFAULT_.value, name="value", curie=DEFAULT_.curie('value'),
                   model_uri=DEFAULT_.value, domain=None, range=str)

slots.role = Slot(uri=DEFAULT_.role, name="role", curie=DEFAULT_.curie('role'),
                   model_uri=DEFAULT_.role, domain=None, range=Optional[str])

slots.relationship = Slot(uri=DEFAULT_.relationship, name="relationship", curie=DEFAULT_.curie('relationship'),
                   model_uri=DEFAULT_.relationship, domain=None, range=Optional[Union[dict, RelationShip]])

slots.subject = Slot(uri=DEFAULT_.subject, name="subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.subject, domain=None, range=str)

slots.linking_phrase = Slot(uri=DEFAULT_.linking_phrase, name="linking_phrase", curie=DEFAULT_.curie('linking_phrase'),
                   model_uri=DEFAULT_.linking_phrase, domain=None, range=Union[str, "LinkingPhrase"])

slots.predicate_term = Slot(uri=DEFAULT_.predicate_term, name="predicate_term", curie=DEFAULT_.curie('predicate_term'),
                   model_uri=DEFAULT_.predicate_term, domain=None, range=Union[str, "PredicateTerm"])

slots.object = Slot(uri=DEFAULT_.object, name="object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.object, domain=None, range=str)

slots.data_type = Slot(uri=DEFAULT_.data_type, name="data_type", curie=DEFAULT_.curie('data_type'),
                   model_uri=DEFAULT_.data_type, domain=None, range=Optional[Union[str, "SDTMVariableDataType"]])

slots.length = Slot(uri=DEFAULT_.length, name="length", curie=DEFAULT_.curie('length'),
                   model_uri=DEFAULT_.length, domain=None, range=Optional[int])

slots.format = Slot(uri=DEFAULT_.format, name="format", curie=DEFAULT_.curie('format'),
                   model_uri=DEFAULT_.format, domain=None, range=Optional[str])

slots.significant_digits = Slot(uri=DEFAULT_.significant_digits, name="significant_digits", curie=DEFAULT_.curie('significant_digits'),
                   model_uri=DEFAULT_.significant_digits, domain=None, range=Optional[int])

slots.mandatory_variable = Slot(uri=DEFAULT_.mandatory_variable, name="mandatory_variable", curie=DEFAULT_.curie('mandatory_variable'),
                   model_uri=DEFAULT_.mandatory_variable, domain=None, range=Optional[Union[bool, Bool]])

slots.mandatory_value = Slot(uri=DEFAULT_.mandatory_value, name="mandatory_value", curie=DEFAULT_.curie('mandatory_value'),
                   model_uri=DEFAULT_.mandatory_value, domain=None, range=Optional[Union[bool, Bool]])

slots.origin_type = Slot(uri=DEFAULT_.origin_type, name="origin_type", curie=DEFAULT_.curie('origin_type'),
                   model_uri=DEFAULT_.origin_type, domain=None, range=Optional[Union[str, "OriginType"]])

slots.origin_source = Slot(uri=DEFAULT_.origin_source, name="origin_source", curie=DEFAULT_.curie('origin_source'),
                   model_uri=DEFAULT_.origin_source, domain=None, range=Optional[Union[str, "OriginSource"]])

slots.comparator = Slot(uri=DEFAULT_.comparator, name="comparator", curie=DEFAULT_.curie('comparator'),
                   model_uri=DEFAULT_.comparator, domain=None, range=Optional[Union[str, "Comparator"]])

slots.vlm_target = Slot(uri=DEFAULT_.vlm_target, name="vlm_target", curie=DEFAULT_.curie('vlm_target'),
                   model_uri=DEFAULT_.vlm_target, domain=None, range=Optional[Union[bool, Bool]])
