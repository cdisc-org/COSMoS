import argparse
import logging
import os

from cosmoslib.cdisc_library_cache import CodelistIndex, load_codelist_cache
from cosmoslib.enums import load_enum_cache
from cosmoslib.issues import IssueLog
from cosmoslib.manifest import load_manifest
from cosmoslib.relations_cache import RelationsIndex, load_relation_cache
from cosmoslib.sdtm_converter import convert_sdtm_job
from cosmoslib.templates import SDTM_ISSUE_ID_COLUMNS

"""
This script converts a release's SDTM curation Excel workbooks into per-specialization YAML
files under yaml/<release>/sdtm/, replacing utilities/convert_sdtm_xlsx2yaml.sas. There is
no separate script for the _dht variant - point --manifest at
utilities/manifests/sdtm/dht_test.yaml instead.

Run from the repository root, since manifest job paths (excel_file, out_folder,
subsets_source.file) are relative to it:

  python scripts/convert_sdtm_xlsx2yaml.py --manifest utilities/manifests/sdtm/20260714_r18.yaml

Before the first run, build the caches this script reads from:

  python scripts/refresh_enums.py
  python scripts/refresh_codelists.py
  python scripts/refresh_sdtm_relations.py
"""

DEFAULT_ENUM_CACHE = "utilities/data/linkml_enums.json"
DEFAULT_CODELIST_CACHE = "utilities/data/sdtm_latest_codelist_package.json"
DEFAULT_LINKINGPHRASES_PREDTERMS_CACHE = "utilities/data/sdtm_linkingphrases_predterms.json"
DEFAULT_PREDICATETERMS_CACHE = "utilities/data/sdtm_predicateterms.json"


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--manifest", required=True, dest="manifest",
        help="Path to an SDTM release manifest, e.g. utilities/manifests/sdtm/20260714_r18.yaml"
    )
    parser.add_argument(
        "--enum-cache", default=DEFAULT_ENUM_CACHE, dest="enum_cache",
        help="Path to the enum permissible-value cache built by refresh_enums.py"
    )
    parser.add_argument(
        "--codelist-cache", default=DEFAULT_CODELIST_CACHE, dest="codelist_cache",
        help="Path to the sdtm codelist/term cache built by refresh_codelists.py"
    )
    parser.add_argument(
        "--linkingphrases-predterms-cache", default=DEFAULT_LINKINGPHRASES_PREDTERMS_CACHE,
        dest="linkingphrases_predterms_cache",
        help="Path to the linking-phrase/predicate-term pair cache built by refresh_sdtm_relations.py"
    )
    parser.add_argument(
        "--predicateterms-cache", default=DEFAULT_PREDICATETERMS_CACHE, dest="predicateterms_cache",
        help="Path to the predicate-term cache built by refresh_sdtm_relations.py"
    )
    parser.add_argument(
        "--issues-out", default=None, dest="issues_out",
        help="Base path (without extension) for the .csv/.xlsx issues report; defaults to "
             "utilities/reports/convert_sdtm_xlsx2yaml_issues_<release>"
    )
    args = parser.parse_args()
    return args


def _require_cache(path, refresh_script, logger):
    if not os.path.isfile(path):
        logger.error(f"Cache {path} not found - run scripts/{refresh_script} first.")
        return False
    return True


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    caches_ok = all([
        _require_cache(args.enum_cache, "refresh_enums.py", logger),
        _require_cache(args.codelist_cache, "refresh_codelists.py", logger),
        _require_cache(args.linkingphrases_predterms_cache, "refresh_sdtm_relations.py", logger),
        _require_cache(args.predicateterms_cache, "refresh_sdtm_relations.py", logger),
    ])
    if not caches_ok:
        return

    manifest = load_manifest(args.manifest)
    enum_index = load_enum_cache(args.enum_cache)
    codelist_index = CodelistIndex(load_codelist_cache(args.codelist_cache))
    relations_index = RelationsIndex(
        load_relation_cache(args.linkingphrases_predterms_cache),
        load_relation_cache(args.predicateterms_cache),
    )
    issue_log = IssueLog(SDTM_ISSUE_ID_COLUMNS)

    written = []
    for job in manifest.jobs:
        logger.info(f"Converting {job.excel_file} [{job.range}] -> {job.out_folder}")
        written.extend(convert_sdtm_job(job, enum_index, codelist_index, relations_index, issue_log))

    issues_out = args.issues_out or f"utilities/reports/convert_sdtm_xlsx2yaml_issues_{manifest.release}"
    issue_log.write_csv(issues_out + ".csv")
    issue_log.write_xlsx(issues_out + ".xlsx")
    issue_log.print_summary()

    logger.info(f"Wrote {len(written)} YAML file(s) for release {manifest.release}")


if __name__ == "__main__":
    main()
