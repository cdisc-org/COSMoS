import argparse
import logging
import os

from cosmoslib.bc_converter import convert_bc_job
from cosmoslib.enums import load_enum_cache
from cosmoslib.issues import IssueLog
from cosmoslib.manifest import load_manifest
from cosmoslib.ncievs_cache import NCIEVSCache
from cosmoslib.templates import BC_ISSUE_ID_COLUMNS

"""
This script converts a release's BC curation Excel workbooks into per-concept YAML files
under yaml/<release>/bc/, replacing utilities/convert_bc_xlsx2yaml.sas. There is no separate
script for the _dht variant - point --manifest at utilities/manifests/bc/dht_test.yaml
instead.

Run from the repository root, since manifest job paths (excel_file, out_folder) are
relative to it:

  python scripts/convert_bc_xlsx2yaml.py --manifest utilities/manifests/bc/20260714_r18.yaml

Before the first run for a schema change, build the enum cache this script reads from:

  python scripts/refresh_enums.py
"""

DEFAULT_ENUM_CACHE = "utilities/data/linkml_enums.json"
DEFAULT_NCIEVS_CACHE = "utilities/data/ncievs_cache.json"


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--manifest", required=True, dest="manifest",
        help="Path to a BC release manifest, e.g. utilities/manifests/bc/20260714_r18.yaml"
    )
    parser.add_argument(
        "--enum-cache", default=DEFAULT_ENUM_CACHE, dest="enum_cache",
        help="Path to the enum permissible-value cache built by refresh_enums.py"
    )
    parser.add_argument(
        "--ncievs-cache", default=DEFAULT_NCIEVS_CACHE, dest="ncievs_cache",
        help="Path to the NCI EVS lookup cache"
    )
    parser.add_argument(
        "--no-cache", action="store_true", dest="no_cache",
        help="Disable the NCI EVS lookup cache entirely (always hit the live API, cache nothing)"
    )
    parser.add_argument(
        "--refresh-cache", action="store_true", dest="refresh_cache",
        help="Ignore cached NCI EVS lookups and re-fetch every one"
    )
    parser.add_argument(
        "--issues-out", default=None, dest="issues_out",
        help="Base path (without extension) for the .csv/.xlsx issues report; defaults to "
             "utilities/reports/convert_bc_xlsx2yaml_issues_<release>"
    )
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    if not os.path.isfile(args.enum_cache):
        logger.error(f"Enum cache {args.enum_cache} not found - run scripts/refresh_enums.py first.")
        return

    manifest = load_manifest(args.manifest)
    enum_index = load_enum_cache(args.enum_cache)
    ncievs = NCIEVSCache(args.ncievs_cache, use_cache=not args.no_cache, refresh_cache=args.refresh_cache)
    issue_log = IssueLog(BC_ISSUE_ID_COLUMNS)

    written = []
    for job in manifest.jobs:
        logger.info(f"Converting {job.excel_file} [{job.range}] -> {job.out_folder}")
        written.extend(convert_bc_job(job, enum_index, ncievs, issue_log))

    ncievs.save()

    issues_out = args.issues_out or f"utilities/reports/convert_bc_xlsx2yaml_issues_{manifest.release}"
    issue_log.write_csv(issues_out + ".csv")
    issue_log.write_xlsx(issues_out + ".xlsx")
    issue_log.print_summary()

    logger.info(f"Wrote {len(written)} YAML file(s) for release {manifest.release}")


if __name__ == "__main__":
    main()
