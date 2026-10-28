"""
CRF-specific cross-workbook checks, replacing the CRF-corpus portion of
utilities/validate_spreadsheet_crf.sas. As the plan notes, today's SAS source for this
validator is a near-duplicate copy-paste of validate_spreadsheet_sdtm.sas plus CRF checks -
this module is built on cosmoslib.validators.common and .sdtm (for the SDTM vlm_group_id
corpus a CRF specialization's sdtmDatasetSpecializationId is checked against) instead of
repeating that logic.

Two confirmed asymmetries with the SDTM validator (not fixed - see cosmoslib.validators.sdtm's
module docstring on the DHT variant, which drops the *same* suppression on the SDTM side, so
this isn't obviously a bug, just an inconsistency worth flagging rather than unilaterally
"fixing"): UNRESOLVED_CRF_BC_DEC and CRF_POINTS_TO_RETIRED_BC have no
`index(short_name, "[RETIRED]") = 0` suppression at all, unlike their SDTM counterparts.
"""

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
from cosmoslib.validators.sdtm import BC_ID_COLUMNS

CRF_ID_COLUMNS = ["domain", "crf_group_id", "order_number", "crf_item"]


def find_unresolved_crf_bc(crf_df, bc_ids):
    """"Missing CRF Specialization bc_id link to BC bc_id"."""
    return find_unresolved_references(crf_df, "bc_id", bc_ids, "UNRESOLVED_CRF_BC", CRF_ID_COLUMNS)


def find_unresolved_crf_bc_dec(crf_df, valid_bc_dec_pairs):
    """"Missing CRF Specialization bc_id/dec_id link to BC bc_id/dec_id" - no retired-tag
    suppression (see module docstring)."""
    return find_unresolved_bc_dec(crf_df, valid_bc_dec_pairs, "UNRESOLVED_CRF_BC_DEC", CRF_ID_COLUMNS)


def find_unresolved_crf_sdtm(crf_df, sdtm_vlm_group_ids):
    """"Missing CRF Specialization vlm_group_id link to SDTM vlm_group_id" - only checked
    when vlm_group_id is present (`(not missing(col.vlm_group_id)) and (... not in ...)`)."""
    return find_unresolved_references(
        crf_df, "vlm_group_id", sdtm_vlm_group_ids, "UNRESOLVED_CRF_SDTM", CRF_ID_COLUMNS, skip_blank=True,
    )


def find_duplicate_crf(crf_df):
    """"Duplicate CRF Specialization records (package_date, crf_group_id, crf_item)" - note
    the group key includes `standard`, not `domain` (matches the SAS source)."""
    return find_duplicates(
        crf_df, ["package_date", "standard", "crf_group_id", "crf_item"], "DUPLICATE_CRF",
        ["domain", "crf_group_id", "crf_item", "order_number", "standard_start_version", "standard_end_version"],
    )


def find_crf_pointing_to_retired_bc(crf_df, bc_retired_ids):
    """"CRF Specializations pointing to retired BCs" - no retired-tag suppression (see
    module docstring)."""
    findings = []
    for _, row in crf_df.iterrows():
        bc_id = clean_value(row.get("bc_id"))
        if bc_id not in bc_retired_ids:
            continue
        findings.append({
            "severity": "WARNING",
            "check": "CRF_POINTS_TO_RETIRED_BC",
            "package_date": clean_value(row.get("package_date")),
            "_excel_file_": clean_value(row.get("_excel_file_")),
            "_tab_": clean_value(row.get("_tab_")),
            "identifier": ", ".join(f"{c}={clean_value(row.get(c))}" for c in CRF_ID_COLUMNS),
            "comment": f"bc_id={bc_id}",
        })
    return findings


def run_crf_validation(
    manifest_paths, bc_manifest_paths, sdtm_manifest_paths, bc_latest, sdtm_latest,
    distinct_parent_check=False, high_byte_max=159,
):
    """Runs every CRF cross-workbook check and returns the combined list of findings,
    replacing the body of utilities/validate_spreadsheet_crf.sas from the corpus-building
    `data bc(...)`/`data sdtm(...)`/`data crf(...)` steps through the six PROC SQL checks.
    Unlike the BC/SDTM corpora, the CRF corpus is not merged with a "latest" export - the
    SAS source has none to merge (see the module docstring in cosmoslib/crf_converter.py)."""
    bc_df = load_manifest_corpus(bc_manifest_paths, "bc_id")
    bc_df = merge_with_latest(bc_df, bc_latest["file"], bc_latest["range"], "bc_id")

    sdtm_df = load_manifest_corpus(sdtm_manifest_paths, "vlm_group_id")
    sdtm_df = merge_with_latest(sdtm_df, sdtm_latest["file"], sdtm_latest["range"], "vlm_group_id")

    crf_df = load_manifest_corpus(manifest_paths, "crf_group_id")

    bc_ids = set(bc_df["bc_id"].map(clean_value)) - {""}
    valid_bc_dec_pairs = bc_dec_pairs(bc_df)
    bc_retired_ids = retired_bc_ids(bc_df)
    sdtm_vlm_group_ids = set(sdtm_df["vlm_group_id"].map(clean_value)) - {""}

    findings = []
    findings.extend(find_character_coding_issues(bc_df, BC_ID_COLUMNS, high_byte_max=high_byte_max))
    findings.extend(find_character_coding_issues(crf_df, CRF_ID_COLUMNS, high_byte_max=high_byte_max))
    findings.extend(find_unresolved_parent_bc(bc_df, distinct=distinct_parent_check))
    findings.extend(find_unresolved_crf_bc(crf_df, bc_ids))
    findings.extend(find_unresolved_crf_bc_dec(crf_df, valid_bc_dec_pairs))
    findings.extend(find_unresolved_crf_sdtm(crf_df, sdtm_vlm_group_ids))
    findings.extend(find_duplicate_bc(bc_df))
    findings.extend(find_duplicate_crf(crf_df))
    findings.extend(find_crf_pointing_to_retired_bc(crf_df, bc_retired_ids))
    return findings
