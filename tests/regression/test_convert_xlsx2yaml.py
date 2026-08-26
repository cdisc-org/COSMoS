"""
Golden-file regression tests: run the Python converters against a real curation workbook
and diff the result against YAML already published under yaml/20260714_r18/. None of the
fields these converters write to YAML depend on a live NCI EVS lookup (see
cosmoslib/bc_converter.py's module docstring) - only the issues log would differ - so these
tests run against a stub ncievs client with no network access at all.
"""

import os

import pytest
import yaml

from cosmoslib.bc_converter import convert_bc_job
from cosmoslib.crf_converter import convert_crf_job
from cosmoslib.enums import build_enum_index
from cosmoslib.issues import IssueLog
from cosmoslib.manifest import load_manifest
from cosmoslib.sdtm_converter import convert_sdtm_job
from cosmoslib.templates import BC_ISSUE_ID_COLUMNS, CRF_ISSUE_ID_COLUMNS, SDTM_ISSUE_ID_COLUMNS

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFESTS_DIR = os.path.join(REPO_ROOT, "utilities", "manifests")
MODEL_DIR = os.path.join(REPO_ROOT, "model")
GOLDEN_BC_DIR = os.path.join(REPO_ROOT, "yaml", "20260714_r18", "bc")
GOLDEN_SDTM_DIR = os.path.join(REPO_ROOT, "yaml", "20260714_r18", "sdtm")
GOLDEN_CRF_DIR = os.path.join(REPO_ROOT, "yaml", "20260630_draft", "crf")

SCHEMA_PATHS = [
    os.path.join(MODEL_DIR, "cosmos_bc_model.yaml"),
    os.path.join(MODEL_DIR, "cosmos_sdtm_model.yaml"),
    os.path.join(MODEL_DIR, "cosmos_crf_model.yaml"),
]


class _StubNCIEVS:
    """No-op NCI EVS client: every lookup a converter can make returns an empty/blank
    result, so these tests exercise zero network access. Fine for golden-file diffing
    because none of these lookups feed the emitted YAML - see the bc_converter module
    docstring."""

    def get_concept_status(self, ncit_code):
        return ""

    def get_shortname(self, ncit_code):
        return ""

    def get_parent_code_shortname(self, ncit_code):
        return ["", ""]

    def get_definitions(self, ncit_code):
        return ["", ""]


class _StubCodelistIndex:
    """No-op codelist/term lookup: every lookup returns blank, so these tests exercise zero
    network access. Fine for golden-file diffing because none of these lookups feed the
    emitted YAML - see the sdtm_converter module docstring (the YAML's codelist/
    submissionValue/assignedTerm fields are all sourced straight from curation, not from a
    live CT lookup)."""

    def get_term_code(self, codelist_conceptid, coded_value):
        return ""

    def get_term_value(self, codelist_conceptid, coded_value_conceptid):
        return ""

    def get_term_preferred_term(self, codelist_conceptid, coded_value_conceptid):
        return ""

    def get_codelist_submissionvalue(self, codelist_conceptid):
        return ""

    def get_codelist_extensible(self, codelist_conceptid):
        return ""


class _StubRelationsIndex:
    """No-op linking-phrase/predicate-term lookup - see _StubCodelistIndex."""

    def get_predicateterm(self, linking_phrase):
        return ""

    def exists_predicaterm_linkingphrase(self, linking_phrase, predicate_term):
        return True

    def exists_predicateterm(self, predicate_term):
        return True


def _bc_pasi_fredriksson_job():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "bc", "20260714_r18.yaml"))
    jobs = [job for job in manifest.jobs if job.range == "BC_PASI_FREDRIKSSON"]
    assert len(jobs) == 1
    return jobs[0]


def _crf_draft_job():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "crf", "20260630_draft.yaml"))
    assert len(manifest.jobs) == 1
    return manifest.jobs[0]


def _sdtm_pasi_fredriksson_job():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "sdtm", "20260714_r18.yaml"))
    jobs = [job for job in manifest.jobs if job.range == "SDTM_PASI_FREDRIKSSON"]
    assert len(jobs) == 1
    job = jobs[0]
    job.subsets_source = dict(job.subsets_source)
    job.subsets_source["file"] = os.path.join(REPO_ROOT, job.subsets_source["file"])
    return job


@pytest.mark.golden
def test_bc_pasi_fredriksson_matches_published_yaml(tmp_path):
    job = _bc_pasi_fredriksson_job()
    job.excel_file = os.path.join(REPO_ROOT, job.excel_file)
    job.out_folder = str(tmp_path)

    enum_index = build_enum_index(SCHEMA_PATHS)
    issue_log = IssueLog(BC_ISSUE_ID_COLUMNS)

    written = convert_bc_job(job, enum_index, _StubNCIEVS(), issue_log)

    pasi_bc_ids = ["C191040", "C190947"] + [f"C1910{n}" for n in range(66, 82)]
    golden_names = {f"bc__{bc_id.lower()}.yaml" for bc_id in pasi_bc_ids}

    generated_names = {os.path.basename(path) for path in written}
    assert generated_names == golden_names
    assert golden_names <= set(os.listdir(GOLDEN_BC_DIR))

    for name in generated_names:
        with open(os.path.join(tmp_path, name), "r", encoding="utf-8") as fh:
            generated = yaml.safe_load(fh)
        with open(os.path.join(GOLDEN_BC_DIR, name), "r", encoding="utf-8") as fh:
            golden = yaml.safe_load(fh)
        assert generated == golden, name


@pytest.mark.golden
def test_sdtm_pasi_fredriksson_matches_published_yaml(tmp_path):
    job = _sdtm_pasi_fredriksson_job()
    job.excel_file = os.path.join(REPO_ROOT, job.excel_file)
    job.out_folder = str(tmp_path)

    enum_index = build_enum_index(SCHEMA_PATHS)
    issue_log = IssueLog(SDTM_ISSUE_ID_COLUMNS)

    written = convert_sdtm_job(job, enum_index, _StubCodelistIndex(), _StubRelationsIndex(), issue_log)

    pasi_vlm_group_ids = [
        f"PASI03{region}{measure}"
        for region in ("HEAD", "TRUNK", "UPPEREX", "LOWEREX")
        for measure in ("ERYTHEMA", "THICKNESS", "SCALING", "AREASCORE")
    ]
    golden_names = {f"sdtm_{vlm_group_id.lower()}.yaml" for vlm_group_id in pasi_vlm_group_ids}

    generated_names = {os.path.basename(path) for path in written}
    assert generated_names == golden_names
    assert golden_names <= set(os.listdir(GOLDEN_SDTM_DIR))

    for name in generated_names:
        with open(os.path.join(tmp_path, name), "r", encoding="utf-8") as fh:
            generated = yaml.safe_load(fh)
        with open(os.path.join(GOLDEN_SDTM_DIR, name), "r", encoding="utf-8") as fh:
            golden = yaml.safe_load(fh)
        assert generated == golden, name


@pytest.mark.golden
def test_crf_draft_matches_published_yaml(tmp_path):
    # Lower-confidence fixture (per plans/port-sas-utilities-to-python.md): this is the only
    # CRF package published anywhere in yaml/ - but it's the full 317-specialization package,
    # not a small excerpt, so it exercises the converter thoroughly.
    job = _crf_draft_job()
    job.excel_file = os.path.join(REPO_ROOT, job.excel_file)
    job.out_folder = str(tmp_path)

    issue_log = IssueLog(CRF_ISSUE_ID_COLUMNS)
    written = convert_crf_job(job, _StubCodelistIndex(), issue_log)

    generated_names = {os.path.basename(path) for path in written}
    golden_names = set(os.listdir(GOLDEN_CRF_DIR))
    assert generated_names == golden_names
    assert len(golden_names) == 317

    for name in generated_names:
        with open(os.path.join(tmp_path, name), "r", encoding="utf-8") as fh:
            generated = yaml.safe_load(fh)
        with open(os.path.join(GOLDEN_CRF_DIR, name), "r", encoding="utf-8") as fh:
            golden = yaml.safe_load(fh)
        assert generated == golden, name
