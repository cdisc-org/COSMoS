import os

from cosmoslib.excel_reader import read_named_range

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_sheet_lookup_is_case_insensitive():
    # utilities/manifests/bc/20260714_r18.yaml's BC_SURROGATES job differs in case from the
    # actual "BC_Surrogates" sheet in this workbook - PROC IMPORT resolves that on Windows,
    # so read_named_range must too.
    path = os.path.join(REPO_ROOT, "curation", "package18", "R18_BC_Surrogates.xlsx")
    df = read_named_range(path, "BC_SURROGATES$")
    assert len(df) > 0
    assert "bc_id" in df.columns


def test_blank_header_columns_are_dropped_not_kept_as_duplicates():
    # R18_BC_SDTM_SC.xlsx's "SDTM_SC" sheet has ~400 trailing blank-header columns from
    # openpyxl's used-range detection - these must not survive as duplicate "" columns,
    # which would break pd.concat/merge across sheets.
    path = os.path.join(REPO_ROOT, "curation", "package18", "R18_BC_SDTM_SC.xlsx")
    df = read_named_range(path, "SDTM_SC$")
    assert "" not in df.columns
    assert not df.columns.duplicated().any()
    assert "vlm_group_id" in df.columns
