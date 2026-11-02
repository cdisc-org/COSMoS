import pandas as pd

from cosmoslib.subset_codelists import build_subset_codelists, subset_value_list_by_name


def _row(parent_codelist, subset_short_name, submission_value):
    return {
        "parent_codelist": parent_codelist,
        "subset_short_name": subset_short_name,
        "submission_value": submission_value,
    }


def test_values_are_joined_in_sorted_order_per_subset():
    df = pd.DataFrame([
        _row("C1", "SUBSET_A", "ZEBRA"),
        _row("C1", "SUBSET_A", "APPLE"),
        _row("C1", "SUBSET_A", "MANGO"),
    ])
    rows = build_subset_codelists(df)
    assert len(rows) == 1
    assert rows[0]["subset_value_list"] == "APPLE;MANGO;ZEBRA"


def test_parent_codelist_takes_the_value_from_the_alphabetically_last_row():
    # SAS's `retain Parent_Codelist` is a no-op - `set` overwrites it from the current
    # (sorted-order) row every iteration - so it's whatever the LAST sorted row carries.
    df = pd.DataFrame([
        _row("C1", "SUBSET_A", "APPLE"),
        _row("C2", "SUBSET_A", "ZEBRA"),
    ])
    rows = build_subset_codelists(df)
    assert rows[0]["parent_codelist"] == "C2"


def test_multiple_subsets_each_get_their_own_row():
    df = pd.DataFrame([
        _row("C1", "SUBSET_A", "APPLE"),
        _row("C2", "SUBSET_B", "ZEBRA"),
        _row("C1", "SUBSET_A", "MANGO"),
    ])
    rows = build_subset_codelists(df)
    by_name = {row["subset_short_name"]: row for row in rows}
    assert by_name["SUBSET_A"]["subset_value_list"] == "APPLE;MANGO"
    assert by_name["SUBSET_B"]["subset_value_list"] == "ZEBRA"


def test_rows_missing_subset_short_name_are_dropped():
    df = pd.DataFrame([
        _row("C1", None, "APPLE"),
        _row("C1", "SUBSET_A", "MANGO"),
    ])
    rows = build_subset_codelists(df)
    assert len(rows) == 1
    assert rows[0]["subset_short_name"] == "SUBSET_A"


def test_blank_submission_values_are_excluded_from_the_joined_list():
    df = pd.DataFrame([
        _row("C1", "SUBSET_A", "APPLE"),
        _row("C1", "SUBSET_A", None),
        _row("C1", "SUBSET_A", "  "),
    ])
    rows = build_subset_codelists(df)
    assert rows[0]["subset_value_list"] == "APPLE"


def test_subset_value_list_by_name_builds_the_join_lookup():
    df = pd.DataFrame([
        _row("C1", "SUBSET_A", "APPLE"),
        _row("C2", "SUBSET_B", "ZEBRA"),
    ])
    lookup = subset_value_list_by_name(build_subset_codelists(df))
    assert lookup == {"SUBSET_A": "APPLE", "SUBSET_B": "ZEBRA"}
    assert lookup.get("NOT_A_SUBSET", "") == ""
