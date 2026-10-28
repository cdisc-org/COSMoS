import os

from cosmoslib.manifest import load_manifest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MANIFESTS_DIR = os.path.join(REPO_ROOT, "utilities", "manifests")


def test_bc_r18_manifest_matches_transcribed_sas_block():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "bc", "20260714_r18.yaml"))
    assert manifest.release == "20260714_r18"
    assert manifest.domain == "bc"
    assert len(manifest.jobs) == 6

    job = manifest.jobs[0]
    assert job.excel_file == "curation/package18/R18_BC_DSS_BrCa_TAUG.xlsx"
    assert job.range == "BC_BrCa"
    assert job.type == ""
    assert job.package == "20260714"
    assert job.override_package_date == "2026-07-14"
    assert job.out_folder == "yaml/20260714_r18/bc"

    sc_job = manifest.jobs[-1]
    assert sc_job.type == "sc"
    assert sc_job.range == "BC_SC"


def test_sdtm_r18_manifest_carries_subsets_source_and_check_relationships():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "sdtm", "20260714_r18.yaml"))
    assert len(manifest.jobs) == 6
    for job in manifest.jobs:
        assert job.check_relationships is True
        assert job.subsets_source == {
            "file": "curation/package06/BC_Package_R6_LZZT.xlsx",
            "range": "Subset Codelist Example",
        }
    assert manifest.jobs[0].range == "SDTM_IS"
    assert manifest.jobs[0].type == "is"


def test_crf_draft_manifest_fixes_folder_typo():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "crf", "20260630_draft.yaml"))
    assert len(manifest.jobs) == 1
    job = manifest.jobs[0]
    # SAS source targets yaml/20260630_draft2/crf (an approved-fix typo); the manifest
    # records the corrected, standard yaml/<folder>/crf path instead.
    assert job.out_folder == "yaml/20260630_draft/crf"


def test_job_level_override_wins_over_manifest_default():
    manifest = load_manifest(os.path.join(MANIFESTS_DIR, "bc", "dht_test.yaml"))
    assert len(manifest.jobs) == 4
    types = [job.type for job in manifest.jobs]
    assert types == ["di", "sleep", "mk", "hr"]
    for job in manifest.jobs:
        assert job.out_folder == "yaml/dht_test/bc"
