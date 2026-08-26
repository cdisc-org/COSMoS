import argparse
import logging
import os
from datetime import datetime, timezone

from cdisc_library_client import CDISCLibraryClient

from cosmoslib.relations_cache import build_relation_caches, extract_relationships, save_relation_cache

"""
This script rebuilds the three linking-phrase/predicate-term caches under utilities/data/
that cosmoslib.relations_cache.RelationsIndex is built from, replacing
utilities/get_latest_relations_sdtm_api.sas.

This is the slowest refresh in the pipeline - it crawls every published SDTM dataset
specialization one at a time - so it is never bundled into an implicit "refresh all"
default; run it explicitly, and only when the SDTM relationship corpus actually needs
updating.

Usage: python refresh_sdtm_relations.py [-e prod|dev] [-v v2]
"""

OUT_FILES = {
    "linkingphrases_predterms": "utilities/data/sdtm_linkingphrases_predterms.json",
    "predicateterms": "utilities/data/sdtm_predicateterms.json",
    "linkingphrases": "utilities/data/sdtm_linkingphrases.json",
}


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--env", default="prod", choices=["prod", "dev"], dest="env",
        help="Which CDISC Library environment to fetch from"
    )
    parser.add_argument(
        "-v", "--api-version", default="v2", dest="api_version",
        help="COSMoS API version segment (e.g. v2)"
    )
    args = parser.parse_args()
    return args


def collect_all_relationships(client, api_version, logger):
    specialization_links = client.get_sdtm_latest_sdtm_datasetspecializations(api_version)
    total = len(specialization_links)
    logger.info(f"Crawling {total} SDTM dataset specialization(s)...")

    relationships = []
    failed_ids = []
    for i, link in enumerate(specialization_links, start=1):
        specialization_id = link.get("href", "").split("/")[-1]
        # CDISCLibraryClient.get_api_json() already retries transient HTTP errors
        # (429/502/503/504/408) per-request; this catches everything else (a single bad id,
        # a request that exhausts those retries) so one failure doesn't lose the rest of a
        # crawl that can cover 1000+ specializations - the slowest refresh in the pipeline.
        try:
            specialization_json = client.get_sdtm_latest_sdtm_datasetspecialization(api_version, specialization_id)
        except Exception as exc:
            logger.warning(f"Failed to fetch specialization {specialization_id}: {exc}")
            failed_ids.append(specialization_id)
            continue
        relationships.extend(extract_relationships(specialization_json))
        if i % 100 == 0 or i == total:
            logger.info(f"  ...{i}/{total}")

    if failed_ids:
        logger.warning(f"{len(failed_ids)} specialization(s) failed and were skipped: {failed_ids}")
    return relationships


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    suffix = "_DEV" if args.env == "dev" else ""
    api_key = os.environ.get(f"CDISC_LIBRARY_API_KEY{suffix}")
    base_api_url = os.environ.get(f"CDISC_LIBRARY_API_URL{suffix}")
    if not api_key or not base_api_url:
        logger.error(f"Please set the CDISC_LIBRARY_API_KEY{suffix} and CDISC_LIBRARY_API_URL{suffix} "
                     f"environment variables.")
        return

    client = CDISCLibraryClient(api_key=api_key, base_api_url=base_api_url)

    relationships = collect_all_relationships(client, args.api_version, logger)
    caches = build_relation_caches(relationships)

    fetched_at = datetime.now(timezone.utc).isoformat()
    for key, path in OUT_FILES.items():
        save_relation_cache(path, caches[key], fetched_at)
        logger.info(f"{key}: {len(caches[key])} value(s) -> {path}")


if __name__ == "__main__":
    main()
