import os
from unittest.mock import patch

import pandas as pd
import yaml

from cosmoslib.bc_converter import convert_bc_job
from cosmoslib.issues import IssueLog
from cosmoslib.templates import BC_ISSUE_ID_COLUMNS

ENUM_INDEX = {
    "BiomedicalConceptResultScale": ["Ordinal", "Nominal"],
    "DataElementConceptDataType": ["string", "integer"],
}


class _FakeJob:
    def __init__(self, out_folder, type="", override_package_date="2026-07-14", select=None):
        self.excel_file = "irrelevant.xlsx"
        self.range = "BC_TEST"
        self.type = type
        self.select = select
        self.out_folder = out_folder
        self.override_package_date = override_package_date


class _FakeNCIEVS:
    def __init__(self, statuses=None, shortnames=None, parents=None, definitions=None):
        self.statuses = statuses or {}
        self.shortnames = shortnames or {}
        self.parents = parents or {}
        self.definitions = definitions or {}

    def get_concept_status(self, code):
        return self.statuses.get(code, "")

    def get_shortname(self, code):
        return self.shortnames.get(code, "")

    def get_parent_code_shortname(self, code):
        return self.parents.get(code, ["", ""])

    def get_definitions(self, code):
        return self.definitions.get(code, ["", ""])


def _run(df, tmp_path, ncievs=None, job=None, enum_index=ENUM_INDEX):
    job = job or _FakeJob(str(tmp_path))
    issue_log = IssueLog(BC_ISSUE_ID_COLUMNS)
    with patch("cosmoslib.bc_converter.read_named_range", return_value=df):
        written = convert_bc_job(job, enum_index, ncievs or _FakeNCIEVS(), issue_log)
    return written, issue_log


def _row(bc_id, **kwargs):
    row = {"bc_id": bc_id, "_excel_file_": "wb.xlsx", "_tab_": "BC_TEST"}
    row.update(kwargs)
    return row


def test_header_only_prints_when_first_or_second_row_has_a_dec_id(tmp_path):
    # SAS-QUIRK(preserved): neither of the group's first two rows carries a dec_id, so the
    # "dataElementConcepts:" header never prints, even though row 3 has one.
    df = pd.DataFrame([
        _row("C1", short_name="Alpha", definition="Def"),
        _row("C1"),
        _row("C1", dec_id="D1", dec_label="Label", data_type="string"),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "dataElementConcepts:" not in text
    assert "  - conceptId: D1" in text


def test_header_prints_on_first_row_when_it_carries_a_dec_id(tmp_path):
    df = pd.DataFrame([
        _row("C1", short_name="Alpha", definition="Def", dec_id="D1", dec_label="Label", data_type="string"),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "dataElementConcepts:" in text
    assert text.index("dataElementConcepts:") < text.index("- conceptId: D1")


def test_invalid_enum_values_flagged_as_error(tmp_path):
    df = pd.DataFrame([
        _row(
            "C1", short_name="Alpha", definition="Def", result_scales="Bogus",
            dec_id="D1", dec_label="Label", data_type="wrong_type",
        ),
    ])
    _, issue_log = _run(df, tmp_path)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["INVALID_VALUE_RESULTSCALE"]["severity"] == "ERROR"
    assert by_type["INVALID_VALUE_RESULTSCALE"]["actual_value"] == "Bogus"
    assert by_type["INVALID_VALUE_DATATYPE"]["severity"] == "ERROR"
    assert by_type["INVALID_VALUE_DATATYPE"]["actual_value"] == "wrong_type"


def test_coding_block_aligns_code_system_systemname_by_position(tmp_path):
    # code has fewer ';'-entries than system/system_name - a SAS-QUIRK(preserved) case
    # where the second coding entry has no "- code:" of its own (see bc_converter.py).
    df = pd.DataFrame([
        _row(
            "C1", short_name="Alpha", definition="Def",
            system="SNOMED;LOINC", system_name="Snomed CT;LOINC Code", code="1234",
        ),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "  - code: 1234\n    system: SNOMED\n    systemName: Snomed CT\n" in text
    assert "    system: LOINC\n    systemName: LOINC Code\n" in text


def test_missing_code_with_system_present_flags_system_code_missing(tmp_path):
    df = pd.DataFrame([
        _row("C1", short_name="Alpha", definition="Def", system="SNOMED"),
    ])
    _, issue_log = _run(df, tmp_path)
    assert any(row["issue_type"] == "BC_SYSTEM_CODE_MISSING" for row in issue_log.rows)


def test_retired_concept_status_flagged_but_shortname_mismatch_suppressed_when_tagged_retired(tmp_path):
    df = pd.DataFrame([
        _row("C1", ncit_code="C1", short_name="Old Name [RETIRED]", definition="Def"),
    ])
    ncievs = _FakeNCIEVS(statuses={"C1": "Retired_Concept"}, shortnames={"C1": "New Name"})
    _, issue_log = _run(df, tmp_path, ncievs=ncievs)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["BC_ID_CONCEPTSTATUS"]["actual_value"] == "Retired_Concept"
    assert "BC_SHORTNAME_MISMATCH_OR_MISSING" not in by_type


def test_shortname_mismatch_flagged_when_not_tagged_retired(tmp_path):
    df = pd.DataFrame([
        _row("C1", ncit_code="C1", short_name="Old Name", definition="Def"),
    ])
    ncievs = _FakeNCIEVS(shortnames={"C1": "New Name"})
    _, issue_log = _run(df, tmp_path, ncievs=ncievs)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["BC_SHORTNAME_MISMATCH_OR_MISSING"]["severity"] == "WARNING"
    assert by_type["BC_SHORTNAME_MISMATCH_OR_MISSING"]["expected_value"] == "New Name"


def test_parent_id_mismatch_severity_depends_on_whether_nci_returned_any_parent(tmp_path):
    df = pd.DataFrame([
        _row("C1", parent_bc_id="C999", short_name="Alpha", definition="Def"),
    ])
    ncievs = _FakeNCIEVS(parents={"C1": ["C2;C3", "Parent Two;Parent Three"]})
    _, issue_log = _run(df, tmp_path, ncievs=ncievs)
    mismatches = [row for row in issue_log.rows if row["issue_type"] == "PARENT_ID_MISMATCH"]
    assert len(mismatches) == 1
    assert mismatches[0]["severity"] == "WARNING"
    assert mismatches[0]["expected_value"] == "C2;C3"


def test_parent_id_mismatch_is_a_note_when_nci_has_no_parent_at_all(tmp_path):
    df = pd.DataFrame([
        _row("C1", parent_bc_id="C999", short_name="Alpha", definition="Def"),
    ])
    _, issue_log = _run(df, tmp_path, ncievs=_FakeNCIEVS())
    mismatches = [row for row in issue_log.rows if row["issue_type"] == "PARENT_ID_MISMATCH"]
    assert len(mismatches) == 1
    assert mismatches[0]["severity"] == "NOTE"


def test_dec_level_issues_use_dec_specific_types_and_ncievs_lookups(tmp_path):
    df = pd.DataFrame([
        _row(
            "C1", short_name="Alpha", definition="Def",
            dec_id="D1", ncit_dec_code="D1", dec_label="Old Label", data_type="string",
        ),
    ])
    ncievs = _FakeNCIEVS(statuses={"D1": "Retired_Concept"}, shortnames={"D1": "New Label"})
    _, issue_log = _run(df, tmp_path, ncievs=ncievs)
    by_type = {row["issue_type"]: row for row in issue_log.rows}
    assert by_type["DEC_ID_CONCEPTSTATUS"]["actual_value"] == "Retired_Concept"
    assert by_type["DEC_SHORTNAME_MISMATCH_OR_MISSING"]["expected_value"] == "New Label"


def test_dec_shortname_is_never_quoted_even_with_a_dash(tmp_path):
    df = pd.DataFrame([
        _row("C1", short_name="Alpha", definition="Def", dec_id="D1", dec_label="Not-Done Reason"),
    ])
    written, _ = _run(df, tmp_path)
    text = open(written[0], encoding="utf-8").read()
    assert "    shortName: Not-Done Reason\n" in text


def test_synonyms_quote_on_curly_braces_unlike_categories(tmp_path):
    df = pd.DataFrame([
        _row("C1", short_name="Alpha", definition="Def", synonyms="Plain;Has{Brace}"),
    ])
    written, _ = _run(df, tmp_path)
    with open(written[0], encoding="utf-8") as fh:
        loaded = yaml.safe_load(fh)
    assert loaded["synonyms"] == ["Plain", "Has{Brace}"]
    text = open(written[0], encoding="utf-8").read()
    assert '- "Has{Brace}"' in text
    assert "- Plain\n" in text


def test_bc_type_dashes_become_underscores_in_filename(tmp_path):
    df = pd.DataFrame([_row("C1", short_name="Alpha", definition="Def")])
    job = _FakeJob(str(tmp_path), type="ham-a")
    written, _ = _run(df, tmp_path, job=job)
    assert os.path.basename(written[0]) == "bc_ham_a_c1.yaml"


def test_rows_missing_bc_id_are_dropped_and_group_order_is_stable(tmp_path):
    df = pd.DataFrame([
        _row("C2", short_name="Two", definition="Def2"),
        _row(None, short_name="Skip me"),
        _row("C1", short_name="One", definition="Def1"),
    ])
    written, _ = _run(df, tmp_path)
    assert {os.path.basename(p) for p in written} == {"bc__c1.yaml", "bc__c2.yaml"}
