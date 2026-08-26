import pandas as pd

from cosmoslib.validators.common import (
    bc_dec_pairs,
    find_character_coding_issues,
    find_duplicate_bc,
    find_duplicates,
    find_unresolved_bc_dec,
    find_unresolved_parent_bc,
    find_unresolved_references,
    retired_bc_ids,
)


def _bc_row(bc_id, parent_bc_id=None, dec_id=None, short_name="Alpha", package_date="R18",
            excel_file="wb.xlsx", tab="BC_TEST", bc_categories="Cat"):
    return {
        "bc_id": bc_id, "parent_bc_id": parent_bc_id, "dec_id": dec_id, "short_name": short_name,
        "package_date": package_date, "_excel_file_": excel_file, "_tab_": tab, "bc_categories": bc_categories,
        "dec_label": "Label",
    }


def test_find_unresolved_references_flags_dangling_ref_and_skips_blank_when_asked():
    df = pd.DataFrame([
        {"ref": "X", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"},
        {"ref": None, "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"},
        {"ref": "Y", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"},
    ])
    findings = find_unresolved_references(df, "ref", {"Y"}, "CHECK", ["ref"], skip_blank=True)
    assert len(findings) == 1
    assert findings[0]["comment"] == "ref=X"


def test_find_unresolved_references_flags_blank_when_not_skipped():
    df = pd.DataFrame([{"ref": None, "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"}])
    findings = find_unresolved_references(df, "ref", {"Y"}, "CHECK", ["ref"], skip_blank=False)
    assert len(findings) == 1


def test_find_unresolved_bc_dec_suppresses_own_retired_when_asked():
    df = pd.DataFrame([
        {"bc_id": "B1", "dec_id": "D1", "short_name": "Old [RETIRED]", "_excel_file_": "wb", "_tab_": "t",
         "package_date": "R1"},
        {"bc_id": "B2", "dec_id": "D2", "short_name": "Active", "_excel_file_": "wb", "_tab_": "t",
         "package_date": "R1"},
    ])
    suppressed = find_unresolved_bc_dec(
        df, valid_bc_dec_pairs=set(), check_name="CHECK", id_columns=["bc_id"], suppress_own_retired=True
    )
    assert len(suppressed) == 1
    assert suppressed[0]["comment"] == "bc_id=B2, dec_id=D2"

    unsuppressed = find_unresolved_bc_dec(
        df, valid_bc_dec_pairs=set(), check_name="CHECK", id_columns=["bc_id"], suppress_own_retired=False
    )
    assert len(unsuppressed) == 2


def test_find_unresolved_bc_dec_skips_rows_without_dec_id():
    df = pd.DataFrame([
        {"bc_id": "B1", "dec_id": None, "short_name": "x", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"}
    ])
    assert find_unresolved_bc_dec(df, set(), "CHECK", ["bc_id"]) == []


def test_find_duplicates_flags_every_row_in_a_group_of_size_greater_than_one():
    df = pd.DataFrame([
        {"package_date": "R1", "bc_id": "B1", "dec_id": "D1", "short_name": "a", "_excel_file_": "wb", "_tab_": "t"},
        {"package_date": "R1", "bc_id": "B1", "dec_id": "D1", "short_name": "b", "_excel_file_": "wb", "_tab_": "t"},
        {"package_date": "R1", "bc_id": "B2", "dec_id": "D2", "short_name": "c", "_excel_file_": "wb", "_tab_": "t"},
    ])
    findings = find_duplicates(df, ["package_date", "bc_id", "dec_id"], "DUP", ["bc_id"])
    assert len(findings) == 2
    assert all(f["check"] == "DUP" for f in findings)


def test_find_unresolved_parent_bc_distinct_dedupes_identical_findings():
    bc_df = pd.DataFrame([
        _bc_row("B1", parent_bc_id="MISSING"),
        _bc_row("B1", parent_bc_id="MISSING"),  # exact duplicate row -> same finding
    ])
    all_findings = find_unresolved_parent_bc(bc_df, distinct=False)
    assert len(all_findings) == 2
    distinct_findings = find_unresolved_parent_bc(bc_df, distinct=True)
    assert len(distinct_findings) == 1


def test_find_unresolved_parent_bc_skips_blank_and_resolved_parents():
    bc_df = pd.DataFrame([
        _bc_row("B1", parent_bc_id=None),
        _bc_row("B2", parent_bc_id="B1"),  # resolves fine
    ])
    assert find_unresolved_parent_bc(bc_df) == []


def test_find_duplicate_bc_groups_by_package_date_bc_id_dec_id():
    bc_df = pd.DataFrame([
        _bc_row("B1", dec_id="D1"),
        _bc_row("B1", dec_id="D1"),
    ])
    findings = find_duplicate_bc(bc_df)
    assert len(findings) == 2
    assert findings[0]["check"] == "DUPLICATE_BC"


def test_retired_bc_ids_matches_on_short_name_tag():
    bc_df = pd.DataFrame([
        _bc_row("B1", short_name="Old Name [RETIRED]"),
        _bc_row("B2", short_name="Active Name"),
    ])
    assert retired_bc_ids(bc_df) == {"B1"}


def test_bc_dec_pairs_excludes_rows_without_dec_id():
    bc_df = pd.DataFrame([
        _bc_row("B1", dec_id="D1"),
        _bc_row("B1", dec_id=None),
    ])
    assert bc_dec_pairs(bc_df) == {("B1", "D1")}


def test_find_character_coding_issues_flags_control_and_high_byte_chars():
    df = pd.DataFrame([
        {"short_name": "Clean value", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"},
        {"short_name": "Bad\x01Char", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"},
        {"short_name": "High\x9dByte", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"},
    ])
    findings = find_character_coding_issues(df, ["short_name"])
    assert len(findings) == 2
    assert all(f["check"] == "CHARACTER_CODING_ISSUE" for f in findings)


def test_find_character_coding_issues_high_byte_max_widens_the_catch_range():
    # 0xA0 (160) is outside [128,159] (the bc/sdtm default) but inside [128,255] (CRF/DHT).
    df = pd.DataFrame([{"short_name": "\xa0nbsp", "_excel_file_": "wb", "_tab_": "t", "package_date": "R1"}])
    assert find_character_coding_issues(df, ["short_name"], high_byte_max=159) == []
    assert len(find_character_coding_issues(df, ["short_name"], high_byte_max=255)) == 1
