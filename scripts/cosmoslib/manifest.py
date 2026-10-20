"""
Release manifests: the single source of truth for which curation workbook + named range +
package parameters get converted for a given release/domain, shared by the convert_*.py
drivers and the validate_spreadsheet_*.py cross-workbook checkers.

Replaces the SAS pattern (utilities/convert_{bc,sdtm,crf}_xlsx2yaml.sas) of hand-editing
commented-out historical blocks in the driver script itself, and the independent, duplicated
re-listing of the same workbook/range pairs inside utilities/validate_spreadsheet_{sdtm,crf}.sas.

One manifest file per release per domain, e.g. utilities/manifests/sdtm/20260714_r18.yaml:

    release: "20260714_r18"
    domain: sdtm
    jobs:
      - excel_file: curation/package18/R18_SDTM_IS_MAST7.xlsx
        range: SDTM_IS
        type: is
        package: "20260714"
        override_package_date: "2026-07-14"
        out_folder: yaml/20260714_r18/sdtm
        subsets_source: {file: curation/package06/BC_Package_R6_LZZT.xlsx, range: "Subset Codelist Example"}
        check_relationships: true
"""

import glob
import os

import yaml


class ManifestJob:
    def __init__(self, data):
        self.excel_file = data["excel_file"]
        self.range = data["range"]
        self.type = data.get("type", "")
        self.package = data.get("package", "")
        self.override_package_date = data.get("override_package_date", "")
        self.out_folder = data["out_folder"]
        self.select = data.get("select")
        self.subsets_source = data.get("subsets_source")
        self.check_relationships = data.get("check_relationships", True)
        self.debug = data.get("debug", False)


class Manifest:
    def __init__(self, release, domain, jobs):
        self.release = release
        self.domain = domain
        self.jobs = jobs


_JOB_DEFAULT_KEYS = (
    "package",
    "override_package_date",
    "out_folder",
    "select",
    "subsets_source",
    "check_relationships",
    "debug",
)


def load_manifest(path):
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)

    defaults = {key: data[key] for key in _JOB_DEFAULT_KEYS if key in data}
    jobs = []
    for job_data in data.get("jobs", []):
        merged = dict(defaults)
        merged.update(job_data)
        jobs.append(ManifestJob(merged))

    return Manifest(data["release"], data["domain"], jobs)


def load_manifests(paths):
    return [load_manifest(path) for path in paths]


def find_manifests(manifests_root, domain):
    pattern = os.path.join(manifests_root, domain, "*.yaml")
    return sorted(glob.glob(pattern))


def resolve_path(root, relative_path):
    return os.path.join(root, relative_path)
