# Auto generated from cosmos_sdtm_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2024-06-10T11:02:35
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
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
COSMOS = CurieNamespace('cosmos', 'https://www.cdisc.org/cosmos/1-0')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = COSMOS


# Types

# Class references
class SDTMGroupDatasetSpecializationId(extended_str):
    pass


class SDTMVariableName(extended_str):
    pass


class CodeListConceptId(extended_str):
    pass


@dataclass
class SDTMGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.SDTMGroup
    class_class_curie: ClassVar[str] = "cosmos:SDTMGroup"
    class_name: ClassVar[str] = "SDTMGroup"
    class_model_uri: ClassVar[URIRef] = COSMOS.SDTMGroup

    datasetSpecializationId: Union[str, SDTMGroupDatasetSpecializationId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "SDTMDatasetSpecializationPackageTypeEnum"] = None
    domain: str = None
    shortName: str = None
    source: str = None
    sdtmigStartVersion: str = None
    sdtmigEndVersion: Optional[str] = None
    biomedicalConceptId: Optional[str] = None
    variables: Optional[Union[Dict[Union[str, SDTMVariableName], Union[dict, "SDTMVariable"]], List[Union[dict, "SDTMVariable"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.datasetSpecializationId):
            self.MissingRequiredField("datasetSpecializationId")
        if not isinstance(self.datasetSpecializationId, SDTMGroupDatasetSpecializationId):
            self.datasetSpecializationId = SDTMGroupDatasetSpecializationId(self.datasetSpecializationId)

        if self._is_empty(self.packageDate):
            self.MissingRequiredField("packageDate")
        if not isinstance(self.packageDate, XSDDate):
            self.packageDate = XSDDate(self.packageDate)

        if self._is_empty(self.packageType):
            self.MissingRequiredField("packageType")
        if not isinstance(self.packageType, SDTMDatasetSpecializationPackageTypeEnum):
            self.packageType = SDTMDatasetSpecializationPackageTypeEnum(self.packageType)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.sdtmigStartVersion):
            self.MissingRequiredField("sdtmigStartVersion")
        if not isinstance(self.sdtmigStartVersion, str):
            self.sdtmigStartVersion = str(self.sdtmigStartVersion)

        if self.sdtmigEndVersion is not None and not isinstance(self.sdtmigEndVersion, str):
            self.sdtmigEndVersion = str(self.sdtmigEndVersion)

        if self.biomedicalConceptId is not None and not isinstance(self.biomedicalConceptId, str):
            self.biomedicalConceptId = str(self.biomedicalConceptId)

        self._normalize_inlined_as_list(slot_name="variables", slot_type=SDTMVariable, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class SDTMVariable(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.SDTMVariable
    class_class_curie: ClassVar[str] = "cosmos:SDTMVariable"
    class_name: ClassVar[str] = "SDTMVariable"
    class_model_uri: ClassVar[URIRef] = COSMOS.SDTMVariable

    name: Union[str, SDTMVariableName] = None
    dataElementConceptId: Optional[str] = None
    isNonStandard: Optional[Union[bool, Bool]] = None
    codelist: Optional[Union[dict, "CodeList"]] = None
    subsetCodelist: Optional[str] = None
    valueList: Optional[Union[str, List[str]]] = empty_list()
    assignedTerm: Optional[Union[dict, "AssignedTerm"]] = None
    role: Optional[Union[str, "RoleEnum"]] = None
    relationship: Optional[Union[dict, "RelationShip"]] = None
    dataType: Optional[Union[str, "SDTMVariableDataTypeEnum"]] = None
    length: Optional[int] = None
    format: Optional[str] = None
    significantDigits: Optional[int] = None
    mandatoryVariable: Optional[Union[bool, Bool]] = None
    mandatoryValue: Optional[Union[bool, Bool]] = None
    originType: Optional[Union[str, "OriginTypeEnum"]] = None
    originSource: Optional[Union[str, "OriginSourceEnum"]] = None
    comparator: Optional[Union[str, "ComparatorEnum"]] = None
    vlmTarget: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, SDTMVariableName):
            self.name = SDTMVariableName(self.name)

        if self.dataElementConceptId is not None and not isinstance(self.dataElementConceptId, str):
            self.dataElementConceptId = str(self.dataElementConceptId)

        if self.isNonStandard is not None and not isinstance(self.isNonStandard, Bool):
            self.isNonStandard = Bool(self.isNonStandard)

        if self.codelist is not None and not isinstance(self.codelist, CodeList):
            self.codelist = CodeList(**as_dict(self.codelist))

        if self.subsetCodelist is not None and not isinstance(self.subsetCodelist, str):
            self.subsetCodelist = str(self.subsetCodelist)

        if not isinstance(self.valueList, list):
            self.valueList = [self.valueList] if self.valueList is not None else []
        self.valueList = [v if isinstance(v, str) else str(v) for v in self.valueList]

        if self.assignedTerm is not None and not isinstance(self.assignedTerm, AssignedTerm):
            self.assignedTerm = AssignedTerm(**as_dict(self.assignedTerm))

        if self.role is not None and not isinstance(self.role, RoleEnum):
            self.role = RoleEnum(self.role)

        if self.relationship is not None and not isinstance(self.relationship, RelationShip):
            self.relationship = RelationShip(**as_dict(self.relationship))

        if self.dataType is not None and not isinstance(self.dataType, SDTMVariableDataTypeEnum):
            self.dataType = SDTMVariableDataTypeEnum(self.dataType)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.significantDigits is not None and not isinstance(self.significantDigits, int):
            self.significantDigits = int(self.significantDigits)

        if self.mandatoryVariable is not None and not isinstance(self.mandatoryVariable, Bool):
            self.mandatoryVariable = Bool(self.mandatoryVariable)

        if self.mandatoryValue is not None and not isinstance(self.mandatoryValue, Bool):
            self.mandatoryValue = Bool(self.mandatoryValue)

        if self.originType is not None and not isinstance(self.originType, OriginTypeEnum):
            self.originType = OriginTypeEnum(self.originType)

        if self.originSource is not None and not isinstance(self.originSource, OriginSourceEnum):
            self.originSource = OriginSourceEnum(self.originSource)

        if self.comparator is not None and not isinstance(self.comparator, ComparatorEnum):
            self.comparator = ComparatorEnum(self.comparator)

        if self.vlmTarget is not None and not isinstance(self.vlmTarget, Bool):
            self.vlmTarget = Bool(self.vlmTarget)

        super().__post_init__(**kwargs)


@dataclass
class RelationShip(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.RelationShip
    class_class_curie: ClassVar[str] = "cosmos:RelationShip"
    class_name: ClassVar[str] = "RelationShip"
    class_model_uri: ClassVar[URIRef] = COSMOS.RelationShip

    subject: str = None
    linkingPhrase: Union[str, "LinkingPhraseEnum"] = None
    predicateTerm: Union[str, "PredicateTermEnum"] = None
    object: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.linkingPhrase):
            self.MissingRequiredField("linkingPhrase")
        if not isinstance(self.linkingPhrase, LinkingPhraseEnum):
            self.linkingPhrase = LinkingPhraseEnum(self.linkingPhrase)

        if self._is_empty(self.predicateTerm):
            self.MissingRequiredField("predicateTerm")
        if not isinstance(self.predicateTerm, PredicateTermEnum):
            self.predicateTerm = PredicateTermEnum(self.predicateTerm)

        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, str):
            self.object = str(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CodeList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.CodeList
    class_class_curie: ClassVar[str] = "cosmos:CodeList"
    class_name: ClassVar[str] = "CodeList"
    class_model_uri: ClassVar[URIRef] = COSMOS.CodeList

    conceptId: Union[str, CodeListConceptId] = None
    submissionValue: str = None
    href: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.conceptId):
            self.MissingRequiredField("conceptId")
        if not isinstance(self.conceptId, CodeListConceptId):
            self.conceptId = CodeListConceptId(self.conceptId)

        if self._is_empty(self.submissionValue):
            self.MissingRequiredField("submissionValue")
        if not isinstance(self.submissionValue, str):
            self.submissionValue = str(self.submissionValue)

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        super().__post_init__(**kwargs)


@dataclass
class CodeListTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.CodeListTerm
    class_class_curie: ClassVar[str] = "cosmos:CodeListTerm"
    class_name: ClassVar[str] = "CodeListTerm"
    class_model_uri: ClassVar[URIRef] = COSMOS.CodeListTerm

    termId: str = None
    termValue: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.termId):
            self.MissingRequiredField("termId")
        if not isinstance(self.termId, str):
            self.termId = str(self.termId)

        if self._is_empty(self.termValue):
            self.MissingRequiredField("termValue")
        if not isinstance(self.termValue, str):
            self.termValue = str(self.termValue)

        super().__post_init__(**kwargs)


@dataclass
class SubsetCodeList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.SubsetCodeList
    class_class_curie: ClassVar[str] = "cosmos:SubsetCodeList"
    class_name: ClassVar[str] = "SubsetCodeList"
    class_model_uri: ClassVar[URIRef] = COSMOS.SubsetCodeList

    parentCodelist: str = None
    subsetShortName: str = None
    subsetLabel: str = None
    codelistTerm: Union[Union[dict, CodeListTerm], List[Union[dict, CodeListTerm]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.parentCodelist):
            self.MissingRequiredField("parentCodelist")
        if not isinstance(self.parentCodelist, str):
            self.parentCodelist = str(self.parentCodelist)

        if self._is_empty(self.subsetShortName):
            self.MissingRequiredField("subsetShortName")
        if not isinstance(self.subsetShortName, str):
            self.subsetShortName = str(self.subsetShortName)

        if self._is_empty(self.subsetLabel):
            self.MissingRequiredField("subsetLabel")
        if not isinstance(self.subsetLabel, str):
            self.subsetLabel = str(self.subsetLabel)

        if self._is_empty(self.codelistTerm):
            self.MissingRequiredField("codelistTerm")
        if not isinstance(self.codelistTerm, list):
            self.codelistTerm = [self.codelistTerm] if self.codelistTerm is not None else []
        self.codelistTerm = [v if isinstance(v, CodeListTerm) else CodeListTerm(**as_dict(v)) for v in self.codelistTerm]

        super().__post_init__(**kwargs)


@dataclass
class AssignedTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.AssignedTerm
    class_class_curie: ClassVar[str] = "cosmos:AssignedTerm"
    class_name: ClassVar[str] = "AssignedTerm"
    class_model_uri: ClassVar[URIRef] = COSMOS.AssignedTerm

    value: str = None
    conceptId: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.conceptId is not None and not isinstance(self.conceptId, str):
            self.conceptId = str(self.conceptId)

        super().__post_init__(**kwargs)


# Enumerations
class SDTMDatasetSpecializationPackageTypeEnum(EnumDefinitionImpl):

    sdtm = PermissibleValue(text="sdtm")

    _defn = EnumDefinition(
        name="SDTMDatasetSpecializationPackageTypeEnum",
    )

class SDTMVariableDataTypeEnum(EnumDefinitionImpl):

    datetime = PermissibleValue(text="datetime")
    durationDatetime = PermissibleValue(text="durationDatetime")
    float = PermissibleValue(text="float")
    integer = PermissibleValue(text="integer")
    text = PermissibleValue(text="text")

    _defn = EnumDefinition(
        name="SDTMVariableDataTypeEnum",
    )

class LinkingPhraseEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LinkingPhraseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "associates the tumor identified in",
                PermissibleValue(text="associates the tumor identified in") )
        setattr(cls, "decodes the value in",
                PermissibleValue(text="decodes the value in") )
        setattr(cls, "describes actions taken",
                PermissibleValue(text="describes actions taken") )
        setattr(cls, "describes relationship of",
                PermissibleValue(text="describes relationship of") )
        setattr(cls, "describes the outcome of",
                PermissibleValue(text="describes the outcome of") )
        setattr(cls, "further describes the test in",
                PermissibleValue(text="further describes the test in") )
        setattr(cls, "further specifies the anatomical location in",
                PermissibleValue(text="further specifies the anatomical location in") )
        setattr(cls, "groups tumor assessments used in overall response identified by",
                PermissibleValue(text="groups tumor assessments used in overall response identified by") )
        setattr(cls, "groups values in",
                PermissibleValue(text="groups values in") )
        setattr(cls, "identifies a pattern of",
                PermissibleValue(text="identifies a pattern of") )
        setattr(cls, "identifies an observation described by",
                PermissibleValue(text="identifies an observation described by") )
        setattr(cls, "identifies overall response supported by tumor assessments identified by",
                PermissibleValue(text="identifies overall response supported by tumor assessments identified by") )
        setattr(cls, "identifies the image from the procedure in",
                PermissibleValue(text="identifies the image from the procedure in") )
        setattr(cls, "identifies the tumor found by the test in",
                PermissibleValue(text="identifies the tumor found by the test in") )
        setattr(cls, "indicates occurrence of the value in",
                PermissibleValue(text="indicates occurrence of the value in") )
        setattr(cls, "indicates pre-specification of the value in",
                PermissibleValue(text="indicates pre-specification of the value in") )
        setattr(cls, "indicates severity of",
                PermissibleValue(text="indicates severity of") )
        setattr(cls, "indicates the previous irradiation status of the tumor identified by",
                PermissibleValue(text="indicates the previous irradiation status of the tumor identified by") )
        setattr(cls, "indicates the progression status of the previous irradiated tumor identified by",
                PermissibleValue(text="indicates the progression status of the previous irradiated tumor identified by") )
        setattr(cls, "is a dictionary-derived term for the value in",
                PermissibleValue(text="is a dictionary-derived term for the value in") )
        setattr(cls, "is decoded by the value in",
                PermissibleValue(text="is decoded by the value in") )
        setattr(cls, "is original text for",
                PermissibleValue(text="is original text for") )
        setattr(cls, "is the administered amount of the treatment in",
                PermissibleValue(text="is the administered amount of the treatment in") )
        setattr(cls, "is the administration anatomical location for the treatment in",
                PermissibleValue(text="is the administration anatomical location for the treatment in") )
        setattr(cls, "is the aspect of the event used to define the date in",
                PermissibleValue(text="is the aspect of the event used to define the date in") )
        setattr(cls, "is the clinical significance interpretation for",
                PermissibleValue(text="is the clinical significance interpretation for") )
        setattr(cls, "is the code for the value in",
                PermissibleValue(text="is the code for the value in") )
        setattr(cls, "is the dictionary code for the test in",
                PermissibleValue(text="is the dictionary code for the test in") )
        setattr(cls, "is the dictionary-derived term for the value in",
                PermissibleValue(text="is the dictionary-derived term for the value in") )
        setattr(cls, "is the dictionary-derived class code for the value in",
                PermissibleValue(text="is the dictionary-derived class code for the value in") )
        setattr(cls, "is the dictionary-derived class name for the value in",
                PermissibleValue(text="is the dictionary-derived class name for the value in") )
        setattr(cls, "is the duration for",
                PermissibleValue(text="is the duration for") )
        setattr(cls, "is the end date for",
                PermissibleValue(text="is the end date for") )
        setattr(cls, "is the epoch of the performance of the test in",
                PermissibleValue(text="is the epoch of the performance of the test in") )
        setattr(cls, "is the frequency of administration of the amount in",
                PermissibleValue(text="is the frequency of administration of the amount in") )
        setattr(cls, "is the identifier for the source data used in the performance of the test in",
                PermissibleValue(text="is the identifier for the source data used in the performance of the test in") )
        setattr(cls, "is the material type of the subject of the activity in",
                PermissibleValue(text="is the material type of the subject of the activity in") )
        setattr(cls, "is the medical condition that is the reason for the treatment in",
                PermissibleValue(text="is the medical condition that is the reason for the treatment in") )
        setattr(cls, "is the method for the test in",
                PermissibleValue(text="is the method for the test in") )
        setattr(cls, "is the part of the body through which is administered the treatment in",
                PermissibleValue(text="is the part of the body through which is administered the treatment in") )
        setattr(cls, "is the physical form of the product in",
                PermissibleValue(text="is the physical form of the product in") )
        setattr(cls, "is the result of the test in",
                PermissibleValue(text="is the result of the test in") )
        setattr(cls, "is the role of the assessor who performed the test in",
                PermissibleValue(text="is the role of the assessor who performed the test in") )
        setattr(cls, "is the specimen tested in",
                PermissibleValue(text="is the specimen tested in") )
        setattr(cls, "is the start date for",
                PermissibleValue(text="is the start date for") )
        setattr(cls, "is the subject position during performance of the test in",
                PermissibleValue(text="is the subject position during performance of the test in") )
        setattr(cls, "is the subject's fasting status during the performance of the test in",
                PermissibleValue(text="is the subject's fasting status during the performance of the test in") )
        setattr(cls, "is the unit for the value in",
                PermissibleValue(text="is the unit for the value in") )
        setattr(cls, "is the unit for",
                PermissibleValue(text="is the unit for") )
        setattr(cls, "specifies the anatomical location of",
                PermissibleValue(text="specifies the anatomical location of") )
        setattr(cls, "specifies the anatomical location of the performance of the test in",
                PermissibleValue(text="specifies the anatomical location of the performance of the test in") )
        setattr(cls, "specifies the severity of",
                PermissibleValue(text="specifies the severity of") )
        setattr(cls, "values are grouped by",
                PermissibleValue(text="values are grouped by") )
        setattr(cls, "was the subject position during performance of the test in",
                PermissibleValue(text="was the subject position during performance of the test in") )
        setattr(cls, "identifies the reference used in the genomic test in",
                PermissibleValue(text="identifies the reference used in the genomic test in") )
        setattr(cls, "indicates heritability of the genetic variant in",
                PermissibleValue(text="indicates heritability of the genetic variant in") )
        setattr(cls, "is an identifier for a published reference for the genetic variant in",
                PermissibleValue(text="is an identifier for a published reference for the genetic variant in") )
        setattr(cls, "is an identifier for the copy, on one of two homologous chromosones, of the genetic variant in",
                PermissibleValue(text="is an identifier for the copy, on one of two homologous chromosones, of the genetic variant in") )
        setattr(cls, "is an identifier for the genetic sequence of the genetic entity represented by",
                PermissibleValue(text="is an identifier for the genetic sequence of the genetic entity represented by") )
        setattr(cls, "is the chromosome that is the position of the result in",
                PermissibleValue(text="is the chromosome that is the position of the result in") )
        setattr(cls, "is the date of occurrence",
                PermissibleValue(text="is the date of occurrence") )
        setattr(cls, "is the date of occurrence for",
                PermissibleValue(text="is the date of occurrence for") )
        setattr(cls, "is the method of secondary analysis of results in",
                PermissibleValue(text="is the method of secondary analysis of results in") )
        setattr(cls, "is the numeric location, within a chromosone, genetic entity, or genetic sub-region, of the result in",
                PermissibleValue(text="is the numeric location, within a chromosone, genetic entity, or genetic sub-region, of the result in") )
        setattr(cls, "is the symbol for the genomic entity that is the position of the result in",
                PermissibleValue(text="is the symbol for the genomic entity that is the position of the result in") )
        setattr(cls, "is the type of genomic entity that is the position of the result in",
                PermissibleValue(text="is the type of genomic entity that is the position of the result in") )
        setattr(cls, "is the genetic sub-location of the result in",
                PermissibleValue(text="is the genetic sub-location of the result in") )
        setattr(cls, "is the object of the observation in",
                PermissibleValue(text="is the object of the observation in") )
        setattr(cls, "is an identifier for the evaluator with the role in",
                PermissibleValue(text="is an identifier for the evaluator with the role in") )

class PredicateTermEnum(EnumDefinitionImpl):

    DECODES = PermissibleValue(text="DECODES")
    DESCRIBES = PermissibleValue(text="DESCRIBES")
    GROUPS = PermissibleValue(text="GROUPS")
    GROUPS_BY = PermissibleValue(text="GROUPS_BY")
    IDENTIFIES = PermissibleValue(text="IDENTIFIES")
    IDENTIFIES_OBSERVATION = PermissibleValue(text="IDENTIFIES_OBSERVATION")
    IDENTIFIES_PRODUCT_IN = PermissibleValue(text="IDENTIFIES_PRODUCT_IN")
    IDENTIFIES_TUMOR_IN = PermissibleValue(text="IDENTIFIES_TUMOR_IN")
    INDICATES = PermissibleValue(text="INDICATES")
    IS_ATTRIBUTE_FOR = PermissibleValue(text="IS_ATTRIBUTE_FOR")
    IS_DECODED_BY = PermissibleValue(text="IS_DECODED_BY")
    IS_DERIVED_FROM = PermissibleValue(text="IS_DERIVED_FROM")
    IS_EPOCH_OF = PermissibleValue(text="IS_EPOCH_OF")
    IS_GROUPED_BY = PermissibleValue(text="IS_GROUPED_BY")
    IS_INDICATOR_FOR = PermissibleValue(text="IS_INDICATOR_FOR")
    IS_ORIGINAL_TEXT_FOR = PermissibleValue(text="IS_ORIGINAL_TEXT_FOR")
    IS_POSITION_FOR = PermissibleValue(text="IS_POSITION_FOR")
    IS_RESULT_OF = PermissibleValue(text="IS_RESULT_OF")
    IS_SPECIMEN_TESTED_IN = PermissibleValue(text="IS_SPECIMEN_TESTED_IN")
    IS_SUBJECT_STATE_FOR = PermissibleValue(text="IS_SUBJECT_STATE_FOR")
    IS_TIMING_FOR = PermissibleValue(text="IS_TIMING_FOR")
    IS_UNIT_FOR = PermissibleValue(text="IS_UNIT_FOR")
    PERFORMED = PermissibleValue(text="PERFORMED")
    PERFORMS = PermissibleValue(text="PERFORMS")
    SPECIFIES = PermissibleValue(text="SPECIFIES")

    _defn = EnumDefinition(
        name="PredicateTermEnum",
    )

class OriginTypeEnum(EnumDefinitionImpl):
    """
    Terminology relevant to the origin type for datasets in the Define-XML document.
    """
    Assigned = PermissibleValue(text="Assigned",
                                       description="A value that is derived through designation, such as values from a look up table or a label on a CRF.",
                                       meaning=NCIT.C170547)
    Collected = PermissibleValue(text="Collected",
                                         description="A value that is actually observed and recorded by a person or obtained by an instrument.",
                                         meaning=NCIT.C170548)
    Derived = PermissibleValue(text="Derived",
                                     description="A value that is calculated by an algorithm or reproducible rule, and which is dependent upon other data values.",
                                     meaning=NCIT.C170549)
    Predecessor = PermissibleValue(text="Predecessor",
                                             description="A value that is copied from a variable in another dataset.",
                                             meaning=NCIT.C170550)
    Protocol = PermissibleValue(text="Protocol",
                                       description="A value that is included as part of the study protocol.",
                                       meaning=NCIT.C170551)

    _defn = EnumDefinition(
        name="OriginTypeEnum",
        description="Terminology relevant to the origin type for datasets in the Define-XML document.",
        code_set=NCIT.C170449,
    )

class OriginSourceEnum(EnumDefinitionImpl):
    """
    Terminology relevant to the origin source for datasets in the Define-XML document.
    """
    Investigator = PermissibleValue(text="Investigator",
                                               description="A person responsible for the conduct of the clinical trial at a trial site. If a trial is conducted by a team of individuals at the trial site, the investigator is the responsible leader of the team and may be called the principal investigator.",
                                               meaning=NCIT.C25936)
    Sponsor = PermissibleValue(text="Sponsor",
                                     description="An individual, company, institution, or organization that takes responsibility for the initiation, management, and/or financing of a clinical study. [After ICH E6, WHO, 21 CFR 50.3 (e), and after IDMP]",
                                     meaning=NCIT.C70793)
    Subject = PermissibleValue(text="Subject",
                                     description="An individual who is observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study.",
                                     meaning=NCIT.C41189)
    Vendor = PermissibleValue(text="Vendor",
                                   description="A person or agency that promotes or exchanges goods or services for money. (NCI)",
                                   meaning=NCIT.C68608)

    _defn = EnumDefinition(
        name="OriginSourceEnum",
        description="Terminology relevant to the origin source for datasets in the Define-XML document.",
        code_set=NCIT.C170450,
    )

class RoleEnum(EnumDefinitionImpl):

    Identifier = PermissibleValue(text="Identifier")
    Qualifier = PermissibleValue(text="Qualifier")
    Timing = PermissibleValue(text="Timing")
    Topic = PermissibleValue(text="Topic")

    _defn = EnumDefinition(
        name="RoleEnum",
    )

class ComparatorEnum(EnumDefinitionImpl):

    EQ = PermissibleValue(text="EQ")
    IN = PermissibleValue(text="IN")

    _defn = EnumDefinition(
        name="ComparatorEnum",
    )

# Slots
class slots:
    pass

slots.packageDate = Slot(uri=COSMOS.packageDate, name="packageDate", curie=COSMOS.curie('packageDate'),
                   model_uri=COSMOS.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=COSMOS.packageType, name="packageType", curie=COSMOS.curie('packageType'),
                   model_uri=COSMOS.packageType, domain=None, range=Union[str, "SDTMDatasetSpecializationPackageTypeEnum"])

slots.domain = Slot(uri=COSMOS.domain, name="domain", curie=COSMOS.curie('domain'),
                   model_uri=COSMOS.domain, domain=None, range=str)

slots.datasetSpecializationId = Slot(uri=COSMOS.datasetSpecializationId, name="datasetSpecializationId", curie=COSMOS.curie('datasetSpecializationId'),
                   model_uri=COSMOS.datasetSpecializationId, domain=None, range=URIRef)

slots.source = Slot(uri=COSMOS.source, name="source", curie=COSMOS.curie('source'),
                   model_uri=COSMOS.source, domain=None, range=str)

slots.shortName = Slot(uri=COSMOS.shortName, name="shortName", curie=COSMOS.curie('shortName'),
                   model_uri=COSMOS.shortName, domain=None, range=str)

slots.sdtmigStartVersion = Slot(uri=COSMOS.sdtmigStartVersion, name="sdtmigStartVersion", curie=COSMOS.curie('sdtmigStartVersion'),
                   model_uri=COSMOS.sdtmigStartVersion, domain=None, range=str)

slots.sdtmigEndVersion = Slot(uri=COSMOS.sdtmigEndVersion, name="sdtmigEndVersion", curie=COSMOS.curie('sdtmigEndVersion'),
                   model_uri=COSMOS.sdtmigEndVersion, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=COSMOS.biomedicalConceptId, name="biomedicalConceptId", curie=COSMOS.curie('biomedicalConceptId'),
                   model_uri=COSMOS.biomedicalConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.variables = Slot(uri=COSMOS.variables, name="variables", curie=COSMOS.curie('variables'),
                   model_uri=COSMOS.variables, domain=None, range=Optional[Union[Dict[Union[str, SDTMVariableName], Union[dict, SDTMVariable]], List[Union[dict, SDTMVariable]]]])

slots.name = Slot(uri=COSMOS.name, name="name", curie=COSMOS.curie('name'),
                   model_uri=COSMOS.name, domain=None, range=URIRef)

slots.dataElementConceptId = Slot(uri=COSMOS.dataElementConceptId, name="dataElementConceptId", curie=COSMOS.curie('dataElementConceptId'),
                   model_uri=COSMOS.dataElementConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.isNonStandard = Slot(uri=COSMOS.isNonStandard, name="isNonStandard", curie=COSMOS.curie('isNonStandard'),
                   model_uri=COSMOS.isNonStandard, domain=None, range=Optional[Union[bool, Bool]])

slots.codelist = Slot(uri=COSMOS.codelist, name="codelist", curie=COSMOS.curie('codelist'),
                   model_uri=COSMOS.codelist, domain=None, range=Optional[Union[dict, CodeList]])

slots.subsetCodelist = Slot(uri=COSMOS.subsetCodelist, name="subsetCodelist", curie=COSMOS.curie('subsetCodelist'),
                   model_uri=COSMOS.subsetCodelist, domain=None, range=Optional[str])

slots.conceptId = Slot(uri=COSMOS.conceptId, name="conceptId", curie=COSMOS.curie('conceptId'),
                   model_uri=COSMOS.conceptId, domain=None, range=URIRef,
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.href = Slot(uri=COSMOS.href, name="href", curie=COSMOS.curie('href'),
                   model_uri=COSMOS.href, domain=None, range=Optional[Union[str, URI]])

slots.submissionValue = Slot(uri=COSMOS.submissionValue, name="submissionValue", curie=COSMOS.curie('submissionValue'),
                   model_uri=COSMOS.submissionValue, domain=None, range=str)

slots.parentCodelist = Slot(uri=COSMOS.parentCodelist, name="parentCodelist", curie=COSMOS.curie('parentCodelist'),
                   model_uri=COSMOS.parentCodelist, domain=None, range=str)

slots.subsetShortName = Slot(uri=COSMOS.subsetShortName, name="subsetShortName", curie=COSMOS.curie('subsetShortName'),
                   model_uri=COSMOS.subsetShortName, domain=None, range=str)

slots.subsetLabel = Slot(uri=COSMOS.subsetLabel, name="subsetLabel", curie=COSMOS.curie('subsetLabel'),
                   model_uri=COSMOS.subsetLabel, domain=None, range=str)

slots.codelistTerm = Slot(uri=COSMOS.codelistTerm, name="codelistTerm", curie=COSMOS.curie('codelistTerm'),
                   model_uri=COSMOS.codelistTerm, domain=None, range=Union[Union[dict, CodeListTerm], List[Union[dict, CodeListTerm]]])

slots.termId = Slot(uri=COSMOS.termId, name="termId", curie=COSMOS.curie('termId'),
                   model_uri=COSMOS.termId, domain=None, range=str)

slots.termValue = Slot(uri=COSMOS.termValue, name="termValue", curie=COSMOS.curie('termValue'),
                   model_uri=COSMOS.termValue, domain=None, range=str)

slots.valueList = Slot(uri=COSMOS.valueList, name="valueList", curie=COSMOS.curie('valueList'),
                   model_uri=COSMOS.valueList, domain=None, range=Optional[Union[str, List[str]]])

slots.assignedTerm = Slot(uri=COSMOS.assignedTerm, name="assignedTerm", curie=COSMOS.curie('assignedTerm'),
                   model_uri=COSMOS.assignedTerm, domain=None, range=Optional[Union[dict, AssignedTerm]])

slots.role = Slot(uri=COSMOS.role, name="role", curie=COSMOS.curie('role'),
                   model_uri=COSMOS.role, domain=None, range=Optional[Union[str, "RoleEnum"]])

slots.relationship = Slot(uri=COSMOS.relationship, name="relationship", curie=COSMOS.curie('relationship'),
                   model_uri=COSMOS.relationship, domain=None, range=Optional[Union[dict, RelationShip]])

slots.subject = Slot(uri=COSMOS.subject, name="subject", curie=COSMOS.curie('subject'),
                   model_uri=COSMOS.subject, domain=None, range=str)

slots.linkingPhrase = Slot(uri=COSMOS.linkingPhrase, name="linkingPhrase", curie=COSMOS.curie('linkingPhrase'),
                   model_uri=COSMOS.linkingPhrase, domain=None, range=Union[str, "LinkingPhraseEnum"])

slots.predicateTerm = Slot(uri=COSMOS.predicateTerm, name="predicateTerm", curie=COSMOS.curie('predicateTerm'),
                   model_uri=COSMOS.predicateTerm, domain=None, range=Union[str, "PredicateTermEnum"])

slots.object = Slot(uri=COSMOS.object, name="object", curie=COSMOS.curie('object'),
                   model_uri=COSMOS.object, domain=None, range=str)

slots.dataType = Slot(uri=COSMOS.dataType, name="dataType", curie=COSMOS.curie('dataType'),
                   model_uri=COSMOS.dataType, domain=None, range=Optional[Union[str, "SDTMVariableDataTypeEnum"]])

slots.length = Slot(uri=COSMOS.length, name="length", curie=COSMOS.curie('length'),
                   model_uri=COSMOS.length, domain=None, range=Optional[int])

slots.format = Slot(uri=COSMOS.format, name="format", curie=COSMOS.curie('format'),
                   model_uri=COSMOS.format, domain=None, range=Optional[str])

slots.significantDigits = Slot(uri=COSMOS.significantDigits, name="significantDigits", curie=COSMOS.curie('significantDigits'),
                   model_uri=COSMOS.significantDigits, domain=None, range=Optional[int])

slots.mandatoryVariable = Slot(uri=COSMOS.mandatoryVariable, name="mandatoryVariable", curie=COSMOS.curie('mandatoryVariable'),
                   model_uri=COSMOS.mandatoryVariable, domain=None, range=Optional[Union[bool, Bool]])

slots.mandatoryValue = Slot(uri=COSMOS.mandatoryValue, name="mandatoryValue", curie=COSMOS.curie('mandatoryValue'),
                   model_uri=COSMOS.mandatoryValue, domain=None, range=Optional[Union[bool, Bool]])

slots.originType = Slot(uri=COSMOS.originType, name="originType", curie=COSMOS.curie('originType'),
                   model_uri=COSMOS.originType, domain=None, range=Optional[Union[str, "OriginTypeEnum"]])

slots.originSource = Slot(uri=COSMOS.originSource, name="originSource", curie=COSMOS.curie('originSource'),
                   model_uri=COSMOS.originSource, domain=None, range=Optional[Union[str, "OriginSourceEnum"]])

slots.comparator = Slot(uri=COSMOS.comparator, name="comparator", curie=COSMOS.curie('comparator'),
                   model_uri=COSMOS.comparator, domain=None, range=Optional[Union[str, "ComparatorEnum"]])

slots.vlmTarget = Slot(uri=COSMOS.vlmTarget, name="vlmTarget", curie=COSMOS.curie('vlmTarget'),
                   model_uri=COSMOS.vlmTarget, domain=None, range=Optional[Union[bool, Bool]])

slots.assignedTerm__conceptId = Slot(uri=COSMOS.conceptId, name="assignedTerm__conceptId", curie=COSMOS.curie('conceptId'),
                   model_uri=COSMOS.assignedTerm__conceptId, domain=None, range=Optional[str])

slots.assignedTerm__value = Slot(uri=COSMOS.value, name="assignedTerm__value", curie=COSMOS.curie('value'),
                   model_uri=COSMOS.assignedTerm__value, domain=None, range=str)
