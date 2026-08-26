import argparse
import csv
import json
import logging
import os
import sys

from cdisc_library_client import CDISCLibraryClient

from cosmoslib.json_roundtrip import sdtm_rows_from_json

"""
Fetches one SDTM dataset specialization (by datasetSpecializationId, from the live CDISC
Library API) or reads one from a local JSON file, flattens it via
cosmoslib.json_roundtrip.sdtm_rows_from_json(), and writes the result as CSV - a thin CLI
wrapper replacing utilities/macros/read_sdtm_from_json.sas, used for ad hoc round-trip
comparison against curation data.

Usage:
  python scripts/dump_sdtm_from_json.py --id PASI03HEADSCALING [--out sdtm.csv]
  python scripts/dump_sdtm_from_json.py --json-file path/to/sdtm.json [--out sdtm.csv]

Reads CDISC_LIBRARY_API_KEY/CDISC_LIBRARY_API_URL from the environment when --id is given.
"""


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--id", dest="dataset_specialization_id", help="datasetSpecializationId to fetch")
    group.add_argument("--json-file", dest="json_file", help="Path to a local SDTM specialization JSON file")
    parser.add_argument("-v", "--api-version", default="v2", dest="api_version", help="COSMoS API version segment")
    parser.add_argument("--out", default=None, dest="out_file", help="CSV output path (default: stdout)")
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    if args.json_file:
        with open(args.json_file, "r", encoding="utf-8") as fh:
            sdtm_json = json.load(fh)
    else:
        api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
        base_api_url = os.environ.get("CDISC_LIBRARY_API_URL")
        if not api_key or not base_api_url:
            logger.error("Please set the CDISC_LIBRARY_API_KEY and CDISC_LIBRARY_API_URL environment variables.")
            return
        client = CDISCLibraryClient(api_key=api_key, base_api_url=base_api_url)
        sdtm_json = client.get_sdtm_latest_sdtm_datasetspecialization(
            args.api_version, args.dataset_specialization_id
        )

    rows = sdtm_rows_from_json(sdtm_json)
    if not rows:
        logger.warning("No rows produced.")
        return

    out = open(args.out_file, "w", newline="", encoding="utf-8") if args.out_file else sys.stdout
    try:
        writer = csv.DictWriter(out, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    finally:
        if args.out_file:
            out.close()

    if args.out_file:
        logger.info(f"Wrote {len(rows)} row(s) to {args.out_file}")


if __name__ == "__main__":
    main()
