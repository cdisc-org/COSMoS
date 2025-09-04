# Auto generated from cosmos_sdtm_bc_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-09-04T13:40:17
# Schema: COSMoS-Biomedical-Concepts-SDTM-Schema
#
# id: https://www.cdisc.org/cosmos/sdtm_v1.0
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
COSMOS_SDTM = CurieNamespace('cosmos_sdtm', 'https://www.cdisc.org/cosmos/sdtm_v1.0/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = COSMOS_SDTM


# Types

# Class references
class SDTMGroupDatasetSpecializationId(extended_str):
    pass


class SDTMVariableName(extended_str):
    pass


class CodeListConceptId(extended_str):
    pass


@dataclass(repr=False)
class SDTMGroup(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["SDTMGroup"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:SDTMGroup"
    class_name: ClassVar[str] = "SDTMGroup"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.SDTMGroup

    datasetSpecializationId: Union[str, SDTMGroupDatasetSpecializationId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "PackageTypeEnum"] = None
    domain: str = None
    shortName: str = None
    source: str = None
    sdtmigStartVersion: str = None
    variables: Union[dict[Union[str, SDTMVariableName], Union[dict, "SDTMVariable"]], list[Union[dict, "SDTMVariable"]]] = empty_dict()
    sdtmigEndVersion: Optional[str] = None
    biomedicalConceptId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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
        if not isinstance(self.packageType, PackageTypeEnum):
            self.packageType = PackageTypeEnum(self.packageType)

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

        if self._is_empty(self.variables):
            self.MissingRequiredField("variables")
        self._normalize_inlined_as_list(slot_name="variables", slot_type=SDTMVariable, key_name="name", keyed=True)

        if self.sdtmigEndVersion is not None and not isinstance(self.sdtmigEndVersion, str):
            self.sdtmigEndVersion = str(self.sdtmigEndVersion)

        if self.biomedicalConceptId is not None and not isinstance(self.biomedicalConceptId, str):
            self.biomedicalConceptId = str(self.biomedicalConceptId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SDTMVariable(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["SDTMVariable"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:SDTMVariable"
    class_name: ClassVar[str] = "SDTMVariable"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.SDTMVariable

    name: Union[str, SDTMVariableName] = None
    dataElementConceptId: Optional[str] = None
    isNonStandard: Optional[Union[bool, Bool]] = None
    codelist: Optional[Union[dict, "CodeList"]] = None
    subsetCodelist: Optional[str] = None
    valueList: Optional[Union[str, list[str]]] = empty_list()
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

    def __post_init__(self, *_: str, **kwargs: Any):
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


@dataclass(repr=False)
class RelationShip(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["RelationShip"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:RelationShip"
    class_name: ClassVar[str] = "RelationShip"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.RelationShip

    subject: str = None
    linkingPhrase: Union[str, "LinkingPhraseEnum"] = None
    predicateTerm: Union[str, "PredicateTermEnum"] = None
    object: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
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


@dataclass(repr=False)
class CodeList(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["CodeList"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:CodeList"
    class_name: ClassVar[str] = "CodeList"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.CodeList

    conceptId: Union[str, CodeListConceptId] = None
    submissionValue: str = None
    href: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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


@dataclass(repr=False)
class CodeListTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["CodeListTerm"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:CodeListTerm"
    class_name: ClassVar[str] = "CodeListTerm"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.CodeListTerm

    termId: str = None
    termValue: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.termId):
            self.MissingRequiredField("termId")
        if not isinstance(self.termId, str):
            self.termId = str(self.termId)

        if self._is_empty(self.termValue):
            self.MissingRequiredField("termValue")
        if not isinstance(self.termValue, str):
            self.termValue = str(self.termValue)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubsetCodeList(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["SubsetCodeList"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:SubsetCodeList"
    class_name: ClassVar[str] = "SubsetCodeList"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.SubsetCodeList

    parentCodelist: str = None
    subsetShortName: str = None
    subsetLabel: str = None
    codelistTerm: Union[Union[dict, CodeListTerm], list[Union[dict, CodeListTerm]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
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


@dataclass(repr=False)
class AssignedTerm(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_SDTM["AssignedTerm"]
    class_class_curie: ClassVar[str] = "cosmos_sdtm:AssignedTerm"
    class_name: ClassVar[str] = "AssignedTerm"
    class_model_uri: ClassVar[URIRef] = COSMOS_SDTM.AssignedTerm

    value: str = None
    conceptId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.conceptId is not None and not isinstance(self.conceptId, str):
            self.conceptId = str(self.conceptId)

        super().__post_init__(**kwargs)


# Enumerations
class PackageTypeEnum(EnumDefinitionImpl):

    sdtm = PermissibleValue(text="sdtm")

    _defn = EnumDefinition(
        name="PackageTypeEnum",
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
        setattr(cls, "assesses seriousness of",
            PermissibleValue(text="assesses seriousness of"))
        setattr(cls, "assesses the severity of",
            PermissibleValue(text="assesses the severity of"))
        setattr(cls, "associates the tumor identified in",
            PermissibleValue(text="associates the tumor identified in"))
        setattr(cls, "decodes the value in",
            PermissibleValue(text="decodes the value in"))
        setattr(cls, "describes actions taken",
            PermissibleValue(text="describes actions taken"))
        setattr(cls, "describes relationship of",
            PermissibleValue(text="describes relationship of"))
        setattr(cls, "describes the outcome of",
            PermissibleValue(text="describes the outcome of"))
        setattr(cls, "further describes the test in",
            PermissibleValue(text="further describes the test in"))
        setattr(cls, "further specifies the anatomical location in",
            PermissibleValue(text="further specifies the anatomical location in"))
        setattr(cls, "groups tumor assessments used in overall response identified by",
            PermissibleValue(text="groups tumor assessments used in overall response identified by"))
        setattr(cls, "groups values in",
            PermissibleValue(text="groups values in"))
        setattr(cls, "groups, within an individual subject, values in",
            PermissibleValue(text="groups, within an individual subject, values in"))
        setattr(cls, "identifies a pattern of",
            PermissibleValue(text="identifies a pattern of"))
        setattr(cls, "identifies an observation described by",
            PermissibleValue(text="identifies an observation described by"))
        setattr(cls, "identifies overall response supported by tumor assessments identified by",
            PermissibleValue(text="identifies overall response supported by tumor assessments identified by"))
        setattr(cls, "identifies the image from the procedure in",
            PermissibleValue(text="identifies the image from the procedure in"))
        setattr(cls, "identifies the tumor found by the test in",
            PermissibleValue(text="identifies the tumor found by the test in"))
        setattr(cls, "indicates occurrence of the value in",
            PermissibleValue(text="indicates occurrence of the value in"))
        setattr(cls, "indicates pre-specification of the value in",
            PermissibleValue(text="indicates pre-specification of the value in"))
        setattr(cls, "indicates severity of",
            PermissibleValue(text="indicates severity of"))
        setattr(cls, "indicates the previous irradiation status of the tumor identified by",
            PermissibleValue(text="indicates the previous irradiation status of the tumor identified by"))
        setattr(cls, "indicates the progression status of the previous irradiated tumor identified by",
            PermissibleValue(text="indicates the progression status of the previous irradiated tumor identified by"))
        setattr(cls, "is a dictionary-derived term for the value in",
            PermissibleValue(text="is a dictionary-derived term for the value in"))
        setattr(cls, "is a dictionary-derived class code for the value in",
            PermissibleValue(text="is a dictionary-derived class code for the value in"))
        setattr(cls, "is a dictionary-derived class name for the value in",
            PermissibleValue(text="is a dictionary-derived class name for the value in"))
        setattr(cls, "is decoded by the value in",
            PermissibleValue(text="is decoded by the value in"))
        setattr(cls, "is original text for",
            PermissibleValue(text="is original text for"))
        setattr(cls, "is the administered amount of the treatment in",
            PermissibleValue(text="is the administered amount of the treatment in"))
        setattr(cls, "is the administration anatomical location for the treatment in",
            PermissibleValue(text="is the administration anatomical location for the treatment in"))
        setattr(cls, "is the aspect of the event used to define the date in",
            PermissibleValue(text="is the aspect of the event used to define the date in"))
        setattr(cls, "is the clinical significance interpretation for",
            PermissibleValue(text="is the clinical significance interpretation for"))
        setattr(cls, "is the code for the value in",
            PermissibleValue(text="is the code for the value in"))
        setattr(cls, "is the dictionary code for the test in",
            PermissibleValue(text="is the dictionary code for the test in"))
        setattr(cls, "is the dictionary-derived term for the value in",
            PermissibleValue(text="is the dictionary-derived term for the value in"))
        setattr(cls, "is the dictionary-derived class code for the value in",
            PermissibleValue(text="is the dictionary-derived class code for the value in"))
        setattr(cls, "is the dictionary-derived class name for the value in",
            PermissibleValue(text="is the dictionary-derived class name for the value in"))
        setattr(cls, "is the duration for",
            PermissibleValue(text="is the duration for"))
        setattr(cls, "is the end date for",
            PermissibleValue(text="is the end date for"))
        setattr(cls, "is the epoch of the performance of the test in",
            PermissibleValue(text="is the epoch of the performance of the test in"))
        setattr(cls, "is the frequency of administration of the amount in",
            PermissibleValue(text="is the frequency of administration of the amount in"))
        setattr(cls, "is the identifier for the source data used in the performance of the test in",
            PermissibleValue(text="is the identifier for the source data used in the performance of the test in"))
        setattr(cls, "is the material type of the subject of the activity in",
            PermissibleValue(text="is the material type of the subject of the activity in"))
        setattr(cls, "is the medical condition that is the reason for the treatment in",
            PermissibleValue(text="is the medical condition that is the reason for the treatment in"))
        setattr(cls, "is the method for the test in",
            PermissibleValue(text="is the method for the test in"))
        setattr(cls, "is the part of the body through which is administered the treatment in",
            PermissibleValue(text="is the part of the body through which is administered the treatment in"))
        setattr(cls, "is the physical form of the product in",
            PermissibleValue(text="is the physical form of the product in"))
        setattr(cls, "is the result of the test in",
            PermissibleValue(text="is the result of the test in"))
        setattr(cls, "is the role of the assessor who performed the test in",
            PermissibleValue(text="is the role of the assessor who performed the test in"))
        setattr(cls, "is the specimen tested in",
            PermissibleValue(text="is the specimen tested in"))
        setattr(cls, "is the start date for",
            PermissibleValue(text="is the start date for"))
        setattr(cls, "is the subject position during performance of the test in",
            PermissibleValue(text="is the subject position during performance of the test in"))
        setattr(cls, "is the subject's fasting status during the performance of the test in",
            PermissibleValue(text="is the subject's fasting status during the performance of the test in"))
        setattr(cls, "is the unit for the value in",
            PermissibleValue(text="is the unit for the value in"))
        setattr(cls, "is the unit for",
            PermissibleValue(text="is the unit for"))
        setattr(cls, "specifies the anatomical location in",
            PermissibleValue(text="specifies the anatomical location in"))
        setattr(cls, "specifies the anatomical location of",
            PermissibleValue(text="specifies the anatomical location of"))
        setattr(cls, "specifies the anatomical location of the performance of the test in",
            PermissibleValue(text="specifies the anatomical location of the performance of the test in"))
        setattr(cls, "specifies the anatomical location of the tumor identified by",
            PermissibleValue(text="specifies the anatomical location of the tumor identified by"))
        setattr(cls, "specifies the severity of",
            PermissibleValue(text="specifies the severity of"))
        setattr(cls, "values are grouped by",
            PermissibleValue(text="values are grouped by"))
        setattr(cls, "was the subject position during performance of the test in",
            PermissibleValue(text="was the subject position during performance of the test in"))
        setattr(cls, "identifies the reference used in the genomic test in",
            PermissibleValue(text="identifies the reference used in the genomic test in"))
        setattr(cls, "indicates heritability of the genetic variant in",
            PermissibleValue(text="indicates heritability of the genetic variant in"))
        setattr(cls, "is an identifier for a published reference for the genetic variant in",
            PermissibleValue(text="is an identifier for a published reference for the genetic variant in"))
        setattr(cls, "is an identifier for the copy, on one of two homologous chromosones, of the genetic variant in",
            PermissibleValue(text="is an identifier for the copy, on one of two homologous chromosones, of the genetic variant in"))
        setattr(cls, "is an identifier for the genetic sequence of the genetic entity represented by",
            PermissibleValue(text="is an identifier for the genetic sequence of the genetic entity represented by"))
        setattr(cls, "is the chromosome that is the position of the result in",
            PermissibleValue(text="is the chromosome that is the position of the result in"))
        setattr(cls, "is the clinical trial or treatment setting for",
            PermissibleValue(text="is the clinical trial or treatment setting for"))
        setattr(cls, "is the date of occurrence",
            PermissibleValue(text="is the date of occurrence"))
        setattr(cls, "is the date of occurrence for",
            PermissibleValue(text="is the date of occurrence for"))
        setattr(cls, "is the intended disease outcome for",
            PermissibleValue(text="is the intended disease outcome for"))
        setattr(cls, "is the method of secondary analysis of results in",
            PermissibleValue(text="is the method of secondary analysis of results in"))
        setattr(cls, "is the numeric location, within a chromosone, genetic entity, or genetic sub-region, of the result in",
            PermissibleValue(text="is the numeric location, within a chromosone, genetic entity, or genetic sub-region, of the result in"))
        setattr(cls, "is the symbol for the genomic entity that is the position of the result in",
            PermissibleValue(text="is the symbol for the genomic entity that is the position of the result in"))
        setattr(cls, "is the type of genomic entity that is the position of the result in",
            PermissibleValue(text="is the type of genomic entity that is the position of the result in"))
        setattr(cls, "is the genetic sub-location of the result in",
            PermissibleValue(text="is the genetic sub-location of the result in"))
        setattr(cls, "is the object of the observation in",
            PermissibleValue(text="is the object of the observation in"))
        setattr(cls, "is an identifier for the evaluator with the role in",
            PermissibleValue(text="is an identifier for the evaluator with the role in"))
        setattr(cls, "is the severity of the toxicity in",
            PermissibleValue(text="is the severity of the toxicity in"))
        setattr(cls, "is a grouping of values in",
            PermissibleValue(text="is a grouping of values in"))
        setattr(cls, "is the textual description of the intended dose regimen for",
            PermissibleValue(text="is the textual description of the intended dose regimen for"))
        setattr(cls, "is the reason for stopping administration of",
            PermissibleValue(text="is the reason for stopping administration of"))
        setattr(cls, "is the value of the property identified by",
            PermissibleValue(text="is the value of the property identified by"))
        setattr(cls, "is the name of the reference terminology for",
            PermissibleValue(text="is the name of the reference terminology for"))
        setattr(cls, "is the version of the reference terminology in",
            PermissibleValue(text="is the version of the reference terminology in"))
        setattr(cls, "is the period of time for the test in",
            PermissibleValue(text="is the period of time for the test in"))
        setattr(cls, "is a reference range value for",
            PermissibleValue(text="is a reference range value for"))
        setattr(cls, "is the identifier for the device which collected data for the test in",
            PermissibleValue(text="is the identifier for the device which collected data for the test in"))
        setattr(cls, "is the substance bound to the analyte in",
            PermissibleValue(text="is the substance bound to the analyte in"))
        setattr(cls, "is the operational objective of the test in",
            PermissibleValue(text="is the operational objective of the test in"))
        setattr(cls, "is the period of time to be considered when answering the question in",
            PermissibleValue(text="is the period of time to be considered when answering the question in"))

class PredicateTermEnum(EnumDefinitionImpl):

    ASSESSES = PermissibleValue(text="ASSESSES")
    CLASSIFIES = PermissibleValue(text="CLASSIFIES")
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
    IS_REASON_FOR = PermissibleValue(text="IS_REASON_FOR")
    IS_RESULT_OF = PermissibleValue(text="IS_RESULT_OF")
    IS_SPECIMEN_TESTED_IN = PermissibleValue(text="IS_SPECIMEN_TESTED_IN")
    IS_SUBJECT_STATE_FOR = PermissibleValue(text="IS_SUBJECT_STATE_FOR")
    IS_TIMING_FOR = PermissibleValue(text="IS_TIMING_FOR")
    IS_UNIT_FOR = PermissibleValue(text="IS_UNIT_FOR")
    PERFORMED = PermissibleValue(text="PERFORMED")
    PERFORMS = PermissibleValue(text="PERFORMS")
    QUALIFIES = PermissibleValue(text="QUALIFIES")
    SPECIFIES = PermissibleValue(text="SPECIFIES")
    IS_VALUE_OF = PermissibleValue(text="IS_VALUE_OF")
    IS_REFERENCE_TERMINOLOGY_FOR = PermissibleValue(text="IS_REFERENCE_TERMINOLOGY_FOR")
    IS_REFERENCE_VALUE_FOR = PermissibleValue(text="IS_REFERENCE_VALUE_FOR")

    _defn = EnumDefinition(
        name="PredicateTermEnum",
    )

class OriginTypeEnum(EnumDefinitionImpl):
    """
    Terminology relevant to the origin type for datasets in the Define-XML document.
    """
    Assigned = PermissibleValue(
        text="Assigned",
        description="""A value that is derived through designation, such as values from a look up table or a label on a CRF.""",
        meaning=NCIT["C170547"])
    Collected = PermissibleValue(
        text="Collected",
        description="A value that is actually observed and recorded by a person or obtained by an instrument.",
        meaning=NCIT["C170548"])
    Derived = PermissibleValue(
        text="Derived",
        description="""A value that is calculated by an algorithm or reproducible rule, and which is dependent upon other data values.""",
        meaning=NCIT["C170549"])
    Predecessor = PermissibleValue(
        text="Predecessor",
        description="A value that is copied from a variable in another dataset.",
        meaning=NCIT["C170550"])
    Protocol = PermissibleValue(
        text="Protocol",
        description="A value that is included as part of the study protocol.",
        meaning=NCIT["C170551"])

    _defn = EnumDefinition(
        name="OriginTypeEnum",
        description="Terminology relevant to the origin type for datasets in the Define-XML document.",
        code_set=NCIT["C170449"],
    )

class OriginSourceEnum(EnumDefinitionImpl):
    """
    Terminology relevant to the origin source for datasets in the Define-XML document.
    """
    Investigator = PermissibleValue(
        text="Investigator",
        description="""A person responsible for the conduct of the clinical trial at a trial site. If a trial is conducted by a team of individuals at the trial site, the investigator is the responsible leader of the team and may be called the principal investigator.""",
        meaning=NCIT["C25936"])
    Sponsor = PermissibleValue(
        text="Sponsor",
        description="""An individual, company, institution, or organization that takes responsibility for the initiation, management, and/or financing of a clinical study. [After ICH E6, WHO, 21 CFR 50.3 (e), and after IDMP]""",
        meaning=NCIT["C70793"])
    Subject = PermissibleValue(
        text="Subject",
        description="""An individual who is observed, analyzed, examined, investigated, experimented upon, or/and treated in the course of a particular study.""",
        meaning=NCIT["C41189"])
    Vendor = PermissibleValue(
        text="Vendor",
        description="A person or agency that promotes or exchanges goods or services for money. (NCI)",
        meaning=NCIT["C68608"])

    _defn = EnumDefinition(
        name="OriginSourceEnum",
        description="Terminology relevant to the origin source for datasets in the Define-XML document.",
        code_set=NCIT["C170450"],
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

slots.packageDate = Slot(uri=COSMOS_SDTM.packageDate, name="packageDate", curie=COSMOS_SDTM.curie('packageDate'),
                   model_uri=COSMOS_SDTM.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=COSMOS_SDTM.packageType, name="packageType", curie=COSMOS_SDTM.curie('packageType'),
                   model_uri=COSMOS_SDTM.packageType, domain=None, range=Union[str, "PackageTypeEnum"])

slots.datasetSpecializationId = Slot(uri=COSMOS_SDTM.datasetSpecializationId, name="datasetSpecializationId", curie=COSMOS_SDTM.curie('datasetSpecializationId'),
                   model_uri=COSMOS_SDTM.datasetSpecializationId, domain=None, range=URIRef,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.domain = Slot(uri=COSMOS_SDTM.domain, name="domain", curie=COSMOS_SDTM.curie('domain'),
                   model_uri=COSMOS_SDTM.domain, domain=None, range=str)

slots.source = Slot(uri=COSMOS_SDTM.source, name="source", curie=COSMOS_SDTM.curie('source'),
                   model_uri=COSMOS_SDTM.source, domain=None, range=str)

slots.shortName = Slot(uri=COSMOS_SDTM.shortName, name="shortName", curie=COSMOS_SDTM.curie('shortName'),
                   model_uri=COSMOS_SDTM.shortName, domain=None, range=str)

slots.sdtmigStartVersion = Slot(uri=COSMOS_SDTM.sdtmigStartVersion, name="sdtmigStartVersion", curie=COSMOS_SDTM.curie('sdtmigStartVersion'),
                   model_uri=COSMOS_SDTM.sdtmigStartVersion, domain=None, range=str)

slots.sdtmigEndVersion = Slot(uri=COSMOS_SDTM.sdtmigEndVersion, name="sdtmigEndVersion", curie=COSMOS_SDTM.curie('sdtmigEndVersion'),
                   model_uri=COSMOS_SDTM.sdtmigEndVersion, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=COSMOS_SDTM.biomedicalConceptId, name="biomedicalConceptId", curie=COSMOS_SDTM.curie('biomedicalConceptId'),
                   model_uri=COSMOS_SDTM.biomedicalConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+|NEW_[A-Z]*[0-9]*)$'))

slots.variables = Slot(uri=COSMOS_SDTM.variables, name="variables", curie=COSMOS_SDTM.curie('variables'),
                   model_uri=COSMOS_SDTM.variables, domain=None, range=Union[dict[Union[str, SDTMVariableName], Union[dict, SDTMVariable]], list[Union[dict, SDTMVariable]]])

slots.name = Slot(uri=COSMOS_SDTM.name, name="name", curie=COSMOS_SDTM.curie('name'),
                   model_uri=COSMOS_SDTM.name, domain=None, range=URIRef,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.dataElementConceptId = Slot(uri=COSMOS_SDTM.dataElementConceptId, name="dataElementConceptId", curie=COSMOS_SDTM.curie('dataElementConceptId'),
                   model_uri=COSMOS_SDTM.dataElementConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+|NEW_[A-Z]*[0-9]*)$'))

slots.isNonStandard = Slot(uri=COSMOS_SDTM.isNonStandard, name="isNonStandard", curie=COSMOS_SDTM.curie('isNonStandard'),
                   model_uri=COSMOS_SDTM.isNonStandard, domain=None, range=Optional[Union[bool, Bool]])

slots.codelist = Slot(uri=COSMOS_SDTM.codelist, name="codelist", curie=COSMOS_SDTM.curie('codelist'),
                   model_uri=COSMOS_SDTM.codelist, domain=None, range=Optional[Union[dict, CodeList]])

slots.subsetCodelist = Slot(uri=COSMOS_SDTM.subsetCodelist, name="subsetCodelist", curie=COSMOS_SDTM.curie('subsetCodelist'),
                   model_uri=COSMOS_SDTM.subsetCodelist, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.conceptId = Slot(uri=COSMOS_SDTM.conceptId, name="conceptId", curie=COSMOS_SDTM.curie('conceptId'),
                   model_uri=COSMOS_SDTM.conceptId, domain=None, range=URIRef,
                   pattern=re.compile(r'^C[0-9]+$'))

slots.href = Slot(uri=COSMOS_SDTM.href, name="href", curie=COSMOS_SDTM.curie('href'),
                   model_uri=COSMOS_SDTM.href, domain=None, range=Optional[Union[str, URI]])

slots.submissionValue = Slot(uri=COSMOS_SDTM.submissionValue, name="submissionValue", curie=COSMOS_SDTM.curie('submissionValue'),
                   model_uri=COSMOS_SDTM.submissionValue, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.parentCodelist = Slot(uri=COSMOS_SDTM.parentCodelist, name="parentCodelist", curie=COSMOS_SDTM.curie('parentCodelist'),
                   model_uri=COSMOS_SDTM.parentCodelist, domain=None, range=str,
                   pattern=re.compile(r'^C[0-9]+$'))

slots.subsetShortName = Slot(uri=COSMOS_SDTM.subsetShortName, name="subsetShortName", curie=COSMOS_SDTM.curie('subsetShortName'),
                   model_uri=COSMOS_SDTM.subsetShortName, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.subsetLabel = Slot(uri=COSMOS_SDTM.subsetLabel, name="subsetLabel", curie=COSMOS_SDTM.curie('subsetLabel'),
                   model_uri=COSMOS_SDTM.subsetLabel, domain=None, range=str)

slots.codelistTerm = Slot(uri=COSMOS_SDTM.codelistTerm, name="codelistTerm", curie=COSMOS_SDTM.curie('codelistTerm'),
                   model_uri=COSMOS_SDTM.codelistTerm, domain=None, range=Union[Union[dict, CodeListTerm], list[Union[dict, CodeListTerm]]])

slots.termId = Slot(uri=COSMOS_SDTM.termId, name="termId", curie=COSMOS_SDTM.curie('termId'),
                   model_uri=COSMOS_SDTM.termId, domain=None, range=str,
                   pattern=re.compile(r'^(C[0-9]+)$'))

slots.termValue = Slot(uri=COSMOS_SDTM.termValue, name="termValue", curie=COSMOS_SDTM.curie('termValue'),
                   model_uri=COSMOS_SDTM.termValue, domain=None, range=str)

slots.valueList = Slot(uri=COSMOS_SDTM.valueList, name="valueList", curie=COSMOS_SDTM.curie('valueList'),
                   model_uri=COSMOS_SDTM.valueList, domain=None, range=Optional[Union[str, list[str]]])

slots.assignedTerm = Slot(uri=COSMOS_SDTM.assignedTerm, name="assignedTerm", curie=COSMOS_SDTM.curie('assignedTerm'),
                   model_uri=COSMOS_SDTM.assignedTerm, domain=None, range=Optional[Union[dict, AssignedTerm]])

slots.role = Slot(uri=COSMOS_SDTM.role, name="role", curie=COSMOS_SDTM.curie('role'),
                   model_uri=COSMOS_SDTM.role, domain=None, range=Optional[Union[str, "RoleEnum"]])

slots.relationship = Slot(uri=COSMOS_SDTM.relationship, name="relationship", curie=COSMOS_SDTM.curie('relationship'),
                   model_uri=COSMOS_SDTM.relationship, domain=None, range=Optional[Union[dict, RelationShip]])

slots.subject = Slot(uri=COSMOS_SDTM.subject, name="subject", curie=COSMOS_SDTM.curie('subject'),
                   model_uri=COSMOS_SDTM.subject, domain=None, range=str)

slots.linkingPhrase = Slot(uri=COSMOS_SDTM.linkingPhrase, name="linkingPhrase", curie=COSMOS_SDTM.curie('linkingPhrase'),
                   model_uri=COSMOS_SDTM.linkingPhrase, domain=None, range=Union[str, "LinkingPhraseEnum"])

slots.predicateTerm = Slot(uri=COSMOS_SDTM.predicateTerm, name="predicateTerm", curie=COSMOS_SDTM.curie('predicateTerm'),
                   model_uri=COSMOS_SDTM.predicateTerm, domain=None, range=Union[str, "PredicateTermEnum"])

slots.object = Slot(uri=COSMOS_SDTM.object, name="object", curie=COSMOS_SDTM.curie('object'),
                   model_uri=COSMOS_SDTM.object, domain=None, range=str)

slots.dataType = Slot(uri=COSMOS_SDTM.dataType, name="dataType", curie=COSMOS_SDTM.curie('dataType'),
                   model_uri=COSMOS_SDTM.dataType, domain=None, range=Optional[Union[str, "SDTMVariableDataTypeEnum"]])

slots.length = Slot(uri=COSMOS_SDTM.length, name="length", curie=COSMOS_SDTM.curie('length'),
                   model_uri=COSMOS_SDTM.length, domain=None, range=Optional[int])

slots.format = Slot(uri=COSMOS_SDTM.format, name="format", curie=COSMOS_SDTM.curie('format'),
                   model_uri=COSMOS_SDTM.format, domain=None, range=Optional[str])

slots.significantDigits = Slot(uri=COSMOS_SDTM.significantDigits, name="significantDigits", curie=COSMOS_SDTM.curie('significantDigits'),
                   model_uri=COSMOS_SDTM.significantDigits, domain=None, range=Optional[int])

slots.mandatoryVariable = Slot(uri=COSMOS_SDTM.mandatoryVariable, name="mandatoryVariable", curie=COSMOS_SDTM.curie('mandatoryVariable'),
                   model_uri=COSMOS_SDTM.mandatoryVariable, domain=None, range=Optional[Union[bool, Bool]])

slots.mandatoryValue = Slot(uri=COSMOS_SDTM.mandatoryValue, name="mandatoryValue", curie=COSMOS_SDTM.curie('mandatoryValue'),
                   model_uri=COSMOS_SDTM.mandatoryValue, domain=None, range=Optional[Union[bool, Bool]])

slots.originType = Slot(uri=COSMOS_SDTM.originType, name="originType", curie=COSMOS_SDTM.curie('originType'),
                   model_uri=COSMOS_SDTM.originType, domain=None, range=Optional[Union[str, "OriginTypeEnum"]])

slots.originSource = Slot(uri=COSMOS_SDTM.originSource, name="originSource", curie=COSMOS_SDTM.curie('originSource'),
                   model_uri=COSMOS_SDTM.originSource, domain=None, range=Optional[Union[str, "OriginSourceEnum"]])

slots.comparator = Slot(uri=COSMOS_SDTM.comparator, name="comparator", curie=COSMOS_SDTM.curie('comparator'),
                   model_uri=COSMOS_SDTM.comparator, domain=None, range=Optional[Union[str, "ComparatorEnum"]])

slots.vlmTarget = Slot(uri=COSMOS_SDTM.vlmTarget, name="vlmTarget", curie=COSMOS_SDTM.curie('vlmTarget'),
                   model_uri=COSMOS_SDTM.vlmTarget, domain=None, range=Optional[Union[bool, Bool]])

slots.assignedTerm__conceptId = Slot(uri=COSMOS_SDTM.conceptId, name="assignedTerm__conceptId", curie=COSMOS_SDTM.curie('conceptId'),
                   model_uri=COSMOS_SDTM.assignedTerm__conceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+)$'))

slots.assignedTerm__value = Slot(uri=COSMOS_SDTM.value, name="assignedTerm__value", curie=COSMOS_SDTM.curie('value'),
                   model_uri=COSMOS_SDTM.assignedTerm__value, domain=None, range=str)
