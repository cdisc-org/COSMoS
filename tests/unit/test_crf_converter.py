import os
from unittest.mock import patch

import pandas as pd
import yaml

from cosmoslib.crf_converter import convert_crf_job
from cosmoslib.issues import IssueLog
from cosmoslib.templates import CRF_ISSUE_ID_COLUMNS


class _FakeJob:
    def __init__(self, out_folder, select=None):
        self.excel_file = "irrelevant.xlsx"
        self.range = "CRF_TEST"
        self.select = select
        self.out_folder = out_folder
        self.override_package_date = "2026-06-30"


class _FakeCodelistIndex:
    def __init__(self, term_codes=None, term_values=None, submission_values=None, extensible=None):
        self.term_codes = term_codes or {}
        self.term_values = term_values or {}
        self.submission_values = submission_values or {}
        self.extensible = extensible or {}

    def get_term_code(self, codelist_conceptid, coded_value):
        return self.term_codes.get((codelist_conceptid, coded_value), "")

    def get_term_value(self, codelist_conceptid, coded_value_conceptid):
        return self.term_values.get((codelist_conceptid, coded_value_conceptid), "")

    def get_term_preferred_term(self, codelist_conceptid, coded_value_conceptid):
        return ""

    def get_codelist_submissionvalue(self, codelist_conceptid):
        return self.submission_values.get(codelist_conceptid, "")

    def get_codelist_extensible(self, codelist_conceptid):
        return self.extensible.get(codelist_conceptid, "")


def _run(df, tmp_path, codelist_index=None, job=None):
    job = job or _FakeJob(str(tmp_path))
    issue_log = IssueLog(CRF_ISSUE_ID_COLUMNS)
    with patch("cosmoslib.crf_converter.read_named_range", return_value=df):
        written = convert_crf_job(job, codelist_index or _FakeCodelistIndex(), issue_log)
    return written, issue_log


def _row(crf_group_id, crf_item=None, **kwargs):
    row = {
        "crf_group_id": crf_group_id, "_excel_file_": "wb.xlsx", "_tab_": "CRF_TEST", "domain": "AE",
        "order_number": None,
    }
    if crf_item is not None:
        row["crf_item"] = crf_item
    row.update(kwargs)
    return row


def test_items_header_prints_only_when_first_row_has_an_item(tmp_path):
    df = pd.DataFrame([
        _row("G1", short_name="Alpha"),
        _row("G1", "ITEM1", variable_name="VAR1", order_number=1),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "items:" not in text
    assert "- name: ITEM1" in text


def test_sorted_by_order_number_with_missing_sorting_first(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM_B", variable_name="B", order_number=2.0),
        _row("G1", "ITEM_NONE", variable_name="N"),
        _row("G1", "ITEM_A", variable_name="A", order_number=1.0),
    ])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)
    names = [item["name"] for item in loaded["items"]]
    assert names == ["ITEM_NONE", "ITEM_A", "ITEM_B"]


def test_domain_always_emitted_even_when_blank(tmp_path):
    df = pd.DataFrame([_row("G1", "ITEM1", variable_name="VAR1", domain=None)])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)
    assert loaded["domain"] is None


def test_missing_short_name_is_an_error(tmp_path):
    df = pd.DataFrame([_row("G1", "ITEM1", variable_name="VAR1")])
    _, issue_log = _run(df, tmp_path)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["MISSING_SHORT_NAME"]["severity"] == "ERROR"


def test_question_text_is_always_quoted_and_escapes_newlines(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", question_text="Line1\nLine2"),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert 'questionText: "Line1\\rLine2"' in text


def test_question_text_and_prompt_both_present_is_flagged_with_fixed_typo(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", question_text="Q?", prompt="P"),
    ])
    _, issue_log = _run(df, tmp_path)
    types = {row["issue_type"] for row in issue_log.rows}
    assert "QUESTION_TEXT_PROMPT_BOTH_NOT_MISSING" in types
    assert not any("NOT MISSING" in t for t in types)  # the SAS typo string never appears


def test_completion_instructions_spelling_is_fixed(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", completion_instructions="Do X"),
    ])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["items"][0]
    assert loaded["completionInstructions"] == "Do X"
    assert "completionIinstructions" not in loaded


def test_mandatory_variable_expected_for_term_suffix(tmp_path):
    df = pd.DataFrame([_row("G1", "AETERM", variable_name="AETERM", short_name="Alpha", mandatory_variable="N")])
    _, issue_log = _run(df, tmp_path)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["MANDATORY_VARIABLE_EXPECTED"]["severity"] == "ERROR"


def test_mandatory_variable_not_expected_for_testcd_suffix(tmp_path):
    # CRF's suffix set (TEST|TERM|TRT) is narrower than SDTM's - TESTCD isn't included.
    df = pd.DataFrame([_row("G1", "AETESTCD", variable_name="AETESTCD", short_name="Alpha", mandatory_variable="N")])
    _, issue_log = _run(df, tmp_path)
    assert not any(row["issue_type"] == "MANDATORY_VARIABLE_EXPECTED" for row in issue_log.rows)


def test_codelist_block_omitted_when_submission_value_missing_even_with_codelist_present(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", codelist="C1"),
    ])
    _, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "CODELIST_SUBMISSION_VALUE_MISSING" for row in issue_log.rows)


def test_codelist_href_is_emitted_even_when_codelist_is_blank(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", codelist_submission_value="NY"),
    ])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["items"][0]
    assert loaded["codelist"]["submissionValue"] == "NY"
    assert "conceptId" not in loaded["codelist"]
    assert loaded["codelist"]["href"] == "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/"


def test_value_list_term_counts_mismatch_and_missing_cdisc_term(tmp_path):
    df = pd.DataFrame([
        _row(
            "G1", "ITEM1", variable_name="VAR1", short_name="Alpha", codelist="C1",
            codelist_submission_value="NY", value_display_list="No;Yes;Extra", value_list="N;Y",
        ),
    ])
    codelist_index = _FakeCodelistIndex(extensible={"C1": "No"})
    written, issue_log = _run(df, tmp_path, codelist_index=codelist_index)
    types = {row["issue_type"] for row in issue_log.rows}
    assert "CODELIST_VALUE_LISTS_TERM_COUNTS" in types
    assert "CODELIST_VALUE_LIST_TERM_CDISC_MISSING" in types
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["items"][0]
    assert loaded["valueList"] == [
        {"displayValue": "No", "value": "N"},
        {"displayValue": "Yes", "value": "Y"},
        {"displayValue": "Extra"},
    ]


def test_selection_type_missing_flagged_when_value_display_list_present(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", value_display_list="No;Yes",
             value_list="N;Y"),
    ])
    _, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "VALUE_LIST_MISSING_SELECTION_TYPE" for row in issue_log.rows)


def test_prepopulated_value_block_and_mismatch_issue(tmp_path):
    df = pd.DataFrame([
        _row(
            "G1", "ITEM1", variable_name="VAR1", short_name="Alpha", codelist="C1",
            prepopulated_term="ANTI-CANCER THERAPY", prepopulated_code="C100",
        ),
    ])
    codelist_index = _FakeCodelistIndex(term_values={("C1", "C100"): "DIFFERENT TERM"})
    written, issue_log = _run(df, tmp_path, codelist_index=codelist_index)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["items"][0]
    assert loaded["prepopulatedValue"] == {"value": "ANTI-CANCER THERAPY", "conceptId": "C100"}
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["CODELIST_TERM_CCODE_MISMATCH"]["expected_value"] == "DIFFERENT TERM"


def test_sdtm_target_variables_use_double_space_after_dash(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", sdtm_target_variable="AETERM;AEDECOD"),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert '        -  "AETERM"\n' in text
    assert '        -  "AEDECOD"\n' in text


def test_sdtm_annotation_collapses_blanks_and_is_always_quoted(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha", sdtm_annotation="AETERM   AEDECOD"),
    ])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)["items"][0]
    assert loaded["sdtmTarget"]["sdtmAnnotation"] == "AETERM AEDECOD"


def test_rows_missing_crf_group_id_are_dropped(tmp_path):
    df = pd.DataFrame([
        _row("G1", "ITEM1", variable_name="VAR1", short_name="Alpha"),
        _row(None, "SHOULD_BE_DROPPED", variable_name="X"),
    ])
    written, _ = _run(df, tmp_path)
    assert {os.path.basename(p) for p in written} == {"crf_ae_g1.yaml"}
