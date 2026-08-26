import json

from cosmoslib.cdisc_library_cache import (
    CodelistIndex,
    find_latest_package_href,
    flatten_codelist_package,
    load_codelist_cache,
    save_codelist_cache,
)

PRODUCTS_JSON = {
    "_links": {
        "packages": [
            {"href": "/mdr/ct/packages/sdtmct-2025-03-28"},
            {"href": "/mdr/ct/packages/sdtmct-2026-06-26"},
            {"href": "/mdr/ct/packages/cdashct-2026-06-26"},
            {"href": "/mdr/sdtm/1-4"},
        ]
    }
}

PACKAGE_JSON = {
    "version": "2026-06-26",
    "codelists": [
        {
            "conceptId": "C66742",
            "name": "No Yes Response",
            "submissionValue": "NY",
            "extensible": "false",
            "terms": [
                {"conceptId": "C49488", "submissionValue": "N", "preferredTerm": "No"},
                {"conceptId": "C49487", "submissionValue": "Y", "preferredTerm": "Yes"},
            ],
        },
        {
            "conceptId": "C78735",
            "name": "Route of Administration Response",
            "submissionValue": "ROUTE",
            "extensible": True,
            "terms": [
                {"conceptId": "C38288", "submissionValue": "ORAL", "preferredTerm": "Oral"},
            ],
        },
    ],
}


def test_find_latest_package_href_picks_lexically_last_matching_href():
    assert find_latest_package_href(PRODUCTS_JSON, "sdtmct") == "/mdr/ct/packages/sdtmct-2026-06-26"
    assert find_latest_package_href(PRODUCTS_JSON, "cdashct") == "/mdr/ct/packages/cdashct-2026-06-26"


def test_find_latest_package_href_returns_none_when_no_match():
    assert find_latest_package_href(PRODUCTS_JSON, "ddfct") is None


def test_flatten_codelist_package_maps_extensible_string_and_boolean():
    rows = flatten_codelist_package(PACKAGE_JSON)
    assert len(rows) == 3
    ny_rows = [r for r in rows if r["codelist_conceptId"] == "C66742"]
    assert all(r["codelist_extensible"] == "No" for r in ny_rows)
    route_rows = [r for r in rows if r["codelist_conceptId"] == "C78735"]
    assert all(r["codelist_extensible"] == "Yes" for r in route_rows)
    assert {r["codedValue"] for r in ny_rows} == {"N", "Y"}


def test_codelist_index_lookups_are_case_sensitive():
    rows = flatten_codelist_package(PACKAGE_JSON)
    index = CodelistIndex(rows)

    assert index.get_term_code("C66742", "N") == "C49488"
    assert index.get_term_code("C66742", "n") == ""  # case-sensitive, not folded

    assert index.get_term_value("C66742", "C49488") == "N"
    assert index.get_term_preferred_term("C66742", "C49488") == "No"

    assert index.get_codelist_submissionvalue("C66742") == "NY"
    assert index.get_codelist_extensible("C66742") == "No"
    assert index.get_codelist_extensible("C78735") == "Yes"


def test_codelist_index_returns_empty_string_for_unknown_keys():
    index = CodelistIndex(flatten_codelist_package(PACKAGE_JSON))
    assert index.get_term_code("NOPE", "N") == ""
    assert index.get_term_value("C66742", "NOPE") == ""
    assert index.get_codelist_submissionvalue("NOPE") == ""


def test_save_and_load_codelist_cache_round_trips(tmp_path):
    rows = flatten_codelist_package(PACKAGE_JSON)
    cache_path = str(tmp_path / "sdtm_latest_codelist_package.json")

    save_codelist_cache(cache_path, rows, fetched_at="2026-08-25T00:00:00+00:00")

    with open(cache_path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)
    assert raw["_meta"] == {"fetched_at": "2026-08-25T00:00:00+00:00"}

    loaded = load_codelist_cache(cache_path)
    assert loaded == rows
