import argparse
import logging
import os

from cosmoslib.bc_converter import convert_bc_job
from cosmoslib.cdisc_library_cache import CodelistIndex, load_codelist_cache
from cosmoslib.enums import load_enum_cache
from cosmoslib.issues import IssueLog
from cosmoslib.manifest import ManifestJob
from cosmoslib.ncievs_cache import NCIEVSCache
from cosmoslib.relations_cache import RelationsIndex, load_relation_cache
from cosmoslib.sdtm_converter import convert_sdtm_job
from cosmoslib.templates import BC_ISSUE_ID_COLUMNS, SDTM_ISSUE_ID_COLUMNS

"""
Regenerates YAML for every already-published BC/SDTM record from the "latest" export
(export/cdisc_{biomedical_concepts,sdtm_dataset_specializations}_latest.xlsx), replacing
utilities/convert_latest_xlsx2yaml.sas's run_latest_bc/run_latest_sdtm macros.

Usage:
  python scripts/convert_latest_xlsx2yaml.py --domain bc --release 20260714_r18
  python scripts/convert_latest_xlsx2yaml.py --domain sdtm --release 20260714_r18

Without --release, regenerates the full "latest" export corpus into yaml/latest/<domain>/ -
useful for a from-scratch rebuild of that folder (e.g. after a schema or converter change).

With --release, writes to yaml/latest_test/<domain>/ instead - a dry-run area - and excludes
every id already produced under yaml/<release>/<domain>/, found by reading each already-
published YAML file's conceptId (bc) / datasetSpecializationId (sdtm) field. This is
simpler, and one less redundant Excel read, than the SAS source's approach of re-reading a
curation/draft/cdisc_..._<release>_draft.xlsx workbook just to compute the same exclusion
set (see plans/port-sas-utilities-to-python.md's script-to-script mapping).

The "latest" BC job uses type="latest" (matching the SAS source exactly), so output
filenames are bc_latest_<id>.yaml - distinct from a normal release's bc_<type>_<id>.yaml,
avoiding any collision with files already in yaml/<release>/bc/.
"""

DEFAULT_BC_LATEST_FILE = "export/cdisc_biomedical_concepts_latest.xlsx"
DEFAULT_BC_LATEST_RANGE = "Biomedical Concepts"
DEFAULT_SDTM_LATEST_FILE = "export/cdisc_sdtm_dataset_specializations_latest.xlsx"
DEFAULT_SDTM_LATEST_RANGE = "SDTM Dataset Specializations"

# utilities/convert_latest_xlsx2yaml.sas's run_latest_sdtm macro unions subset-codelist
# sheets from two historical packages - see sdtm_converter.convert_sdtm_job's docstring note
# on job.subsets_source accepting a list.
DEFAULT_SUBSETS_SOURCES = [
    {"file": "curation/package06/BC_Package_R6_LZZT.xlsx", "range": "Subset Codelist Example"},
    {"file": "curation/package16/R16_BC_DS_Edits.xlsx", "range": "Subset Codelist"},
]

DEFAULT_ENUM_CACHE = "utilities/data/linkml_enums.json"
DEFAULT_NCIEVS_CACHE = "utilities/data/ncievs_cache.json"
DEFAULT_CODELIST_CACHE = "utilities/data/sdtm_latest_codelist_package.json"
DEFAULT_LINKINGPHRASES_PREDTERMS_CACHE = "utilities/data/sdtm_linkingphrases_predterms.json"
DEFAULT_PREDICATETERMS_CACHE = "utilities/data/sdtm_predicateterms.json"

ID_FIELD_BY_DOMAIN = {"bc": "conceptId", "sdtm": "datasetSpecializationId"}


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", required=True, choices=["bc", "sdtm"], dest="domain")
    parser.add_argument(
        "--release", default=None, dest="release",
        help="Exclude ids already produced under yaml/<release>/<domain>/ and write to "
             "yaml/latest_test/<domain>/ instead of yaml/latest/<domain>/"
    )
    parser.add_argument("--enum-cache", default=DEFAULT_ENUM_CACHE, dest="enum_cache")
    parser.add_argument("--ncievs-cache", default=DEFAULT_NCIEVS_CACHE, dest="ncievs_cache")
    parser.add_argument("--no-cache", action="store_true", dest="no_cache")
    parser.add_argument("--refresh-cache", action="store_true", dest="refresh_cache")
    parser.add_argument("--codelist-cache", default=DEFAULT_CODELIST_CACHE, dest="codelist_cache")
    parser.add_argument(
        "--linkingphrases-predterms-cache", default=DEFAULT_LINKINGPHRASES_PREDTERMS_CACHE,
        dest="linkingphrases_predterms_cache"
    )
    parser.add_argument("--predicateterms-cache", default=DEFAULT_PREDICATETERMS_CACHE, dest="predicateterms_cache")
    parser.add_argument("--issues-out", default=None, dest="issues_out")
    args = parser.parse_args()
    return args


def already_produced_ids(release_folder, id_field):
    """Reads the top-level `<id_field>:` line out of every YAML file already published
    under release_folder. Cheaper and simpler than the SAS source's approach of re-reading
    a curation draft workbook to compute the same exclusion set."""
    ids = []
    if not os.path.isdir(release_folder):
        return ids
    prefix = f"{id_field}:"
    for name in sorted(os.listdir(release_folder)):
        if not name.endswith(".yaml"):
            continue
        with open(os.path.join(release_folder, name), "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith(prefix):
                    ids.append(line[len(prefix):].strip())
                    break
    return ids


def _require_cache(path, refresh_script, logger):
    if not os.path.isfile(path):
        logger.error(f"Cache {path} not found - run scripts/{refresh_script} first.")
        return False
    return True


def run_bc(args, logger):
    if not _require_cache(args.enum_cache, "refresh_enums.py", logger):
        return

    excluded_ids = []
    out_folder = "yaml/latest/bc"
    if args.release:
        excluded_ids = already_produced_ids(f"yaml/{args.release}/bc", ID_FIELD_BY_DOMAIN["bc"])
        out_folder = "yaml/latest_test/bc"
    logger.info(f"Excluding {len(excluded_ids)} already-produced bc_id(s); writing to {out_folder}")

    job = ManifestJob({
        "excel_file": DEFAULT_BC_LATEST_FILE,
        "range": DEFAULT_BC_LATEST_RANGE,
        "type": "latest",
        "out_folder": out_folder,
        "select": f"bc_id not in {excluded_ids!r}" if excluded_ids else None,
    })

    enum_index = load_enum_cache(args.enum_cache)
    ncievs = NCIEVSCache(args.ncievs_cache, use_cache=not args.no_cache, refresh_cache=args.refresh_cache)
    issue_log = IssueLog(BC_ISSUE_ID_COLUMNS)

    written = convert_bc_job(job, enum_index, ncievs, issue_log)
    ncievs.save()

    issues_out = args.issues_out or f"utilities/reports/convert_bc_xlsx2yaml_issues_latest_{args.release or 'all'}"
    issue_log.write_csv(issues_out + ".csv")
    issue_log.write_xlsx(issues_out + ".xlsx")
    issue_log.print_summary()
    logger.info(f"Wrote {len(written)} YAML file(s) to {out_folder}")


def run_sdtm(args, logger):
    caches_ok = all([
        _require_cache(args.enum_cache, "refresh_enums.py", logger),
        _require_cache(args.codelist_cache, "refresh_codelists.py", logger),
        _require_cache(args.linkingphrases_predterms_cache, "refresh_sdtm_relations.py", logger),
        _require_cache(args.predicateterms_cache, "refresh_sdtm_relations.py", logger),
    ])
    if not caches_ok:
        return

    excluded_ids = []
    out_folder = "yaml/latest/sdtm"
    if args.release:
        excluded_ids = already_produced_ids(f"yaml/{args.release}/sdtm", ID_FIELD_BY_DOMAIN["sdtm"])
        out_folder = "yaml/latest_test/sdtm"
    logger.info(f"Excluding {len(excluded_ids)} already-produced vlm_group_id(s); writing to {out_folder}")

    job = ManifestJob({
        "excel_file": DEFAULT_SDTM_LATEST_FILE,
        "range": DEFAULT_SDTM_LATEST_RANGE,
        "out_folder": out_folder,
        "select": f"vlm_group_id not in {excluded_ids!r}" if excluded_ids else None,
        "subsets_source": DEFAULT_SUBSETS_SOURCES,
        "check_relationships": True,
    })

    enum_index = load_enum_cache(args.enum_cache)
    codelist_index = CodelistIndex(load_codelist_cache(args.codelist_cache))
    relations_index = RelationsIndex(
        load_relation_cache(args.linkingphrases_predterms_cache),
        load_relation_cache(args.predicateterms_cache),
    )
    issue_log = IssueLog(SDTM_ISSUE_ID_COLUMNS)

    written = convert_sdtm_job(job, enum_index, codelist_index, relations_index, issue_log)

    issues_out = (
        args.issues_out or f"utilities/reports/convert_sdtm_xlsx2yaml_issues_latest_{args.release or 'all'}"
    )
    issue_log.write_csv(issues_out + ".csv")
    issue_log.write_xlsx(issues_out + ".xlsx")
    issue_log.print_summary()
    logger.info(f"Wrote {len(written)} YAML file(s) to {out_folder}")


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    if args.domain == "bc":
        run_bc(args, logger)
    else:
        run_sdtm(args, logger)


if __name__ == "__main__":
    main()
