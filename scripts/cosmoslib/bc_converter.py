"""
Python port of utilities/macros/generate_yaml_from_bc.sas. Reads one curation Excel named
range (one manifest job), groups rows by bc_id, and writes one BC YAML file per group plus
a row per validation finding to an IssueLog.

Only the ISSUES depend on live NCI EVS lookups (BC_ID_CONCEPTSTATUS, BC_SHORTNAME_MISMATCH_
OR_MISSING, DEFINITION_MISMATCH_OR_MISSING, PARENT_ID_MISMATCH, DEC_ID_CONCEPTSTATUS,
DEC_SHORTNAME_MISMATCH_OR_MISSING) - every field written to the YAML itself comes straight
from the curation workbook, so golden-file regression tests can run against a stub/fake
`ncievs` with no network access at all.

Group-boundary state machine (SAS-QUIRK(preserved), see plans/port-sas-utilities-to-python.md
"Subtle behaviors to preserve or fix"): `count`/`decs` are reset only when bc_id changes and
incremented on every row thereafter; the "dataElementConcepts:" list header is only ever
printed when checked at count==1 or count==2. If neither of a group's first two rows carries
a dec_id, the header never prints for that group even if a later row does have one - ported
exactly, not "fixed", since it's unclear whether any curated data actually depends on it.

Two more preserved SAS-isms, both confirmed against yaml/20260714_r18/bc/*.yaml:
- The DEC-level "shortName:" (dec_label) has no index('"')/index(':')/index('-') quoting
  guard in the SAS source, unlike every other quoted field - see bc__c100761.yaml's
  unquoted "shortName: Not-Done Reason". Ported via YamlWriter.raw(), not .scalar().
- resultScale list items are never quoted at all (enum-constrained values, so this never
  differs from the general quoting rule in practice).

The RESULTSCALE_MISSING/DEC_SHORTNAME_MISSING/DEC_DATATYPE_MISSING checks are gated by that
same count==1-or-2 header-print condition, so they only ever fire against the group's first
DEC-bearing row, not every DEC - also preserved as-is.
"""

import os

from cosmoslib.enums import exists_enum_term
from cosmoslib.excel_reader import read_named_range
from cosmoslib.naming import bc_yaml_filename, ncit_href, output_path
from cosmoslib.text import clean_value, squeeze_spaces, words as _words
from cosmoslib.yaml_writer import needs_quoting, YamlWriter


def _get(row, column):
    return clean_value(row.get(column))


def _sorted_groups(df):
    """`set ...(where=(not missing(bc_id))); bc_id = kcompress(bc_id,,'s'); _order_ = _n_;`
    then `proc sort by bc_id _order_;` - drop rows with no bc_id, then a stable sort by
    (bc_id, original row order)."""
    working = df.copy()
    working.loc[:, "bc_id"] = working["bc_id"].map(clean_value)
    working = working[working["bc_id"] != ""].copy()
    working.loc[:, "bc_id"] = working["bc_id"].map(squeeze_spaces)
    working.loc[:, "_order_"] = range(1, len(working) + 1)
    return working.sort_values(["bc_id", "_order_"], kind="stable")


def convert_bc_job(job, enum_index, ncievs, issue_log):
    """Runs one manifest job (one curation Excel named range) through the BC converter.
    Returns the list of YAML file paths written."""
    df = read_named_range(job.excel_file, job.range + "$")
    if job.select:
        # Manifests carry this as a pandas DataFrame.query() expression, not a literal SAS
        # WHERE clause - no current manifest uses it (see plans/port-sas-utilities-to-python.md).
        df = df.query(job.select)

    bc_type = job.type.replace("-", "_")
    os.makedirs(job.out_folder, exist_ok=True)

    written = []
    for bc_id, rows in _sorted_groups(df).groupby("bc_id", sort=False):
        path = output_path(job.out_folder, bc_yaml_filename(bc_type, bc_id))
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            _write_bc_group(YamlWriter(fh), rows, job, enum_index, ncievs, issue_log)
        written.append(path)
    return written


def _write_bc_group(writer, rows, job, enum_index, ncievs, issue_log):
    count = 0
    decs = 0
    result_scales_yn = False

    for is_first, (_, row) in _enumerate_first(rows):
        excel_file = _get(row, "_excel_file_")
        tab = _get(row, "_tab_")
        bc_id = _get(row, "bc_id")
        short_name_row = _get(row, "short_name")  # per-row, not retained - matches SAS
        dec_id = _get(row, "dec_id")

        def emit_issue(condition, issue_type, expected="", actual="", comment="", severity="WARNING"):
            if condition:
                issue_log.add(
                    excel_file, tab, severity, issue_type,
                    expected_value=expected, actual_value=actual, comment=comment,
                    BC_ID=bc_id, short_name=short_name_row, dec_id=dec_id,
                )

        if is_first:
            count = 0
            decs = 0
            result_scales_yn = False
            package_date = job.override_package_date or _get(row, "package_date")
            result_scales_yn = _write_bc_header(writer, row, bc_id, package_date, enum_index, ncievs, emit_issue)

        count += 1
        decs = _write_dec(writer, row, dec_id, count, decs, result_scales_yn, enum_index, ncievs, emit_issue)


def _enumerate_first(rows):
    first = True
    for item in rows.iterrows():
        yield first, item
        first = False


def _write_bc_header(writer, row, bc_id, package_date, enum_index, ncievs, emit_issue):
    ncit_code = squeeze_spaces(_get(row, "ncit_code"))

    writer.scalar_always_quoted("packageDate", package_date)
    writer.scalar("packageType", "bc")
    writer.scalar("conceptId", bc_id)

    _write_ncit_code_block(writer, bc_id, ncit_code, ncievs, emit_issue)
    _write_parent_block(writer, row, bc_id, ncievs, emit_issue)
    _write_categories_block(writer, row, emit_issue)
    _write_shortname_block(writer, row, ncit_code, ncievs, emit_issue)
    _write_synonyms_block(writer, row, emit_issue)
    result_scales_yn = _write_result_scales_block(writer, row, enum_index, emit_issue)
    _write_definition_block(writer, row, ncit_code, ncievs, emit_issue)
    _write_coding_block(writer, row, emit_issue)

    return result_scales_yn


def _write_ncit_code_block(writer, bc_id, ncit_code, ncievs, emit_issue):
    emit_issue(not ncit_code, "NCIT_CODE_MISSING")
    if not ncit_code:
        return
    writer.scalar("ncitCode", ncit_code)
    writer.raw("href", ncit_href(ncit_code))
    emit_issue(bc_id != ncit_code, "BC_ID_NCIT_CODEMISMATCH", expected=bc_id, actual=ncit_code)

    concept_status = ncievs.get_concept_status(ncit_code)
    emit_issue(
        bool(concept_status) and "Retired" in concept_status,
        "BC_ID_CONCEPTSTATUS", actual=concept_status,
    )


def _write_parent_block(writer, row, bc_id, ncievs, emit_issue):
    parent_bc_id = squeeze_spaces(_get(row, "parent_bc_id"))
    if not parent_bc_id:
        return

    short_name_parent = ncievs.get_shortname(parent_bc_id)
    parent_bc_id_nci, short_name_parent_nci = ncievs.get_parent_code_shortname(bc_id)
    parent_bc_id_nci = squeeze_spaces(parent_bc_id_nci).strip()
    found_parent = parent_bc_id_nci.find(parent_bc_id) >= 0
    parent_comment = f"parent_shortname={short_name_parent}, parent_shortname_nci={short_name_parent_nci}"
    emit_issue(
        not found_parent and bool(parent_bc_id_nci),
        "PARENT_ID_MISMATCH", expected=parent_bc_id_nci, actual=parent_bc_id, comment=parent_comment,
    )
    emit_issue(
        not found_parent and not parent_bc_id_nci,
        "PARENT_ID_MISMATCH", expected=parent_bc_id_nci, actual=parent_bc_id, comment=parent_comment,
        severity="NOTE",
    )
    writer.scalar("parentConceptId", parent_bc_id)


def _write_categories_block(writer, row, emit_issue):
    bc_categories = _get(row, "bc_categories")
    emit_issue(not bc_categories, "CATEGORIES_MISSING")
    if not bc_categories:
        return
    writer.block_key("categories")
    for value in _words(bc_categories):
        writer.list_scalar(value, indent=2)


def _write_shortname_block(writer, row, ncit_code, ncievs, emit_issue):
    short_name = _get(row, "short_name")
    if short_name:
        writer.scalar("shortName", short_name)

    short_name_nci = ncievs.get_shortname(ncit_code) if ncit_code else ""
    retired = "[RETIRED]" in short_name
    emit_issue(
        (short_name != short_name_nci and not retired and bool(short_name_nci)) or not short_name,
        "BC_SHORTNAME_MISMATCH_OR_MISSING", expected=short_name_nci, actual=short_name,
    )
    emit_issue(
        short_name != short_name_nci and not retired and not short_name_nci,
        "BC_SHORTNAME_MISMATCH_OR_MISSING", expected=short_name_nci, actual=short_name,
        severity="NOTE",
    )


def _write_synonyms_block(writer, row, emit_issue):
    synonyms = _get(row, "synonyms")
    if not synonyms:
        return
    emit_issue("," in synonyms, "SYNONYM_ISSUE_COMMA", actual=synonyms, severity="NOTE")
    writer.block_key("synonyms")
    for value in _words(synonyms):
        _write_synonym_item(writer, value)


def _write_result_scales_block(writer, row, enum_index, emit_issue):
    result_scales = _get(row, "result_scales")
    if not result_scales:
        return False

    writer.block_key("resultScales")
    for value in _words(result_scales):
        # SAS-QUIRK(preserved, approximated): the SAS put for this list has no quoting
        # check at all, unlike every other list field. list_scalar()'s conditional quoting
        # is used here instead of a truly bare "- value" write since it never actually
        # differs in practice - resultScale values are enum-constrained.
        writer.list_scalar(value, indent=2)
        emit_issue(
            not exists_enum_term(enum_index, "BiomedicalConceptResultScale", value),
            "INVALID_VALUE_RESULTSCALE", actual=value, comment=f"result_scales={result_scales}",
            severity="ERROR",
        )
    return True


def _write_definition_block(writer, row, ncit_code, ncievs, emit_issue):
    definition = squeeze_spaces(_get(row, "definition"))

    definition_nci, _ = ncievs.get_definitions(ncit_code) if ncit_code else ("", "")
    definition_nci = squeeze_spaces(definition_nci.strip())
    retired_definition = "[RETIRED]" in definition
    emit_issue(
        (definition != definition_nci and not retired_definition and bool(definition_nci)) or not definition,
        "DEFINITION_MISMATCH_OR_MISSING", expected=definition_nci, actual=definition,
    )
    emit_issue(
        definition != definition_nci and not definition_nci and not retired_definition,
        "DEFINITION_MISMATCH_OR_MISSING", expected=definition_nci, actual=definition,
        severity="NOTE",
    )
    if definition:
        writer.scalar("definition", definition)


def _write_coding_block(writer, row, emit_issue):
    system_name = _get(row, "system_name")
    system = _get(row, "system")
    code = _get(row, "code")

    if system_name:
        emit_issue(
            not system or not code, "BC_SYSTEM_CODE_MISSING",
            comment=f"system_name={system_name}system={system}code={code}",
        )
    if not system:
        return

    emit_issue(not code, "BC_SYSTEM_CODE_MISSING", comment=f"system={system}")
    writer.block_key("coding")
    # SAS-QUIRK(preserved): iteration count and list-item boundaries both follow `system`'s
    # word count, not `code`'s - if `code` has fewer ';'-separated entries than `system`,
    # the entries beyond that point emit "system:"/"systemName:" with no preceding
    # "- code:" to start a new list item, so they get merged as extra keys onto the
    # *previous* coding entry when parsed (generate_yaml_from_bc.sas has the exact same
    # behavior; nothing here corrects it).
    system_words = _words(system)
    code_words = _words(code)
    system_name_words = _words(system_name)
    for i in range(len(system_words)):
        if i < len(code_words) and code_words[i]:
            writer.raw("- code", code_words[i], indent=2)
        writer.raw("system", system_words[i], indent=4)
        if i < len(system_name_words) and system_name_words[i]:
            writer.raw("systemName", system_name_words[i], indent=4)


def _write_synonym_item(writer, value):
    # SAS-QUIRK(preserved): synonyms quote on '{'/'}' in addition to the usual
    # '"'/':'/'-' trigger set (generate_yaml_from_bc.sas), unlike categories/resultScales.
    if needs_quoting(value) or "{" in value or "}" in value:
        writer.list_quoted(value, indent=2)
    else:
        writer.list_scalar(value, indent=2)


def _write_dec(writer, row, dec_id, count, decs, result_scales_yn, enum_index, ncievs, emit_issue):
    ncit_dec_code = squeeze_spaces(_get(row, "ncit_dec_code"))
    dec_label = _get(row, "dec_label")
    data_type = _get(row, "data_type")
    example_set = _get(row, "example_set")

    if (count == 2 and dec_id and decs == 0) or (count == 1 and dec_id):
        emit_issue(not result_scales_yn, "RESULTSCALE_MISSING", severity="WARNING")
        emit_issue(not dec_label, "DEC_SHORTNAME_MISSING", severity="ERROR")
        emit_issue(not data_type, "DEC_DATATYPE_MISSING", severity="ERROR")
        decs += 1
        writer.block_key("dataElementConcepts")

    if not dec_id:
        return decs

    writer.raw("- conceptId", dec_id, indent=2)

    emit_issue(not ncit_dec_code, "NCIT_DEC_CODE_MISSING")
    if ncit_dec_code:
        writer.raw("ncitCode", ncit_dec_code, indent=4)
        writer.raw("href", ncit_href(ncit_dec_code), indent=4)

        concept_status = ncievs.get_concept_status(ncit_dec_code)
        emit_issue(
            bool(concept_status) and "Retired" in concept_status,
            "DEC_ID_CONCEPTSTATUS", actual=concept_status,
        )

    emit_issue(dec_id != ncit_dec_code, "BC_DEC_ID_NCIT_CODEMISMATCH", expected=dec_id, actual=ncit_dec_code)

    if ncit_dec_code:
        short_name_dec_nci = ncievs.get_shortname(ncit_dec_code)
        emit_issue(
            (dec_label != short_name_dec_nci and bool(short_name_dec_nci)) or not dec_label,
            "DEC_SHORTNAME_MISMATCH_OR_MISSING", expected=short_name_dec_nci, actual=dec_label,
        )

    writer.raw("shortName", dec_label, indent=4)

    emit_issue(not data_type, "BC_DEC_DATATYPE_MISSING", comment=f"dec_label={dec_label}")
    if data_type:
        emit_issue(
            not exists_enum_term(enum_index, "DataElementConceptDataType", data_type),
            "INVALID_VALUE_DATATYPE", actual=data_type, severity="ERROR",
        )
        writer.scalar("dataType", data_type, indent=4)

    if example_set:
        emit_issue(
            "," in example_set, "EXAMPLE_SET_ISSUE_COMMA", actual=example_set,
            comment=f"dec_label={dec_label}", severity="NOTE",
        )
        writer.block_key("exampleSet", indent=4)
        for value in _words(example_set):
            writer.list_quoted(value, indent=6)

    return decs
