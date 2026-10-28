import argparse
import logging
import os

from cosmoslib.cdisc_library_cache import CodelistIndex, load_codelist_cache
from cosmoslib.crf_converter import convert_crf_job
from cosmoslib.issues import IssueLog
from cosmoslib.manifest import load_manifest
from cosmoslib.templates import CRF_ISSUE_ID_COLUMNS

"""
This script converts a release's CRF curation Excel workbook(s) into per-specialization
YAML files under yaml/<release>/crf/, replacing utilities/convert_crf_xlsx2yaml.sas. There
is no _dht variant for CRF.

Run from the repository root, since manifest job paths (excel_file, out_folder) are
relative to it:

  python scripts/convert_crf_xlsx2yaml.py --manifest utilities/manifests/crf/20260630_draft.yaml

Before the first run, build the cache this script reads from:

  python scripts/refresh_codelists.py
"""

DEFAULT_CODELIST_CACHE = "utilities/data/sdtm_latest_codelist_package.json"


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--manifest", required=True, dest="manifest",
        help="Path to a CRF release manifest, e.g. utilities/manifests/crf/20260630_draft.yaml"
    )
    parser.add_argument(
        "--codelist-cache", default=DEFAULT_CODELIST_CACHE, dest="codelist_cache",
        help="Path to the sdtm codelist/term cache built by refresh_codelists.py"
    )
    parser.add_argument(
        "--issues-out", default=None, dest="issues_out",
        help="Base path (without extension) for the .csv/.xlsx issues report; defaults to "
             "utilities/reports/convert_crf_xlsx2yaml_issues_<release>"
    )
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    if not os.path.isfile(args.codelist_cache):
        logger.error(f"Cache {args.codelist_cache} not found - run scripts/refresh_codelists.py first.")
        return

    manifest = load_manifest(args.manifest)
    codelist_index = CodelistIndex(load_codelist_cache(args.codelist_cache))
    issue_log = IssueLog(CRF_ISSUE_ID_COLUMNS)

    written = []
    for job in manifest.jobs:
        logger.info(f"Converting {job.excel_file} [{job.range}] -> {job.out_folder}")
        written.extend(convert_crf_job(job, codelist_index, issue_log))

    issues_out = args.issues_out or f"utilities/reports/convert_crf_xlsx2yaml_issues_{manifest.release}"
    issue_log.write_csv(issues_out + ".csv")
    issue_log.write_xlsx(issues_out + ".xlsx")
    issue_log.print_summary()

    logger.info(f"Wrote {len(written)} YAML file(s) for release {manifest.release}")


if __name__ == "__main__":
    main()
