"""
Python port of utilities/macros/generate_yaml_from_sdtm.sas - the largest, most rule-dense
converter macro (~50 distinct add2issues_{bc,sdtm} call sites). Reads one curation Excel
named range (one manifest job), groups rows by vlm_group_id, and writes one SDTM YAML file
per group plus a row per validation finding to an IssueLog.

As with the BC converter, every field written to the YAML comes straight from the curation
workbook or the (network-free) subset-codelist merge - only the ISSUES depend on the live
CDISC Library codelist/relationship lookups (via `codelist_index`/`relations_index`), so
golden-file regression tests can run against stub/fake versions of both with no network
access at all.

`job.type` is read (and dash-to-underscore normalized) by the SAS macro only to build
internal WORK dataset names - it has no effect on the emitted YAML or the output filename
(unlike the BC converter, sdtm_yaml_filename() takes only vlm_group_id) - so it is not
referenced here at all.

SAS-QUIRK(preserved): the "variables:" list header prints only when checked at count==1
(the group's very first row) - stricter than the BC converter's count-in-{1,2} allowance -
so if a group's first row has no sdtm_variable, "variables:" never prints for that group at
all, even though later rows plainly do have one.

SAS-QUIRK(preserved): `comparator=""` auto-clear (approved to preserve exactly, see
plans/port-sas-utilities-to-python.md) - a *TEST-suffixed variable with a comparator logs
WHERECLAUSE_UNEXPECTED and then clears the comparator as a side effect, in that order, so
the cleared value (not the original) is what ends up in the emitted YAML.

SAS-QUIRK(not ported, harmless): get_predicateterm()/exists_predicateterm() are computed in
the SAS source but their own issue checks are commented out, and exists_predicateterm's
result is overwritten before ever being read - neither influences output, so neither is
called here. Only RelationsIndex.exists_predicaterm_linkingphrase() (the *_COMBINATION_NOT_
FOUND check) and the LinkML enum checks for LinkingPhrase/PredicateTerm are live.
"""

import os
import re

from cosmoslib.enums import exists_enum_term
from cosmoslib.excel_reader import read_named_range
from cosmoslib.naming import ncit_href, output_path, sdtm_yaml_filename
from cosmoslib.subset_codelists import load_subset_codelists, subset_value_list_by_name
from cosmoslib.text import clean_value, format_number, words
from cosmoslib.yaml_writer import YamlWriter

_MANDATORY_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(TEST|TESTCD|TERM|TRT|QSCAT|FTCAT|IECAT)$')
_ORRES_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(ORRES)$')
_STRESC_STRESN_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(STRESC|STRESN)$')
_STRESU_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(STRESU)$')
_DECOD_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(DECOD)$')
_TEST_TESTCD_SUFFIX_RE = re.compile(r'^[A-Z]{0,2}(TEST|TESTCD)$')
_VLM_TARGET_EXPECTED_RE = re.compile(r'.*(ORRES|ORRESU|STRESC|STRESN|STRESU)$')
_VLM_TARGET_UNEXPECTED_EXCLUDE = ("ORRES", "ORRESU", "DECOD", "STRESC", "STRESN", "STRESU", "VAL", "VCDREF", "VCDVER")
_WHERECLAUSE_TEST_SUFFIXES = ("RESU", "RRES", "RESC", "RESN")


def _get(row, column):
    return clean_value(row.get(column))


def _sorted_groups(df):
    """`set ...(where=(not missing(vlm_group_id))); order=_n_;` then `proc sort by
    vlm_group_id order;` - drop rows with no vlm_group_id, then a stable sort by
    (vlm_group_id, original row order)."""
    working = df.copy()
    working.loc[:, "vlm_group_id"] = working["vlm_group_id"].map(clean_value)
    working = working[working["vlm_group_id"] != ""].copy()
    working.loc[:, "_order_"] = range(1, len(working) + 1)
    return working.sort_values(["vlm_group_id", "_order_"], kind="stable")


def convert_sdtm_job(job, enum_index, codelist_index, relations_index, issue_log):
    """Runs one manifest job (one curation Excel named range) through the SDTM converter.
    Returns the list of YAML file paths written."""
    df = read_named_range(job.excel_file, job.range + "$")
    if job.select:
        df = df.query(job.select)

    subset_lookup = {}
    if job.subsets_source:
        # job.subsets_source is usually one {file, range} dict, but convert_latest_xlsx2yaml.py's
        # "latest" regeneration unions two historical subset-codelist sheets (matching
        # `data subsets; set work.subsets subsets1 subsets2; run;` in
        # utilities/convert_latest_xlsx2yaml.sas's run_latest_sdtm macro), so a list of
        # {file, range} dicts is accepted too - later sources win on a duplicate
        # subset_short_name, same as the SAS union's last-row-wins hash-key semantics.
        sources = job.subsets_source if isinstance(job.subsets_source, list) else [job.subsets_source]
        subset_rows = []
        for source in sources:
            subset_rows.extend(load_subset_codelists(source["file"], source["range"]))
        subset_lookup = subset_value_list_by_name(subset_rows)

    os.makedirs(job.out_folder, exist_ok=True)

    written = []
    for vlm_group_id, rows in _sorted_groups(df).groupby("vlm_group_id", sort=False):
        path = output_path(job.out_folder, sdtm_yaml_filename(vlm_group_id))
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            _write_sdtm_group(
                YamlWriter(fh), rows, job, enum_index, codelist_index, relations_index, subset_lookup, issue_log
            )
        written.append(path)
    return written


def _write_sdtm_group(writer, rows, job, enum_index, codelist_index, relations_index, subset_lookup, issue_log):
    count = 0

    for is_first, (_, row) in _enumerate_first(rows):
        excel_file = _get(row, "_excel_file_")
        tab = _get(row, "_tab_")
        vlm_group_id = _get(row, "vlm_group_id")
        short_name_row = _get(row, "short_name")  # per-row, not retained - matches SAS
        sdtm_variable = _get(row, "sdtm_variable")

        def emit_issue(condition, issue_type, expected="", actual="", comment="", severity="WARNING"):
            if condition:
                issue_log.add(
                    excel_file, tab, severity, issue_type,
                    expected_value=expected, actual_value=actual, comment=comment,
                    vlm_group_id=vlm_group_id, short_name=short_name_row, sdtm_variable=sdtm_variable,
                )

        if is_first:
            count = 0
            package_date = job.override_package_date or _get(row, "package_date")
            _write_sdtm_header(writer, row, vlm_group_id, package_date)

        count += 1
        if count == 1 and sdtm_variable:
            writer.block_key("variables")

        if sdtm_variable:
            _write_variable(
                writer, row, sdtm_variable, job.check_relationships,
                enum_index, codelist_index, relations_index, subset_lookup, emit_issue,
            )


def _enumerate_first(rows):
    first = True
    for item in rows.iterrows():
        yield first, item
        first = False


def _write_sdtm_header(writer, row, vlm_group_id, package_date):
    short_name = _get(row, "short_name")

    writer.scalar_always_quoted("packageDate", package_date)
    writer.raw("packageType", "sdtm")
    writer.raw("datasetSpecializationId", vlm_group_id)
    writer.raw("domain", _get(row, "domain"))
    if short_name:
        writer.scalar("shortName", short_name)
    writer.raw("source", _get(row, "vlm_source"))
    writer.scalar_always_quoted("sdtmigStartVersion", _get(row, "sdtmig_start_version"))
    writer.scalar_always_quoted("sdtmigEndVersion", _get(row, "sdtmig_end_version"))
    bc_id = _get(row, "bc_id")
    if bc_id:
        writer.raw("biomedicalConceptId", bc_id)


def _write_variable(
    writer, row, sdtm_variable, check_relationships, enum_index, codelist_index, relations_index,
    subset_lookup, emit_issue,
):
    dec_id = _get(row, "dec_id")
    nsv_flag = _get(row, "nsv_flag") or "N"

    writer.raw("- name", sdtm_variable, indent=2)
    if dec_id:
        writer.raw("dataElementConceptId", dec_id, indent=4)
    writer.raw("isNonStandard", "true" if nsv_flag.upper() == "Y" else "false", indent=4)

    codelist = _get(row, "codelist")
    codelist_submission_value = _get(row, "codelist_submission_value")
    codelist_extensible = codelist_index.get_codelist_extensible(codelist) if codelist else ""
    _write_codelist_block(writer, row, codelist, codelist_index, emit_issue)
    value_list = _write_subset_codelist_block(writer, row, subset_lookup, emit_issue)
    _write_value_list_block(
        writer, value_list, codelist, codelist_submission_value, codelist_extensible, codelist_index, emit_issue
    )
    _write_assigned_term_block(writer, row, codelist, codelist_extensible, codelist_index, emit_issue)
    _write_role_datatype_block(writer, row, enum_index, emit_issue)
    _write_relationship_block(
        writer, row, sdtm_variable, check_relationships, enum_index, relations_index, emit_issue
    )
    _write_mandatory_block(writer, row, sdtm_variable, emit_issue)
    _write_origin_block(writer, row, sdtm_variable, enum_index, emit_issue)
    _write_comparator_and_vlm_target_block(writer, row, sdtm_variable, value_list, enum_index, emit_issue)


def _write_codelist_block(writer, row, codelist, codelist_index, emit_issue):
    if not codelist:
        return
    codelist_submission_value = _get(row, "codelist_submission_value")
    codelist_submission_value_cdisc = codelist_index.get_codelist_submissionvalue(codelist)

    emit_issue(
        not codelist_submission_value, "CODELIST_SUBMISSION_VALUE_MISSING",
        expected=codelist_submission_value_cdisc, comment=f"codelist={codelist}",
    )
    emit_issue(
        codelist_submission_value != codelist_submission_value_cdisc,
        "CODELIST_SUBMISSION_VALUE_MISMATCH",
        expected=codelist_submission_value_cdisc, actual=codelist_submission_value,
        comment=f"codelist={codelist}",
    )

    writer.block_key("codelist", indent=4)
    writer.raw("conceptId", codelist, indent=6)
    writer.raw("href", ncit_href(codelist), indent=6)
    if codelist_submission_value:
        writer.raw("submissionValue", codelist_submission_value, indent=6)


def _write_subset_codelist_block(writer, row, subset_lookup, emit_issue):
    value_list = _get(row, "value_list")
    subset_codelist = _get(row, "subset_codelist")
    if not subset_codelist:
        return value_list

    subset_value_list = subset_lookup.get(subset_codelist, "")
    codelist = _get(row, "codelist")
    codelist_submission_value = _get(row, "codelist_submission_value")
    comment_prefix = f"codelist={codelist}, codelist_submission_value={codelist_submission_value}"

    writer.raw("subsetCodelist", subset_codelist, indent=4)
    emit_issue(
        bool(value_list) and bool(subset_value_list) and value_list != subset_value_list,
        "SUBSETCODELIST_VALUE_LIST_NOT_MISSING_AND_NOT_EQUAL",
        expected=subset_value_list, actual=value_list,
        comment=f"{comment_prefix}, subset_codelist={subset_codelist}, value_list={value_list}",
    )
    emit_issue(
        not value_list and not subset_value_list,
        "SUBSETCODELIST_SUBSET_VALUE_LIST_AND_VALUE_LIST_MISSING",
        actual=value_list,
        comment=f"{comment_prefix}, subset_codelist={subset_codelist}, "
                f"subset_value_list={subset_value_list}, value_list={value_list}",
    )
    emit_issue(
        not subset_value_list,
        "SUBSETCODELIST_SUBSET_VALUE_LIST_MISSING",
        actual=value_list,
        comment=f"{comment_prefix}, subset_codelist={subset_codelist}, "
                f"subset_value_list={subset_value_list}, value_list={value_list}",
    )
    return subset_value_list


def _write_value_list_block(
    writer, value_list, codelist, codelist_submission_value, codelist_extensible, codelist_index, emit_issue
):
    if not value_list:
        return
    comment = f"codelist={codelist}, codelist_submission_value={codelist_submission_value}, value_list={value_list}"

    emit_issue("," in value_list, "VALUE_LIST_COMMA", actual=value_list, comment=comment)
    emit_issue(";" not in value_list, "VALUE_LIST_1_TERM", actual=value_list, comment=comment, severity="NOTE")

    writer.block_key("valueList", indent=4)
    for value in words(value_list):
        writer.list_quoted(value, indent=6)
        if not codelist:
            continue
        value_code_cdisc = codelist_index.get_term_code(codelist, value)
        value_up = value.upper()
        value_code_cdisc_up = codelist_index.get_term_code(codelist, value_up)

        value_comment = (
            f"codelist_extensible={codelist_extensible}, codelist={codelist}, "
            f"codelist_submission_value={codelist_submission_value}, value_list={value_list}, value={value}"
        )
        emit_issue(
            not value_code_cdisc and codelist_extensible == "No",
            "CODELIST_NOTEXTENSIBLE_VALUE_LIST_TERM_CDISC_MISSING", expected=value_code_cdisc,
            comment=value_comment,
        )
        emit_issue(
            not value_code_cdisc and codelist_extensible == "Yes",
            "CODELIST_EXTENSIBLE_VALUE_LIST_TERM_CDISC_MISSING", expected=value_code_cdisc,
            comment=value_comment,
        )
        emit_issue(
            value_code_cdisc != value_code_cdisc_up and bool(value_code_cdisc_up),
            "CODELIST_VALUE_LIST_TERM_WRONG_CASE", expected=value_up, actual=value,
            comment=f"codelist={codelist}, value_list={value_list}, value={value}, "
                    f"value_code_cdisc={value_code_cdisc}, value_code_cdisc_up={value_code_cdisc_up}",
        )


def _write_assigned_term_block(writer, row, codelist, codelist_extensible, codelist_index, emit_issue):
    assigned_value = _get(row, "assigned_value")
    if not assigned_value:
        return
    assigned_term = _get(row, "assigned_term")
    value_list = _get(row, "value_list")
    codelist_submission_value = _get(row, "codelist_submission_value")

    writer.block_key("assignedTerm", indent=4)
    if assigned_term:
        writer.raw("conceptId", assigned_term, indent=6)
    writer.scalar_always_quoted("value", assigned_value, indent=6)

    emit_issue(
        bool(value_list), "ASSIGNED_VALUE_AND_VALUE_LIST_NOT_MISSING", actual=value_list,
        comment=f"codelist={codelist}, codelist_submission_value={codelist_submission_value}, "
                f"value_list={value_list}, assigned_value={assigned_value}",
    )
    emit_issue(
        ";" in assigned_value, "ASSIGNED_VALUE_SEMI-COLON", actual=assigned_value,
        comment=f"codelist={codelist}, codelist_submission_value={codelist_submission_value}, "
                f"assigned_value={assigned_value}",
    )

    if not codelist:
        return
    assigned_term_cdisc = codelist_index.get_term_code(codelist, assigned_value)
    value_up = assigned_value.upper()
    value_code_cdisc_up = codelist_index.get_term_code(codelist, value_up)
    comment_prefix = (
        f"codelist_extensible={codelist_extensible}, codelist={codelist}, "
        f"codelist_submission_value={codelist_submission_value}, assigned_value={assigned_value}"
    )

    emit_issue(
        not assigned_term_cdisc and bool(assigned_term),
        "CODELIST_TERM_CDISC_CCODE_MISSING", expected=assigned_term_cdisc, actual=assigned_term,
        comment=comment_prefix,
    )
    emit_issue(
        bool(assigned_term_cdisc) and not assigned_term,
        "CODELIST_TERM_CCODE_MISSING", expected=assigned_term_cdisc, actual=assigned_term,
        comment=comment_prefix,
    )
    emit_issue(
        assigned_term_cdisc != assigned_term and bool(assigned_term_cdisc) and bool(assigned_term),
        "CODELIST_TERM_CCODE_MISMATCH", expected=assigned_term_cdisc, actual=assigned_term,
        comment=comment_prefix,
    )
    emit_issue(
        not assigned_term_cdisc and codelist_extensible == "No",
        "CODELIST_NOTEXTENSIBLE_TERM_CCODE_MISSING", expected=assigned_term_cdisc, actual=assigned_term,
        comment=comment_prefix,
    )
    emit_issue(
        not assigned_term_cdisc and codelist_extensible == "Yes",
        "CODELIST_EXTENSIBLE_TERM_CCODE_MISSING", expected=assigned_term_cdisc, actual=assigned_term,
        comment=comment_prefix,
    )
    emit_issue(
        assigned_term_cdisc != value_code_cdisc_up and bool(value_code_cdisc_up),
        "CODELIST_ASSIGNED_TERM_WRONG_CASE", expected=value_up, actual=assigned_value,
        comment=f"codelist={codelist}, codelist_submission_value={codelist_submission_value}, "
                f"assigned_term={assigned_term}, assigned_term_cdisc={assigned_term_cdisc}, "
                f"value_code_cdisc_up={value_code_cdisc_up}",
    )


def _write_role_datatype_block(writer, row, enum_index, emit_issue):
    role = _get(row, "role")
    if role:
        emit_issue(
            not exists_enum_term(enum_index, "Role", role), "INVALID_VALUE_ROLE", actual=role, severity="ERROR"
        )
        writer.raw("role", role, indent=4)

    data_type = _get(row, "data_type")
    if data_type:
        emit_issue(
            not exists_enum_term(enum_index, "SDTMVariableDataType", data_type), "INVALID_VALUE_DATATYPE",
            actual=data_type, severity="ERROR",
        )
        writer.raw("dataType", data_type, indent=4)

    length = _get(row, "length")
    if length:
        writer.raw("length", format_number(row.get("length")), indent=4)

    format_value = _get(row, "format")
    if format_value:
        writer.scalar_always_quoted("format", format_value, indent=4)

    significant_digits = _get(row, "significant_digits")
    if significant_digits:
        writer.raw("significantDigits", format_number(row.get("significant_digits")), indent=4)

    comment = f"data_type={data_type}, format={format_value}, significant_digits={significant_digits}"
    emit_issue(
        bool(data_type) and data_type != "float" and bool(format_value),
        "DATATYPE_NOT_FLOAT_FORMAT", actual=format_value, comment=comment,
    )
    emit_issue(
        bool(data_type) and data_type != "float" and bool(significant_digits),
        "DATATYPE_NOT_FLOAT_SIGNIFICANT_DIGITS", actual=significant_digits, comment=comment,
    )
    emit_issue(
        data_type == "float" and not significant_digits,
        "DATATYPE_FLOAT_MISSING_SIGNIFICANT_DIGITS", actual=significant_digits, comment=comment,
    )


def _write_relationship_block(
    writer, row, sdtm_variable, check_relationships, enum_index, relations_index, emit_issue
):
    subject = _get(row, "subject")
    linking_phrase = _get(row, "linking_phrase")
    predicate_term = _get(row, "predicate_term")
    obj = _get(row, "object")
    relationship_comment = (
        f"subject={subject}, linking_phrase={linking_phrase}, "
        f"predicate_term={predicate_term}, object={obj}"
    )

    any_present = bool(subject or linking_phrase or predicate_term or obj)
    all_present = bool(subject and linking_phrase and predicate_term and obj)
    emit_issue(any_present and not all_present, "RELATIONSHIP_ISSUE", comment=relationship_comment)

    if check_relationships:
        if linking_phrase:
            emit_issue(
                not exists_enum_term(enum_index, "LinkingPhrase", linking_phrase),
                "INVALID_VALUE_LINKING_PHRASE", actual=linking_phrase, comment=relationship_comment,
                severity="ERROR",
            )
        if predicate_term:
            emit_issue(
                not exists_enum_term(enum_index, "PredicateTerm", predicate_term),
                "INVALID_VALUE_PREDICATE_TERM", actual=predicate_term, comment=relationship_comment,
                severity="ERROR",
            )
        if predicate_term and linking_phrase:
            found = relations_index.exists_predicaterm_linkingphrase(linking_phrase, predicate_term)
            emit_issue(
                not found, "RELATIONSHIP_ISSUE_COMBINATION_NOT_FOUND",
                actual=f"{linking_phrase},{predicate_term}", comment=relationship_comment,
            )

    if not subject:
        return

    emit_issue(
        sdtm_variable != subject, "RELATIONSHIP_ISSUE_VARIABLE_NE_SUBJECT",
        expected=sdtm_variable, actual=subject, comment=f"sdtm_variable={sdtm_variable}, {relationship_comment}",
    )
    emit_issue(
        subject == obj, "RELATIONSHIP_ISSUE_SUBJECT_EQ_OBJECT",
        actual=subject, comment=f"sdtm_variable={sdtm_variable}, {relationship_comment}",
    )
    emit_issue(
        sdtm_variable == obj, "RELATIONSHIP_ISSUE_VARIABLE_EQ_OBJECT",
        actual=obj, comment=f"sdtm_variable={sdtm_variable}, {relationship_comment}",
    )
    emit_issue(
        subject[:2] != obj[:2], "RELATIONSHIP_ISSUE_DIFFERENT_DOMAINS",
        comment=f"sdtm_variable={sdtm_variable}, {relationship_comment}",
    )

    writer.block_key("relationship", indent=4)
    writer.raw("subject", subject, indent=6)
    writer.raw("linkingPhrase", linking_phrase.lower(), indent=6)
    writer.raw("predicateTerm", predicate_term, indent=6)
    writer.raw("object", obj, indent=6)


def _write_mandatory_block(writer, row, sdtm_variable, emit_issue):
    mandatory_variable = _get(row, "mandatory_variable")
    emit_issue(
        bool(_MANDATORY_SUFFIX_RE.match(sdtm_variable)) and mandatory_variable != "Y",
        "MANDATORY_VARIABLE_EXPECTED", expected=mandatory_variable, severity="ERROR",
    )
    writer.raw("mandatoryVariable", "true" if mandatory_variable == "Y" else "false", indent=4)

    mandatory_value = _get(row, "mandatory_value")
    emit_issue(
        bool(_MANDATORY_SUFFIX_RE.match(sdtm_variable)) and mandatory_value != "Y",
        "MANDATORY_VALUE_EXPECTED", expected=mandatory_value, severity="ERROR",
    )
    writer.raw("mandatoryValue", "true" if mandatory_value == "Y" else "false", indent=4)


def _write_origin_block(writer, row, sdtm_variable, enum_index, emit_issue):
    origin_type = _get(row, "origin_type")
    emit_issue(bool(_ORRES_SUFFIX_RE.match(sdtm_variable)) and origin_type != "Collected",
               "INVALID_ORIGIN_TYPE_ORRES", actual=origin_type, severity="ERROR")
    emit_issue(bool(_STRESC_STRESN_SUFFIX_RE.match(sdtm_variable)) and origin_type != "Derived",
               "INVALID_ORIGIN_TYPE_STRESC_STRESN", actual=origin_type, severity="ERROR")
    emit_issue(bool(_STRESU_SUFFIX_RE.match(sdtm_variable)) and origin_type != "Assigned",
               "INVALID_ORIGIN_TYPE_STRESU", actual=origin_type, severity="ERROR")
    emit_issue(bool(_DECOD_SUFFIX_RE.match(sdtm_variable)) and origin_type != "Assigned",
               "INVALID_ORIGIN_TYPE_DECOD", actual=origin_type, severity="ERROR")
    emit_issue(bool(_TEST_TESTCD_SUFFIX_RE.match(sdtm_variable)) and origin_type != "Assigned",
               "INVALID_ORIGIN_TYPE_TEST_TESTCD", actual=origin_type, severity="ERROR")
    if origin_type:
        emit_issue(
            not exists_enum_term(enum_index, "OriginType", origin_type), "INVALID_VALUE_ORIGIN_TYPE",
            actual=origin_type, severity="ERROR",
        )
        writer.raw("originType", origin_type, indent=4)

    origin_source = _get(row, "origin_source")
    emit_issue(bool(_DECOD_SUFFIX_RE.match(sdtm_variable)) and origin_source != "Sponsor",
               "INVALID_ORIGIN_SOURCE_DECOD", actual=origin_source, severity="ERROR")
    emit_issue(bool(_TEST_TESTCD_SUFFIX_RE.match(sdtm_variable)) and origin_source != "Sponsor",
               "INVALID_ORIGIN_SOURCE_TEST_TESTCD", actual=origin_source, severity="ERROR")
    if origin_source:
        emit_issue(
            not exists_enum_term(enum_index, "OriginSource", origin_source), "INVALID_VALUE_ORIGIN_SOURCE",
            actual=origin_source, severity="ERROR",
        )
        writer.raw("originSource", origin_source, indent=4)


def _write_comparator_and_vlm_target_block(writer, row, sdtm_variable, value_list, enum_index, emit_issue):
    comparator = _get(row, "comparator")
    assigned_value = _get(row, "assigned_value")
    vlm_target = _get(row, "vlm_target")

    if len(sdtm_variable) >= 4:
        suffix = sdtm_variable[-4:]
        if suffix == "TEST" and comparator:
            emit_issue(
                True, "WHERECLAUSE_UNEXPECTED", actual=comparator,
                comment=f"comparator={comparator}, assigned_value={assigned_value}, "
                        f"comparator will be set to missing",
            )
            comparator = ""  # SAS-QUIRK(preserved): logged first, then cleared - in that order
        elif suffix in _WHERECLAUSE_TEST_SUFFIXES and comparator:
            emit_issue(
                True, "WHERECLAUSE_UNEXPECTED", actual=comparator,
                comment=f"comparator={comparator}, assigned_value={assigned_value}, value_list={value_list}",
            )

    emit_issue(
        comparator == "EQ" and not assigned_value, "COMPARATOR_ASSIGNED_VALUE_MISSING", actual=comparator,
        comment=f"comparator={comparator}, value_list={value_list}, assigned_value={assigned_value}",
    )
    emit_issue(
        comparator == "IN" and not value_list, "COMPARATOR_VALUE_LIST_MISSING", actual=comparator,
        comment=f"comparator={comparator}, value_list={value_list}, assigned_value={assigned_value}",
    )
    emit_issue(
        bool(comparator) and bool(vlm_target), "COMPARATOR_AND_VLM_TARGET_NOT_MISSING",
        comment=f"comparator={comparator}, vlm_target={vlm_target}",
    )
    emit_issue(
        bool(vlm_target) and not any(token in sdtm_variable for token in _VLM_TARGET_UNEXPECTED_EXCLUDE),
        "VLM_TARGET_UNEXPECTED",
        comment=f"sdtm_variable={sdtm_variable}, comparator={comparator}, vlm_target={vlm_target}",
    )
    emit_issue(
        not vlm_target and bool(_VLM_TARGET_EXPECTED_RE.match(sdtm_variable)),
        "VLM_TARGET_EXPECTED",
        comment=f"sdtm_variable={sdtm_variable}, comparator={comparator}, vlm_target={vlm_target}",
    )

    if comparator:
        emit_issue(
            not exists_enum_term(enum_index, "Comparator", comparator), "INVALID_VALUE_COMPARATOR",
            actual=comparator, severity="ERROR",
        )
        writer.raw("comparator", comparator, indent=4)

    if vlm_target.upper() == "Y":
        writer.raw("vlmTarget", "true", indent=4)
