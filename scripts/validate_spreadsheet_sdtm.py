import argparse
import glob
import logging

from cosmoslib.issues import IssueLog
from cosmoslib.templates import VALIDATION_ISSUE_ID_COLUMNS
from cosmoslib.validators.sdtm import run_sdtm_validation

"""
This script runs the SDTM cross-workbook validation checks (unresolved BC/DEC references,
duplicate records, retired-BC pointers, character-coding issues) against every SDTM release
manifest matched by --manifests, replacing utilities/validate_spreadsheet_sdtm.sas.
Collapses that file's ~800 lines of hand-listed %ReadExcel calls (one per historical
package) to "load these manifests" - see cosmoslib/validators/common.py's module docstring
for how the corpus is built as more manifests are added over time.

There is no separate script for the _dht variant - utilities/validate_spreadsheet_sdtm_dht.sas
differs from the main script in three real ways (confirmed by diffing them), each exposed
here as a flag:
  --high-byte-max 255      (dht scans a wider "high byte" character range)
  --no-suppress-retired    (dht drops the "and index(short_name, '[RETIRED]')=0" guard on
                             two checks)
  --distinct-parent-check  (dht's unresolved-parent-BC query adds `select DISTINCT`)

Run from the repository root, since manifest job paths are relative to it:

  python scripts/validate_spreadsheet_sdtm.py --manifests "utilities/manifests/sdtm/*.yaml"
"""

DEFAULT_MANIFESTS = "utilities/manifests/sdtm/*.yaml"
DEFAULT_BC_MANIFESTS = "utilities/manifests/bc/*.yaml"
DEFAULT_BC_LATEST_FILE = "export/cdisc_biomedical_concepts_latest.xlsx"
DEFAULT_BC_LATEST_RANGE = "Biomedical Concepts"
DEFAULT_SDTM_LATEST_FILE = "export/cdisc_sdtm_dataset_specializations_latest.xlsx"
DEFAULT_SDTM_LATEST_RANGE = "SDTM Dataset Specializations"
DEFAULT_SUBSETS_FILE = "curation/package06/BC_Package_R6_LZZT.xlsx"
DEFAULT_SUBSETS_RANGE = "Subset Codelist Example"


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifests", default=DEFAULT_MANIFESTS, dest="manifests", help="Glob of SDTM manifests")
    parser.add_argument(
        "--bc-manifests", default=DEFAULT_BC_MANIFESTS, dest="bc_manifests", help="Glob of BC manifests"
    )
    parser.add_argument("--bc-latest-file", default=DEFAULT_BC_LATEST_FILE, dest="bc_latest_file")
    parser.add_argument("--bc-latest-range", default=DEFAULT_BC_LATEST_RANGE, dest="bc_latest_range")
    parser.add_argument("--sdtm-latest-file", default=DEFAULT_SDTM_LATEST_FILE, dest="sdtm_latest_file")
    parser.add_argument("--sdtm-latest-range", default=DEFAULT_SDTM_LATEST_RANGE, dest="sdtm_latest_range")
    parser.add_argument("--subsets-file", default=DEFAULT_SUBSETS_FILE, dest="subsets_file")
    parser.add_argument("--subsets-range", default=DEFAULT_SUBSETS_RANGE, dest="subsets_range")
    parser.add_argument(
        "--distinct-parent-check", action="store_true", dest="distinct_parent_check",
        help="Dedupe the unresolved-parent-BC check like the _dht SAS variant does"
    )
    parser.add_argument(
        "--no-suppress-retired", action="store_false", dest="suppress_own_retired",
        help="Don't suppress findings on rows whose own short_name is tagged [RETIRED] (dht behavior)"
    )
    parser.add_argument(
        "--high-byte-max", type=int, default=159, dest="high_byte_max",
        help="Upper bound of the disallowed high-byte character range (dht/CRF use 255)"
    )
    parser.add_argument(
        "--issues-out", default="utilities/reports/validate_spreadsheet_sdtm_issues", dest="issues_out",
        help="Base path (without extension) for the .csv/.xlsx issues report"
    )
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    manifest_paths = sorted(glob.glob(args.manifests))
    bc_manifest_paths = sorted(glob.glob(args.bc_manifests))
    if not manifest_paths or not bc_manifest_paths:
        logger.error(f"No manifests matched --manifests={args.manifests!r} / --bc-manifests={args.bc_manifests!r}")
        return

    logger.info(f"SDTM manifests: {manifest_paths}")
    logger.info(f"BC manifests: {bc_manifest_paths}")

    findings = run_sdtm_validation(
        manifest_paths=manifest_paths,
        bc_manifest_paths=bc_manifest_paths,
        bc_latest={"file": args.bc_latest_file, "range": args.bc_latest_range},
        sdtm_latest={"file": args.sdtm_latest_file, "range": args.sdtm_latest_range},
        subsets_source={"file": args.subsets_file, "range": args.subsets_range},
        distinct_parent_check=args.distinct_parent_check,
        suppress_own_retired=args.suppress_own_retired,
        high_byte_max=args.high_byte_max,
    )

    issue_log = IssueLog(VALIDATION_ISSUE_ID_COLUMNS)
    for finding in findings:
        issue_log.add(
            finding["_excel_file_"], finding["_tab_"], finding["severity"], finding["check"],
            comment=finding["comment"], package_date=finding["package_date"], identifier=finding["identifier"],
        )

    issue_log.write_csv(args.issues_out + ".csv")
    issue_log.write_xlsx(args.issues_out + ".xlsx")
    issue_log.print_summary()


if __name__ == "__main__":
    main()
