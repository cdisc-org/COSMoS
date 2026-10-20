"""
Subset codelist lookup, replacing utilities/macros/get_subset_codelists.sas. Reads a
curation "subset codelist" named range (columns Parent_Codelist / Subset_Short_Name /
Submission_Value - after excel_reader's header normalization: parent_codelist /
subset_short_name / submission_value) and reduces it to one row per subset_short_name with
every submission_value joined into a single ';'-separated subset_value_list: the shape
generate_yaml_from_sdtm.sas's `left join &subsetsDS ss on bcsdtm.subset_codelist =
ss.subset_short_name` consumes.
"""

from cosmoslib.excel_reader import read_named_range


def load_subset_codelists(file_path, range_name):
    df = read_named_range(file_path, range_name.rstrip("$") + "$")
    return build_subset_codelists(df)


def build_subset_codelists(df):
    """`proc sort by Subset_Short_Name Submission_Value; ... subset_value_list=catx(";",
    subset_value_list, Submission_Value) ... if last.Subset_Short_Name then output;` -
    group by subset_short_name, joining every submission_value (sorted ascending, matching
    the SAS `by` order) into one ';'-separated string. Parent_Codelist is carried through
    unchanged per group (SAS's `retain` there is a no-op - `set` overwrites it from the
    current row every iteration regardless - so the value output is simply whichever row
    sorts last within the group)."""
    working = df.copy()
    working.loc[:, "subset_short_name"] = working["subset_short_name"].map(_clean)
    working = working[working["subset_short_name"] != ""].copy()
    working.loc[:, "submission_value"] = working["submission_value"].map(_clean)
    working = working.sort_values(["subset_short_name", "submission_value"], kind="stable")

    rows = []
    for subset_short_name, group in working.groupby("subset_short_name", sort=True):
        submission_values = [v for v in group["submission_value"] if v]
        parent_codelist = _clean(group["parent_codelist"].iloc[-1]) if len(group) else ""
        rows.append({
            "parent_codelist": parent_codelist,
            "subset_short_name": subset_short_name,
            "subset_value_list": ";".join(submission_values),
        })
    return rows


def subset_value_list_by_name(rows):
    """The lookup shape generate_yaml_from_sdtm.sas's left join on subset_short_name
    actually consumes."""
    return {row["subset_short_name"]: row["subset_value_list"] for row in rows}


def _clean(value):
    if value is None:
        return ""
    if isinstance(value, float) and value != value:  # NaN
        return ""
    return str(value).strip()
