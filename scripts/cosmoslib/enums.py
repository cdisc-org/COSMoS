"""
LinkML enum permissible-value lookup, replacing utilities/get_latest_enums_linkml.sas
(which parsed the *generated* JSON Schema files via a SAS JSON libname engine) and the
exists_enum_term() FCMP function in utilities/create_functions.sas.

Reads enums directly from the canonical model/cosmos_{bc,sdtm,crf}_model.yaml schemas via
linkml_runtime.SchemaView, rather than the generated JSON Schema — one less dependency on
the Windows-only gen-jsonschema regeneration step, and the same permissible values either
way. Matches the SAS script's `enum = tranwrd(enum, "Enum", "")` naming: callers use
"BiomedicalConceptResultScale", not "BiomedicalConceptResultScaleEnum", per the
exists_enum_term("BiomedicalConceptResultScale", value) call sites in
generate_yaml_from_{bc,sdtm}.sas.
"""

import json
import os

from linkml_runtime.utils.schemaview import SchemaView


def build_enum_index(schema_paths):
    """Returns {enum_name: sorted [permissible values]}, merged across schema_paths."""
    index = {}
    for schema_path in schema_paths:
        view = SchemaView(schema_path)
        for enum_name, enum_def in view.all_enums().items():
            key = enum_name.replace("Enum", "")
            index.setdefault(key, set()).update(enum_def.permissible_values.keys())
    return {name: sorted(values) for name, values in index.items()}


def save_enum_cache(path, enum_index, fetched_at):
    payload = dict(enum_index)
    payload["_meta"] = {"fetched_at": fetched_at}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")


def load_enum_cache(path):
    with open(path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    payload.pop("_meta", None)
    return payload


def exists_enum_term(enum_index, enum, value):
    return value in enum_index.get(enum, ())
