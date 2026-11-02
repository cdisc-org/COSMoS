from unittest.mock import patch

import pandas as pd

from cosmoslib.validators.sdtm import (
    find_duplicate_sdtm,
    find_sdtm_pointing_to_retired_bc,
    find_unresolved_sdtm_bc,
    find_unresolved_sdtm_bc_dec,
    merge_subsets,
    run_sdtm_validation,
)


def _sdtm_row(vlm_group_id, bc_id="B1", dec_id=None, short_name="Alpha", sdtm_variable="VAR1",
              package_date="R1", subset_codelist=None):
    return {
        "vlm_group_id": vlm_group_id, "bc_id": bc_id, "dec_id": dec_id, "short_name": short_name,
        "sdtm_variable": sdtm_variable, "package_date": package_date, "domain": "SC",
        "_excel_file_": "wb.xlsx", "_tab_": "SDTM_TEST", "subset_codelist": subset_codelist,
        "sdtmig_start_version": "3-2", "sdtmig_end_version": "",
    }


def test_find_unresolved_sdtm_bc():
    df = pd.DataFrame([_sdtm_row("G1", bc_id="NOPE")])
    findings = find_unresolved_sdtm_bc(df, {"B1"})
    assert len(findings) == 1
    assert findings[0]["check"] == "UNRESOLVED_SDTM_BC"


def test_find_unresolved_sdtm_bc_dec_suppression_default_true():
    df = pd.DataFrame([_sdtm_row("G1", dec_id="D1", short_name="X [RETIRED]")])
    assert find_unresolved_sdtm_bc_dec(df, valid_bc_dec_pairs=set()) == []
    assert len(find_unresolved_sdtm_bc_dec(df, valid_bc_dec_pairs=set(), suppress_own_retired=False)) == 1


def test_find_duplicate_sdtm_groups_by_package_date_group_id_variable():
    df = pd.DataFrame([
        _sdtm_row("G1", sdtm_variable="VAR1"),
        _sdtm_row("G1", sdtm_variable="VAR1"),
        _sdtm_row("G1", sdtm_variable="VAR2"),
    ])
    findings = find_duplicate_sdtm(df)
    assert len(findings) == 2


def test_find_sdtm_pointing_to_retired_bc():
    df = pd.DataFrame([
        _sdtm_row("G1", bc_id="RETIRED_BC", short_name="Fine"),
        _sdtm_row("G2", bc_id="RETIRED_BC", short_name="Already [RETIRED]"),
    ])
    findings = find_sdtm_pointing_to_retired_bc(df, {"RETIRED_BC"})
    assert len(findings) == 1
    assert findings[0]["identifier"].startswith("domain=SC, vlm_group_id=G1")


def test_merge_subsets_adds_subset_value_list_column():
    df = pd.DataFrame([_sdtm_row("G1", subset_codelist="MYSUBSET")])
    with patch("cosmoslib.validators.sdtm.load_subset_codelists", return_value=[]), \
         patch("cosmoslib.validators.sdtm.subset_value_list_by_name", return_value={"MYSUBSET": "A;B"}):
        merged = merge_subsets(df, {"file": "irrelevant.xlsx", "range": "irrelevant"})
    assert merged["subset_value_list"].iloc[0] == "A;B"


def test_run_sdtm_validation_wires_all_checks_together():
    bc_df = pd.DataFrame([
        {"bc_id": "B1", "parent_bc_id": None, "dec_id": None, "short_name": "Alpha",
         "package_date": "R1", "_excel_file_": "bc.xlsx", "_tab_": "BC", "bc_categories": "Cat"},
    ])
    sdtm_df = pd.DataFrame([_sdtm_row("G1", bc_id="NOPE")])

    with patch("cosmoslib.validators.sdtm.load_manifest_corpus", side_effect=[bc_df, sdtm_df]), \
         patch("cosmoslib.validators.sdtm.merge_with_latest", side_effect=lambda df, *a, **k: df), \
         patch("cosmoslib.validators.sdtm.merge_subsets", side_effect=lambda df, *a, **k: df):
        findings = run_sdtm_validation(
            manifest_paths=["sdtm.yaml"], bc_manifest_paths=["bc.yaml"],
            bc_latest={"file": "x", "range": "y"}, sdtm_latest={"file": "x", "range": "y"},
            subsets_source={"file": "x", "range": "y"},
        )
    checks = {f["check"] for f in findings}
    assert "UNRESOLVED_SDTM_BC" in checks
