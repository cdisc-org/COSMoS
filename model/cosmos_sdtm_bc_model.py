# Auto generated from cosmos_sdtm_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-06-15T17:04:30
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
class SDTMGroupDatasetSpecializationId(extended_str):
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

    datasetSpecializationId: Union[str, SDTMGroupDatasetSpecializationId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "SDTMDatasetSpecializationPackageType"] = None
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
        if not isinstance(self.packageType, SDTMDatasetSpecializationPackageType):
            self.packageType = SDTMDatasetSpecializationPackageType(self.packageType)

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMVariable")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SDTMVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMVariable")

    name: Union[str, SDTMVariableName] = None
    dataElementConceptId: Optional[str] = None
    isNonStandard: Optional[Union[bool, Bool]] = None
    codelist: Optional[Union[dict, "CodeList"]] = None
    subsetCodelist: Optional[str] = None
    valueList: Optional[Union[str, List[str]]] = empty_list()
    assignedTerm: Optional[Union[dict, "AssignedTerm"]] = None
    role: Optional[str] = None
    relationship: Optional[Union[dict, "RelationShip"]] = None
    dataType: Optional[Union[str, "SDTMVariableDataType"]] = None
    length: Optional[int] = None
    format: Optional[str] = None
    significantDigits: Optional[int] = None
    mandatoryVariable: Optional[Union[bool, Bool]] = None
    mandatoryValue: Optional[Union[bool, Bool]] = None
    originType: Optional[Union[str, "OriginType"]] = None
    originSource: Optional[Union[str, "OriginSource"]] = None
    comparator: Optional[Union[str, "Comparator"]] = None
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

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.relationship is not None and not isinstance(self.relationship, RelationShip):
            self.relationship = RelationShip(**as_dict(self.relationship))

        if self.dataType is not None and not isinstance(self.dataType, SDTMVariableDataType):
            self.dataType = SDTMVariableDataType(self.dataType)

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

        if self.originType is not None and not isinstance(self.originType, OriginType):
            self.originType = OriginType(self.originType)

        if self.originSource is not None and not isinstance(self.originSource, OriginSource):
            self.originSource = OriginSource(self.originSource)

        if self.comparator is not None and not isinstance(self.comparator, Comparator):
            self.comparator = Comparator(self.comparator)

        if self.vlmTarget is not None and not isinstance(self.vlmTarget, Bool):
            self.vlmTarget = Bool(self.vlmTarget)

        super().__post_init__(**kwargs)


@dataclass
class RelationShip(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/RelationShip")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "RelationShip"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/RelationShip")

    subject: str = None
    linkingPhrase: Union[str, "LinkingPhrase"] = None
    predicateTerm: Union[str, "PredicateTerm"] = None
    object: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.subject):
            self.MissingRequiredField("subject")
        if not isinstance(self.subject, str):
            self.subject = str(self.subject)

        if self._is_empty(self.linkingPhrase):
            self.MissingRequiredField("linkingPhrase")
        if not isinstance(self.linkingPhrase, LinkingPhrase):
            self.linkingPhrase = LinkingPhrase(self.linkingPhrase)

        if self._is_empty(self.predicateTerm):
            self.MissingRequiredField("predicateTerm")
        if not isinstance(self.predicateTerm, PredicateTerm):
            self.predicateTerm = PredicateTerm(self.predicateTerm)

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CodeListTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CodeListTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CodeListTerm")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SubsetCodeList")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SubsetCodeList"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SubsetCodeList")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/AssignedTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AssignedTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/AssignedTerm")

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
class SDTMDatasetSpecializationPackageType(EnumDefinitionImpl):

    sdtm = PermissibleValue(text="sdtm")

    _defn = EnumDefinition(
        name="SDTMDatasetSpecializationPackageType",
    )

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
        setattr(cls, "is the role of the assessor who performed the test in",
                PermissibleValue(text="is the role of the assessor who performed the test in") )
        setattr(cls, "is the epoch of the performance of the test in",
                PermissibleValue(text="is the epoch of the performance of the test in") )
        setattr(cls, "identifies overall response supported by tumor assessments identified by",
                PermissibleValue(text="identifies overall response supported by tumor assessments identified by") )
        setattr(cls, "identifies the image from the procedure in",
                PermissibleValue(text="identifies the image from the procedure in") )
        setattr(cls, "identifies the tumor found by the test in",
                PermissibleValue(text="identifies the tumor found by the test in") )
        setattr(cls, "groups tumor assessments used in overall response identified by",
                PermissibleValue(text="groups tumor assessments used in overall response identified by") )
        setattr(cls, "is the identifier for the source data used in the performance of the test in",
                PermissibleValue(text="is the identifier for the source data used in the performance of the test in") )
        setattr(cls, "associates the tumor identified in",
                PermissibleValue(text="associates the tumor identified in") )
        setattr(cls, "indicates the previous irradiation status of the tumor identified by",
                PermissibleValue(text="indicates the previous irradiation status of the tumor identified by") )
        setattr(cls, "indicates the progression status of the previous irradiated tumor identified by",
                PermissibleValue(text="indicates the progression status of the previous irradiated tumor identified by") )
        setattr(cls, "further describes the test in",
                PermissibleValue(text="further describes the test in") )
        setattr(cls, "is a dictionary-derived term for the value in",
                PermissibleValue(text="is a dictionary-derived term for the value in") )
        setattr(cls, "is original text for",
                PermissibleValue(text="is original text for") )

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
    PERFORMED = PermissibleValue(text="PERFORMED")
    IS_EPOCH_OF = PermissibleValue(text="IS_EPOCH_OF")
    GROUPS_BY = PermissibleValue(text="GROUPS_BY")
    IDENTIFIES_PRODUCT_IN = PermissibleValue(text="IDENTIFIES_PRODUCT_IN")
    IDENTIFIES_TUMOR_IN = PermissibleValue(text="IDENTIFIES_TUMOR_IN")
    IS_ORIGINAL_TEXT_FOR = PermissibleValue(text="IS_ORIGINAL_TEXT_FOR")
    IS_DERIVED_FROM = PermissibleValue(text="IS_DERIVED_FROM")

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

slots.packageDate = Slot(uri=DEFAULT_.packageDate, name="packageDate", curie=DEFAULT_.curie('packageDate'),
                   model_uri=DEFAULT_.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=DEFAULT_.packageType, name="packageType", curie=DEFAULT_.curie('packageType'),
                   model_uri=DEFAULT_.packageType, domain=None, range=Union[str, "SDTMDatasetSpecializationPackageType"])

slots.domain = Slot(uri=DEFAULT_.domain, name="domain", curie=DEFAULT_.curie('domain'),
                   model_uri=DEFAULT_.domain, domain=None, range=str)

slots.datasetSpecializationId = Slot(uri=DEFAULT_.datasetSpecializationId, name="datasetSpecializationId", curie=DEFAULT_.curie('datasetSpecializationId'),
                   model_uri=DEFAULT_.datasetSpecializationId, domain=None, range=URIRef)

slots.source = Slot(uri=DEFAULT_.source, name="source", curie=DEFAULT_.curie('source'),
                   model_uri=DEFAULT_.source, domain=None, range=str)

slots.shortName = Slot(uri=DEFAULT_.shortName, name="shortName", curie=DEFAULT_.curie('shortName'),
                   model_uri=DEFAULT_.shortName, domain=None, range=str)

slots.sdtmigStartVersion = Slot(uri=DEFAULT_.sdtmigStartVersion, name="sdtmigStartVersion", curie=DEFAULT_.curie('sdtmigStartVersion'),
                   model_uri=DEFAULT_.sdtmigStartVersion, domain=None, range=str)

slots.sdtmigEndVersion = Slot(uri=DEFAULT_.sdtmigEndVersion, name="sdtmigEndVersion", curie=DEFAULT_.curie('sdtmigEndVersion'),
                   model_uri=DEFAULT_.sdtmigEndVersion, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=DEFAULT_.biomedicalConceptId, name="biomedicalConceptId", curie=DEFAULT_.curie('biomedicalConceptId'),
                   model_uri=DEFAULT_.biomedicalConceptId, domain=None, range=Optional[str])

slots.variables = Slot(uri=DEFAULT_.variables, name="variables", curie=DEFAULT_.curie('variables'),
                   model_uri=DEFAULT_.variables, domain=None, range=Optional[Union[Dict[Union[str, SDTMVariableName], Union[dict, SDTMVariable]], List[Union[dict, SDTMVariable]]]])

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=URIRef)

slots.dataElementConceptId = Slot(uri=DEFAULT_.dataElementConceptId, name="dataElementConceptId", curie=DEFAULT_.curie('dataElementConceptId'),
                   model_uri=DEFAULT_.dataElementConceptId, domain=None, range=Optional[str])

slots.isNonStandard = Slot(uri=DEFAULT_.isNonStandard, name="isNonStandard", curie=DEFAULT_.curie('isNonStandard'),
                   model_uri=DEFAULT_.isNonStandard, domain=None, range=Optional[Union[bool, Bool]])

slots.codelist = Slot(uri=DEFAULT_.codelist, name="codelist", curie=DEFAULT_.curie('codelist'),
                   model_uri=DEFAULT_.codelist, domain=None, range=Optional[Union[dict, CodeList]])

slots.subsetCodelist = Slot(uri=DEFAULT_.subsetCodelist, name="subsetCodelist", curie=DEFAULT_.curie('subsetCodelist'),
                   model_uri=DEFAULT_.subsetCodelist, domain=None, range=Optional[str])

slots.conceptId = Slot(uri=DEFAULT_.conceptId, name="conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.conceptId, domain=None, range=URIRef)

slots.href = Slot(uri=DEFAULT_.href, name="href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.href, domain=None, range=Optional[Union[str, URI]])

slots.submissionValue = Slot(uri=DEFAULT_.submissionValue, name="submissionValue", curie=DEFAULT_.curie('submissionValue'),
                   model_uri=DEFAULT_.submissionValue, domain=None, range=str)

slots.parentCodelist = Slot(uri=DEFAULT_.parentCodelist, name="parentCodelist", curie=DEFAULT_.curie('parentCodelist'),
                   model_uri=DEFAULT_.parentCodelist, domain=None, range=str)

slots.subsetShortName = Slot(uri=DEFAULT_.subsetShortName, name="subsetShortName", curie=DEFAULT_.curie('subsetShortName'),
                   model_uri=DEFAULT_.subsetShortName, domain=None, range=str)

slots.subsetLabel = Slot(uri=DEFAULT_.subsetLabel, name="subsetLabel", curie=DEFAULT_.curie('subsetLabel'),
                   model_uri=DEFAULT_.subsetLabel, domain=None, range=str)

slots.codelistTerm = Slot(uri=DEFAULT_.codelistTerm, name="codelistTerm", curie=DEFAULT_.curie('codelistTerm'),
                   model_uri=DEFAULT_.codelistTerm, domain=None, range=Union[Union[dict, CodeListTerm], List[Union[dict, CodeListTerm]]])

slots.termId = Slot(uri=DEFAULT_.termId, name="termId", curie=DEFAULT_.curie('termId'),
                   model_uri=DEFAULT_.termId, domain=None, range=str)

slots.termValue = Slot(uri=DEFAULT_.termValue, name="termValue", curie=DEFAULT_.curie('termValue'),
                   model_uri=DEFAULT_.termValue, domain=None, range=str)

slots.valueList = Slot(uri=DEFAULT_.valueList, name="valueList", curie=DEFAULT_.curie('valueList'),
                   model_uri=DEFAULT_.valueList, domain=None, range=Optional[Union[str, List[str]]])

slots.assignedTerm = Slot(uri=DEFAULT_.assignedTerm, name="assignedTerm", curie=DEFAULT_.curie('assignedTerm'),
                   model_uri=DEFAULT_.assignedTerm, domain=None, range=Optional[Union[dict, AssignedTerm]])

slots.role = Slot(uri=DEFAULT_.role, name="role", curie=DEFAULT_.curie('role'),
                   model_uri=DEFAULT_.role, domain=None, range=Optional[str])

slots.relationship = Slot(uri=DEFAULT_.relationship, name="relationship", curie=DEFAULT_.curie('relationship'),
                   model_uri=DEFAULT_.relationship, domain=None, range=Optional[Union[dict, RelationShip]])

slots.subject = Slot(uri=DEFAULT_.subject, name="subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.subject, domain=None, range=str)

slots.linkingPhrase = Slot(uri=DEFAULT_.linkingPhrase, name="linkingPhrase", curie=DEFAULT_.curie('linkingPhrase'),
                   model_uri=DEFAULT_.linkingPhrase, domain=None, range=Union[str, "LinkingPhrase"])

slots.predicateTerm = Slot(uri=DEFAULT_.predicateTerm, name="predicateTerm", curie=DEFAULT_.curie('predicateTerm'),
                   model_uri=DEFAULT_.predicateTerm, domain=None, range=Union[str, "PredicateTerm"])

slots.object = Slot(uri=DEFAULT_.object, name="object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.object, domain=None, range=str)

slots.dataType = Slot(uri=DEFAULT_.dataType, name="dataType", curie=DEFAULT_.curie('dataType'),
                   model_uri=DEFAULT_.dataType, domain=None, range=Optional[Union[str, "SDTMVariableDataType"]])

slots.length = Slot(uri=DEFAULT_.length, name="length", curie=DEFAULT_.curie('length'),
                   model_uri=DEFAULT_.length, domain=None, range=Optional[int])

slots.format = Slot(uri=DEFAULT_.format, name="format", curie=DEFAULT_.curie('format'),
                   model_uri=DEFAULT_.format, domain=None, range=Optional[str])

slots.significantDigits = Slot(uri=DEFAULT_.significantDigits, name="significantDigits", curie=DEFAULT_.curie('significantDigits'),
                   model_uri=DEFAULT_.significantDigits, domain=None, range=Optional[int])

slots.mandatoryVariable = Slot(uri=DEFAULT_.mandatoryVariable, name="mandatoryVariable", curie=DEFAULT_.curie('mandatoryVariable'),
                   model_uri=DEFAULT_.mandatoryVariable, domain=None, range=Optional[Union[bool, Bool]])

slots.mandatoryValue = Slot(uri=DEFAULT_.mandatoryValue, name="mandatoryValue", curie=DEFAULT_.curie('mandatoryValue'),
                   model_uri=DEFAULT_.mandatoryValue, domain=None, range=Optional[Union[bool, Bool]])

slots.originType = Slot(uri=DEFAULT_.originType, name="originType", curie=DEFAULT_.curie('originType'),
                   model_uri=DEFAULT_.originType, domain=None, range=Optional[Union[str, "OriginType"]])

slots.originSource = Slot(uri=DEFAULT_.originSource, name="originSource", curie=DEFAULT_.curie('originSource'),
                   model_uri=DEFAULT_.originSource, domain=None, range=Optional[Union[str, "OriginSource"]])

slots.comparator = Slot(uri=DEFAULT_.comparator, name="comparator", curie=DEFAULT_.curie('comparator'),
                   model_uri=DEFAULT_.comparator, domain=None, range=Optional[Union[str, "Comparator"]])

slots.vlmTarget = Slot(uri=DEFAULT_.vlmTarget, name="vlmTarget", curie=DEFAULT_.curie('vlmTarget'),
                   model_uri=DEFAULT_.vlmTarget, domain=None, range=Optional[Union[bool, Bool]])

slots.assignedTerm__conceptId = Slot(uri=DEFAULT_.conceptId, name="assignedTerm__conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.assignedTerm__conceptId, domain=None, range=Optional[str])

slots.assignedTerm__value = Slot(uri=DEFAULT_.value, name="assignedTerm__value", curie=DEFAULT_.curie('value'),
                   model_uri=DEFAULT_.assignedTerm__value, domain=None, range=str)
