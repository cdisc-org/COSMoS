import json

from cosmoslib.relations_cache import (
    RelationsIndex,
    build_relation_caches,
    extract_relationships,
    load_relation_cache,
    save_relation_cache,
)

SPECIALIZATION_JSON = {
    "datasetSpecializationId": "PASI03HEADEDEMA",
    "variables": [
        {"name": "AEDECOD", "relationship": {
            "subject": "AEDECOD", "linkingPhrase": "is decoded by the value in",
            "predicateTerm": "decodes", "object": "AETERM",
        }},
        {"name": "AETERM"},  # no relationship
    ],
}

SPECIALIZATION_JSON_2 = {
    "datasetSpecializationId": "OTHER01",
    "variables": [
        {"name": "X", "relationship": {
            "subject": "X", "linkingPhrase": "is decoded by the value in",
            "predicateTerm": "codes", "object": "Y",  # same phrase, different (smaller) term
        }},
    ],
}


def test_extract_relationships_skips_variables_without_one():
    relationships = extract_relationships(SPECIALIZATION_JSON)
    assert relationships == [
        {"subject": "AEDECOD", "linkingPhrase": "is decoded by the value in",
         "predicateTerm": "decodes", "object": "AETERM"}
    ]


def test_build_relation_caches_dedupes_and_sorts():
    relationships = extract_relationships(SPECIALIZATION_JSON) + extract_relationships(SPECIALIZATION_JSON_2)
    caches = build_relation_caches(relationships)
    assert caches["linkingphrases_predterms"] == [
        ("is decoded by the value in", "codes"),
        ("is decoded by the value in", "decodes"),
    ]
    assert caches["predicateterms"] == ["codes", "decodes"]
    assert caches["linkingphrases"] == ["is decoded by the value in"]


def test_relations_index_get_predicateterm_picks_alphabetically_first_on_ambiguity():
    # SAS-QUIRK(preserved): a linkingPhrase mapping to more than one predicateTerm resolves
    # to the alphabetically-first term, matching the SAS hash's keep-first-on-duplicate-key
    # behavior over data sorted by (linkingPhrase, predicateTerm).
    index = RelationsIndex(
        linkingphrases_predterms=[
            ["is decoded by the value in", "decodes"],
            ["is decoded by the value in", "codes"],
        ],
        predicateterms=["codes", "decodes"],
    )
    assert index.get_predicateterm("is decoded by the value in") == "codes"


def test_relations_index_existence_checks():
    index = RelationsIndex(
        linkingphrases_predterms=[["is decoded by the value in", "decodes"]],
        predicateterms=["decodes"],
    )
    assert index.exists_predicaterm_linkingphrase("is decoded by the value in", "decodes") is True
    assert index.exists_predicaterm_linkingphrase("is decoded by the value in", "codes") is False
    assert index.exists_predicateterm("decodes") is True
    assert index.exists_predicateterm("nope") is False
    assert index.get_predicateterm("no such phrase") == ""


def test_save_and_load_relation_cache_round_trips(tmp_path):
    path = str(tmp_path / "sdtm_predicateterms.json")
    save_relation_cache(path, ["decodes", "codes"], fetched_at="2026-08-25T00:00:00+00:00")

    with open(path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    assert raw["_meta"] == {"fetched_at": "2026-08-25T00:00:00+00:00"}

    assert load_relation_cache(path) == ["decodes", "codes"]
