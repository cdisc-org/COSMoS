"""
Small string-cleaning helpers shared by the bc/sdtm/crf converters, replacing a handful of
SAS idioms (kcompress/compbl space-squeezing, countw/scan semicolon-list splitting, missing-
value coercion) that recur across generate_yaml_from_{bc,sdtm,crf}.sas.
"""

import re

_SPACE_RUN = re.compile(r" {2,}")


def squeeze_spaces(text):
    """kcompress(x, , 's') / compbl(x): collapse runs of the space character to one."""
    return _SPACE_RUN.sub(" ", text)


def clean_value(value):
    """Coerces a raw cell value (possibly None or NaN from pandas) to a stripped string,
    matching the SAS convention of treating a missing/blank cell as an empty string."""
    if value is None:
        return ""
    if isinstance(value, float) and value != value:  # NaN
        return ""
    return str(value).strip()


def words(raw_value, delimiter=";"):
    """scan(value, i, ';')/countw(value, ';') under SAS's default modifiers treat runs of
    consecutive delimiters as one and never produce/count an empty word - matched here by
    dropping empty (post-strip) tokens rather than a plain str.split()."""
    return [part.strip() for part in raw_value.split(delimiter) if part.strip()]


def format_number(value):
    """A numeric column read through pandas/openpyxl as a float (e.g. 20.0) renders as "20"
    here, matching how the source Excel cell displayed an integer length/significantDigits/
    orderNumber value - not SAS's own numeric-to-text formatting per se, just "no needless
    .0"."""
    if isinstance(value, float) and value == int(value):
        return str(int(value))
    return str(value)
