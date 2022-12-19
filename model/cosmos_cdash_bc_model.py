# Auto generated from cosmos_cdash_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-19T16:23:17
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
from linkml_runtime.linkml_model.types import Date, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://www.cdisc.org/cosmos/1-0/')


# Types

# Class references
class CDASHGroupDatasetSpecializationId(extended_str):
    pass


class CDASHVariableName(extended_str):
    pass


class CodeListConceptId(extended_str):
    pass


@dataclass
class CDASHGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CDASHGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CDASHGroup"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CDASHGroup")

    datasetSpecializationId: Union[str, CDASHGroupDatasetSpecializationId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "CDASHDatasetSpecializationPackageType"] = None
    domain: str = None
    shortName: str = None
    cdashigStartVersion: str = None
    scenario: Optional[Union[str, "CDASHScenario"]] = None
    cdashigEndVersion: Optional[str] = None
    biomedicalConceptId: Optional[str] = None
    variables: Optional[Union[Dict[Union[str, CDASHVariableName], Union[dict, "CDASHVariable"]], List[Union[dict, "CDASHVariable"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.datasetSpecializationId):
            self.MissingRequiredField("datasetSpecializationId")
        if not isinstance(self.datasetSpecializationId, CDASHGroupDatasetSpecializationId):
            self.datasetSpecializationId = CDASHGroupDatasetSpecializationId(self.datasetSpecializationId)

        if self._is_empty(self.packageDate):
            self.MissingRequiredField("packageDate")
        if not isinstance(self.packageDate, XSDDate):
            self.packageDate = XSDDate(self.packageDate)

        if self._is_empty(self.packageType):
            self.MissingRequiredField("packageType")
        if not isinstance(self.packageType, CDASHDatasetSpecializationPackageType):
            self.packageType = CDASHDatasetSpecializationPackageType(self.packageType)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.cdashigStartVersion):
            self.MissingRequiredField("cdashigStartVersion")
        if not isinstance(self.cdashigStartVersion, str):
            self.cdashigStartVersion = str(self.cdashigStartVersion)

        if self.scenario is not None and not isinstance(self.scenario, CDASHScenario):
            self.scenario = CDASHScenario(self.scenario)

        if self.cdashigEndVersion is not None and not isinstance(self.cdashigEndVersion, str):
            self.cdashigEndVersion = str(self.cdashigEndVersion)

        if self.biomedicalConceptId is not None and not isinstance(self.biomedicalConceptId, str):
            self.biomedicalConceptId = str(self.biomedicalConceptId)

        self._normalize_inlined_as_list(slot_name="variables", slot_type=CDASHVariable, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class CDASHVariable(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CDASHVariable")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CDASHVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/CDASHVariable")

    name: Union[str, CDASHVariableName] = None
    cdashigCore: Union[str, "CDASHIGCore"] = None
    questionText: Optional[str] = None
    dataElementConceptId: Optional[str] = None
    prompt: Optional[str] = None
    codelist: Optional[Union[dict, "CodeList"]] = None
    subsetCodelist: Optional[str] = None
    valueList: Optional[Union[str, List[str]]] = empty_list()
    valueDisplayList: Optional[Union[str, List[str]]] = empty_list()
    prepopulatedValue: Optional[str] = None
    relationship: Optional[Union[dict, "RelationShip"]] = None
    dataType: Optional[Union[str, "CDASHVariableDataType"]] = None
    length: Optional[int] = None
    significantDigits: Optional[int] = None
    sdtmTarget: Optional[Union[dict, "SDTMTarget"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CDASHVariableName):
            self.name = CDASHVariableName(self.name)

        if self._is_empty(self.cdashigCore):
            self.MissingRequiredField("cdashigCore")
        if not isinstance(self.cdashigCore, CDASHIGCore):
            self.cdashigCore = CDASHIGCore(self.cdashigCore)

        if self.questionText is not None and not isinstance(self.questionText, str):
            self.questionText = str(self.questionText)

        if self.dataElementConceptId is not None and not isinstance(self.dataElementConceptId, str):
            self.dataElementConceptId = str(self.dataElementConceptId)

        if self.prompt is not None and not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        if self.codelist is not None and not isinstance(self.codelist, CodeList):
            self.codelist = CodeList(**as_dict(self.codelist))

        if self.subsetCodelist is not None and not isinstance(self.subsetCodelist, str):
            self.subsetCodelist = str(self.subsetCodelist)

        if not isinstance(self.valueList, list):
            self.valueList = [self.valueList] if self.valueList is not None else []
        self.valueList = [v if isinstance(v, str) else str(v) for v in self.valueList]

        if not isinstance(self.valueDisplayList, list):
            self.valueDisplayList = [self.valueDisplayList] if self.valueDisplayList is not None else []
        self.valueDisplayList = [v if isinstance(v, str) else str(v) for v in self.valueDisplayList]

        if self.prepopulatedValue is not None and not isinstance(self.prepopulatedValue, str):
            self.prepopulatedValue = str(self.prepopulatedValue)

        if self.relationship is not None and not isinstance(self.relationship, RelationShip):
            self.relationship = RelationShip(**as_dict(self.relationship))

        if self.dataType is not None and not isinstance(self.dataType, CDASHVariableDataType):
            self.dataType = CDASHVariableDataType(self.dataType)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.significantDigits is not None and not isinstance(self.significantDigits, int):
            self.significantDigits = int(self.significantDigits)

        if self.sdtmTarget is not None and not isinstance(self.sdtmTarget, SDTMTarget):
            self.sdtmTarget = SDTMTarget(**as_dict(self.sdtmTarget))

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
class SDTMTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMTarget")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SDTMTarget"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SDTMTarget")

    sdtmTargetVariable: str = None
    sdtmTargetMapping: str = None
    sdtmTargetGroup: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sdtmTargetVariable):
            self.MissingRequiredField("sdtmTargetVariable")
        if not isinstance(self.sdtmTargetVariable, str):
            self.sdtmTargetVariable = str(self.sdtmTargetVariable)

        if self._is_empty(self.sdtmTargetMapping):
            self.MissingRequiredField("sdtmTargetMapping")
        if not isinstance(self.sdtmTargetMapping, str):
            self.sdtmTargetMapping = str(self.sdtmTargetMapping)

        if self._is_empty(self.sdtmTargetGroup):
            self.MissingRequiredField("sdtmTargetGroup")
        if not isinstance(self.sdtmTargetGroup, str):
            self.sdtmTargetGroup = str(self.sdtmTargetGroup)

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


# Enumerations
class CDASHDatasetSpecializationPackageType(EnumDefinitionImpl):

    cdash = PermissibleValue(text="cdash")

    _defn = EnumDefinition(
        name="CDASHDatasetSpecializationPackageType",
    )

class CDASHScenario(EnumDefinitionImpl):

    Horizontal = PermissibleValue(text="Horizontal")
    Vertical = PermissibleValue(text="Vertical")

    _defn = EnumDefinition(
        name="CDASHScenario",
    )

class CDASHIGCore(EnumDefinitionImpl):

    HR = PermissibleValue(text="HR")
    O = PermissibleValue(text="O")

    _defn = EnumDefinition(
        name="CDASHIGCore",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "R/C",
                PermissibleValue(text="R/C") )

class CDASHVariableDataType(EnumDefinitionImpl):

    boolean = PermissibleValue(text="boolean")
    float = PermissibleValue(text="float")
    integer = PermissibleValue(text="integer")
    text = PermissibleValue(text="text")

    _defn = EnumDefinition(
        name="CDASHVariableDataType",
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

slots.packageDate = Slot(uri=DEFAULT_.packageDate, name="packageDate", curie=DEFAULT_.curie('packageDate'),
                   model_uri=DEFAULT_.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=DEFAULT_.packageType, name="packageType", curie=DEFAULT_.curie('packageType'),
                   model_uri=DEFAULT_.packageType, domain=None, range=Union[str, "CDASHDatasetSpecializationPackageType"])

slots.domain = Slot(uri=DEFAULT_.domain, name="domain", curie=DEFAULT_.curie('domain'),
                   model_uri=DEFAULT_.domain, domain=None, range=str)

slots.datasetSpecializationId = Slot(uri=DEFAULT_.datasetSpecializationId, name="datasetSpecializationId", curie=DEFAULT_.curie('datasetSpecializationId'),
                   model_uri=DEFAULT_.datasetSpecializationId, domain=None, range=URIRef)

slots.shortName = Slot(uri=DEFAULT_.shortName, name="shortName", curie=DEFAULT_.curie('shortName'),
                   model_uri=DEFAULT_.shortName, domain=None, range=str)

slots.scenario = Slot(uri=DEFAULT_.scenario, name="scenario", curie=DEFAULT_.curie('scenario'),
                   model_uri=DEFAULT_.scenario, domain=None, range=Optional[Union[str, "CDASHScenario"]])

slots.cdashigStartVersion = Slot(uri=DEFAULT_.cdashigStartVersion, name="cdashigStartVersion", curie=DEFAULT_.curie('cdashigStartVersion'),
                   model_uri=DEFAULT_.cdashigStartVersion, domain=None, range=str)

slots.cdashigEndVersion = Slot(uri=DEFAULT_.cdashigEndVersion, name="cdashigEndVersion", curie=DEFAULT_.curie('cdashigEndVersion'),
                   model_uri=DEFAULT_.cdashigEndVersion, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=DEFAULT_.biomedicalConceptId, name="biomedicalConceptId", curie=DEFAULT_.curie('biomedicalConceptId'),
                   model_uri=DEFAULT_.biomedicalConceptId, domain=None, range=Optional[str])

slots.variables = Slot(uri=DEFAULT_.variables, name="variables", curie=DEFAULT_.curie('variables'),
                   model_uri=DEFAULT_.variables, domain=None, range=Optional[Union[Dict[Union[str, CDASHVariableName], Union[dict, CDASHVariable]], List[Union[dict, CDASHVariable]]]])

slots.name = Slot(uri=DEFAULT_.name, name="name", curie=DEFAULT_.curie('name'),
                   model_uri=DEFAULT_.name, domain=None, range=URIRef)

slots.dataElementConceptId = Slot(uri=DEFAULT_.dataElementConceptId, name="dataElementConceptId", curie=DEFAULT_.curie('dataElementConceptId'),
                   model_uri=DEFAULT_.dataElementConceptId, domain=None, range=Optional[str])

slots.questionText = Slot(uri=DEFAULT_.questionText, name="questionText", curie=DEFAULT_.curie('questionText'),
                   model_uri=DEFAULT_.questionText, domain=None, range=Optional[str])

slots.prompt = Slot(uri=DEFAULT_.prompt, name="prompt", curie=DEFAULT_.curie('prompt'),
                   model_uri=DEFAULT_.prompt, domain=None, range=Optional[str])

slots.codelist = Slot(uri=DEFAULT_.codelist, name="codelist", curie=DEFAULT_.curie('codelist'),
                   model_uri=DEFAULT_.codelist, domain=None, range=Optional[Union[dict, CodeList]])

slots.subsetCodelist = Slot(uri=DEFAULT_.subsetCodelist, name="subsetCodelist", curie=DEFAULT_.curie('subsetCodelist'),
                   model_uri=DEFAULT_.subsetCodelist, domain=None, range=Optional[str])

slots.prepopulatedValue = Slot(uri=DEFAULT_.prepopulatedValue, name="prepopulatedValue", curie=DEFAULT_.curie('prepopulatedValue'),
                   model_uri=DEFAULT_.prepopulatedValue, domain=None, range=Optional[str])

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

slots.valueDisplayList = Slot(uri=DEFAULT_.valueDisplayList, name="valueDisplayList", curie=DEFAULT_.curie('valueDisplayList'),
                   model_uri=DEFAULT_.valueDisplayList, domain=None, range=Optional[Union[str, List[str]]])

slots.sdtmTarget = Slot(uri=DEFAULT_.sdtmTarget, name="sdtmTarget", curie=DEFAULT_.curie('sdtmTarget'),
                   model_uri=DEFAULT_.sdtmTarget, domain=None, range=Optional[Union[dict, SDTMTarget]])

slots.sdtmTargetVariable = Slot(uri=DEFAULT_.sdtmTargetVariable, name="sdtmTargetVariable", curie=DEFAULT_.curie('sdtmTargetVariable'),
                   model_uri=DEFAULT_.sdtmTargetVariable, domain=None, range=str)

slots.sdtmTargetMapping = Slot(uri=DEFAULT_.sdtmTargetMapping, name="sdtmTargetMapping", curie=DEFAULT_.curie('sdtmTargetMapping'),
                   model_uri=DEFAULT_.sdtmTargetMapping, domain=None, range=str)

slots.sdtmTargetGroup = Slot(uri=DEFAULT_.sdtmTargetGroup, name="sdtmTargetGroup", curie=DEFAULT_.curie('sdtmTargetGroup'),
                   model_uri=DEFAULT_.sdtmTargetGroup, domain=None, range=str)

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
                   model_uri=DEFAULT_.dataType, domain=None, range=Optional[Union[str, "CDASHVariableDataType"]])

slots.length = Slot(uri=DEFAULT_.length, name="length", curie=DEFAULT_.curie('length'),
                   model_uri=DEFAULT_.length, domain=None, range=Optional[int])

slots.significantDigits = Slot(uri=DEFAULT_.significantDigits, name="significantDigits", curie=DEFAULT_.curie('significantDigits'),
                   model_uri=DEFAULT_.significantDigits, domain=None, range=Optional[int])

slots.cdashigCore = Slot(uri=DEFAULT_.cdashigCore, name="cdashigCore", curie=DEFAULT_.curie('cdashigCore'),
                   model_uri=DEFAULT_.cdashigCore, domain=None, range=Union[str, "CDASHIGCore"])
