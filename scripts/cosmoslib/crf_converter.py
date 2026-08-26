"""
Python port of utilities/macros/generate_yaml_from_crf.sas. Reads one curation Excel named
range (one manifest job), groups rows by crf_group_id, and writes one CRF YAML file per
group plus a row per validation finding to an IssueLog.

As with the BC/SDTM converters, every field written to the YAML comes straight from the
curation workbook - only the ISSUES depend on the live CDISC Library codelist lookups (via
`codelist_index`, reusing cosmoslib.cdisc_library_cache from Phase 4), so golden-file
regression tests can run against a stub codelist_index with no network access at all.

Two approved fixes from plans/port-sas-utilities-to-python.md (both confirmed absent from
yaml/20260630_draft/crf/*.yaml - the field is never populated in that fixture, so neither
fix is exercised by the golden test):
- `completionIinstructions` (SAS typo) -> `completionInstructions`.
- The `&folder.2` output-path bug is fixed at the manifest level (see
  utilities/manifests/crf/20260630_draft.yaml), not here.

Also fixed here (an approved issue-type-string typo, not a data-shape fix):
`QUESTION_TEXT_PROMPT_BOTH_NOT MISSING` (space) -> `QUESTION_TEXT_PROMPT_BOTH_NOT_MISSING`.

Sort key: unlike the BC/SDTM converters (which sort by original row order within a group),
CRF sorts by the curated `order_number` column itself (`proc sort; by crf_group_id
order_number;`) - a missing order_number sorts first, matching SAS's "missing numeric is the
smallest possible value" sort semantics.

SAS-QUIRK(preserved): the "items:" list header prints only when checked at count==1 (same
strict rule as the SDTM converter, stricter than BC's count-in-{1,2}).

SAS-QUIRK(preserved): the codelist: block is gated on codelist_submission_value being
present, not on codelist itself - a codelist with no codelist_submission_value emits no
"codelist:" block at all (only a WARNING). Within the block, "href:" is unconditional even
when codelist itself is blank (producing a dangling ncit_href("")).

SAS-QUIRK(preserved): questionText is *unconditionally* quoted (`cats('"', question_text,
'"')`, no index()-based trigger-char guard, unlike prompt/completionInstructions/
derivationDescription right below it in the same macro) - this looks like an intentional
asymmetry (or a bug never revisited) rather than an oversight worth "fixing", since
unconditional quoting of a plain scalar is a value-preserving no-op for YAML parsing anyway
(confirmed against yaml/20260630_draft/crf/*.yaml's *mix* of quoted/unquoted questionText
values, which resolve to the same parsed strings as this converter's always-quoted output).

SAS-QUIRK(not ported, harmless): `prepopulated_code_cdisc` (via get_term_code) and
`prepopulated_term_cdisc_preferd` (via get_term_preferred_term) are computed but never read
by any issue check - only `prepopulated_term_cdisc` (via get_term_value) and
`codelist_extensible` are. Neither of the two dead lookups is called here.

SAS-QUIRK(not reproduced): CODELIST_TERM_CCODE_MISMATCH's comment string includes
`value_code_cdisc`, a variable last set (or left at its row-initial blank) by the *earlier*
valueList loop on the same row - a stale cross-block value SAS happens to still have lying
around in the PDV, not a deliberate lookup for this check. This port scopes each block's
locals independently, so that comment segment is always blank here; low-stakes since it only
affects one comment string on one already-rare combination (a prepopulated term paired with
a term-code mismatch on the same item).
"""

import os
import re

from cosmoslib.excel_reader import read_named_range
from cosmoslib.naming import crf_yaml_filename, ncit_href, output_path
from cosmoslib.text import clean_value, format_number, squeeze_spaces, words
from cosmoslib.yaml_writer import escape_and_quote, YamlWriter

_MANDATORY_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(TEST|TERM|TRT)$')


def _get(row, column):
    return clean_value(row.get(column))


def _order_sort_key(value):
    """Missing numeric sorts first in SAS (proc sort treats it as the smallest possible
    value); a blank/non-numeric cell here sorts before every real order_number."""
    if value is None:
        return float("-inf")
    if isinstance(value, float) and value != value:  # NaN
        return float("-inf")
    try:
        return float(value)
    except (TypeError, ValueError):
        return float("-inf")


def _sorted_groups(df):
    """`set ...(where=(not missing(crf_group_id)));` then `proc sort by crf_group_id
    order_number;` - drop rows with no crf_group_id, then sort by (crf_group_id,
    order_number) using SAS's missing-sorts-first numeric order."""
    working = df.copy()
    working.loc[:, "crf_group_id"] = working["crf_group_id"].map(clean_value)
    working = working[working["crf_group_id"] != ""].copy()
    working.loc[:, "_order_key_"] = working["order_number"].map(_order_sort_key)
    return working.sort_values(["crf_group_id", "_order_key_"], kind="stable")


def convert_crf_job(job, codelist_index, issue_log):
    """Runs one manifest job (one curation Excel named range) through the CRF converter.
    Returns the list of YAML file paths written."""
    df = read_named_range(job.excel_file, job.range + "$")
    if job.select:
        df = df.query(job.select)

    os.makedirs(job.out_folder, exist_ok=True)

    written = []
    for crf_group_id, rows in _sorted_groups(df).groupby("crf_group_id", sort=False):
        domain = clean_value(rows.iloc[0].get("domain"))
        path = output_path(job.out_folder, crf_yaml_filename(domain, crf_group_id))
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            _write_crf_group(YamlWriter(fh), rows, job, codelist_index, issue_log)
        written.append(path)
    return written


def _write_crf_group(writer, rows, job, codelist_index, issue_log):
    count = 0

    for is_first, (_, row) in _enumerate_first(rows):
        excel_file = _get(row, "_excel_file_")
        tab = _get(row, "_tab_")
        crf_group_id = _get(row, "crf_group_id")
        short_name_row = _get(row, "short_name")  # per-row, not retained - matches SAS
        crf_item = _get(row, "crf_item")

        def emit_issue(condition, issue_type, expected="", actual="", comment="", severity="WARNING"):
            if condition:
                issue_log.add(
                    excel_file, tab, severity, issue_type,
                    expected_value=expected, actual_value=actual, comment=comment,
                    crf_group_id=crf_group_id, short_name=short_name_row, crf_item=crf_item,
                )

        if is_first:
            count = 0
            package_date = job.override_package_date or _get(row, "package_date")
            _write_crf_header(writer, row, crf_group_id, package_date, emit_issue)

        count += 1
        if count == 1 and crf_item:
            writer.block_key("items")

        if crf_item:
            _write_item(writer, row, crf_item, codelist_index, emit_issue)


def _enumerate_first(rows):
    first = True
    for item in rows.iterrows():
        yield first, item
        first = False


def _write_crf_header(writer, row, crf_group_id, package_date, emit_issue):
    short_name = _get(row, "short_name")

    writer.scalar_always_quoted("packageDate", package_date)
    writer.raw("packageType", "crf")
    writer.raw("crfSpecializationId", crf_group_id)

    emit_issue(not short_name, "MISSING_SHORT_NAME", severity="ERROR")
    if short_name:
        writer.scalar("shortName", short_name)

    writer.raw("standard", _get(row, "standard"))
    writer.scalar_always_quoted("standardStartVersion", _get(row, "standard_start_version"))
    writer.scalar_always_quoted("standardEndVersion", _get(row, "standard_end_version"))

    implementation_option = _get(row, "implementation_option")
    if implementation_option:
        writer.raw("implementationOption", implementation_option)
    scenario = _get(row, "scenario")
    if scenario:
        writer.raw("scenario", scenario)

    categories = _get(row, "categories")
    if categories:
        writer.block_key("categories")
        for value in words(categories):
            # SAS-QUIRK(preserved, approximated): SAS backslash-escapes embedded quotes
            # then also runs the result through quote() (which doubles embedded quotes),
            # a redundant double-escape this port doesn't reproduce byte-for-byte - harmless
            # for the categories actually curated so far (plain values, no embedded quotes).
            writer.list_quoted(value, indent=2)

    writer.raw("domain", _get(row, "domain"))

    bc_id = _get(row, "bc_id")
    if bc_id:
        writer.raw("biomedicalConceptId", bc_id)
    vlm_group_id = _get(row, "vlm_group_id")
    if vlm_group_id:
        writer.raw("sdtmDatasetSpecializationId", vlm_group_id)
    emit_issue(not vlm_group_id, "MISSING_VLM_GROUP_ID", severity="NOTE")


def _write_item(writer, row, crf_item, codelist_index, emit_issue):
    variable_name = _get(row, "variable_name")

    writer.raw("- name", crf_item, indent=2)
    writer.raw("variableName", variable_name, indent=4)
    dec_id = _get(row, "dec_id")
    if dec_id:
        writer.raw("dataElementConceptId", dec_id, indent=4)

    _write_text_fields_block(writer, row, emit_issue)
    _write_mandatory_variable_block(writer, row, variable_name, emit_issue)
    _write_datatype_block(writer, row)
    _write_codelist_block(writer, row, codelist_index, emit_issue)
    value_display_list = _write_value_list_block(writer, row, codelist_index, emit_issue)
    _write_selection_type_block(writer, row, value_display_list, emit_issue)
    _write_prepopulated_value_block(writer, row, codelist_index, emit_issue)
    _write_sdtm_target_block(writer, row)


def _write_text_fields_block(writer, row, emit_issue):
    question_text = _get(row, "question_text")
    prompt = _get(row, "prompt")

    emit_issue(not question_text and not prompt, "QUESTION_TEXT_PROMPT_BOTH_MISSING", severity="ERROR")
    emit_issue(
        bool(question_text) and bool(prompt), "QUESTION_TEXT_PROMPT_BOTH_NOT_MISSING",
        comment=f"question_text={question_text}, prompt={prompt}", severity="ERROR",
    )

    if question_text:
        writer.raw("questionText", _escape_question_text(question_text), indent=4)
    if prompt:
        writer.scalar("prompt", prompt, indent=4)

    completion_instructions = _get(row, "completion_instructions")
    if completion_instructions:
        writer.scalar("completionInstructions", completion_instructions, indent=4)


def _escape_question_text(text):
    escaped = text.replace('"', '\\"')
    escaped = escaped.replace("\r\n", "\\r").replace("\n", "\\r")
    return f'"{escaped}"'


def _write_mandatory_variable_block(writer, row, variable_name, emit_issue):
    order_number = _get(row, "order_number")
    if order_number:
        writer.raw("orderNumber", format_number(row.get("order_number")), indent=4)

    mandatory_variable = _get(row, "mandatory_variable") or "N"
    emit_issue(
        bool(_MANDATORY_SUFFIX_RE.match(variable_name)) and mandatory_variable != "Y",
        "MANDATORY_VARIABLE_EXPECTED", expected=mandatory_variable, severity="ERROR",
    )
    writer.raw("mandatoryVariable", "true" if mandatory_variable == "Y" else "false", indent=4)


def _write_datatype_block(writer, row):
    data_type = _get(row, "data_type")
    if data_type:
        writer.raw("dataType", data_type, indent=4)
    length = _get(row, "length")
    if length:
        writer.raw("length", format_number(row.get("length")), indent=4)
    significant_digits = _get(row, "significant_digits")
    if significant_digits:
        writer.raw("significantDigits", format_number(row.get("significant_digits")), indent=4)

    display_hidden = _get(row, "display_hidden") or "N"
    writer.raw("displayHidden", "true" if display_hidden.upper() == "Y" else "false", indent=4)
    derived_variable = _get(row, "derived_variable") or "N"
    writer.raw("derivedVariable", "true" if derived_variable.upper() == "Y" else "false", indent=4)

    derivation_description = _get(row, "derivation_description")
    if derivation_description:
        writer.scalar("derivationDescription", derivation_description, indent=4)


def _write_codelist_block(writer, row, codelist_index, emit_issue):
    codelist = _get(row, "codelist")
    codelist_submission_value = _get(row, "codelist_submission_value")

    if not codelist_submission_value and codelist:
        codelist_submission_value_cdisc = codelist_index.get_codelist_submissionvalue(codelist)
        emit_issue(
            True, "CODELIST_SUBMISSION_VALUE_MISSING", expected=codelist_submission_value_cdisc,
            comment=f"codelist={codelist}",
        )

    if not codelist_submission_value:
        return

    if codelist:
        codelist_submission_value_cdisc = codelist_index.get_codelist_submissionvalue(codelist)
        emit_issue(
            codelist_submission_value != codelist_submission_value_cdisc,
            "CODELIST_SUBMISSION_VALUE_MISMATCH",
            expected=codelist_submission_value_cdisc, actual=codelist_submission_value,
            comment=f"codelist={codelist}",
        )

    writer.block_key("codelist", indent=4)
    writer.raw("submissionValue", codelist_submission_value, indent=6)
    if codelist:
        writer.raw("conceptId", codelist, indent=6)
    writer.raw("href", ncit_href(codelist), indent=6)


def _write_value_list_block(writer, row, codelist_index, emit_issue):
    value_display_list = _get(row, "value_display_list")
    value_list = _get(row, "value_list")
    if not value_display_list:
        return value_display_list

    codelist = _get(row, "codelist")
    codelist_submission_value = _get(row, "codelist_submission_value")
    display_words = words(value_display_list)
    value_words = words(value_list)
    comment = (
        f"value_display_list={value_display_list} ({len(display_words)}), codelist={codelist}, "
        f"codelist_submission_value={codelist_submission_value}, value_list={value_list} ({len(value_words)})"
    )
    emit_issue(len(display_words) == 1, "CODELIST_VALUE_LISTS_1_TERM", comment=comment)
    emit_issue(len(display_words) != len(value_words), "CODELIST_VALUE_LISTS_TERM_COUNTS", comment=comment)

    writer.block_key("valueList", indent=4)
    for i, display_value in enumerate(display_words):
        writer.scalar_always_quoted("- displayValue", display_value, indent=6)
        if i >= len(value_words):
            continue
        value = value_words[i]
        if codelist:
            value_code_cdisc = codelist_index.get_term_code(codelist, value)
            codelist_extensible = codelist_index.get_codelist_extensible(codelist)
            emit_issue(
                not value_code_cdisc and codelist_extensible == "No",
                "CODELIST_VALUE_LIST_TERM_CDISC_MISSING", expected=value_code_cdisc,
                comment=f"codelist_extensible={codelist_extensible}, codelist={codelist}, "
                        f"codelist_submission_value={codelist_submission_value}, "
                        f"value_list={value_list}, value={value}",
            )
        writer.raw("  value", escape_and_quote(value), indent=6)
    return value_display_list


def _write_selection_type_block(writer, row, value_display_list, emit_issue):
    selection_type = _get(row, "selection_type")
    codelist = _get(row, "codelist")
    codelist_submission_value = _get(row, "codelist_submission_value")
    emit_issue(
        not selection_type and bool(value_display_list), "VALUE_LIST_MISSING_SELECTION_TYPE",
        comment=f"value_display_list={value_display_list}, codelist={codelist}, "
                f"codelist_submission_value={codelist_submission_value}",
    )
    if selection_type:
        writer.raw("selectionType", selection_type, indent=4)


def _write_prepopulated_value_block(writer, row, codelist_index, emit_issue):
    prepopulated_term = _get(row, "prepopulated_term")
    if not prepopulated_term:
        return

    prepopulated_code = _get(row, "prepopulated_code")
    codelist = _get(row, "codelist")
    codelist_submission_value = _get(row, "codelist_submission_value")
    value_list = _get(row, "value_list")

    writer.block_key("prepopulatedValue", indent=4)
    writer.scalar_always_quoted("value", prepopulated_term, indent=6)
    if prepopulated_code:
        writer.raw("conceptId", prepopulated_code, indent=6)

    emit_issue(
        bool(value_list), "BOTH_PREPOPULATED_TERM_AND_VALUE_LIST_NOT_MISSING", actual=value_list,
        comment=f"codelist={codelist}, codelist_submission_value={codelist_submission_value}, "
                f"value_list={value_list}, prepopulated_term={prepopulated_term}, "
                f"prepopulated_code={prepopulated_code}",
    )

    if not codelist or not prepopulated_code:
        return
    prepopulated_term_cdisc = codelist_index.get_term_value(codelist, prepopulated_code)
    codelist_extensible = codelist_index.get_codelist_extensible(codelist)
    comment_prefix = (
        f"codelist_extensible={codelist_extensible}, codelist={codelist}, "
        f"codelist_submission_value={codelist_submission_value}, prepopulated_term={prepopulated_term}"
    )

    emit_issue(
        bool(prepopulated_term_cdisc) and not prepopulated_term,
        "CODELIST_TERM_VALUE_MISSING", expected=prepopulated_term_cdisc, actual=prepopulated_term,
        comment=comment_prefix,
    )
    emit_issue(
        prepopulated_term_cdisc != prepopulated_term and bool(prepopulated_term_cdisc) and bool(prepopulated_term),
        "CODELIST_TERM_CCODE_MISMATCH", expected=prepopulated_term_cdisc, actual=prepopulated_term,
        comment=f"{comment_prefix}, value_code_cdisc=",
    )
    emit_issue(
        not prepopulated_term_cdisc and codelist_extensible == "No",
        "CODELIST_TERM_CCODE_MISSING_NOTEXTENSIBLE", expected=prepopulated_term_cdisc, actual=prepopulated_term,
        comment=comment_prefix,
    )


def _write_sdtm_target_block(writer, row):
    sdtm_target_variable = _get(row, "sdtm_target_variable")
    sdtm_annotation = _get(row, "sdtm_annotation")
    if not sdtm_target_variable and not sdtm_annotation:
        return

    writer.block_key("sdtmTarget", indent=4)
    if sdtm_annotation:
        writer.raw("sdtmAnnotation", escape_and_quote(squeeze_spaces(sdtm_annotation)), indent=6)
    if sdtm_target_variable:
        writer.block_key("sdtmVariables", indent=6)
        for value in words(sdtm_target_variable):
            # SAS-QUIRK(preserved): `put +8 "- " +1 qvalue;` - the literal "- " already ends
            # in a space, and +1 inserts another, so there really are two spaces after the
            # dash (confirmed against yaml/20260630_draft/crf/*.yaml: "-  \"AETERM\"").
            writer.fh.write(f"{' ' * 8}-  {escape_and_quote(value)}\n")
