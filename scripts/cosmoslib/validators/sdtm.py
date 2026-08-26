"""
SDTM-specific cross-workbook checks, replacing the SDTM-corpus portion of
utilities/validate_spreadsheet_sdtm.sas (and its _dht variant - see run_sdtm_validation's
`suppress_own_retired`/`high_byte_max`/`distinct_parent_check` parameters, which the DHT
variant sets differently; confirmed by diffing the two SAS files).
"""

from cosmoslib.subset_codelists import load_subset_codelists, subset_value_list_by_name
from cosmoslib.text import clean_value
from cosmoslib.validators.common import (
    bc_dec_pairs,
    find_character_coding_issues,
    find_duplicate_bc,
    find_duplicates,
    find_unresolved_bc_dec,
    find_unresolved_parent_bc,
    find_unresolved_references,
    load_manifest_corpus,
    merge_with_latest,
    retired_bc_ids,
)

BC_ID_COLUMNS = ["_excel_file_", "_tab_", "bc_categories", "bc_id", "short_name"]
SDTM_ID_COLUMNS = ["domain", "vlm_group_id", "short_name", "sdtm_variable"]


def merge_subsets(sdtm_df, subsets_source):
    """`left join &subsetsDS ss on sdtm.subset_codelist = ss.subset_short_name` - adds a
    subset_value_list column, blank where subset_codelist doesn't match any subset."""
    subset_rows = load_subset_codelists(subsets_source["file"], subsets_source["range"])
    lookup = subset_value_list_by_name(subset_rows)
    sdtm_df = sdtm_df.copy()
    sdtm_df.loc[:, "subset_value_list"] = sdtm_df["subset_codelist"].map(lambda v: lookup.get(clean_value(v), ""))
    return sdtm_df


def find_unresolved_sdtm_bc(sdtm_df, bc_ids):
    """"Missing SDTM Specialization bc_id link to BC bc_id"."""
    return find_unresolved_references(
        sdtm_df, "bc_id", bc_ids, "UNRESOLVED_SDTM_BC", SDTM_ID_COLUMNS,
    )


def find_unresolved_sdtm_bc_dec(sdtm_df, valid_bc_dec_pairs, suppress_own_retired=True):
    """"Missing SDTM Specialization bc_id/dec_id link to BC bc_id/dec_id"."""
    return find_unresolved_bc_dec(
        sdtm_df, valid_bc_dec_pairs, "UNRESOLVED_SDTM_BC_DEC", SDTM_ID_COLUMNS,
        suppress_own_retired=suppress_own_retired,
    )


def find_duplicate_sdtm(sdtm_df):
    """"Duplicate SDTM Specialization records (package_date, vlm_group_id, sdtm_variable)"."""
    return find_duplicates(
        sdtm_df, ["package_date", "vlm_group_id", "sdtm_variable"], "DUPLICATE_SDTM",
        ["domain", "vlm_group_id", "short_name", "sdtm_variable", "sdtmig_start_version", "sdtmig_end_version"],
    )


def find_sdtm_pointing_to_retired_bc(sdtm_df, bc_retired_ids, suppress_own_retired=True):
    """"SDTM Specializations pointing to retired BCs"."""
    findings = []
    for _, row in sdtm_df.iterrows():
        bc_id = clean_value(row.get("bc_id"))
        if bc_id not in bc_retired_ids:
            continue
        if suppress_own_retired and "[RETIRED]" in clean_value(row.get("short_name")):
            continue
        findings.append({
            "severity": "WARNING",
            "check": "SDTM_POINTS_TO_RETIRED_BC",
            "package_date": clean_value(row.get("package_date")),
            "_excel_file_": clean_value(row.get("_excel_file_")),
            "_tab_": clean_value(row.get("_tab_")),
            "identifier": ", ".join(f"{c}={clean_value(row.get(c))}" for c in SDTM_ID_COLUMNS),
            "comment": f"bc_id={bc_id}",
        })
    return findings


def run_sdtm_validation(
    manifest_paths, bc_manifest_paths, bc_latest, sdtm_latest, subsets_source,
    distinct_parent_check=False, suppress_own_retired=True, high_byte_max=159,
):
    """Runs every SDTM cross-workbook check and returns the combined list of findings,
    replacing the body of utilities/validate_spreadsheet_sdtm.sas from the corpus-building
    `data bc(...)`/`data sdtm(...)` steps through the six PROC SQL checks."""
    bc_df = load_manifest_corpus(bc_manifest_paths, "bc_id")
    bc_df = merge_with_latest(bc_df, bc_latest["file"], bc_latest["range"], "bc_id")

    sdtm_df = load_manifest_corpus(manifest_paths, "vlm_group_id")
    sdtm_df = merge_with_latest(sdtm_df, sdtm_latest["file"], sdtm_latest["range"], "vlm_group_id")
    sdtm_df = merge_subsets(sdtm_df, subsets_source)

    bc_ids = set(bc_df["bc_id"].map(clean_value)) - {""}
    valid_bc_dec_pairs = bc_dec_pairs(bc_df)
    bc_retired_ids = retired_bc_ids(bc_df)

    findings = []
    findings.extend(find_character_coding_issues(bc_df, BC_ID_COLUMNS, high_byte_max=high_byte_max))
    findings.extend(find_character_coding_issues(sdtm_df, SDTM_ID_COLUMNS, high_byte_max=high_byte_max))
    findings.extend(find_unresolved_parent_bc(bc_df, distinct=distinct_parent_check))
    findings.extend(find_unresolved_sdtm_bc(sdtm_df, bc_ids))
    findings.extend(
        find_unresolved_sdtm_bc_dec(sdtm_df, valid_bc_dec_pairs, suppress_own_retired=suppress_own_retired)
    )
    findings.extend(find_duplicate_bc(bc_df))
    findings.extend(find_duplicate_sdtm(sdtm_df))
    findings.extend(
        find_sdtm_pointing_to_retired_bc(sdtm_df, bc_retired_ids, suppress_own_retired=suppress_own_retired)
    )
    return findings
