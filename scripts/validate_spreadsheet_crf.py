import argparse
import glob
import logging

from cosmoslib.issues import IssueLog
from cosmoslib.templates import VALIDATION_ISSUE_ID_COLUMNS
from cosmoslib.validators.crf import run_crf_validation

"""
This script runs the CRF cross-workbook validation checks (unresolved BC/DEC/SDTM
references, duplicate records, retired-BC pointers, character-coding issues) against every
CRF release manifest matched by --manifests, replacing utilities/validate_spreadsheet_crf.sas.
Built on cosmoslib.validators.common/.sdtm, since today's SAS source for this script is a
near-duplicate copy-paste of validate_spreadsheet_sdtm.sas plus CRF checks (see
cosmoslib/validators/crf.py's module docstring for the two confirmed asymmetries between the
two validators that this port preserves rather than "fixes").

Run from the repository root, since manifest job paths are relative to it:

  python scripts/validate_spreadsheet_crf.py --manifests "utilities/manifests/crf/*.yaml"

The CRF validator always uses the wider (128-255) character-coding range, matching the SAS
source's `collate(128, 255)` in the CRF corpus step (bc/sdtm/dht default to 128-159).
"""

DEFAULT_MANIFESTS = "utilities/manifests/crf/*.yaml"
DEFAULT_BC_MANIFESTS = "utilities/manifests/bc/*.yaml"
DEFAULT_SDTM_MANIFESTS = "utilities/manifests/sdtm/*.yaml"
DEFAULT_BC_LATEST_FILE = "export/cdisc_biomedical_concepts_latest.xlsx"
DEFAULT_BC_LATEST_RANGE = "Biomedical Concepts"
DEFAULT_SDTM_LATEST_FILE = "export/cdisc_sdtm_dataset_specializations_latest.xlsx"
DEFAULT_SDTM_LATEST_RANGE = "SDTM Dataset Specializations"


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifests", default=DEFAULT_MANIFESTS, dest="manifests", help="Glob of CRF manifests")
    parser.add_argument(
        "--bc-manifests", default=DEFAULT_BC_MANIFESTS, dest="bc_manifests", help="Glob of BC manifests"
    )
    parser.add_argument(
        "--sdtm-manifests", default=DEFAULT_SDTM_MANIFESTS, dest="sdtm_manifests", help="Glob of SDTM manifests"
    )
    parser.add_argument("--bc-latest-file", default=DEFAULT_BC_LATEST_FILE, dest="bc_latest_file")
    parser.add_argument("--bc-latest-range", default=DEFAULT_BC_LATEST_RANGE, dest="bc_latest_range")
    parser.add_argument("--sdtm-latest-file", default=DEFAULT_SDTM_LATEST_FILE, dest="sdtm_latest_file")
    parser.add_argument("--sdtm-latest-range", default=DEFAULT_SDTM_LATEST_RANGE, dest="sdtm_latest_range")
    parser.add_argument(
        "--distinct-parent-check", action="store_true", dest="distinct_parent_check",
        help="Dedupe the unresolved-parent-BC check like the _dht SAS variant does"
    )
    parser.add_argument(
        "--high-byte-max", type=int, default=255, dest="high_byte_max",
        help="Upper bound of the disallowed high-byte character range"
    )
    parser.add_argument(
        "--issues-out", default="utilities/reports/validate_spreadsheet_crf_issues", dest="issues_out",
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
    sdtm_manifest_paths = sorted(glob.glob(args.sdtm_manifests))
    if not manifest_paths or not bc_manifest_paths or not sdtm_manifest_paths:
        logger.error(
            f"No manifests matched --manifests={args.manifests!r} / --bc-manifests={args.bc_manifests!r} / "
            f"--sdtm-manifests={args.sdtm_manifests!r}"
        )
        return

    logger.info(f"CRF manifests: {manifest_paths}")
    logger.info(f"BC manifests: {bc_manifest_paths}")
    logger.info(f"SDTM manifests: {sdtm_manifest_paths}")

    findings = run_crf_validation(
        manifest_paths=manifest_paths,
        bc_manifest_paths=bc_manifest_paths,
        sdtm_manifest_paths=sdtm_manifest_paths,
        bc_latest={"file": args.bc_latest_file, "range": args.bc_latest_range},
        sdtm_latest={"file": args.sdtm_latest_file, "range": args.sdtm_latest_range},
        distinct_parent_check=args.distinct_parent_check,
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
