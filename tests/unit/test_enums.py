import json
import os

from cosmoslib.enums import build_enum_index, exists_enum_term, load_enum_cache, save_enum_cache

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_DIR = os.path.join(REPO_ROOT, "model")

SCHEMA_PATHS = [
    os.path.join(MODEL_DIR, "cosmos_bc_model.yaml"),
    os.path.join(MODEL_DIR, "cosmos_sdtm_model.yaml"),
    os.path.join(MODEL_DIR, "cosmos_crf_model.yaml"),
]


def test_build_enum_index_strips_enum_suffix_and_merges_across_schemas():
    index = build_enum_index(SCHEMA_PATHS)

    # PackageTypeEnum is declared separately (with a different single value) in each of
    # the three schemas; the merged "PackageType" key carries all three.
    assert index["PackageType"] == ["bc", "crf", "sdtm"]

    assert index["BiomedicalConceptResultScale"] == ["Narrative", "Nominal", "Ordinal", "Quantitative", "Temporal"]
    assert "text" in index["SDTMVariableDataType"]
    assert "Multiple" in index["SelectionType"]


def test_exists_enum_term_matches_known_and_rejects_unknown_values():
    index = build_enum_index(SCHEMA_PATHS)

    assert exists_enum_term(index, "BiomedicalConceptResultScale", "Ordinal") is True
    assert exists_enum_term(index, "BiomedicalConceptResultScale", "NotAValue") is False
    assert exists_enum_term(index, "NoSuchEnum", "Ordinal") is False


def test_save_and_load_enum_cache_round_trips(tmp_path):
    index = build_enum_index(SCHEMA_PATHS)
    cache_path = str(tmp_path / "linkml_enums.json")

    save_enum_cache(cache_path, index, fetched_at="2026-08-25T00:00:00+00:00")

    with open(cache_path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    assert raw["_meta"] == {"fetched_at": "2026-08-25T00:00:00+00:00"}

    loaded = load_enum_cache(cache_path)
    assert "_meta" not in loaded
    assert loaded == index
