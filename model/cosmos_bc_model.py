# Auto generated from cosmos_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-13T17:27:42
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
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://www.cdisc.org/cosmos/1-0/')


# Types

# Class references
class BiomedicalConceptConceptId(extended_str):
    pass


class DataElementConceptConceptId(extended_str):
    pass


@dataclass
class BiomedicalConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/BiomedicalConcept")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BiomedicalConcept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/BiomedicalConcept")

    conceptId: Union[str, BiomedicalConceptConceptId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "BiomedicalConceptPackageType"] = None
    category: Union[str, List[str]] = None
    shortName: str = None
    definition: str = None
    href: Optional[Union[str, URI]] = None
    parentConceptId: Optional[str] = None
    synonym: Optional[Union[str, List[str]]] = empty_list()
    resultScale: Optional[Union[str, "BiomedicalConceptResultScale"]] = None
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
        if not isinstance(self.packageType, BiomedicalConceptPackageType):
            self.packageType = BiomedicalConceptPackageType(self.packageType)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, list):
            self.category = [self.category] if self.category is not None else []
        self.category = [v if isinstance(v, str) else str(v) for v in self.category]

        if self._is_empty(self.shortName):
            self.MissingRequiredField("shortName")
        if not isinstance(self.shortName, str):
            self.shortName = str(self.shortName)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        if self.parentConceptId is not None and not isinstance(self.parentConceptId, str):
            self.parentConceptId = str(self.parentConceptId)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, str) else str(v) for v in self.synonym]

        if self.resultScale is not None and not isinstance(self.resultScale, BiomedicalConceptResultScale):
            self.resultScale = BiomedicalConceptResultScale(self.resultScale)

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        self._normalize_inlined_as_list(slot_name="dataElementConcepts", slot_type=DataElementConcept, key_name="conceptId", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Coding(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/Coding")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/Coding")

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

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/DataElementConcept")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataElementConcept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/DataElementConcept")

    conceptId: Union[str, DataElementConceptConceptId] = None
    shortName: str = None
    href: Optional[Union[str, URI]] = None
    dataType: Optional[Union[str, "DataElementConceptDataType"]] = None
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

        if self.href is not None and not isinstance(self.href, URI):
            self.href = URI(self.href)

        if self.dataType is not None and not isinstance(self.dataType, DataElementConceptDataType):
            self.dataType = DataElementConceptDataType(self.dataType)

        if not isinstance(self.exampleSet, list):
            self.exampleSet = [self.exampleSet] if self.exampleSet is not None else []
        self.exampleSet = [v if isinstance(v, str) else str(v) for v in self.exampleSet]

        super().__post_init__(**kwargs)


# Enumerations
class BiomedicalConceptPackageType(EnumDefinitionImpl):

    bc = PermissibleValue(text="bc")

    _defn = EnumDefinition(
        name="BiomedicalConceptPackageType",
    )

class BiomedicalConceptResultScale(EnumDefinitionImpl):

    Quantitative = PermissibleValue(text="Quantitative")
    Ordinal = PermissibleValue(text="Ordinal")
    Nominal = PermissibleValue(text="Nominal")
    Narrative = PermissibleValue(text="Narrative")

    _defn = EnumDefinition(
        name="BiomedicalConceptResultScale",
    )

class DataElementConceptDataType(EnumDefinitionImpl):

    boolean = PermissibleValue(text="boolean")
    decimal = PermissibleValue(text="decimal")
    integer = PermissibleValue(text="integer")
    string = PermissibleValue(text="string")
    uri = PermissibleValue(text="uri")

    _defn = EnumDefinition(
        name="DataElementConceptDataType",
    )

# Slots
class slots:
    pass

slots.conceptId = Slot(uri=DEFAULT_.conceptId, name="conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.conceptId, domain=None, range=URIRef)

slots.href = Slot(uri=DEFAULT_.href, name="href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.href, domain=None, range=Optional[Union[str, URI]])

slots.packageDate = Slot(uri=DEFAULT_.packageDate, name="packageDate", curie=DEFAULT_.curie('packageDate'),
                   model_uri=DEFAULT_.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=DEFAULT_.packageType, name="packageType", curie=DEFAULT_.curie('packageType'),
                   model_uri=DEFAULT_.packageType, domain=None, range=Union[str, "BiomedicalConceptPackageType"])

slots.category = Slot(uri=DEFAULT_.category, name="category", curie=DEFAULT_.curie('category'),
                   model_uri=DEFAULT_.category, domain=None, range=Union[str, List[str]])

slots.parentConceptId = Slot(uri=DEFAULT_.parentConceptId, name="parentConceptId", curie=DEFAULT_.curie('parentConceptId'),
                   model_uri=DEFAULT_.parentConceptId, domain=None, range=Optional[str])

slots.shortName = Slot(uri=DEFAULT_.shortName, name="shortName", curie=DEFAULT_.curie('shortName'),
                   model_uri=DEFAULT_.shortName, domain=None, range=str)

slots.synonym = Slot(uri=DEFAULT_.synonym, name="synonym", curie=DEFAULT_.curie('synonym'),
                   model_uri=DEFAULT_.synonym, domain=None, range=Optional[Union[str, List[str]]])

slots.resultScale = Slot(uri=DEFAULT_.resultScale, name="resultScale", curie=DEFAULT_.curie('resultScale'),
                   model_uri=DEFAULT_.resultScale, domain=None, range=Optional[Union[str, "BiomedicalConceptResultScale"]])

slots.definition = Slot(uri=DEFAULT_.definition, name="definition", curie=DEFAULT_.curie('definition'),
                   model_uri=DEFAULT_.definition, domain=None, range=str)

slots.coding = Slot(uri=DEFAULT_.coding, name="coding", curie=DEFAULT_.curie('coding'),
                   model_uri=DEFAULT_.coding, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.system = Slot(uri=DEFAULT_.system, name="system", curie=DEFAULT_.curie('system'),
                   model_uri=DEFAULT_.system, domain=None, range=str)

slots.systemName = Slot(uri=DEFAULT_.systemName, name="systemName", curie=DEFAULT_.curie('systemName'),
                   model_uri=DEFAULT_.systemName, domain=None, range=Optional[str])

slots.code = Slot(uri=DEFAULT_.code, name="code", curie=DEFAULT_.curie('code'),
                   model_uri=DEFAULT_.code, domain=None, range=str)

slots.dataElementConcepts = Slot(uri=DEFAULT_.dataElementConcepts, name="dataElementConcepts", curie=DEFAULT_.curie('dataElementConcepts'),
                   model_uri=DEFAULT_.dataElementConcepts, domain=None, range=Optional[Union[Dict[Union[str, DataElementConceptConceptId], Union[dict, DataElementConcept]], List[Union[dict, DataElementConcept]]]])

slots.dataType = Slot(uri=DEFAULT_.dataType, name="dataType", curie=DEFAULT_.curie('dataType'),
                   model_uri=DEFAULT_.dataType, domain=None, range=Optional[Union[str, "DataElementConceptDataType"]])

slots.exampleSet = Slot(uri=DEFAULT_.exampleSet, name="exampleSet", curie=DEFAULT_.curie('exampleSet'),
                   model_uri=DEFAULT_.exampleSet, domain=None, range=Optional[Union[str, List[str]]])

slots.BiomedicalConcept_conceptId = Slot(uri=DEFAULT_.conceptId, name="BiomedicalConcept_conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.BiomedicalConcept_conceptId, domain=BiomedicalConcept, range=Union[str, BiomedicalConceptConceptId])

slots.BiomedicalConcept_href = Slot(uri=DEFAULT_.href, name="BiomedicalConcept_href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.BiomedicalConcept_href, domain=BiomedicalConcept, range=Optional[Union[str, URI]])

slots.DataElementConcept_conceptId = Slot(uri=DEFAULT_.conceptId, name="DataElementConcept_conceptId", curie=DEFAULT_.curie('conceptId'),
                   model_uri=DEFAULT_.DataElementConcept_conceptId, domain=DataElementConcept, range=Union[str, DataElementConceptConceptId])

slots.DataElementConcept_href = Slot(uri=DEFAULT_.href, name="DataElementConcept_href", curie=DEFAULT_.curie('href'),
                   model_uri=DEFAULT_.DataElementConcept_href, domain=DataElementConcept, range=Optional[Union[str, URI]])
