import os

import yaml

from cosmoslib.json_roundtrip import bc_rows_from_json, crf_rows_from_json, sdtm_rows_from_json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_bc_rows_from_json_round_trips_a_real_published_bc(tmp_path):
    path = os.path.join(REPO_ROOT, "yaml", "20260714_r18", "bc", "bc__c191040.yaml")
    with open(path, "r", encoding="utf-8") as fh:
        bc_json = yaml.safe_load(fh)

    rows = bc_rows_from_json(bc_json)

    assert len(rows) == 4
    assert all(r["bc_id"] == "C191040" for r in rows)
    assert all(r["parent_bc_id"] == "C118969" for r in rows)
    assert rows[0]["dec_id"] == "C25372"
    assert rows[0]["dec_label"] == "Category"
    assert rows[0]["example_set"] == "PASI FREDRIKSSON"
    assert rows[1]["dec_label"] == "Collection Date Time"
    assert rows[1]["example_set"] == ""


def test_bc_rows_from_json_emits_one_blank_dec_row_when_there_are_no_decs():
    rows = bc_rows_from_json({"conceptId": "C1", "href": "https://x/C1", "shortName": "Alpha"})
    assert len(rows) == 1
    assert rows[0]["dec_id"] == ""
    assert rows[0]["bc_id"] == "C1"


def test_bc_rows_from_json_uses_links_when_present():
    # Matches the href shape scripts/create_cosmos_bc_excel.py's get_bc_data() already
    # relies on (.split("/")[-2] for the package date) - the date isn't the href's last
    # path segment.
    bc = {
        "_links": {
            "parentPackage": {"href": "/mdr/bc/packages/2026-07-14/biomedicalconcepts"},
            "parentBiomedicalConcept": {"href": "/mdr/bc/biomedicalconcepts/C999"},
        },
        "conceptId": "C1",
        "href": "https://x/C1",
    }
    rows = bc_rows_from_json(bc)
    assert rows[0]["parent_bc_id"] == "C999"
    assert rows[0]["package_date"] == "2026-07-14"


def test_sdtm_rows_from_json_round_trips_a_real_published_specialization():
    path = os.path.join(REPO_ROOT, "yaml", "20260714_r18", "sdtm", "sdtm_pasi03headscaling.yaml")
    with open(path, "r", encoding="utf-8") as fh:
        sdtm_json = yaml.safe_load(fh)

    rows = sdtm_rows_from_json(sdtm_json)

    assert len(rows) == 8
    assert rows[0]["sdtm_variable"] == "RSTESTCD"
    assert rows[0]["codelist"] == "C190934"
    assert rows[0]["codelist_submission_value"] == "PASI03TC"
    assert rows[0]["assigned_term"] == "C191068"
    assert rows[0]["assigned_value"] == "PASI0303"
    assert rows[0]["comparator"] == "EQ"
    assert rows[0]["mandatory_variable"] == "Y"
    assert rows[0]["order"] == 1
    assert rows[1]["order"] == 2


def test_sdtm_rows_from_json_handles_missing_optional_nested_objects():
    rows = sdtm_rows_from_json({"datasetSpecializationId": "G1", "variables": [{"name": "VAR1"}]})
    assert len(rows) == 1
    assert rows[0]["codelist"] == ""
    assert rows[0]["assigned_term"] == ""
    assert rows[0]["subject"] == ""
    assert rows[0]["mandatory_variable"] == ""  # missing boolean -> blank, not "N"


def test_crf_rows_from_json_maps_items_and_nested_objects():
    crf = {
        "packageDate": "2026-06-30",
        "crfSpecializationId": "AE_NORMALIZED",
        "domain": "AE",
        "items": [
            {
                "name": "AESEV",
                "variableName": "AESEV",
                "questionText": "What is the severity?",
                "mandatoryVariable": False,
                "codelist": {"conceptId": "C66769", "submissionValue": "AESEV"},
                "valueList": [
                    {"displayValue": "Mild", "value": "MILD"},
                    {"displayValue": "Severe", "value": "SEVERE"},
                ],
                "sdtmTarget": {"sdtmAnnotation": "AESEV", "sdtmVariables": ["AESEV"]},
            },
        ],
    }
    rows = crf_rows_from_json(crf)
    assert len(rows) == 1
    row = rows[0]
    assert row["crf_group_id"] == "AE_NORMALIZED"
    assert row["crf_item"] == "AESEV"
    assert row["mandatory_variable"] == "N"
    assert row["codelist"] == "C66769"
    assert row["value_display_list"] == "Mild;Severe"
    assert row["value_list"] == "MILD;SEVERE"
    assert row["sdtm_annotation"] == "AESEV"
    assert row["sdtm_target_variable"] == "AESEV"


def test_crf_rows_from_json_handles_item_with_no_nested_objects():
    rows = crf_rows_from_json({"crfSpecializationId": "G1", "items": [{"name": "ITEM1"}]})
    assert len(rows) == 1
    assert rows[0]["codelist"] == ""
    assert rows[0]["prepopulated_term"] == ""
    assert rows[0]["sdtm_annotation"] == ""
    assert rows[0]["mandatory_variable"] == ""
