# Auto generated from cosmos_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-11-13T20:49:19
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
from linkml_runtime.linkml_model.types import Date, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate

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
class BiomedicalConceptConceptId(extended_str):
    pass


class DataElementConceptConceptId(extended_str):
    pass


@dataclass
class BiomedicalConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.BiomedicalConcept
    class_class_curie: ClassVar[str] = "cosmos:BiomedicalConcept"
    class_name: ClassVar[str] = "BiomedicalConcept"
    class_model_uri: ClassVar[URIRef] = COSMOS.BiomedicalConcept

    conceptId: Union[str, BiomedicalConceptConceptId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "BiomedicalConceptPackageTypeEnum"] = None
    categories: Union[str, List[str]] = None
    shortName: str = None
    definition: str = None
    ncitCode: Optional[str] = None
    href: Optional[Union[str, URI]] = None
    parentConceptId: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    resultScales: Optional[Union[Union[str, "BiomedicalConceptResultScaleEnum"], List[Union[str, "BiomedicalConceptResultScaleEnum"]]]] = empty_list()
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    dataElementConcepts: Optional[Union[Dict[Union[str, DataElementConceptConceptId], Union[dict, "DataElementConcept"]], List[Union[dict, "DataElementConcept"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.conceptId):
            self.MissingRequiredField("conceptId")
        if not isinstance(self.conceptId, BiomedicalConceptConceptId):
            self.conceptId = BiomedicalConceptConceptId(self.conceptId)

        if self._is_empty(self.packageDate):
            self.MissingRequiredField("packageDate")
        if not isinstance(self.packageDate, XSDDate):
            self.packageDate = XSDDate(self.packageDate)

        if self._is_empty(self.packageType):
            self.MissingRequiredField("packageType")
        if not isinstance(self.packageType, BiomedicalConceptPackageTypeEnum):
            self.packageType = BiomedicalConceptPackageTypeEnum(self.packageType)

        if self._is_empty(self.categories):
            self.MissingRequiredField("categories")
        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, str) else str(v) for v in self.categories]

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.ncitCode is not None and not isinstance(self.ncitCode, str):
            self.ncitCode = str(self.ncitCode)

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        if self.parentConceptId is not None and not isinstance(self.parentConceptId, str):
            self.parentConceptId = str(self.parentConceptId)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.resultScales, list):
            self.resultScales = [self.resultScales] if self.resultScales is not None else []
        self.resultScales = [v if isinstance(v, BiomedicalConceptResultScaleEnum) else BiomedicalConceptResultScaleEnum(v) for v in self.resultScales]

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        self._normalize_inlined_as_list(slot_name="dataElementConcepts", slot_type=DataElementConcept, key_name="conceptId", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Coding(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.Coding
    class_class_curie: ClassVar[str] = "cosmos:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = COSMOS.Coding

    code: str = None
    system: str = None
    systemName: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.systemName is not None and not isinstance(self.systemName, str):
            self.systemName = str(self.systemName)

        super().__post_init__(**kwargs)


@dataclass
class DataElementConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS.DataElementConcept
    class_class_curie: ClassVar[str] = "cosmos:DataElementConcept"
    class_name: ClassVar[str] = "DataElementConcept"
    class_model_uri: ClassVar[URIRef] = COSMOS.DataElementConcept

    conceptId: Union[str, DataElementConceptConceptId] = None
    shortName: str = None
    dataType: Union[str, "DataElementConceptDataTypeEnum"] = None
    ncitCode: Optional[str] = None
    href: Optional[Union[str, URI]] = None
    exampleSet: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.conceptId):
            self.MissingRequiredField("conceptId")
        if not isinstance(self.conceptId, DataElementConceptConceptId):
            self.conceptId = DataElementConceptConceptId(self.conceptId)

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.dataType):
            self.MissingRequiredField("dataType")
        if not isinstance(self.dataType, DataElementConceptDataTypeEnum):
            self.dataType = DataElementConceptDataTypeEnum(self.dataType)

        if self.ncitCode is not None and not isinstance(self.ncitCode, str):
            self.ncitCode = str(self.ncitCode)

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        if not isinstance(self.exampleSet, list):
            self.exampleSet = [self.exampleSet] if self.exampleSet is not None else []
        self.exampleSet = [v if isinstance(v, str) else str(v) for v in self.exampleSet]

        super().__post_init__(**kwargs)


# Enumerations
class BiomedicalConceptPackageTypeEnum(EnumDefinitionImpl):

    bc = PermissibleValue(text="bc")

    _defn = EnumDefinition(
        name="BiomedicalConceptPackageTypeEnum",
    )

class BiomedicalConceptResultScaleEnum(EnumDefinitionImpl):

    Quantitative = PermissibleValue(text="Quantitative")
    Ordinal = PermissibleValue(text="Ordinal")
    Nominal = PermissibleValue(text="Nominal")
    Narrative = PermissibleValue(text="Narrative")

    _defn = EnumDefinition(
        name="BiomedicalConceptResultScaleEnum",
    )

class DataElementConceptDataTypeEnum(EnumDefinitionImpl):

    boolean = PermissibleValue(text="boolean")
    date = PermissibleValue(text="date")
    datetime = PermissibleValue(text="datetime")
    decimal = PermissibleValue(text="decimal")
    integer = PermissibleValue(text="integer")
    string = PermissibleValue(text="string")
    uri = PermissibleValue(text="uri")

    _defn = EnumDefinition(
        name="DataElementConceptDataTypeEnum",
    )

# Slots
class slots:
    pass

slots.conceptId = Slot(uri=COSMOS.conceptId, name="conceptId", curie=COSMOS.curie('conceptId'),
                   model_uri=COSMOS.conceptId, domain=None, range=URIRef,
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]+[0123456789]*)$'))

slots.ncitCode = Slot(uri=COSMOS.ncitCode, name="ncitCode", curie=COSMOS.curie('ncitCode'),
                   model_uri=COSMOS.ncitCode, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.href = Slot(uri=COSMOS.href, name="href", curie=COSMOS.curie('href'),
                   model_uri=COSMOS.href, domain=None, range=Optional[Union[str, URI]])

slots.packageDate = Slot(uri=COSMOS.packageDate, name="packageDate", curie=COSMOS.curie('packageDate'),
                   model_uri=COSMOS.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=COSMOS.packageType, name="packageType", curie=COSMOS.curie('packageType'),
                   model_uri=COSMOS.packageType, domain=None, range=Union[str, "BiomedicalConceptPackageTypeEnum"])

slots.categories = Slot(uri=COSMOS.categories, name="categories", curie=COSMOS.curie('categories'),
                   model_uri=COSMOS.categories, domain=None, range=Union[str, List[str]])

slots.parentConceptId = Slot(uri=COSMOS.parentConceptId, name="parentConceptId", curie=COSMOS.curie('parentConceptId'),
                   model_uri=COSMOS.parentConceptId, domain=None, range=Optional[str])

slots.shortName = Slot(uri=COSMOS.shortName, name="shortName", curie=COSMOS.curie('shortName'),
                   model_uri=COSMOS.shortName, domain=None, range=str)

slots.synonyms = Slot(uri=COSMOS.synonyms, name="synonyms", curie=COSMOS.curie('synonyms'),
                   model_uri=COSMOS.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.resultScales = Slot(uri=COSMOS.resultScales, name="resultScales", curie=COSMOS.curie('resultScales'),
                   model_uri=COSMOS.resultScales, domain=None, range=Optional[Union[Union[str, "BiomedicalConceptResultScaleEnum"], List[Union[str, "BiomedicalConceptResultScaleEnum"]]]])

slots.definition = Slot(uri=COSMOS.definition, name="definition", curie=COSMOS.curie('definition'),
                   model_uri=COSMOS.definition, domain=None, range=str)

slots.coding = Slot(uri=COSMOS.coding, name="coding", curie=COSMOS.curie('coding'),
                   model_uri=COSMOS.coding, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.system = Slot(uri=COSMOS.system, name="system", curie=COSMOS.curie('system'),
                   model_uri=COSMOS.system, domain=None, range=str)

slots.systemName = Slot(uri=COSMOS.systemName, name="systemName", curie=COSMOS.curie('systemName'),
                   model_uri=COSMOS.systemName, domain=None, range=Optional[str])

slots.code = Slot(uri=COSMOS.code, name="code", curie=COSMOS.curie('code'),
                   model_uri=COSMOS.code, domain=None, range=str)

slots.dataElementConcepts = Slot(uri=COSMOS.dataElementConcepts, name="dataElementConcepts", curie=COSMOS.curie('dataElementConcepts'),
                   model_uri=COSMOS.dataElementConcepts, domain=None, range=Optional[Union[Dict[Union[str, DataElementConceptConceptId], Union[dict, DataElementConcept]], List[Union[dict, DataElementConcept]]]])

slots.dataType = Slot(uri=COSMOS.dataType, name="dataType", curie=COSMOS.curie('dataType'),
                   model_uri=COSMOS.dataType, domain=None, range=Union[str, "DataElementConceptDataTypeEnum"])

slots.exampleSet = Slot(uri=COSMOS.exampleSet, name="exampleSet", curie=COSMOS.curie('exampleSet'),
                   model_uri=COSMOS.exampleSet, domain=None, range=Optional[Union[str, List[str]]])

slots.BiomedicalConcept_conceptId = Slot(uri=COSMOS.conceptId, name="BiomedicalConcept_conceptId", curie=COSMOS.curie('conceptId'),
                   model_uri=COSMOS.BiomedicalConcept_conceptId, domain=BiomedicalConcept, range=Union[str, BiomedicalConceptConceptId],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]+[0123456789]*)$'))

slots.BiomedicalConcept_ncitCode = Slot(uri=COSMOS.ncitCode, name="BiomedicalConcept_ncitCode", curie=COSMOS.curie('ncitCode'),
                   model_uri=COSMOS.BiomedicalConcept_ncitCode, domain=BiomedicalConcept, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.BiomedicalConcept_href = Slot(uri=COSMOS.href, name="BiomedicalConcept_href", curie=COSMOS.curie('href'),
                   model_uri=COSMOS.BiomedicalConcept_href, domain=BiomedicalConcept, range=Optional[Union[str, URI]])

slots.DataElementConcept_conceptId = Slot(uri=COSMOS.conceptId, name="DataElementConcept_conceptId", curie=COSMOS.curie('conceptId'),
                   model_uri=COSMOS.DataElementConcept_conceptId, domain=DataElementConcept, range=Union[str, DataElementConceptConceptId],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]+[0123456789]*)$'))

slots.DataElementConcept_ncitCode = Slot(uri=COSMOS.ncitCode, name="DataElementConcept_ncitCode", curie=COSMOS.curie('ncitCode'),
                   model_uri=COSMOS.DataElementConcept_ncitCode, domain=DataElementConcept, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.DataElementConcept_href = Slot(uri=COSMOS.href, name="DataElementConcept_href", curie=COSMOS.curie('href'),
                   model_uri=COSMOS.DataElementConcept_href, domain=DataElementConcept, range=Optional[Union[str, URI]])
