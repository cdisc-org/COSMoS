"""
Output filename/path helpers for the release-folder and per-record filename conventions
used throughout utilities/convert_*_xlsx2yaml.sas and utilities/macros/generate_yaml_from_*.sas.

Release folders follow yaml/<release>/{bc,sdtm,crf}, where <release> is YYYYMMDD_rNN for a
numbered release, or a special-case name like <YYYYMMDD>_draft/dht_test/latest/latest_test.
"""

import os

# The generate_yaml_from_{bc,sdtm,crf}.sas macros all write an "href:" line built from this
# same &ncit_explore macro variable (utilities/config.sas) concatenated directly onto the
# ncit code, with no separator and no quoting.
NCIT_EXPLORE_BASE_URL = "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/"


def ncit_href(ncit_code):
    return f"{NCIT_EXPLORE_BASE_URL}{ncit_code}"


def bc_yaml_filename(bc_type, bc_id):
    return f"bc_{bc_type}_{bc_id.lower()}.yaml"


def sdtm_yaml_filename(vlm_group_id):
    return f"sdtm_{vlm_group_id.lower()}.yaml"


def crf_yaml_filename(domain, crf_group_id):
    return f"crf_{domain.lower()}_{crf_group_id.lower()}.yaml"


def output_path(out_folder, filename):
    return os.path.join(out_folder, filename)
