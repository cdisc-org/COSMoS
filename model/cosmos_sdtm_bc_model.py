# Auto generated from cosmos_sdtm_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-23T16:49:57
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
class SdtmVariableVariableId(extended_str):
    pass


class CodeListConceptId(extended_str):
    pass


class CodeListTermConceptId(extended_str):
    pass


class AssignedTermConceptId(extended_str):
    pass


@dataclass
class SdtmGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SdtmGroup")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SdtmGroup"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SdtmGroup")

    packageDate: Union[str, XSDDate] = None
    domain: str = None
    shortName: str = None
    vlmGroupId: str = None
    vlmSource: str = None
    sdtmigStartVersion: str = None
    sdtmigEndVersion: Optional[str] = None
    biomedicalConceptId: Optional[str] = None
    SdtmVariables: Optional[Union[Dict[Union[str, SdtmVariableVariableId], Union[dict, "SdtmVariable"]], List[Union[dict, "SdtmVariable"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.packageDate):
            self.MissingRequiredField("packageDate")
        if not isinstance(self.packageDate, XSDDate):
            self.packageDate = XSDDate(self.packageDate)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.vlmGroupId):
            self.MissingRequiredField("vlmGroupId")
        if not isinstance(self.vlmGroupId, str):
            self.vlmGroupId = str(self.vlmGroupId)

        if self._is_empty(self.vlmSource):
            self.MissingRequiredField("vlmSource")
        if not isinstance(self.vlmSource, str):
            self.vlmSource = str(self.vlmSource)

        if self._is_empty(self.sdtmigStartVersion):
            self.MissingRequiredField("sdtmigStartVersion")
        if not isinstance(self.sdtmigStartVersion, str):
            self.sdtmigStartVersion = str(self.sdtmigStartVersion)

        if self.sdtmigEndVersion is not None and not isinstance(self.sdtmigEndVersion, str):
            self.sdtmigEndVersion = str(self.sdtmigEndVersion)

        if self.biomedicalConceptId is not None and not isinstance(self.biomedicalConceptId, str):
            self.biomedicalConceptId = str(self.biomedicalConceptId)

        self._normalize_inlined_as_list(slot_name="SdtmVariables", slot_type=SdtmVariable, key_name="variableId", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class SdtmVariable(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SdtmVariable")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SdtmVariable"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/SdtmVariable")

    variableId: Union[str, SdtmVariableVariableId] = None
    href: Optional[Union[str, URI]] = None
    variableConceptId: Optional[str] = None
    nsvFlag: Optional[Union[bool, Bool]] = None
    codelist: Optional[Union[str, CodeListConceptId]] = None
    subsetCodelist: Optional[str] = None
    valuelist: Optional[Union[str, List[str]]] = empty_list()
    assignedTerm: Optional[Union[str, AssignedTermConceptId]] = None
    role: Optional[str] = None
    relationship: Optional[Union[dict, "RelationShip"]] = None
    datatype: Optional[Union[str, "SdtmVariableDataType"]] = None
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
        if self._is_empty(self.variableId):
            self.MissingRequiredField("variableId")
        if not isinstance(self.variableId, SdtmVariableVariableId):
            self.variableId = SdtmVariableVariableId(self.variableId)

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        if self.variableConceptId is not None and not isinstance(self.variableConceptId, str):
            self.variableConceptId = str(self.variableConceptId)

        if self.nsvFlag is not None and not isinstance(self.nsvFlag, Bool):
            self.nsvFlag = Bool(self.nsvFlag)

        if self.codelist is not None and not isinstance(self.codelist, CodeListConceptId):
            self.codelist = CodeListConceptId(self.codelist)

        if self.subsetCodelist is not None and not isinstance(self.subsetCodelist, str):
            self.subsetCodelist = str(self.subsetCodelist)

        if not isinstance(self.valuelist, list):
            self.valuelist = [self.valuelist] if self.valuelist is not None else []
        self.valuelist = [v if isinstance(v, str) else str(v) for v in self.valuelist]

        if self.assignedTerm is not None and not isinstance(self.assignedTerm, AssignedTermConceptId):
            self.assignedTerm = AssignedTermConceptId(self.assignedTerm)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.relationship is not None and not isinstance(self.relationship, RelationShip):
            self.relationship = RelationShip(**as_dict(self.relationship))

        if self.datatype is not None and not isinstance(self.datatype, SdtmVariableDataType):
            self.datatype = SdtmVariableDataType(self.datatype)

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

    conceptId: Union[str, CodeListTermConceptId] = None
    submissionValue: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.conceptId):
            self.MissingRequiredField("conceptId")
        if not isinstance(self.conceptId, CodeListTermConceptId):
            self.conceptId = CodeListTermConceptId(self.conceptId)

        if self._is_empty(self.submissionValue):
            self.MissingRequiredField("submissionValue")
        if not isinstance(self.submissionValue, str):
            self.submissionValue = str(self.submissionValue)

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
    codelistTerm: Union[Dict[Union[str, CodeListTermConceptId], Union[dict, CodeListTerm]], List[Union[dict, CodeListTerm]]] = empty_dict()

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
        self._normalize_inlined_as_list(slot_name="codelistTerm", slot_type=CodeListTerm, key_name="conceptId", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class AssignedTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/AssignedTerm")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AssignedTerm"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/AssignedTerm")

    conceptId: Union[str, AssignedTermConceptId] = None
    submissionValue: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.conceptId):
            self.MissingRequiredField("conceptId")
        if not isinstance(self.conceptId, AssignedTermConceptId):
            self.conceptId = AssignedTermConceptId(self.conceptId)

        if self._is_empty(self.submissionValue):
            self.MissingRequiredField("submissionValue")
        if not isinstance(self.submissionValue, str):
            self.submissionValue = str(self.submissionValue)

        super().__post_init__(**kwargs)


# Enumerations
class SdtmVariableDataType(EnumDefinitionImpl):

    float = PermissibleValue(text="float")
    integer = PermissibleValue(text="integer")
    text = PermissibleValue(text="text")

    _defn = EnumDefinition(
        name="SdtmVariableDataType",
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

slots.conceptId = Slot(uri=DEFAULT_.conceptId, name="conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.conceptId, domain=None, range=URIRef)

slots.variableId = Slot(uri=DEFAULT_.variableId, name="variableId", curie=DEFAULT_.curie('variableId'),
                   model_uri=DEFAULT_.variableId, domain=None, range=URIRef)

slots.href = Slot(uri=DEFAULT_.href, name="href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.href, domain=None, range=Optional[Union[str, URI]])

slots.variableConceptId = Slot(uri=DEFAULT_.variableConceptId, name="variableConceptId", curie=DEFAULT_.curie('variableConceptId'),
                   model_uri=DEFAULT_.variableConceptId, domain=None, range=Optional[str])

slots.packageDate = Slot(uri=DEFAULT_.packageDate, name="packageDate", curie=DEFAULT_.curie('packageDate'),
                   model_uri=DEFAULT_.packageDate, domain=None, range=Union[str, XSDDate])

slots.domain = Slot(uri=DEFAULT_.domain, name="domain", curie=DEFAULT_.curie('domain'),
                   model_uri=DEFAULT_.domain, domain=None, range=str)

slots.vlmGroupId = Slot(uri=DEFAULT_.vlmGroupId, name="vlmGroupId", curie=DEFAULT_.curie('vlmGroupId'),
                   model_uri=DEFAULT_.vlmGroupId, domain=None, range=str)

slots.vlmSource = Slot(uri=DEFAULT_.vlmSource, name="vlmSource", curie=DEFAULT_.curie('vlmSource'),
                   model_uri=DEFAULT_.vlmSource, domain=None, range=str)

slots.shortName = Slot(uri=DEFAULT_.shortName, name="shortName", curie=DEFAULT_.curie('shortName'),
                   model_uri=DEFAULT_.shortName, domain=None, range=str)

slots.sdtmigStartVersion = Slot(uri=DEFAULT_.sdtmigStartVersion, name="sdtmigStartVersion", curie=DEFAULT_.curie('sdtmigStartVersion'),
                   model_uri=DEFAULT_.sdtmigStartVersion, domain=None, range=str)

slots.sdtmigEndVersion = Slot(uri=DEFAULT_.sdtmigEndVersion, name="sdtmigEndVersion", curie=DEFAULT_.curie('sdtmigEndVersion'),
                   model_uri=DEFAULT_.sdtmigEndVersion, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=DEFAULT_.biomedicalConceptId, name="biomedicalConceptId", curie=DEFAULT_.curie('biomedicalConceptId'),
                   model_uri=DEFAULT_.biomedicalConceptId, domain=None, range=Optional[str])

slots.SdtmVariables = Slot(uri=DEFAULT_.SdtmVariables, name="SdtmVariables", curie=DEFAULT_.curie('SdtmVariables'),
                   model_uri=DEFAULT_.SdtmVariables, domain=None, range=Optional[Union[Dict[Union[str, SdtmVariableVariableId], Union[dict, SdtmVariable]], List[Union[dict, SdtmVariable]]]])

slots.nsvFlag = Slot(uri=DEFAULT_.nsvFlag, name="nsvFlag", curie=DEFAULT_.curie('nsvFlag'),
                   model_uri=DEFAULT_.nsvFlag, domain=None, range=Optional[Union[bool, Bool]])

slots.codelist = Slot(uri=DEFAULT_.codelist, name="codelist", curie=DEFAULT_.curie('codelist'),
                   model_uri=DEFAULT_.codelist, domain=None, range=Optional[Union[str, CodeListConceptId]])

slots.subsetCodelist = Slot(uri=DEFAULT_.subsetCodelist, name="subsetCodelist", curie=DEFAULT_.curie('subsetCodelist'),
                   model_uri=DEFAULT_.subsetCodelist, domain=None, range=Optional[str])

slots.submissionValue = Slot(uri=DEFAULT_.submissionValue, name="submissionValue", curie=DEFAULT_.curie('submissionValue'),
                   model_uri=DEFAULT_.submissionValue, domain=None, range=str)

slots.parentCodelist = Slot(uri=DEFAULT_.parentCodelist, name="parentCodelist", curie=DEFAULT_.curie('parentCodelist'),
                   model_uri=DEFAULT_.parentCodelist, domain=None, range=str)

slots.subsetShortName = Slot(uri=DEFAULT_.subsetShortName, name="subsetShortName", curie=DEFAULT_.curie('subsetShortName'),
                   model_uri=DEFAULT_.subsetShortName, domain=None, range=str)

slots.subsetLabel = Slot(uri=DEFAULT_.subsetLabel, name="subsetLabel", curie=DEFAULT_.curie('subsetLabel'),
                   model_uri=DEFAULT_.subsetLabel, domain=None, range=str)

slots.codelistTerm = Slot(uri=DEFAULT_.codelistTerm, name="codelistTerm", curie=DEFAULT_.curie('codelistTerm'),
                   model_uri=DEFAULT_.codelistTerm, domain=None, range=Union[Dict[Union[str, CodeListTermConceptId], Union[dict, CodeListTerm]], List[Union[dict, CodeListTerm]]])

slots.valuelist = Slot(uri=DEFAULT_.valuelist, name="valuelist", curie=DEFAULT_.curie('valuelist'),
                   model_uri=DEFAULT_.valuelist, domain=None, range=Optional[Union[str, List[str]]])

slots.assignedTerm = Slot(uri=DEFAULT_.assignedTerm, name="assignedTerm", curie=DEFAULT_.curie('assignedTerm'),
                   model_uri=DEFAULT_.assignedTerm, domain=None, range=Optional[Union[str, AssignedTermConceptId]])

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

slots.datatype = Slot(uri=DEFAULT_.datatype, name="datatype", curie=DEFAULT_.curie('datatype'),
                   model_uri=DEFAULT_.datatype, domain=None, range=Optional[Union[str, "SdtmVariableDataType"]])

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

slots.SdtmVariable_href = Slot(uri=DEFAULT_.href, name="SdtmVariable_href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.SdtmVariable_href, domain=SdtmVariable, range=Optional[Union[str, URI]])

slots.CodeList_conceptId = Slot(uri=DEFAULT_.conceptId, name="CodeList_conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.CodeList_conceptId, domain=CodeList, range=Union[str, CodeListConceptId])

slots.CodeList_href = Slot(uri=DEFAULT_.href, name="CodeList_href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.CodeList_href, domain=CodeList, range=Optional[Union[str, URI]])

slots.CodeList_submissionValue = Slot(uri=DEFAULT_.submissionValue, name="CodeList_submissionValue", curie=DEFAULT_.curie('submissionValue'),
                   model_uri=DEFAULT_.CodeList_submissionValue, domain=CodeList, range=str)

slots.CodeListTerm_conceptId = Slot(uri=DEFAULT_.conceptId, name="CodeListTerm_conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.CodeListTerm_conceptId, domain=CodeListTerm, range=Union[str, CodeListTermConceptId])

slots.CodeListTerm_submissionValue = Slot(uri=DEFAULT_.submissionValue, name="CodeListTerm_submissionValue", curie=DEFAULT_.curie('submissionValue'),
                   model_uri=DEFAULT_.CodeListTerm_submissionValue, domain=CodeListTerm, range=str)

slots.AssignedTerm_conceptId = Slot(uri=DEFAULT_.conceptId, name="AssignedTerm_conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.AssignedTerm_conceptId, domain=AssignedTerm, range=Union[str, AssignedTermConceptId])

slots.AssignedTerm_submissionValue = Slot(uri=DEFAULT_.submissionValue, name="AssignedTerm_submissionValue", curie=DEFAULT_.curie('submissionValue'),
                   model_uri=DEFAULT_.AssignedTerm_submissionValue, domain=AssignedTerm, range=str)
