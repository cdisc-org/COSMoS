import json
from unittest.mock import patch

from cosmoslib.ncievs_cache import NCIEVSCache

SUMMARY_RESPONSE = {
    "name": "Erythema",
    "definitions": [
        {"source": "NCI", "definition": "Redness of the skin."},
        {"source": "CDISC", "definition": "CDISC definition of erythema."},
    ],
}

SYNONYMS_RESPONSE = {
    "synonyms": [
        {"name": "Erythema", "type": "Preferred_Name"},
        {"name": "Skin Redness", "type": "Synonym"},
        {"name": "Erythema", "type": "Synonym"},
    ],
}

PARENTS_RESPONSE = [
    {"code": "C1", "name": "Skin Finding"},
    {"code": "C2", "name": "Dermatologic Finding"},
]

MINIMAL_RESPONSE = {"conceptStatus": "Retired_Concept"}


def _fake_get_api_json(href):
    if "include=summary" in href:
        return SUMMARY_RESPONSE
    if "include=synonyms" in href:
        return SYNONYMS_RESPONSE
    if href.endswith("/parents"):
        return PARENTS_RESPONSE
    if "include=minimal" in href:
        return MINIMAL_RESPONSE
    raise AssertionError(f"unexpected href {href}")


def test_get_definitions_prefers_nci_and_falls_back_through_sources(tmp_path):
    cache = NCIEVSCache(str(tmp_path / "cache.json"))
    with patch.object(cache, "get_api_json", side_effect=_fake_get_api_json):
        definition_nci, definition_cdisc = cache.get_definitions("C12345")
    assert definition_nci == "Redness of the skin."
    assert definition_cdisc == "CDISC definition of erythema."


def test_get_shortname_and_status_and_synonyms_and_parents(tmp_path):
    cache = NCIEVSCache(str(tmp_path / "cache.json"))
    with patch.object(cache, "get_api_json", side_effect=_fake_get_api_json):
        assert cache.get_shortname("C12345") == "Erythema"
        assert cache.get_concept_status("C12345") == "Retired_Concept"
        assert cache.get_preferred_term("C12345") == "Erythema"
        assert cache.get_synonyms("C12345") == "Erythema;Skin Redness"
        parent_code, parent_name = cache.get_parent_code_shortname("C12345")
        assert parent_code == "C1;C2"
        assert parent_name == "Skin Finding;Dermatologic Finding"


def test_second_call_is_served_from_memory_without_a_new_request(tmp_path):
    cache = NCIEVSCache(str(tmp_path / "cache.json"))
    with patch.object(cache, "get_api_json", side_effect=_fake_get_api_json) as mocked:
        cache.get_shortname("C12345")
        cache.get_shortname("C12345")
    assert mocked.call_count == 1


def test_save_then_reload_serves_from_disk_cache_with_no_network_call(tmp_path):
    cache_path = str(tmp_path / "cache.json")
    cache = NCIEVSCache(cache_path)
    with patch.object(cache, "get_api_json", side_effect=_fake_get_api_json):
        cache.get_shortname("C12345")
    cache.save()

    with open(cache_path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    assert payload["get_shortname:C12345"] == "Erythema"
    assert "fetched_at" in payload["_meta"]

    reloaded = NCIEVSCache(cache_path)
    with patch.object(reloaded, "get_api_json", side_effect=AssertionError("should not hit network")):
        assert reloaded.get_shortname("C12345") == "Erythema"


def test_refresh_cache_bypasses_stale_disk_entry(tmp_path):
    cache_path = str(tmp_path / "cache.json")
    with open(cache_path, "w", encoding="utf-8") as fh:
        json.dump({"get_shortname:C12345": "Stale Name"}, fh)

    cache = NCIEVSCache(cache_path, refresh_cache=True)
    with patch.object(cache, "get_api_json", side_effect=_fake_get_api_json):
        assert cache.get_shortname("C12345") == "Erythema"


def test_use_cache_false_never_reads_or_writes_disk(tmp_path):
    cache_path = str(tmp_path / "cache.json")
    with open(cache_path, "w", encoding="utf-8") as fh:
        json.dump({"get_shortname:C12345": "Stale Name"}, fh)

    cache = NCIEVSCache(cache_path, use_cache=False)
    with patch.object(cache, "get_api_json", side_effect=_fake_get_api_json):
        assert cache.get_shortname("C12345") == "Erythema"
    cache.save()

    with open(cache_path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    assert payload == {"get_shortname:C12345": "Stale Name"}


def test_lookup_failure_degrades_to_empty_default_instead_of_raising(tmp_path):
    cache = NCIEVSCache(str(tmp_path / "cache.json"))

    def _raise(href):
        raise Exception("503 Service Unavailable")

    with patch.object(cache, "get_api_json", side_effect=_raise):
        assert cache.get_shortname("C99999") == ""
        assert cache.get_concept_status("C99999") == ""
        assert cache.get_synonyms("C99999") == ""
        assert cache.get_definitions("C99999") == ["", ""]
        assert cache.get_parent_code_shortname("C99999") == ["", ""]


def test_ncievs_cache_still_exposes_the_base_client_api(tmp_path):
    cache = NCIEVSCache(str(tmp_path / "cache.json"))
    assert cache.base_api_url == "https://api-evsrest.nci.nih.gov/api/v1"
