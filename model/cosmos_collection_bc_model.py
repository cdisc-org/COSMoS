# Auto generated from cosmos_collection_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2025-01-23T15:38:34
# Schema: COSMoS-Biomedical-Concepts-Collection-Schema
#
# id: https://www.cdisc.org/cosmos/collection_v1.0
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
COSMOS_COLLECTION = CurieNamespace('cosmos_collection', 'https://www.cdisc.org/cosmos/collection_v1.0')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = COSMOS_COLLECTION


# Types

# Class references
class DataCollectionGroupDatasetSpecializationId(extended_str):
    pass


class DataCollectionItemName(extended_str):
    pass


class CodeListConceptId(extended_str):
    pass


@dataclass
class DataCollectionGroup(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_COLLECTION.DataCollectionGroup
    class_class_curie: ClassVar[str] = "cosmos_collection:DataCollectionGroup"
    class_name: ClassVar[str] = "DataCollectionGroup"
    class_model_uri: ClassVar[URIRef] = COSMOS_COLLECTION.DataCollectionGroup

    datasetSpecializationId: Union[str, DataCollectionGroupDatasetSpecializationId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "PackageTypeEnum"] = None
    standard: str = None
    domain: str = None
    shortName: str = None
    collectionigStartVersion: str = None
    items: Union[Dict[Union[str, DataCollectionItemName], Union[dict, "DataCollectionItem"]], List[Union[dict, "DataCollectionItem"]]] = empty_dict()
    collectionigEndVersion: Optional[str] = None
    biomedicalConceptId: Optional[str] = None
    sdtmDatasetSpecializationId: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.datasetSpecializationId):
            self.MissingRequiredField("datasetSpecializationId")
        if not isinstance(self.datasetSpecializationId, DataCollectionGroupDatasetSpecializationId):
            self.datasetSpecializationId = DataCollectionGroupDatasetSpecializationId(self.datasetSpecializationId)

        if self._is_empty(self.packageDate):
            self.MissingRequiredField("packageDate")
        if not isinstance(self.packageDate, XSDDate):
            self.packageDate = XSDDate(self.packageDate)

        if self._is_empty(self.packageType):
            self.MissingRequiredField("packageType")
        if not isinstance(self.packageType, PackageTypeEnum):
            self.packageType = PackageTypeEnum(self.packageType)

        if self._is_empty(self.standard):
            self.MissingRequiredField("standard")
        if not isinstance(self.standard, str):
            self.standard = str(self.standard)

        if self._is_empty(self.domain):
            self.MissingRequiredField("domain")
        if not isinstance(self.domain, str):
            self.domain = str(self.domain)

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.collectionigStartVersion):
            self.MissingRequiredField("collectionigStartVersion")
        if not isinstance(self.collectionigStartVersion, str):
            self.collectionigStartVersion = str(self.collectionigStartVersion)

        if self._is_empty(self.items):
            self.MissingRequiredField("items")
        self._normalize_inlined_as_list(slot_name="items", slot_type=DataCollectionItem, key_name="name", keyed=True)

        if self.collectionigEndVersion is not None and not isinstance(self.collectionigEndVersion, str):
            self.collectionigEndVersion = str(self.collectionigEndVersion)

        if self.biomedicalConceptId is not None and not isinstance(self.biomedicalConceptId, str):
            self.biomedicalConceptId = str(self.biomedicalConceptId)

        if self.sdtmDatasetSpecializationId is not None and not isinstance(self.sdtmDatasetSpecializationId, str):
            self.sdtmDatasetSpecializationId = str(self.sdtmDatasetSpecializationId)

        super().__post_init__(**kwargs)


@dataclass
class DataCollectionItem(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_COLLECTION.DataCollectionItem
    class_class_curie: ClassVar[str] = "cosmos_collection:DataCollectionItem"
    class_name: ClassVar[str] = "DataCollectionItem"
    class_model_uri: ClassVar[URIRef] = COSMOS_COLLECTION.DataCollectionItem

    name: Union[str, DataCollectionItemName] = None
    eCRFItem: str = None
    orderNumber: int = None
    dataType: Union[str, "CollectionItemDataTypeEnum"] = None
    dataElementConceptId: Optional[str] = None
    isNonStandard: Optional[Union[bool, Bool]] = None
    questionText: Optional[str] = None
    prompt: Optional[str] = None
    codelist: Optional[Union[dict, "CodeList"]] = None
    valueList: Optional[Union[Union[dict, "ListValue"], List[Union[dict, "ListValue"]]]] = empty_list()
    listStyle: Optional[Union[str, "ListTypeEnum"]] = None
    prepopulatedValue: Optional[Union[dict, "PrepopulatedValue"]] = None
    displayHidden: Optional[Union[bool, Bool]] = None
    length: Optional[int] = None
    significantDigits: Optional[int] = None
    mandatoryVariable: Optional[Union[bool, Bool]] = None
    cdashigCore: Optional[Union[str, "CDASHIGCore"]] = None
    sdtmTarget: Optional[Union[Union[dict, "SDTMTarget"], List[Union[dict, "SDTMTarget"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, DataCollectionItemName):
            self.name = DataCollectionItemName(self.name)

        if self._is_empty(self.eCRFItem):
            self.MissingRequiredField("eCRFItem")
        if not isinstance(self.eCRFItem, str):
            self.eCRFItem = str(self.eCRFItem)

        if self._is_empty(self.orderNumber):
            self.MissingRequiredField("orderNumber")
        if not isinstance(self.orderNumber, int):
            self.orderNumber = int(self.orderNumber)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, CollectionItemDataTypeEnum):
            self.dataType = CollectionItemDataTypeEnum(self.dataType)

        if self.dataElementConceptId is not None and not isinstance(self.dataElementConceptId, str):
            self.dataElementConceptId = str(self.dataElementConceptId)

        if self.isNonStandard is not None and not isinstance(self.isNonStandard, Bool):
            self.isNonStandard = Bool(self.isNonStandard)

        if self.questionText is not None and not isinstance(self.questionText, str):
            self.questionText = str(self.questionText)

        if self.prompt is not None and not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        if self.codelist is not None and not isinstance(self.codelist, CodeList):
            self.codelist = CodeList(**as_dict(self.codelist))

        if not isinstance(self.valueList, list):
            self.valueList = [self.valueList] if self.valueList is not None else []
        self.valueList = [v if isinstance(v, ListValue) else ListValue(**as_dict(v)) for v in self.valueList]

        if self.listStyle is not None and not isinstance(self.listStyle, ListTypeEnum):
            self.listStyle = ListTypeEnum(self.listStyle)

        if self.prepopulatedValue is not None and not isinstance(self.prepopulatedValue, PrepopulatedValue):
            self.prepopulatedValue = PrepopulatedValue(**as_dict(self.prepopulatedValue))

        if self.displayHidden is not None and not isinstance(self.displayHidden, Bool):
            self.displayHidden = Bool(self.displayHidden)

        if self.length is not None and not isinstance(self.length, int):
            self.length = int(self.length)

        if self.significantDigits is not None and not isinstance(self.significantDigits, int):
            self.significantDigits = int(self.significantDigits)

        if self.mandatoryVariable is not None and not isinstance(self.mandatoryVariable, Bool):
            self.mandatoryVariable = Bool(self.mandatoryVariable)

        if self.cdashigCore is not None and not isinstance(self.cdashigCore, CDASHIGCore):
            self.cdashigCore = CDASHIGCore(self.cdashigCore)

        if not isinstance(self.sdtmTarget, list):
            self.sdtmTarget = [self.sdtmTarget] if self.sdtmTarget is not None else []
        self.sdtmTarget = [v if isinstance(v, SDTMTarget) else SDTMTarget(**as_dict(v)) for v in self.sdtmTarget]

        super().__post_init__(**kwargs)


@dataclass
class CodeList(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_COLLECTION.CodeList
    class_class_curie: ClassVar[str] = "cosmos_collection:CodeList"
    class_name: ClassVar[str] = "CodeList"
    class_model_uri: ClassVar[URIRef] = COSMOS_COLLECTION.CodeList

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
class ListValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_COLLECTION.ListValue
    class_class_curie: ClassVar[str] = "cosmos_collection:ListValue"
    class_name: ClassVar[str] = "ListValue"
    class_model_uri: ClassVar[URIRef] = COSMOS_COLLECTION.ListValue

    value: str = None
    displayValue: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.displayValue is not None and not isinstance(self.displayValue, str):
            self.displayValue = str(self.displayValue)

        super().__post_init__(**kwargs)


@dataclass
class PrepopulatedValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_COLLECTION.PrepopulatedValue
    class_class_curie: ClassVar[str] = "cosmos_collection:PrepopulatedValue"
    class_name: ClassVar[str] = "PrepopulatedValue"
    class_model_uri: ClassVar[URIRef] = COSMOS_COLLECTION.PrepopulatedValue

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


@dataclass
class SDTMTarget(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_COLLECTION.SDTMTarget
    class_class_curie: ClassVar[str] = "cosmos_collection:SDTMTarget"
    class_name: ClassVar[str] = "SDTMTarget"
    class_model_uri: ClassVar[URIRef] = COSMOS_COLLECTION.SDTMTarget

    sdtmVariable: str = None
    sdtmTargetMapping: str = None
    sdtmAnnotation: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sdtmVariable):
            self.MissingRequiredField("sdtmVariable")
        if not isinstance(self.sdtmVariable, str):
            self.sdtmVariable = str(self.sdtmVariable)

        if self._is_empty(self.sdtmTargetMapping):
            self.MissingRequiredField("sdtmTargetMapping")
        if not isinstance(self.sdtmTargetMapping, str):
            self.sdtmTargetMapping = str(self.sdtmTargetMapping)

        if self.sdtmAnnotation is not None and not isinstance(self.sdtmAnnotation, str):
            self.sdtmAnnotation = str(self.sdtmAnnotation)

        super().__post_init__(**kwargs)


# Enumerations
class PackageTypeEnum(EnumDefinitionImpl):

    collection = PermissibleValue(text="collection")

    _defn = EnumDefinition(
        name="PackageTypeEnum",
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

class CollectionItemDataTypeEnum(EnumDefinitionImpl):

    decimal = PermissibleValue(text="decimal")
    float = PermissibleValue(text="float")
    integer = PermissibleValue(text="integer")
    text = PermissibleValue(text="text")
    date = PermissibleValue(text="date")
    time = PermissibleValue(text="time")

    _defn = EnumDefinition(
        name="CollectionItemDataTypeEnum",
    )

class ListTypeEnum(EnumDefinitionImpl):

    Radio = PermissibleValue(text="Radio")
    Dropdown = PermissibleValue(text="Dropdown")
    DropdownMultiSelect = PermissibleValue(text="DropdownMultiSelect")
    Checkbox = PermissibleValue(text="Checkbox")
    Text = PermissibleValue(text="Text")
    Date = PermissibleValue(text="Date")
    Time = PermissibleValue(text="Time")
    DateTime = PermissibleValue(text="DateTime")

    _defn = EnumDefinition(
        name="ListTypeEnum",
    )

# Slots
class slots:
    pass

slots.packageDate = Slot(uri=COSMOS_COLLECTION.packageDate, name="packageDate", curie=COSMOS_COLLECTION.curie('packageDate'),
                   model_uri=COSMOS_COLLECTION.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=COSMOS_COLLECTION.packageType, name="packageType", curie=COSMOS_COLLECTION.curie('packageType'),
                   model_uri=COSMOS_COLLECTION.packageType, domain=None, range=Union[str, "PackageTypeEnum"])

slots.datasetSpecializationId = Slot(uri=COSMOS_COLLECTION.datasetSpecializationId, name="datasetSpecializationId", curie=COSMOS_COLLECTION.curie('datasetSpecializationId'),
                   model_uri=COSMOS_COLLECTION.datasetSpecializationId, domain=None, range=URIRef)

slots.standard = Slot(uri=COSMOS_COLLECTION.standard, name="standard", curie=COSMOS_COLLECTION.curie('standard'),
                   model_uri=COSMOS_COLLECTION.standard, domain=None, range=str)

slots.domain = Slot(uri=COSMOS_COLLECTION.domain, name="domain", curie=COSMOS_COLLECTION.curie('domain'),
                   model_uri=COSMOS_COLLECTION.domain, domain=None, range=str)

slots.shortName = Slot(uri=COSMOS_COLLECTION.shortName, name="shortName", curie=COSMOS_COLLECTION.curie('shortName'),
                   model_uri=COSMOS_COLLECTION.shortName, domain=None, range=str)

slots.collectionigStartVersion = Slot(uri=COSMOS_COLLECTION.collectionigStartVersion, name="collectionigStartVersion", curie=COSMOS_COLLECTION.curie('collectionigStartVersion'),
                   model_uri=COSMOS_COLLECTION.collectionigStartVersion, domain=None, range=str)

slots.collectionigEndVersion = Slot(uri=COSMOS_COLLECTION.collectionigEndVersion, name="collectionigEndVersion", curie=COSMOS_COLLECTION.curie('collectionigEndVersion'),
                   model_uri=COSMOS_COLLECTION.collectionigEndVersion, domain=None, range=Optional[str])

slots.biomedicalConceptId = Slot(uri=COSMOS_COLLECTION.biomedicalConceptId, name="biomedicalConceptId", curie=COSMOS_COLLECTION.curie('biomedicalConceptId'),
                   model_uri=COSMOS_COLLECTION.biomedicalConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.sdtmDatasetSpecializationId = Slot(uri=COSMOS_COLLECTION.sdtmDatasetSpecializationId, name="sdtmDatasetSpecializationId", curie=COSMOS_COLLECTION.curie('sdtmDatasetSpecializationId'),
                   model_uri=COSMOS_COLLECTION.sdtmDatasetSpecializationId, domain=None, range=Optional[str])

slots.items = Slot(uri=COSMOS_COLLECTION.items, name="items", curie=COSMOS_COLLECTION.curie('items'),
                   model_uri=COSMOS_COLLECTION.items, domain=None, range=Union[Dict[Union[str, DataCollectionItemName], Union[dict, DataCollectionItem]], List[Union[dict, DataCollectionItem]]])

slots.name = Slot(uri=COSMOS_COLLECTION.name, name="name", curie=COSMOS_COLLECTION.curie('name'),
                   model_uri=COSMOS_COLLECTION.name, domain=None, range=URIRef)

slots.dataElementConceptId = Slot(uri=COSMOS_COLLECTION.dataElementConceptId, name="dataElementConceptId", curie=COSMOS_COLLECTION.curie('dataElementConceptId'),
                   model_uri=COSMOS_COLLECTION.dataElementConceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.isNonStandard = Slot(uri=COSMOS_COLLECTION.isNonStandard, name="isNonStandard", curie=COSMOS_COLLECTION.curie('isNonStandard'),
                   model_uri=COSMOS_COLLECTION.isNonStandard, domain=None, range=Optional[Union[bool, Bool]])

slots.eCRFItem = Slot(uri=COSMOS_COLLECTION.eCRFItem, name="eCRFItem", curie=COSMOS_COLLECTION.curie('eCRFItem'),
                   model_uri=COSMOS_COLLECTION.eCRFItem, domain=None, range=str)

slots.questionText = Slot(uri=COSMOS_COLLECTION.questionText, name="questionText", curie=COSMOS_COLLECTION.curie('questionText'),
                   model_uri=COSMOS_COLLECTION.questionText, domain=None, range=Optional[str])

slots.prompt = Slot(uri=COSMOS_COLLECTION.prompt, name="prompt", curie=COSMOS_COLLECTION.curie('prompt'),
                   model_uri=COSMOS_COLLECTION.prompt, domain=None, range=Optional[str])

slots.orderNumber = Slot(uri=COSMOS_COLLECTION.orderNumber, name="orderNumber", curie=COSMOS_COLLECTION.curie('orderNumber'),
                   model_uri=COSMOS_COLLECTION.orderNumber, domain=None, range=int)

slots.codelist = Slot(uri=COSMOS_COLLECTION.codelist, name="codelist", curie=COSMOS_COLLECTION.curie('codelist'),
                   model_uri=COSMOS_COLLECTION.codelist, domain=None, range=Optional[Union[dict, CodeList]])

slots.prepopulatedValue = Slot(uri=COSMOS_COLLECTION.prepopulatedValue, name="prepopulatedValue", curie=COSMOS_COLLECTION.curie('prepopulatedValue'),
                   model_uri=COSMOS_COLLECTION.prepopulatedValue, domain=None, range=Optional[Union[dict, PrepopulatedValue]])

slots.displayHidden = Slot(uri=COSMOS_COLLECTION.displayHidden, name="displayHidden", curie=COSMOS_COLLECTION.curie('displayHidden'),
                   model_uri=COSMOS_COLLECTION.displayHidden, domain=None, range=Optional[Union[bool, Bool]])

slots.conceptId = Slot(uri=COSMOS_COLLECTION.conceptId, name="conceptId", curie=COSMOS_COLLECTION.curie('conceptId'),
                   model_uri=COSMOS_COLLECTION.conceptId, domain=None, range=URIRef,
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.href = Slot(uri=COSMOS_COLLECTION.href, name="href", curie=COSMOS_COLLECTION.curie('href'),
                   model_uri=COSMOS_COLLECTION.href, domain=None, range=Optional[Union[str, URI]])

slots.submissionValue = Slot(uri=COSMOS_COLLECTION.submissionValue, name="submissionValue", curie=COSMOS_COLLECTION.curie('submissionValue'),
                   model_uri=COSMOS_COLLECTION.submissionValue, domain=None, range=str)

slots.valueList = Slot(uri=COSMOS_COLLECTION.valueList, name="valueList", curie=COSMOS_COLLECTION.curie('valueList'),
                   model_uri=COSMOS_COLLECTION.valueList, domain=None, range=Optional[Union[Union[dict, ListValue], List[Union[dict, ListValue]]]])

slots.valueDisplayList = Slot(uri=COSMOS_COLLECTION.valueDisplayList, name="valueDisplayList", curie=COSMOS_COLLECTION.curie('valueDisplayList'),
                   model_uri=COSMOS_COLLECTION.valueDisplayList, domain=None, range=Optional[Union[str, List[str]]])

slots.listStyle = Slot(uri=COSMOS_COLLECTION.listStyle, name="listStyle", curie=COSMOS_COLLECTION.curie('listStyle'),
                   model_uri=COSMOS_COLLECTION.listStyle, domain=None, range=Optional[Union[str, "ListTypeEnum"]])

slots.sdtmTarget = Slot(uri=COSMOS_COLLECTION.sdtmTarget, name="sdtmTarget", curie=COSMOS_COLLECTION.curie('sdtmTarget'),
                   model_uri=COSMOS_COLLECTION.sdtmTarget, domain=None, range=Optional[Union[Union[dict, SDTMTarget], List[Union[dict, SDTMTarget]]]])

slots.sdtmVariable = Slot(uri=COSMOS_COLLECTION.sdtmVariable, name="sdtmVariable", curie=COSMOS_COLLECTION.curie('sdtmVariable'),
                   model_uri=COSMOS_COLLECTION.sdtmVariable, domain=None, range=str)

slots.sdtmAnnotation = Slot(uri=COSMOS_COLLECTION.sdtmAnnotation, name="sdtmAnnotation", curie=COSMOS_COLLECTION.curie('sdtmAnnotation'),
                   model_uri=COSMOS_COLLECTION.sdtmAnnotation, domain=None, range=Optional[str])

slots.sdtmTargetMapping = Slot(uri=COSMOS_COLLECTION.sdtmTargetMapping, name="sdtmTargetMapping", curie=COSMOS_COLLECTION.curie('sdtmTargetMapping'),
                   model_uri=COSMOS_COLLECTION.sdtmTargetMapping, domain=None, range=str)

slots.dataType = Slot(uri=COSMOS_COLLECTION.dataType, name="dataType", curie=COSMOS_COLLECTION.curie('dataType'),
                   model_uri=COSMOS_COLLECTION.dataType, domain=None, range=Union[str, "CollectionItemDataTypeEnum"])

slots.length = Slot(uri=COSMOS_COLLECTION.length, name="length", curie=COSMOS_COLLECTION.curie('length'),
                   model_uri=COSMOS_COLLECTION.length, domain=None, range=Optional[int])

slots.significantDigits = Slot(uri=COSMOS_COLLECTION.significantDigits, name="significantDigits", curie=COSMOS_COLLECTION.curie('significantDigits'),
                   model_uri=COSMOS_COLLECTION.significantDigits, domain=None, range=Optional[int])

slots.mandatoryVariable = Slot(uri=COSMOS_COLLECTION.mandatoryVariable, name="mandatoryVariable", curie=COSMOS_COLLECTION.curie('mandatoryVariable'),
                   model_uri=COSMOS_COLLECTION.mandatoryVariable, domain=None, range=Optional[Union[bool, Bool]])

slots.cdashigCore = Slot(uri=COSMOS_COLLECTION.cdashigCore, name="cdashigCore", curie=COSMOS_COLLECTION.curie('cdashigCore'),
                   model_uri=COSMOS_COLLECTION.cdashigCore, domain=None, range=Optional[Union[str, "CDASHIGCore"]])

slots.listValue__value = Slot(uri=COSMOS_COLLECTION.value, name="listValue__value", curie=COSMOS_COLLECTION.curie('value'),
                   model_uri=COSMOS_COLLECTION.listValue__value, domain=None, range=str)

slots.listValue__displayValue = Slot(uri=COSMOS_COLLECTION.displayValue, name="listValue__displayValue", curie=COSMOS_COLLECTION.curie('displayValue'),
                   model_uri=COSMOS_COLLECTION.listValue__displayValue, domain=None, range=Optional[str])

slots.prepopulatedValue__conceptId = Slot(uri=COSMOS_COLLECTION.conceptId, name="prepopulatedValue__conceptId", curie=COSMOS_COLLECTION.curie('conceptId'),
                   model_uri=COSMOS_COLLECTION.prepopulatedValue__conceptId, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.prepopulatedValue__value = Slot(uri=COSMOS_COLLECTION.value, name="prepopulatedValue__value", curie=COSMOS_COLLECTION.curie('value'),
                   model_uri=COSMOS_COLLECTION.prepopulatedValue__value, domain=None, range=str)
