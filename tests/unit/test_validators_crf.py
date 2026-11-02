from unittest.mock import patch

import pandas as pd

from cosmoslib.validators.crf import (
    find_crf_pointing_to_retired_bc,
    find_duplicate_crf,
    find_unresolved_crf_bc,
    find_unresolved_crf_bc_dec,
    find_unresolved_crf_sdtm,
    run_crf_validation,
)


def _crf_row(crf_group_id, bc_id="B1", dec_id=None, short_name="Alpha", crf_item="ITEM1",
             vlm_group_id=None, package_date="R1", standard="CDASHIG"):
    return {
        "crf_group_id": crf_group_id, "bc_id": bc_id, "dec_id": dec_id, "short_name": short_name,
        "crf_item": crf_item, "vlm_group_id": vlm_group_id, "package_date": package_date,
        "domain": "AE", "order_number": 1, "standard": standard, "standard_start_version": "2-1",
        "standard_end_version": "", "_excel_file_": "wb.xlsx", "_tab_": "CRF_TEST",
    }


def test_find_unresolved_crf_bc():
    df = pd.DataFrame([_crf_row("G1", bc_id="NOPE")])
    findings = find_unresolved_crf_bc(df, {"B1"})
    assert len(findings) == 1
    assert findings[0]["check"] == "UNRESOLVED_CRF_BC"


def test_find_unresolved_crf_bc_dec_has_no_retired_suppression():
    # Unlike SDTM's equivalent check, CRF never suppresses on the row's own [RETIRED] tag.
    df = pd.DataFrame([_crf_row("G1", dec_id="D1", short_name="X [RETIRED]")])
    findings = find_unresolved_crf_bc_dec(df, valid_bc_dec_pairs=set())
    assert len(findings) == 1


def test_find_unresolved_crf_sdtm_only_checks_rows_with_a_vlm_group_id():
    df = pd.DataFrame([
        _crf_row("G1", vlm_group_id=None),
        _crf_row("G2", vlm_group_id="NOPE"),
    ])
    findings = find_unresolved_crf_sdtm(df, {"SOMETHING"})
    assert len(findings) == 1
    assert findings[0]["identifier"].startswith("domain=AE, crf_group_id=G2")


def test_find_duplicate_crf_groups_by_standard_not_domain():
    df = pd.DataFrame([
        _crf_row("G1", crf_item="ITEM1", standard="CDASHIG"),
        _crf_row("G1", crf_item="ITEM1", standard="CDASHIG"),
        _crf_row("G1", crf_item="ITEM1", standard="SDTMIG"),  # different standard -> not a dup
    ])
    findings = find_duplicate_crf(df)
    assert len(findings) == 2


def test_find_crf_pointing_to_retired_bc_has_no_retired_suppression():
    df = pd.DataFrame([_crf_row("G1", bc_id="RETIRED_BC", short_name="Already [RETIRED]")])
    findings = find_crf_pointing_to_retired_bc(df, {"RETIRED_BC"})
    assert len(findings) == 1


def test_run_crf_validation_wires_all_checks_together():
    bc_df = pd.DataFrame([
        {"bc_id": "B1", "parent_bc_id": None, "dec_id": None, "short_name": "Alpha",
         "package_date": "R1", "_excel_file_": "bc.xlsx", "_tab_": "BC", "bc_categories": "Cat"},
    ])
    sdtm_df = pd.DataFrame([{"vlm_group_id": "SDTM1", "_excel_file_": "sdtm.xlsx", "_tab_": "SDTM"}])
    crf_df = pd.DataFrame([_crf_row("G1", bc_id="NOPE")])

    with patch("cosmoslib.validators.crf.load_manifest_corpus", side_effect=[bc_df, sdtm_df, crf_df]), \
         patch("cosmoslib.validators.crf.merge_with_latest", side_effect=lambda df, *a, **k: df):
        findings = run_crf_validation(
            manifest_paths=["crf.yaml"], bc_manifest_paths=["bc.yaml"], sdtm_manifest_paths=["sdtm.yaml"],
            bc_latest={"file": "x", "range": "y"}, sdtm_latest={"file": "x", "range": "y"},
        )
    checks = {f["check"] for f in findings}
    assert "UNRESOLVED_CRF_BC" in checks
