# Auto generated from cosmos_bc_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-08-30T12:01:16
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
class IdentifiableThingConceptId(extended_str):
    pass


class BiomedicalConceptConceptId(IdentifiableThingConceptId):
    pass


class DataElementConceptConceptId(IdentifiableThingConceptId):
    pass


@dataclass
class IdentifiableThing(YAMLRoot):
    """
    A databased entity, concept or class. This is a generic class that is the root of all the other classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/IdentifiableThing")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "IdentifiableThing"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/IdentifiableThing")

    concept_id: Union[str, IdentifiableThingConceptId] = None
    concept_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, IdentifiableThingConceptId):
            self.concept_id = IdentifiableThingConceptId(self.concept_id)

        if self.concept_uri is not None and not isinstance(self.concept_uri, URI):
            self.concept_uri = URI(self.concept_uri)

        super().__post_init__(**kwargs)


@dataclass
class BiomedicalConcept(IdentifiableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/BiomedicalConcept")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BiomedicalConcept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/BiomedicalConcept")

    concept_id: Union[str, BiomedicalConceptConceptId] = None
    package_date: Union[str, XSDDate] = None
    bc_category: Union[str, List[str]] = None
    short_name: str = None
    definition: str = None
    parent_id: Optional[str] = None
    synonym: Optional[Union[str, List[str]]] = empty_list()
    result_scale: Optional[Union[str, "BiomedicalConceptResultScale"]] = None
    coding: Optional[Union[Union[dict, "Coding"], List[Union[dict, "Coding"]]]] = empty_list()
    data_element_concepts: Optional[Union[Dict[Union[str, DataElementConceptConceptId], Union[dict, "DataElementConcept"]], List[Union[dict, "DataElementConcept"]]]] = empty_dict()
    concept_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, BiomedicalConceptConceptId):
            self.concept_id = BiomedicalConceptConceptId(self.concept_id)

        if self._is_empty(self.package_date):
            self.MissingRequiredField("package_date")
        if not isinstance(self.package_date, XSDDate):
            self.package_date = XSDDate(self.package_date)

        if self._is_empty(self.bc_category):
            self.MissingRequiredField("bc_category")
        if not isinstance(self.bc_category, list):
            self.bc_category = [self.bc_category] if self.bc_category is not None else []
        self.bc_category = [v if isinstance(v, str) else str(v) for v in self.bc_category]

        if self._is_empty(self.short_name):
            self.MissingRequiredField("short_name")
        if not isinstance(self.short_name, str):
            self.short_name = str(self.short_name)

        if self._is_empty(self.definition):
            self.MissingRequiredField("definition")
        if not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.parent_id is not None and not isinstance(self.parent_id, str):
            self.parent_id = str(self.parent_id)

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, str) else str(v) for v in self.synonym]

        if self.result_scale is not None and not isinstance(self.result_scale, BiomedicalConceptResultScale):
            self.result_scale = BiomedicalConceptResultScale(self.result_scale)

        if not isinstance(self.coding, list):
            self.coding = [self.coding] if self.coding is not None else []
        self.coding = [v if isinstance(v, Coding) else Coding(**as_dict(v)) for v in self.coding]

        self._normalize_inlined_as_list(slot_name="data_element_concepts", slot_type=DataElementConcept, key_name="concept_id", keyed=True)

        if self.concept_uri is not None and not isinstance(self.concept_uri, URI):
            self.concept_uri = URI(self.concept_uri)

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
    system_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, str):
            self.code = str(self.code)

        if self._is_empty(self.system):
            self.MissingRequiredField("system")
        if not isinstance(self.system, str):
            self.system = str(self.system)

        if self.system_name is not None and not isinstance(self.system_name, str):
            self.system_name = str(self.system_name)

        super().__post_init__(**kwargs)


@dataclass
class DataElementConcept(IdentifiableThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/DataElementConcept")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataElementConcept"
    class_model_uri: ClassVar[URIRef] = URIRef("https://www.cdisc.org/cosmos/1-0/DataElementConcept")

    concept_id: Union[str, DataElementConceptConceptId] = None
    label: str = None
    data_type: Optional[Union[str, "DataElementConceptDataType"]] = None
    example_set: Optional[Union[str, List[str]]] = empty_list()
    concept_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.concept_id):
            self.MissingRequiredField("concept_id")
        if not isinstance(self.concept_id, DataElementConceptConceptId):
            self.concept_id = DataElementConceptConceptId(self.concept_id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.data_type is not None and not isinstance(self.data_type, DataElementConceptDataType):
            self.data_type = DataElementConceptDataType(self.data_type)

        if not isinstance(self.example_set, list):
            self.example_set = [self.example_set] if self.example_set is not None else []
        self.example_set = [v if isinstance(v, str) else str(v) for v in self.example_set]

        if self.concept_uri is not None and not isinstance(self.concept_uri, URI):
            self.concept_uri = URI(self.concept_uri)

        super().__post_init__(**kwargs)


# Enumerations
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

slots.concept_id = Slot(uri=DEFAULT_.concept_id, name="concept_id", curie=DEFAULT_.curie('concept_id'),
                   model_uri=DEFAULT_.concept_id, domain=None, range=URIRef)

slots.concept_uri = Slot(uri=DEFAULT_.concept_uri, name="concept_uri", curie=DEFAULT_.curie('concept_uri'),
                   model_uri=DEFAULT_.concept_uri, domain=None, range=Optional[Union[str, URI]])

slots.package_date = Slot(uri=DEFAULT_.package_date, name="package_date", curie=DEFAULT_.curie('package_date'),
                   model_uri=DEFAULT_.package_date, domain=None, range=Union[str, XSDDate])

slots.bc_category = Slot(uri=DEFAULT_.bc_category, name="bc_category", curie=DEFAULT_.curie('bc_category'),
                   model_uri=DEFAULT_.bc_category, domain=None, range=Union[str, List[str]])

slots.parent_id = Slot(uri=DEFAULT_.parent_id, name="parent_id", curie=DEFAULT_.curie('parent_id'),
                   model_uri=DEFAULT_.parent_id, domain=None, range=Optional[str])

slots.short_name = Slot(uri=DEFAULT_.short_name, name="short_name", curie=DEFAULT_.curie('short_name'),
                   model_uri=DEFAULT_.short_name, domain=None, range=str)

slots.synonym = Slot(uri=DEFAULT_.synonym, name="synonym", curie=DEFAULT_.curie('synonym'),
                   model_uri=DEFAULT_.synonym, domain=None, range=Optional[Union[str, List[str]]])

slots.result_scale = Slot(uri=DEFAULT_.result_scale, name="result_scale", curie=DEFAULT_.curie('result_scale'),
                   model_uri=DEFAULT_.result_scale, domain=None, range=Optional[Union[str, "BiomedicalConceptResultScale"]])

slots.definition = Slot(uri=DEFAULT_.definition, name="definition", curie=DEFAULT_.curie('definition'),
                   model_uri=DEFAULT_.definition, domain=None, range=str)

slots.coding = Slot(uri=DEFAULT_.coding, name="coding", curie=DEFAULT_.curie('coding'),
                   model_uri=DEFAULT_.coding, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.system = Slot(uri=DEFAULT_.system, name="system", curie=DEFAULT_.curie('system'),
                   model_uri=DEFAULT_.system, domain=None, range=str)

slots.system_name = Slot(uri=DEFAULT_.system_name, name="system_name", curie=DEFAULT_.curie('system_name'),
                   model_uri=DEFAULT_.system_name, domain=None, range=Optional[str])

slots.code = Slot(uri=DEFAULT_.code, name="code", curie=DEFAULT_.curie('code'),
                   model_uri=DEFAULT_.code, domain=None, range=str)

slots.data_element_concepts = Slot(uri=DEFAULT_.data_element_concepts, name="data_element_concepts", curie=DEFAULT_.curie('data_element_concepts'),
                   model_uri=DEFAULT_.data_element_concepts, domain=None, range=Optional[Union[Dict[Union[str, DataElementConceptConceptId], Union[dict, DataElementConcept]], List[Union[dict, DataElementConcept]]]])

slots.label = Slot(uri=DEFAULT_.label, name="label", curie=DEFAULT_.curie('label'),
                   model_uri=DEFAULT_.label, domain=None, range=str)

slots.data_type = Slot(uri=DEFAULT_.data_type, name="data_type", curie=DEFAULT_.curie('data_type'),
                   model_uri=DEFAULT_.data_type, domain=None, range=Optional[Union[str, "DataElementConceptDataType"]])

slots.example_set = Slot(uri=DEFAULT_.example_set, name="example_set", curie=DEFAULT_.curie('example_set'),
                   model_uri=DEFAULT_.example_set, domain=None, range=Optional[Union[str, List[str]]])

slots.BiomedicalConcept_concept_id = Slot(uri=DEFAULT_.concept_id, name="BiomedicalConcept_concept_id", curie=DEFAULT_.curie('concept_id'),
                   model_uri=DEFAULT_.BiomedicalConcept_concept_id, domain=BiomedicalConcept, range=Union[str, BiomedicalConceptConceptId])

slots.BiomedicalConcept_concept_uri = Slot(uri=DEFAULT_.concept_uri, name="BiomedicalConcept_concept_uri", curie=DEFAULT_.curie('concept_uri'),
                   model_uri=DEFAULT_.BiomedicalConcept_concept_uri, domain=BiomedicalConcept, range=Optional[Union[str, URI]])

slots.DataElementConcept_concept_id = Slot(uri=DEFAULT_.concept_id, name="DataElementConcept_concept_id", curie=DEFAULT_.curie('concept_id'),
                   model_uri=DEFAULT_.DataElementConcept_concept_id, domain=DataElementConcept, range=Union[str, DataElementConceptConceptId])

slots.DataElementConcept_concept_uri = Slot(uri=DEFAULT_.concept_uri, name="DataElementConcept_concept_uri", curie=DEFAULT_.curie('concept_uri'),
                   model_uri=DEFAULT_.DataElementConcept_concept_uri, domain=DataElementConcept, range=Optional[Union[str, URI]])
