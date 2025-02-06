# Auto generated from cosmos_bc_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-02-06T12:43:39
# Schema: COSMoS-Biomedical-Concepts-Schema
#
# id: https://www.cdisc.org/cosmos/biomedical_concept_v1.0
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
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
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

from linkml_runtime.linkml_model.types import Date, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
COSMOS_BC = CurieNamespace('cosmos_bc', 'https://www.cdisc.org/cosmos/biomedical_concept_v1.0')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = COSMOS_BC


# Types

# Class references
class BiomedicalConceptConceptId(extended_str):
    pass


class DataElementConceptConceptId(extended_str):
    pass


@dataclass(repr=False)
class BiomedicalConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_BC["BiomedicalConcept"]
    class_class_curie: ClassVar[str] = "cosmos_bc:BiomedicalConcept"
    class_name: ClassVar[str] = "BiomedicalConcept"
    class_model_uri: ClassVar[URIRef] = COSMOS_BC.BiomedicalConcept

    conceptId: Union[str, BiomedicalConceptConceptId] = None
    packageDate: Union[str, XSDDate] = None
    packageType: Union[str, "PackageTypeEnum"] = None
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
        if not isinstance(self.packageType, PackageTypeEnum):
            self.packageType = PackageTypeEnum(self.packageType)

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


@dataclass(repr=False)
class Coding(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_BC["Coding"]
    class_class_curie: ClassVar[str] = "cosmos_bc:Coding"
    class_name: ClassVar[str] = "Coding"
    class_model_uri: ClassVar[URIRef] = COSMOS_BC.Coding

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


@dataclass(repr=False)
class DataElementConcept(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COSMOS_BC["DataElementConcept"]
    class_class_curie: ClassVar[str] = "cosmos_bc:DataElementConcept"
    class_name: ClassVar[str] = "DataElementConcept"
    class_model_uri: ClassVar[URIRef] = COSMOS_BC.DataElementConcept

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
class PackageTypeEnum(EnumDefinitionImpl):

    bc = PermissibleValue(text="bc")

    _defn = EnumDefinition(
        name="PackageTypeEnum",
    )

class BiomedicalConceptResultScaleEnum(EnumDefinitionImpl):

    Ordinal = PermissibleValue(text="Ordinal")
    Narrative = PermissibleValue(text="Narrative")
    Nominal = PermissibleValue(text="Nominal")
    Quantitative = PermissibleValue(text="Quantitative")
    Temporal = PermissibleValue(text="Temporal")

    _defn = EnumDefinition(
        name="BiomedicalConceptResultScaleEnum",
    )

class DataElementConceptDataTypeEnum(EnumDefinitionImpl):

    boolean = PermissibleValue(text="boolean")
    date = PermissibleValue(text="date")
    datetime = PermissibleValue(text="datetime")
    decimal = PermissibleValue(text="decimal")
    duration = PermissibleValue(text="duration")
    integer = PermissibleValue(text="integer")
    string = PermissibleValue(text="string")
    uri = PermissibleValue(text="uri")

    _defn = EnumDefinition(
        name="DataElementConceptDataTypeEnum",
    )

# Slots
class slots:
    pass

slots.conceptId = Slot(uri=COSMOS_BC.conceptId, name="conceptId", curie=COSMOS_BC.curie('conceptId'),
                   model_uri=COSMOS_BC.conceptId, domain=None, range=URIRef,
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.ncitCode = Slot(uri=COSMOS_BC.ncitCode, name="ncitCode", curie=COSMOS_BC.curie('ncitCode'),
                   model_uri=COSMOS_BC.ncitCode, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.href = Slot(uri=COSMOS_BC.href, name="href", curie=COSMOS_BC.curie('href'),
                   model_uri=COSMOS_BC.href, domain=None, range=Optional[Union[str, URI]])

slots.packageDate = Slot(uri=COSMOS_BC.packageDate, name="packageDate", curie=COSMOS_BC.curie('packageDate'),
                   model_uri=COSMOS_BC.packageDate, domain=None, range=Union[str, XSDDate])

slots.packageType = Slot(uri=COSMOS_BC.packageType, name="packageType", curie=COSMOS_BC.curie('packageType'),
                   model_uri=COSMOS_BC.packageType, domain=None, range=Union[str, "PackageTypeEnum"])

slots.categories = Slot(uri=COSMOS_BC.categories, name="categories", curie=COSMOS_BC.curie('categories'),
                   model_uri=COSMOS_BC.categories, domain=None, range=Union[str, List[str]])

slots.parentConceptId = Slot(uri=COSMOS_BC.parentConceptId, name="parentConceptId", curie=COSMOS_BC.curie('parentConceptId'),
                   model_uri=COSMOS_BC.parentConceptId, domain=None, range=Optional[str])

slots.shortName = Slot(uri=COSMOS_BC.shortName, name="shortName", curie=COSMOS_BC.curie('shortName'),
                   model_uri=COSMOS_BC.shortName, domain=None, range=str)

slots.synonyms = Slot(uri=COSMOS_BC.synonyms, name="synonyms", curie=COSMOS_BC.curie('synonyms'),
                   model_uri=COSMOS_BC.synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.resultScales = Slot(uri=COSMOS_BC.resultScales, name="resultScales", curie=COSMOS_BC.curie('resultScales'),
                   model_uri=COSMOS_BC.resultScales, domain=None, range=Optional[Union[Union[str, "BiomedicalConceptResultScaleEnum"], List[Union[str, "BiomedicalConceptResultScaleEnum"]]]])

slots.definition = Slot(uri=COSMOS_BC.definition, name="definition", curie=COSMOS_BC.curie('definition'),
                   model_uri=COSMOS_BC.definition, domain=None, range=str)

slots.coding = Slot(uri=COSMOS_BC.coding, name="coding", curie=COSMOS_BC.curie('coding'),
                   model_uri=COSMOS_BC.coding, domain=None, range=Optional[Union[Union[dict, Coding], List[Union[dict, Coding]]]])

slots.system = Slot(uri=COSMOS_BC.system, name="system", curie=COSMOS_BC.curie('system'),
                   model_uri=COSMOS_BC.system, domain=None, range=str)

slots.systemName = Slot(uri=COSMOS_BC.systemName, name="systemName", curie=COSMOS_BC.curie('systemName'),
                   model_uri=COSMOS_BC.systemName, domain=None, range=Optional[str])

slots.code = Slot(uri=COSMOS_BC.code, name="code", curie=COSMOS_BC.curie('code'),
                   model_uri=COSMOS_BC.code, domain=None, range=str)

slots.dataElementConcepts = Slot(uri=COSMOS_BC.dataElementConcepts, name="dataElementConcepts", curie=COSMOS_BC.curie('dataElementConcepts'),
                   model_uri=COSMOS_BC.dataElementConcepts, domain=None, range=Optional[Union[Dict[Union[str, DataElementConceptConceptId], Union[dict, DataElementConcept]], List[Union[dict, DataElementConcept]]]])

slots.dataType = Slot(uri=COSMOS_BC.dataType, name="dataType", curie=COSMOS_BC.curie('dataType'),
                   model_uri=COSMOS_BC.dataType, domain=None, range=Union[str, "DataElementConceptDataTypeEnum"])

slots.exampleSet = Slot(uri=COSMOS_BC.exampleSet, name="exampleSet", curie=COSMOS_BC.curie('exampleSet'),
                   model_uri=COSMOS_BC.exampleSet, domain=None, range=Optional[Union[str, List[str]]])

slots.BiomedicalConcept_conceptId = Slot(uri=COSMOS_BC.conceptId, name="BiomedicalConcept_conceptId", curie=COSMOS_BC.curie('conceptId'),
                   model_uri=COSMOS_BC.BiomedicalConcept_conceptId, domain=BiomedicalConcept, range=Union[str, BiomedicalConceptConceptId],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.BiomedicalConcept_ncitCode = Slot(uri=COSMOS_BC.ncitCode, name="BiomedicalConcept_ncitCode", curie=COSMOS_BC.curie('ncitCode'),
                   model_uri=COSMOS_BC.BiomedicalConcept_ncitCode, domain=BiomedicalConcept, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.BiomedicalConcept_href = Slot(uri=COSMOS_BC.href, name="BiomedicalConcept_href", curie=COSMOS_BC.curie('href'),
                   model_uri=COSMOS_BC.BiomedicalConcept_href, domain=BiomedicalConcept, range=Optional[Union[str, URI]])

slots.DataElementConcept_conceptId = Slot(uri=COSMOS_BC.conceptId, name="DataElementConcept_conceptId", curie=COSMOS_BC.curie('conceptId'),
                   model_uri=COSMOS_BC.DataElementConcept_conceptId, domain=DataElementConcept, range=Union[str, DataElementConceptConceptId],
                   pattern=re.compile(r'^(C[0123456789]+|NEW_[A-Z]*[0123456789]*)$'))

slots.DataElementConcept_ncitCode = Slot(uri=COSMOS_BC.ncitCode, name="DataElementConcept_ncitCode", curie=COSMOS_BC.curie('ncitCode'),
                   model_uri=COSMOS_BC.DataElementConcept_ncitCode, domain=DataElementConcept, range=Optional[str],
                   pattern=re.compile(r'^(C[0123456789]+)$'))

slots.DataElementConcept_href = Slot(uri=COSMOS_BC.href, name="DataElementConcept_href", curie=COSMOS_BC.curie('href'),
                   model_uri=COSMOS_BC.DataElementConcept_href, domain=DataElementConcept, range=Optional[Union[str, URI]])