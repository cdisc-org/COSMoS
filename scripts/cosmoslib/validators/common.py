"""
Shared cross-workbook validation helpers, replacing the corpus-building preamble and the
BC-corpus checks common to both utilities/validate_spreadsheet_sdtm.sas and
utilities/validate_spreadsheet_crf.sas (unresolved parent_bc_id, duplicate BC records,
retired-BC bookkeeping, and the character-coding scan run against every corpus).

Corpus building replicates the SAS pattern (e.g. `set bc18:(where=(not missing(bc_id)))
_bc_latest(where=(not missing(bc_id) and bc_id notin (&bc_set)));`): every row from the
release manifest(s) currently being validated, plus every row from the already-published
"latest" export whose id isn't already covered by those manifests. Historical per-package
%ReadExcel blocks in the SAS source are commented out (dead code, superseded by the "latest"
export once it exists) and are not reproduced here - `load_manifest_corpus` naturally
absorbs more releases as more manifest files are added under utilities/manifests/.

Every check function returns a list of plain finding dicts: {severity, check, package_date,
_excel_file_, _tab_, identifier, comment}. There is no dedicated "*_ISSUE" SAS template for
these cross-workbook checks (the SAS source just prints ad hoc PROC SQL result sets) - this
shape was chosen to fit the same IssueLog machinery the converters use (see
cosmoslib.templates.VALIDATION_ISSUE_ID_COLUMNS), with `identifier`/`comment` absorbing
whatever columns each SQL SELECT happened to project.
"""

import pandas as pd

from cosmoslib.excel_reader import read_named_range
from cosmoslib.manifest import load_manifest
from cosmoslib.text import clean_value

CONTROL_CHAR_MAX = 31
DEFAULT_HIGH_BYTE_MAX = 159  # bc/sdtm: collate(128, 159). CRF/DHT variants use 255.


def load_manifest_corpus(manifest_paths, id_column):
    """`set bc<release>:(where=(not missing(bc_id)));`, generalized: concatenates every job's
    named range across the given manifest files, dropping rows where id_column is blank."""
    frames = []
    for manifest_path in manifest_paths:
        manifest = load_manifest(manifest_path)
        for job in manifest.jobs:
            frames.append(read_named_range(job.excel_file, job.range + "$"))
    if not frames:
        return pd.DataFrame()
    combined = pd.concat(frames, ignore_index=True, sort=False)
    return combined[combined[id_column].map(clean_value) != ""].reset_index(drop=True)


def merge_with_latest(current_df, latest_file, latest_range, id_column):
    """`set current(where=(not missing(id))) latest(where=(not missing(id) and id notin
    (&set)));` - appends every "latest" row whose id isn't already covered by current_df."""
    current_ids = set(current_df[id_column].map(clean_value)) - {""}
    latest_df = read_named_range(latest_file, latest_range + "$")
    latest_df = latest_df[latest_df[id_column].map(clean_value) != ""]
    latest_df = latest_df[~latest_df[id_column].map(clean_value).isin(current_ids)]
    return pd.concat([current_df, latest_df], ignore_index=True, sort=False)


def _finding(row, check, severity, identifier, comment):
    return {
        "severity": severity,
        "check": check,
        "package_date": clean_value(row.get("package_date")),
        "_excel_file_": clean_value(row.get("_excel_file_")),
        "_tab_": clean_value(row.get("_tab_")),
        "identifier": identifier,
        "comment": comment,
    }


def _identifier(row, columns):
    return ", ".join(f"{column}={clean_value(row.get(column))}" for column in columns)


def find_character_coding_issues(df, id_columns, high_byte_max=DEFAULT_HIGH_BYTE_MAX):
    """`translate(x, "", cats(collate(1,31), collate(128,159)))` (or collate(128,255) for
    CRF/DHT) changing a cell's value - a control character or disallowed high-byte
    character got curated into a cell. Log-only in the SAS source (a bare putlog, not an
    add2issues_* call); ported here as a proper finding for the structured report."""
    findings = []
    for _, row in df.iterrows():
        for column in df.columns:
            value = row.get(column)
            if not isinstance(value, str):
                continue
            cleaned = "".join(
                ch for ch in value
                if not (1 <= ord(ch) <= CONTROL_CHAR_MAX or 128 <= ord(ch) <= high_byte_max)
            )
            if cleaned != value:
                findings.append(_finding(
                    row, "CHARACTER_CODING_ISSUE", "WARNING", _identifier(row, id_columns),
                    f"column={column}, value={value!r}",
                ))
    return findings


def find_unresolved_references(df, ref_column, valid_ids, check_name, id_columns, skip_blank=False):
    """`where ref not in (select id from other) [and not missing(ref)]` - flags every row
    whose ref_column doesn't resolve against valid_ids. skip_blank=True reproduces an
    explicit `and not missing(...)` guard some SAS checks have and others don't."""
    findings = []
    for _, row in df.iterrows():
        ref = clean_value(row.get(ref_column))
        if skip_blank and not ref:
            continue
        if ref in valid_ids:
            continue
        findings.append(_finding(
            row, check_name, "WARNING", _identifier(row, id_columns), f"{ref_column}={ref}",
        ))
    return findings


def find_unresolved_bc_dec(df, valid_bc_dec_pairs, check_name, id_columns, suppress_own_retired=False):
    """`cold.bc_dec not in (select unique catx('-', bc_id, dec_id) from bc)` - flags rows
    with a dec_id whose (bc_id, dec_id) pair isn't in the BC corpus. suppress_own_retired
    reproduces the SDTM validator's `and index(short_name, "[RETIRED]") = 0` (checked
    against the row's *own* short_name, not the target BC's) - the CRF validator's
    equivalent check has no such guard."""
    findings = []
    for _, row in df.iterrows():
        dec_id = clean_value(row.get("dec_id"))
        if not dec_id:
            continue
        bc_id = clean_value(row.get("bc_id"))
        if (bc_id, dec_id) in valid_bc_dec_pairs:
            continue
        if suppress_own_retired and "[RETIRED]" in clean_value(row.get("short_name")):
            continue
        findings.append(_finding(
            row, check_name, "WARNING", _identifier(row, id_columns), f"bc_id={bc_id}, dec_id={dec_id}",
        ))
    return findings


def find_duplicates(df, group_columns, check_name, id_columns):
    """`group by <group_columns> having count(*) > 1` - every row belonging to a group of
    size > 1 on (package_date plus the domain's natural key)."""
    keys = list(zip(*[df[column].map(clean_value) for column in group_columns]))
    counts = {}
    for key in keys:
        counts[key] = counts.get(key, 0) + 1

    findings = []
    for key, (_, row) in zip(keys, df.iterrows()):
        if counts[key] <= 1:
            continue
        group_desc = ", ".join(f"{c}={v}" for c, v in zip(group_columns, key))
        findings.append(_finding(row, check_name, "WARNING", _identifier(row, id_columns), f"group=({group_desc})"))
    return findings


def find_unresolved_parent_bc(bc_df, distinct=False):
    """"Missing BC parent_bc_id link to BC bc_id"."""
    bc_ids = set(bc_df["bc_id"].map(clean_value)) - {""}
    findings = find_unresolved_references(
        bc_df, "parent_bc_id", bc_ids, "UNRESOLVED_PARENT_BC",
        ["bc_categories", "bc_id", "short_name"], skip_blank=True,
    )
    if not distinct:
        return findings
    seen = set()
    deduped = []
    for finding in findings:
        key = (finding["package_date"], finding["_excel_file_"], finding["_tab_"], finding["identifier"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(finding)
    return deduped


def find_duplicate_bc(bc_df):
    """"Duplicate BC records (package_date, bc_id, dec_id)"."""
    return find_duplicates(
        bc_df, ["package_date", "bc_id", "dec_id"], "DUPLICATE_BC",
        ["bc_id", "short_name", "dec_id", "dec_label", "bc_categories"],
    )


def retired_bc_ids(bc_df):
    """`select distinct bc_id ... where index(short_name, "[RETIRED]") > 0` - the set of
    bc_id values whose short_name is tagged [RETIRED]."""
    mask = bc_df["short_name"].map(lambda v: "[RETIRED]" in clean_value(v))
    return set(bc_df.loc[mask, "bc_id"].map(clean_value)) - {""}


def bc_dec_pairs(bc_df):
    """`select unique catx('-', bc_id, dec_id) from bc` - as a set of (bc_id, dec_id)
    tuples instead of catx-joined strings (equivalent, avoids a delimiter-collision edge
    case if either id ever contained a literal '-')."""
    working = bc_df[bc_df["dec_id"].map(clean_value) != ""]
    return set(zip(working["bc_id"].map(clean_value), working["dec_id"].map(clean_value)))
