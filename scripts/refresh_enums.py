import argparse
import logging
from datetime import datetime, timezone

from cosmoslib.enums import build_enum_index, save_enum_cache

"""
This script rebuilds utilities/data/linkml_enums.json, the enum permissible-value cache
consumed by the BC/SDTM converters' INVALID_VALUE_* checks (exists_enum_term()).
Replaces utilities/get_latest_enums_linkml.sas.

Usage: python refresh_enums.py [-s SCHEMA [SCHEMA ...]] [-o OUT_FILE]

Unlike utilities/get_latest_enums_linkml.sas (which parsed the generated JSON Schema
files), this reads the canonical model/cosmos_{bc,sdtm,crf}_model.yaml LinkML schemas
directly via SchemaView, so it has no dependency on a prior Windows-only
gen-jsonschema regeneration step.
"""

DEFAULT_SCHEMAS = [
    "model/cosmos_bc_model.yaml",
    "model/cosmos_sdtm_model.yaml",
    "model/cosmos_crf_model.yaml",
]

DEFAULT_OUT_FILE = "utilities/data/linkml_enums.json"


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--schema", nargs="+", default=DEFAULT_SCHEMAS, dest="schemas",
        help="LinkML schema file(s) to read enums from"
    )
    parser.add_argument(
        "-o", "--out-file", default=DEFAULT_OUT_FILE, dest="out_file",
        help="Path to write the enum cache JSON to"
    )
    args = parser.parse_args()
    return args


def main():
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)

    args = set_cmd_line_args()

    logger.info(f"Reading enums from {len(args.schemas)} schema(s): {', '.join(args.schemas)}")
    enum_index = build_enum_index(args.schemas)

    fetched_at = datetime.now(timezone.utc).isoformat()
    save_enum_cache(args.out_file, enum_index, fetched_at)

    logger.info(f"Wrote {len(enum_index)} enum(s) to {args.out_file}")
    for enum_name in sorted(enum_index):
        logger.info(f"  {enum_name}: {len(enum_index[enum_name])} value(s)")


if __name__ == "__main__":
    main()
