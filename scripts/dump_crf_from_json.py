import argparse
import csv
import json
import logging
import sys

from cosmoslib.json_roundtrip import crf_rows_from_json

"""
Reads one CRF specialization from a local JSON file, flattens it via
cosmoslib.json_roundtrip.crf_rows_from_json(), and writes the result as CSV - a thin CLI
wrapper replacing utilities/macros/read_crf_from_json.sas, used for ad hoc round-trip
comparison against curation data.

Usage:
  python scripts/dump_crf_from_json.py --json-file path/to/crf.json [--out crf.csv]

Unlike dump_bc_from_json.py/dump_sdtm_from_json.py, there is no --id/live-fetch option:
cdisc_library_client.CDISCLibraryClient has no CRF specialization endpoint yet (CRF is still
draft-only - see cosmoslib/crf_converter.py's module docstring), so --json-file is the only
input this script supports.
"""


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json-file", required=True, dest="json_file", help="Path to a local CRF specialization JSON file"
    )
    parser.add_argument("--out", default=None, dest="out_file", help="CSV output path (default: stdout)")
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    with open(args.json_file, "r", encoding="utf-8") as fh:
        crf_json = json.load(fh)

    rows = crf_rows_from_json(crf_json)
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
