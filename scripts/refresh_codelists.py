import argparse
import logging
import os
from datetime import datetime, timezone

from cdisc_library_client import CDISCLibraryClient

from cosmoslib.cdisc_library_cache import find_latest_package_href, flatten_codelist_package, save_codelist_cache

"""
This script rebuilds the four CT codelist package caches under utilities/data/ that
cosmoslib.cdisc_library_cache.CodelistIndex is built from (only the sdtm one is currently
wired into a converter/validator lookup - see that module's docstring), replacing
utilities/get_latest_codelists_api.sas.

Usage: python refresh_codelists.py [-e prod|dev]

Reads CDISC_LIBRARY_API_KEY/CDISC_LIBRARY_API_URL (or the _DEV pair with -e dev) from the
environment.
"""

PACKAGE_FAMILIES = {
    "sdtmct": "utilities/data/sdtm_latest_codelist_package.json",
    "cdashct": "utilities/data/cdash_latest_codelist_package.json",
    "ddfct": "utilities/data/ddf_latest_codelist_package.json",
    "protocolct": "utilities/data/protocol_latest_codelist_package.json",
}


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e", "--env", default="prod", choices=["prod", "dev"], dest="env",
        help="Which CDISC Library environment to fetch from"
    )
    args = parser.parse_args()
    return args


def refresh_one_package(client, package_substring, out_file, logger):
    products = client.get_products()
    href = find_latest_package_href(products, package_substring)
    if href is None:
        logger.warning(f"No package found for '{package_substring}' - skipping {out_file}")
        return 0

    package_json = client.get_api_json(href)
    rows = flatten_codelist_package(package_json)
    save_codelist_cache(out_file, rows, datetime.now(timezone.utc).isoformat())
    logger.info(f"{package_substring}: {href} -> {len(rows)} term row(s) -> {out_file}")
    return len(rows)


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

    failed = []
    for package_substring, out_file in PACKAGE_FAMILIES.items():
        # One family's failure (transient network error, unexpected API response) shouldn't
        # stop the other three from refreshing - each writes an independent cache file.
        try:
            refresh_one_package(client, package_substring, out_file, logger)
        except Exception as exc:
            logger.warning(f"Failed to refresh '{package_substring}': {exc}")
            failed.append(package_substring)

    if failed:
        logger.warning(f"{len(failed)} package family(ies) failed and were skipped: {failed}")


if __name__ == "__main__":
    main()
