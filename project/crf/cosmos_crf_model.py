# Auto generated from cosmos_crf_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-26T10:21:57
# Schema: COSMoS-Biomedical-Concepts-CRF-Schema
#
# id: https://www.cdisc.org/cosmos/crf_v1.0
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
COSMOS_CRF = CurieNamespace('cosmos_crf', 'https://www.cdisc.org/cosmos/crf_v1.0')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = COSMOS_CRF


# Types

# Class references
class CRFGroupCrfSpecializationId(extended_str):
    pass


class CRFItemName(extended_str):
    pass


@dataclass(repr=False)
class CRFGroup(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_CRF["CRFGroup"]
    class_class_curie: ClassVar[str] = "cosmos_crf:CRFGroup"
    class_name: ClassVar[str] = "CRFGroup"
    class_model_uri: ClassVar[URIRef] = COSMOS_CRF.CRFGroup

    crfSpecializationId: Union[str, CRFGroupCrfSpecializationId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "PackageTypeEnum"] = None
    shortName: str = None
    standard: str = None
    standardStartVersion: str = None
    items: Union[dict[Union[str, CRFItemName], Union[dict, "CRFItem"]], list[Union[dict, "CRFItem"]]] = empty_dict()
    standardEndVersion: Optional[str] = None
    implementationOption: Optional[Union[str, "ImplementationOptionEnum"]] = None
    scenario: Optional[str] = None
    categories: Optional[Union[str, list[str]]] = empty_list()
    domain: Optional[str] = None
    biomedicalConceptId: Optional[str] = None
    sdtmDatasetSpecializationId: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.crfSpecializationId):
            self.MissingRequiredField("crfSpecializationId")
        if not isinstance(self.crfSpecializationId, CRFGroupCrfSpecializationId):
            self.crfSpecializationId = CRFGroupCrfSpecializationId(self.crfSpecializationId)

        if self._is_empty(self.packageDate):
            self.MissingRequiredField("packageDate")
        if not isinstance(self.packageDate, XSDDate):
            self.packageDate = XSDDate(self.packageDate)

        if self._is_empty(self.packageType):
            self.MissingRequiredField("packageType")
        if not isinstance(self.packageType, PackageTypeEnum):
            self.packageType = PackageTypeEnum(self.packageType)

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.standard):
            self.MissingRequiredField("standard")
        if not isinstance(self.standard, str):
            self.standard = str(self.standard)

        if self._is_empty(self.standardStartVersion):
            self.MissingRequiredField("standardStartVersion")
        if not isinstance(self.standardStartVersion, str):
            self.standardStartVersion = str(self.standardStartVersion)

        if self._is_empty(self.items):
            self.MissingRequiredField("items")
        self._normalize_inlined_as_list(slot_name="items", slot_type=CRFItem, key_name="name", keyed=True)

        if self.standardEndVersion is not None and not isinstance(self.standardEndVersion, str):
            self.standardEndVersion = str(self.standardEndVersion)

        if self.implementationOption is not None and not isinstance(self.implementationOption, ImplementationOptionEnum):
            self.implementationOption = ImplementationOptionEnum(self.implementationOption)

        if self.scenario is not None and not isinstance(self.scenario, str):
            self.scenario = str(self.scenario)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if self.domain is not None and not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self.biomedicalConceptId is not None and not isinstance(self.biomedicalConceptId, str):
            self.biomedicalConceptId = str(self.biomedicalConceptId)

        if self.sdtmDatasetSpecializationId is not None and not isinstance(self.sdtmDatasetSpecializationId, str):
            self.sdtmDatasetSpecializationId = str(self.sdtmDatasetSpecializationId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CRFItem(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_CRF["CRFItem"]
    class_class_curie: ClassVar[str] = "cosmos_crf:CRFItem"
    class_name: ClassVar[str] = "CRFItem"
    class_model_uri: ClassVar[URIRef] = COSMOS_CRF.CRFItem

    name: Union[str, CRFItemName] = None
    variableName: str = None
    orderNumber: int = None
    mandatoryVariable: Union[bool, Bool] = None
    dataType: Union[str, "CRFItemDataTypeEnum"] = None
    dataElementConceptId: Optional[str] = None
    questionText: Optional[str] = None
    prompt: Optional[str] = None
    completionInstructions: Optional[str] = None
    length: Optional[int] = None
    significantDigits: Optional[int] = None
    displayHidden: Optional[Union[bool, Bool]] = None
    derivedVariable: Optional[Union[bool, Bool]] = None
    derivationDescription: Optional[str] = None
    codelist: Optional[Union[dict, "CodeList"]] = None
    valueList: Optional[Union[Union[dict, "ListValue"], list[Union[dict, "ListValue"]]]] = empty_list()
    selectionType: Optional[Union[str, "SelectionTypeEnum"]] = None
    prepopulatedValue: Optional[Union[dict, "PrepopulatedValue"]] = None
    sdtmTarget: Optional[Union[dict, "SDTMTarget"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CRFItemName):
            self.name = CRFItemName(self.name)

        if self._is_empty(self.variableName):
            self.MissingRequiredField("variableName")
        if not isinstance(self.variableName, str):
            self.variableName = str(self.variableName)

        if self._is_empty(self.orderNumber):
            self.MissingRequiredField("orderNumber")
        if not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self._is_empty(self.mandatoryVariable):
            self.MissingRequiredField("mandatoryVariable")
        if not isinstance(self.mandatoryVariable, Bool):
            self.mandatoryVariable = Bool(self.mandatoryVariable)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, CRFItemDataTypeEnum):
            self.dataType = CRFItemDataTypeEnum(self.dataType)

        if self.dataElementConceptId is not None and not isinstance(self.dataElementConceptId, str):
            self.dataElementConceptId = str(self.dataElementConceptId)

        if self.questionText is not None and not isinstance(self.questionText, str):
            self.questionText = str(self.questionText)

        if self.prompt is not None and not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        if self.completionInstructions is not None and not isinstance(self.completionInstructions, str):
            self.completionInstructions = str(self.completionInstructions)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.significantDigits is not None and not isinstance(self.significantDigits, int):
            self.significantDigits = int(self.significantDigits)

        if self.displayHidden is not None and not isinstance(self.displayHidden, Bool):
            self.displayHidden = Bool(self.displayHidden)

        if self.derivedVariable is not None and not isinstance(self.derivedVariable, Bool):
            self.derivedVariable = Bool(self.derivedVariable)

        if self.derivationDescription is not None and not isinstance(self.derivationDescription, str):
            self.derivationDescription = str(self.derivationDescription)

        if self.codelist is not None and not isinstance(self.codelist, CodeList):
            self.codelist = CodeList(**as_dict(self.codelist))

        if not isinstance(self.valueList, list):
            self.valueList = [self.valueList] if self.valueList is not None else []
        self.valueList = [v if isinstance(v, ListValue) else ListValue(**as_dict(v)) for v in self.valueList]

        if self.selectionType is not None and not isinstance(self.selectionType, SelectionTypeEnum):
            self.selectionType = SelectionTypeEnum(self.selectionType)

        if self.prepopulatedValue is not None and not isinstance(self.prepopulatedValue, PrepopulatedValue):
            self.prepopulatedValue = PrepopulatedValue(**as_dict(self.prepopulatedValue))

        if self.sdtmTarget is not None and not isinstance(self.sdtmTarget, SDTMTarget):
            self.sdtmTarget = SDTMTarget(**as_dict(self.sdtmTarget))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ListValue(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_CRF["ListValue"]
    class_class_curie: ClassVar[str] = "cosmos_crf:ListValue"
    class_name: ClassVar[str] = "ListValue"
    class_model_uri: ClassVar[URIRef] = COSMOS_CRF.ListValue

    displayValue: str = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.displayValue):
            self.MissingRequiredField("displayValue")
        if not isinstance(self.displayValue, str):
            self.displayValue = str(self.displayValue)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrepopulatedValue(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_CRF["PrepopulatedValue"]
    class_class_curie: ClassVar[str] = "cosmos_crf:PrepopulatedValue"
    class_name: ClassVar[str] = "PrepopulatedValue"
    class_model_uri: ClassVar[URIRef] = COSMOS_CRF.PrepopulatedValue

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


@dataclass(repr=False)
class CodeList(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_CRF["CodeList"]
    class_class_curie: ClassVar[str] = "cosmos_crf:CodeList"
    class_name: ClassVar[str] = "CodeList"
    class_model_uri: ClassVar[URIRef] = COSMOS_CRF.CodeList

    submissionValue: str = None
    conceptId: Optional[str] = None
    href: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.submissionValue):
            self.MissingRequiredField("submissionValue")
        if not isinstance(self.submissionValue, str):
            self.submissionValue = str(self.submissionValue)

        if self.conceptId is not None and not isinstance(self.conceptId, str):
            self.conceptId = str(self.conceptId)

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SDTMTarget(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_CRF["SDTMTarget"]
    class_class_curie: ClassVar[str] = "cosmos_crf:SDTMTarget"
    class_name: ClassVar[str] = "SDTMTarget"
    class_model_uri: ClassVar[URIRef] = COSMOS_CRF.SDTMTarget

    sdtmAnnotation: Optional[str] = None
    sdtmVariables: Optional[Union[str, list[str]]] = empty_list()
    sdtmTargetMapping: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sdtmAnnotation is not None and not isinstance(self.sdtmAnnotation, str):
            self.sdtmAnnotation = str(self.sdtmAnnotation)

        if not isinstance(self.sdtmVariables, list):
            self.sdtmVariables = [self.sdtmVariables] if self.sdtmVariables is not None else []
        self.sdtmVariables = [v if isinstance(v, str) else str(v) for v in self.sdtmVariables]

        if self.sdtmTargetMapping is not None and not isinstance(self.sdtmTargetMapping, str):
            self.sdtmTargetMapping = str(self.sdtmTargetMapping)

        super().__post_init__(**kwargs)


# Enumerations
class PackageTypeEnum(EnumDefinitionImpl):

    crf = PermissibleValue(text="crf")

    _defn = EnumDefinition(
        name="PackageTypeEnum",
    )

class ImplementationOptionEnum(EnumDefinitionImpl):

    Normalized = PermissibleValue(text="Normalized")
    Denormalized = PermissibleValue(text="Denormalized")

    _defn = EnumDefinition(
        name="ImplementationOptionEnum",
    )

class CRFItemDataTypeEnum(EnumDefinitionImpl):

    decimal = PermissibleValue(text="decimal")
    float = PermissibleValue(text="float")
    integer = PermissibleValue(text="integer")
    text = PermissibleValue(text="text")
    date = PermissibleValue(text="date")
    time = PermissibleValue(text="time")

    _defn = EnumDefinition(
        name="CRFItemDataTypeEnum",
    )

class SelectionTypeEnum(EnumDefinitionImpl):

    Multiple = PermissibleValue(text="Multiple")
    Single = PermissibleValue(text="Single")

    _defn = EnumDefinition(
        name="SelectionTypeEnum",
    )

# Slots
class slots:
    pass

slots.packageDate = Slot(uri=COSMOS_CRF.packageDate, name="packageDate", curie=COSMOS_CRF.curie('packageDate'),
                   model_uri=COSMOS_CRF.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=COSMOS_CRF.packageType, name="packageType", curie=COSMOS_CRF.curie('packageType'),
                   model_uri=COSMOS_CRF.packageType, domain=None, range=Union[str, "PackageTypeEnum"])

slots.crfSpecializationId = Slot(uri=COSMOS_CRF.crfSpecializationId, name="crfSpecializationId", curie=COSMOS_CRF.curie('crfSpecializationId'),
                   model_uri=COSMOS_CRF.crfSpecializationId, domain=None, range=URIRef,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.shortName = Slot(uri=COSMOS_CRF.shortName, name="shortName", curie=COSMOS_CRF.curie('shortName'),
                   model_uri=COSMOS_CRF.shortName, domain=None, range=str)

slots.standard = Slot(uri=COSMOS_CRF.standard, name="standard", curie=COSMOS_CRF.curie('standard'),
                   model_uri=COSMOS_CRF.standard, domain=None, range=str)

slots.standardStartVersion = Slot(uri=COSMOS_CRF.standardStartVersion, name="standardStartVersion", curie=COSMOS_CRF.curie('standardStartVersion'),
                   model_uri=COSMOS_CRF.standardStartVersion, domain=None, range=str)

slots.standardEndVersion = Slot(uri=COSMOS_CRF.standardEndVersion, name="standardEndVersion", curie=COSMOS_CRF.curie('standardEndVersion'),
                   model_uri=COSMOS_CRF.standardEndVersion, domain=None, range=Optional[str])

slots.implementationOption = Slot(uri=COSMOS_CRF.implementationOption, name="implementationOption", curie=COSMOS_CRF.curie('implementationOption'),
                   model_uri=COSMOS_CRF.implementationOption, domain=None, range=Optional[Union[str, "ImplementationOptionEnum"]])

slots.scenario = Slot(uri=COSMOS_CRF.scenario, name="scenario", curie=COSMOS_CRF.curie('scenario'),
                   model_uri=COSMOS_CRF.scenario, domain=None, range=Optional[str])

slots.categories = Slot(uri=COSMOS_CRF.categories, name="categories", curie=COSMOS_CRF.curie('categories'),
                   model_uri=COSMOS_CRF.categories, domain=None, range=Optional[Union[str, list[str]]])

slots.domain = Slot(uri=COSMOS_CRF.domain, name="domain", curie=COSMOS_CRF.curie('domain'),
                   model_uri=COSMOS_CRF.domain, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=COSMOS_CRF.biomedicalConceptId, name="biomedicalConceptId", curie=COSMOS_CRF.curie('biomedicalConceptId'),
                   model_uri=COSMOS_CRF.biomedicalConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+|NEW_[A-Z]*[0-9]*)$'))

slots.sdtmDatasetSpecializationId = Slot(uri=COSMOS_CRF.sdtmDatasetSpecializationId, name="sdtmDatasetSpecializationId", curie=COSMOS_CRF.curie('sdtmDatasetSpecializationId'),
                   model_uri=COSMOS_CRF.sdtmDatasetSpecializationId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.items = Slot(uri=COSMOS_CRF.items, name="items", curie=COSMOS_CRF.curie('items'),
                   model_uri=COSMOS_CRF.items, domain=None, range=Union[dict[Union[str, CRFItemName], Union[dict, CRFItem]], list[Union[dict, CRFItem]]])

slots.name = Slot(uri=COSMOS_CRF.name, name="name", curie=COSMOS_CRF.curie('name'),
                   model_uri=COSMOS_CRF.name, domain=None, range=URIRef,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.variableName = Slot(uri=COSMOS_CRF.variableName, name="variableName", curie=COSMOS_CRF.curie('variableName'),
                   model_uri=COSMOS_CRF.variableName, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.dataElementConceptId = Slot(uri=COSMOS_CRF.dataElementConceptId, name="dataElementConceptId", curie=COSMOS_CRF.curie('dataElementConceptId'),
                   model_uri=COSMOS_CRF.dataElementConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+|NEW_[A-Z]*[0-9]*)$'))

slots.questionText = Slot(uri=COSMOS_CRF.questionText, name="questionText", curie=COSMOS_CRF.curie('questionText'),
                   model_uri=COSMOS_CRF.questionText, domain=None, range=Optional[str])

slots.prompt = Slot(uri=COSMOS_CRF.prompt, name="prompt", curie=COSMOS_CRF.curie('prompt'),
                   model_uri=COSMOS_CRF.prompt, domain=None, range=Optional[str])

slots.completionInstructions = Slot(uri=COSMOS_CRF.completionInstructions, name="completionInstructions", curie=COSMOS_CRF.curie('completionInstructions'),
                   model_uri=COSMOS_CRF.completionInstructions, domain=None, range=Optional[str])

slots.orderNumber = Slot(uri=COSMOS_CRF.orderNumber, name="orderNumber", curie=COSMOS_CRF.curie('orderNumber'),
                   model_uri=COSMOS_CRF.orderNumber, domain=None, range=int)

slots.mandatoryVariable = Slot(uri=COSMOS_CRF.mandatoryVariable, name="mandatoryVariable", curie=COSMOS_CRF.curie('mandatoryVariable'),
                   model_uri=COSMOS_CRF.mandatoryVariable, domain=None, range=Union[bool, Bool])

slots.dataType = Slot(uri=COSMOS_CRF.dataType, name="dataType", curie=COSMOS_CRF.curie('dataType'),
                   model_uri=COSMOS_CRF.dataType, domain=None, range=Union[str, "CRFItemDataTypeEnum"])

slots.length = Slot(uri=COSMOS_CRF.length, name="length", curie=COSMOS_CRF.curie('length'),
                   model_uri=COSMOS_CRF.length, domain=None, range=Optional[int])

slots.significantDigits = Slot(uri=COSMOS_CRF.significantDigits, name="significantDigits", curie=COSMOS_CRF.curie('significantDigits'),
                   model_uri=COSMOS_CRF.significantDigits, domain=None, range=Optional[int])

slots.displayHidden = Slot(uri=COSMOS_CRF.displayHidden, name="displayHidden", curie=COSMOS_CRF.curie('displayHidden'),
                   model_uri=COSMOS_CRF.displayHidden, domain=None, range=Optional[Union[bool, Bool]])

slots.derivedVariable = Slot(uri=COSMOS_CRF.derivedVariable, name="derivedVariable", curie=COSMOS_CRF.curie('derivedVariable'),
                   model_uri=COSMOS_CRF.derivedVariable, domain=None, range=Optional[Union[bool, Bool]])

slots.derivationDescription = Slot(uri=COSMOS_CRF.derivationDescription, name="derivationDescription", curie=COSMOS_CRF.curie('derivationDescription'),
                   model_uri=COSMOS_CRF.derivationDescription, domain=None, range=Optional[str])

slots.codelist = Slot(uri=COSMOS_CRF.codelist, name="codelist", curie=COSMOS_CRF.curie('codelist'),
                   model_uri=COSMOS_CRF.codelist, domain=None, range=Optional[Union[dict, CodeList]])

slots.valueList = Slot(uri=COSMOS_CRF.valueList, name="valueList", curie=COSMOS_CRF.curie('valueList'),
                   model_uri=COSMOS_CRF.valueList, domain=None, range=Optional[Union[Union[dict, ListValue], list[Union[dict, ListValue]]]])

slots.selectionType = Slot(uri=COSMOS_CRF.selectionType, name="selectionType", curie=COSMOS_CRF.curie('selectionType'),
                   model_uri=COSMOS_CRF.selectionType, domain=None, range=Optional[Union[str, "SelectionTypeEnum"]])

slots.prepopulatedValue = Slot(uri=COSMOS_CRF.prepopulatedValue, name="prepopulatedValue", curie=COSMOS_CRF.curie('prepopulatedValue'),
                   model_uri=COSMOS_CRF.prepopulatedValue, domain=None, range=Optional[Union[dict, PrepopulatedValue]])

slots.conceptId = Slot(uri=COSMOS_CRF.conceptId, name="conceptId", curie=COSMOS_CRF.curie('conceptId'),
                   model_uri=COSMOS_CRF.conceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+)$'))

slots.href = Slot(uri=COSMOS_CRF.href, name="href", curie=COSMOS_CRF.curie('href'),
                   model_uri=COSMOS_CRF.href, domain=None, range=Optional[Union[str, URI]])

slots.submissionValue = Slot(uri=COSMOS_CRF.submissionValue, name="submissionValue", curie=COSMOS_CRF.curie('submissionValue'),
                   model_uri=COSMOS_CRF.submissionValue, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.displayValue = Slot(uri=COSMOS_CRF.displayValue, name="displayValue", curie=COSMOS_CRF.curie('displayValue'),
                   model_uri=COSMOS_CRF.displayValue, domain=None, range=str)

slots.value = Slot(uri=COSMOS_CRF.value, name="value", curie=COSMOS_CRF.curie('value'),
                   model_uri=COSMOS_CRF.value, domain=None, range=Optional[str])

slots.sdtmTarget = Slot(uri=COSMOS_CRF.sdtmTarget, name="sdtmTarget", curie=COSMOS_CRF.curie('sdtmTarget'),
                   model_uri=COSMOS_CRF.sdtmTarget, domain=None, range=Optional[Union[dict, SDTMTarget]])

slots.sdtmAnnotation = Slot(uri=COSMOS_CRF.sdtmAnnotation, name="sdtmAnnotation", curie=COSMOS_CRF.curie('sdtmAnnotation'),
                   model_uri=COSMOS_CRF.sdtmAnnotation, domain=None, range=Optional[str])

slots.sdtmVariables = Slot(uri=COSMOS_CRF.sdtmVariables, name="sdtmVariables", curie=COSMOS_CRF.curie('sdtmVariables'),
                   model_uri=COSMOS_CRF.sdtmVariables, domain=None, range=Optional[Union[str, list[str]]])

slots.sdtmTargetMapping = Slot(uri=COSMOS_CRF.sdtmTargetMapping, name="sdtmTargetMapping", curie=COSMOS_CRF.curie('sdtmTargetMapping'),
                   model_uri=COSMOS_CRF.sdtmTargetMapping, domain=None, range=Optional[str])

slots.ListValue_displayValue = Slot(uri=COSMOS_CRF.displayValue, name="ListValue_displayValue", curie=COSMOS_CRF.curie('displayValue'),
                   model_uri=COSMOS_CRF.ListValue_displayValue, domain=ListValue, range=str)

slots.ListValue_value = Slot(uri=COSMOS_CRF.value, name="ListValue_value", curie=COSMOS_CRF.curie('value'),
                   model_uri=COSMOS_CRF.ListValue_value, domain=ListValue, range=Optional[str])

slots.PrepopulatedValue_value = Slot(uri=COSMOS_CRF.value, name="PrepopulatedValue_value", curie=COSMOS_CRF.curie('value'),
                   model_uri=COSMOS_CRF.PrepopulatedValue_value, domain=PrepopulatedValue, range=str)

slots.PrepopulatedValue_conceptId = Slot(uri=COSMOS_CRF.conceptId, name="PrepopulatedValue_conceptId", curie=COSMOS_CRF.curie('conceptId'),
                   model_uri=COSMOS_CRF.PrepopulatedValue_conceptId, domain=PrepopulatedValue, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+)$'))

slots.CodeList_submissionValue = Slot(uri=COSMOS_CRF.submissionValue, name="CodeList_submissionValue", curie=COSMOS_CRF.curie('submissionValue'),
                   model_uri=COSMOS_CRF.CodeList_submissionValue, domain=CodeList, range=str,
                   pattern=re.compile(r'^[A-Z][A-Z0-9_]*$'))

slots.CodeList_conceptId = Slot(uri=COSMOS_CRF.conceptId, name="CodeList_conceptId", curie=COSMOS_CRF.curie('conceptId'),
                   model_uri=COSMOS_CRF.CodeList_conceptId, domain=CodeList, range=Optional[str],
                   pattern=re.compile(r'^(C[0-9]+)$'))

slots.CodeList_href = Slot(uri=COSMOS_CRF.href, name="CodeList_href", curie=COSMOS_CRF.curie('href'),
                   model_uri=COSMOS_CRF.CodeList_href, domain=CodeList, range=Optional[Union[str, URI]])
