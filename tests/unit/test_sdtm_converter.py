import os
from unittest.mock import patch

import pandas as pd
import yaml

from cosmoslib.issues import IssueLog
from cosmoslib.sdtm_converter import convert_sdtm_job
from cosmoslib.templates import SDTM_ISSUE_ID_COLUMNS

ENUM_INDEX = {
    "Role": ["Topic", "Qualifier", "Timing"],
    "SDTMVariableDataType": ["text", "integer", "float"],
    "LinkingPhrase": ["is the result of the test in", "decodes the value in"],
    "PredicateTerm": ["IS_RESULT_OF", "DECODES"],
    "OriginType": ["Collected", "Derived", "Assigned"],
    "OriginSource": ["Sponsor", "Investigator"],
    "Comparator": ["EQ", "IN"],
}


class _FakeJob:
    def __init__(self, out_folder, check_relationships=True, subsets_source=None, select=None):
        self.excel_file = "irrelevant.xlsx"
        self.range = "SDTM_TEST"
        self.type = ""
        self.select = select
        self.out_folder = out_folder
        self.override_package_date = "2026-07-14"
        self.check_relationships = check_relationships
        self.subsets_source = subsets_source


class _FakeCodelistIndex:
    def __init__(self, term_codes=None, submission_values=None, extensible=None):
        self.term_codes = term_codes or {}
        self.submission_values = submission_values or {}
        self.extensible = extensible or {}

    def get_term_code(self, codelist_conceptid, coded_value):
        return self.term_codes.get((codelist_conceptid, coded_value), "")

    def get_term_value(self, codelist_conceptid, coded_value_conceptid):
        return ""

    def get_term_preferred_term(self, codelist_conceptid, coded_value_conceptid):
        return ""

    def get_codelist_submissionvalue(self, codelist_conceptid):
        return self.submission_values.get(codelist_conceptid, "")

    def get_codelist_extensible(self, codelist_conceptid):
        return self.extensible.get(codelist_conceptid, "")


class _FakeRelationsIndex:
    def __init__(self, valid_pairs=None):
        self.valid_pairs = valid_pairs or set()

    def get_predicateterm(self, linking_phrase):
        return ""

    def exists_predicaterm_linkingphrase(self, linking_phrase, predicate_term):
        return (linking_phrase, predicate_term) in self.valid_pairs

    def exists_predicateterm(self, predicate_term):
        return True


def _run(df, tmp_path, codelist_index=None, relations_index=None, job=None, enum_index=ENUM_INDEX):
    job = job or _FakeJob(str(tmp_path))
    issue_log = IssueLog(SDTM_ISSUE_ID_COLUMNS)
    with patch("cosmoslib.sdtm_converter.read_named_range", return_value=df):
        written = convert_sdtm_job(
            job, enum_index, codelist_index or _FakeCodelistIndex(), relations_index or _FakeRelationsIndex(),
            issue_log,
        )
    return written, issue_log


def _row(vlm_group_id, sdtm_variable=None, **kwargs):
    row = {"vlm_group_id": vlm_group_id, "_excel_file_": "wb.xlsx", "_tab_": "SDTM_TEST"}
    if sdtm_variable is not None:
        row["sdtm_variable"] = sdtm_variable
    row.update(kwargs)
    return row


def test_variables_header_prints_only_when_first_row_has_a_variable(tmp_path):
    # SAS-QUIRK(preserved): stricter than BC's count-in-{1,2} - only count==1 counts.
    df = pd.DataFrame([
        _row("G1", short_name="Alpha"),
        _row("G1", "VAR1", role="Topic"),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "variables:" not in text
    assert "- name: VAR1" in text


def test_variables_header_prints_when_first_row_has_a_variable(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", role="Topic")])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "variables:" in text
    assert text.index("variables:") < text.index("- name: VAR1")


def test_domain_and_source_are_always_emitted_even_when_blank(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1")])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)
    assert loaded["domain"] is None
    assert loaded["source"] is None
    assert loaded["sdtmigEndVersion"] == ""


def test_boolean_fields_render_as_yaml_booleans(tmp_path):
    df = pd.DataFrame([
        _row("G1", "VAR1", nsv_flag="Y", mandatory_variable="Y", mandatory_value="N", vlm_target="Y"),
    ])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert loaded["isNonStandard"] is True
    assert loaded["mandatoryVariable"] is True
    assert loaded["mandatoryValue"] is False
    assert loaded["vlmTarget"] is True


def test_vlm_target_false_is_never_emitted(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", vlm_target="N")])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert "vlmTarget" not in loaded


def test_length_and_significant_digits_render_without_trailing_zero(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", length=20.0, significant_digits=2.0, data_type="float")])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "length: 20\n" in text
    assert "significantDigits: 2\n" in text


def test_subset_codelist_overrides_value_list_and_flags_mismatch(tmp_path):
    df = pd.DataFrame([
        _row("G1", "VAR1", subset_codelist="MYSUBSET", value_list="A;B"),
    ])
    job = _FakeJob(str(tmp_path))
    with patch("cosmoslib.sdtm_converter.load_subset_codelists", return_value=[]), \
         patch("cosmoslib.sdtm_converter.subset_value_list_by_name", return_value={"MYSUBSET": "X;Y;Z"}):
        job.subsets_source = {"file": "irrelevant.xlsx", "range": "irrelevant"}
        written, issue_log = _run(df, tmp_path, job=job)

    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert loaded["valueList"] == ["X", "Y", "Z"]
    assert loaded["subsetCodelist"] == "MYSUBSET"
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["SUBSETCODELIST_VALUE_LIST_NOT_MISSING_AND_NOT_EQUAL"]["expected_value"] == "X;Y;Z"


def test_subsets_source_list_merges_multiple_sources(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", subset_codelist="FROM_SECOND", value_list="X;Y")])
    job = _FakeJob(str(tmp_path))
    job.subsets_source = [
        {"file": "first.xlsx", "range": "Subset Codelist Example"},
        {"file": "second.xlsx", "range": "Subset Codelist"},
    ]

    def fake_load(file_path, range_name):
        if file_path == "first.xlsx":
            return [{"parent_codelist": "C1", "subset_short_name": "FROM_FIRST", "subset_value_list": "A;B"}]
        return [{"parent_codelist": "C2", "subset_short_name": "FROM_SECOND", "subset_value_list": "X;Y"}]

    with patch("cosmoslib.sdtm_converter.load_subset_codelists", side_effect=fake_load):
        written, _ = _run(df, tmp_path, job=job)

    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert loaded["valueList"] == ["X", "Y"]


def test_subset_codelist_missing_lookup_flags_two_missing_issues(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", subset_codelist="NOSUCHSUBSET")])
    job = _FakeJob(str(tmp_path))
    with patch("cosmoslib.sdtm_converter.load_subset_codelists", return_value=[]), \
         patch("cosmoslib.sdtm_converter.subset_value_list_by_name", return_value={}):
        job.subsets_source = {"file": "irrelevant.xlsx", "range": "irrelevant"}
        written, issue_log = _run(df, tmp_path, job=job)
    types = {row["issue_type"] for row in issue_log.rows}
    assert "SUBSETCODELIST_SUBSET_VALUE_LIST_AND_VALUE_LIST_MISSING" in types
    assert "SUBSETCODELIST_SUBSET_VALUE_LIST_MISSING" in types
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert "valueList" not in loaded


def test_wrong_case_codelist_term_is_flagged(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", codelist="C1", value_list="apple")])
    codelist_index = _FakeCodelistIndex(term_codes={("C1", "APPLE"): "C99"})
    written, issue_log = _run(df, tmp_path, codelist_index=codelist_index)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["CODELIST_VALUE_LIST_TERM_WRONG_CASE"]["expected_value"] == "APPLE"
    assert by_type["CODELIST_VALUE_LIST_TERM_WRONG_CASE"]["actual_value"] == "apple"
    # value is still emitted as curated, unaffected by the case-mismatch check
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert loaded["valueList"] == ["apple"]


def test_codelist_not_extensible_missing_term_is_an_error(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", codelist="C1", value_list="apple")])
    codelist_index = _FakeCodelistIndex(extensible={"C1": "No"})
    _, issue_log = _run(df, tmp_path, codelist_index=codelist_index)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["CODELIST_NOTEXTENSIBLE_VALUE_LIST_TERM_CDISC_MISSING"]["severity"] == "WARNING"


def test_comparator_cleared_after_logging_for_test_suffixed_variable(tmp_path):
    # SAS-QUIRK(preserved): comparator="" auto-clear - logged first, then cleared, so the
    # cleared (blank) value is what ends up in the emitted YAML, not the original.
    df = pd.DataFrame([_row("G1", "SCTEST", comparator="EQ", assigned_value="X")])
    written, issue_log = _run(df, tmp_path)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["WHERECLAUSE_UNEXPECTED"]["actual_value"] == "EQ"
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert "comparator" not in loaded


def test_comparator_not_cleared_for_resu_suffixed_variable(tmp_path):
    df = pd.DataFrame([_row("G1", "SCSTRESU", comparator="EQ", assigned_value="X")])
    written, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "WHERECLAUSE_UNEXPECTED" for row in issue_log.rows)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["variables"][0]
    assert loaded["comparator"] == "EQ"


def test_relationship_combination_not_found_when_check_relationships_enabled(tmp_path):
    df = pd.DataFrame([
        _row("G1", "VARORRES", subject="VARORRES", linking_phrase="is the result of the test in",
             predicate_term="IS_RESULT_OF", object="VARTESTCD"),
    ])
    relations_index = _FakeRelationsIndex(valid_pairs=set())  # combination not registered
    _, issue_log = _run(df, tmp_path, relations_index=relations_index)
    assert any(row["issue_type"] == "RELATIONSHIP_ISSUE_COMBINATION_NOT_FOUND" for row in issue_log.rows)


def test_relationship_checks_skipped_when_check_relationships_disabled(tmp_path):
    df = pd.DataFrame([
        _row("G1", "VARORRES", subject="VARORRES", linking_phrase="not a real phrase",
             predicate_term="NOT_REAL", object="VARTESTCD"),
    ])
    job = _FakeJob(str(tmp_path), check_relationships=False)
    _, issue_log = _run(df, tmp_path, job=job)
    types = {row["issue_type"] for row in issue_log.rows}
    assert "INVALID_VALUE_LINKING_PHRASE" not in types
    assert "INVALID_VALUE_PREDICATE_TERM" not in types
    assert "RELATIONSHIP_ISSUE_COMBINATION_NOT_FOUND" not in types


def test_relationship_variable_ne_subject_and_different_domains(tmp_path):
    df = pd.DataFrame([
        _row("G1", "AEDECOD", subject="AETERM", linking_phrase="decodes the value in",
             predicate_term="DECODES", object="SCTESTCD"),
    ])
    _, issue_log = _run(df, tmp_path)
    types = {row["issue_type"] for row in issue_log.rows}
    assert "RELATIONSHIP_ISSUE_VARIABLE_NE_SUBJECT" in types
    assert "RELATIONSHIP_ISSUE_DIFFERENT_DOMAINS" in types


def test_mandatory_variable_expected_for_testcd_suffix(tmp_path):
    df = pd.DataFrame([_row("G1", "SCTESTCD", mandatory_variable="N")])
    _, issue_log = _run(df, tmp_path)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["MANDATORY_VARIABLE_EXPECTED"]["severity"] == "ERROR"


def test_origin_type_orres_must_be_collected(tmp_path):
    df = pd.DataFrame([_row("G1", "SCORRES", origin_type="Derived")])
    _, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "INVALID_ORIGIN_TYPE_ORRES" for row in issue_log.rows)


def test_vlm_target_expected_for_orres_without_one(tmp_path):
    df = pd.DataFrame([_row("G1", "SCORRES")])
    _, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "VLM_TARGET_EXPECTED" for row in issue_log.rows)


def test_vlm_target_unexpected_for_unrelated_variable(tmp_path):
    df = pd.DataFrame([_row("G1", "SCCAT", vlm_target="Y")])
    _, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "VLM_TARGET_UNEXPECTED" for row in issue_log.rows)


def test_invalid_enum_values_are_errors(tmp_path):
    df = pd.DataFrame([_row("G1", "VAR1", role="NotARole", data_type="notatype", comparator="NOPE")])
    _, issue_log = _run(df, tmp_path)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["INVALID_VALUE_ROLE"]["severity"] == "ERROR"
    assert by_type["INVALID_VALUE_DATATYPE"]["severity"] == "ERROR"
    assert by_type["INVALID_VALUE_COMPARATOR"]["severity"] == "ERROR"


def test_rows_missing_vlm_group_id_are_dropped(tmp_path):
    df = pd.DataFrame([
        _row("G1", "VAR1"),
        _row(None, "SHOULD_BE_DROPPED"),
    ])
    written, _ = _run(df, tmp_path)
    assert {os.path.basename(p) for p in written} == {"sdtm_g1.yaml"}
