"""
Codelist/term lookup cache wrapping CDISCLibraryClient, replacing the
get_codelist_submissionvalue/get_codelist_extensible/get_term_code/get_term_value/
get_term_preferred_term FCMP hash-lookup functions in utilities/create_functions.sas, all
keyed against the flat table utilities/macros/get_latest_codelist_package.sas builds via a
PROC SQL join of a CT package's root/codelists/codelists.terms.

utilities/get_latest_codelists_api.sas fetches four CT package families - sdtmct, cdashct,
ddfct, protocolct - into four parallel cache files, but only the sdtm one is ever wired
into a hash-lookup function in the SAS source (create_functions.sas has no cdash/ddf/
protocol equivalents). This module mirrors that exactly: CodelistIndex is generic (build one
from whichever package's rows you pass it), while refresh_codelists.py still fetches and
caches all four, so the cdash/ddf/protocol data is there if a future converter needs it.

Case sensitivity: term lookups are keyed exactly as the CT API returns them. Two SDTM
converter call sites (generate_yaml_from_sdtm.sas ~line 154-170) deliberately probe both a
curated value and its uppercased form to detect *_WRONG_CASE issues - folding case in this
index would silently disable that check.
"""

import json
import os


def find_latest_package_href(products_json, package_substring):
    """`select href into :_latest_ctpackage ... where index(href, "&package") > 0 order by
    href DESC` - among every href in the /mdr/products response, the lexically-last one
    containing `package_substring` (e.g. "sdtmct"), matching a package family's dated hrefs
    (.../ct/packages/sdtmct-2026-06-26) sorting correctly by date."""
    hrefs = [
        link.get("href", "")
        for link in products_json.get("_links", {}).get("packages", [])
        if package_substring in link.get("href", "")
    ]
    if not hrefs:
        return None
    return sorted(hrefs, reverse=True)[0]


def flatten_codelist_package(package_json):
    """Flattens a raw CT package API response (root/codelists/codelists.terms) into the
    same flat rows utilities/macros/get_latest_codelist_package.sas's PROC SQL join
    produces."""
    rows = []
    version = package_json.get("version", "")
    for codelist in package_json.get("codelists", []):
        rows.extend(_flatten_codelist(codelist, version))
    return rows


def _flatten_codelist(codelist, version):
    codelist_id = codelist.get("conceptId", "")
    codelist_name = codelist.get("name", "")
    codelist_submission_value = codelist.get("submissionValue", "")
    codelist_extensible = _extensible_flag(codelist.get("extensible"))
    return [
        {
            "codelist_version": version,
            "codelist_conceptId": codelist_id,
            "codelist_name": codelist_name,
            "codelist_submissionValue": codelist_submission_value,
            "codelist_extensible": codelist_extensible,
            "codedValue": term.get("submissionValue", ""),
            "codedValue_conceptId": term.get("conceptId", ""),
            "preferredTerm": term.get("preferredTerm", ""),
        }
        for term in codelist.get("terms", [])
    ]


def _extensible_flag(raw_value):
    """`case when cl.extensible = "true" then "Yes" when cl.extensible = "false" then "No"
    else "" end` - the API has been observed to serialize this as either a JSON boolean or
    the literal strings "true"/"false"; both are handled."""
    if raw_value is True or raw_value == "true":
        return "Yes"
    if raw_value is False or raw_value == "false":
        return "No"
    return ""


def save_codelist_cache(path, rows, fetched_at):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"rows": rows, "_meta": {"fetched_at": fetched_at}}, fh, indent=2, sort_keys=True)
        fh.write("\n")


def load_codelist_cache(path):
    with open(path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    return payload["rows"]


class CodelistIndex:
    def __init__(self, rows):
        self._term_by_value = {}
        self._term_by_conceptid = {}
        self._codelist_submission_value = {}
        self._codelist_extensible = {}
        for row in rows:
            codelist_id = row["codelist_conceptId"]
            self._term_by_value[(codelist_id, row["codedValue"])] = row["codedValue_conceptId"]
            self._term_by_conceptid[(codelist_id, row["codedValue_conceptId"])] = row
            self._codelist_submission_value[codelist_id] = row["codelist_submissionValue"]
            self._codelist_extensible[codelist_id] = row["codelist_extensible"]

    def get_term_code(self, codelist_conceptid, coded_value):
        return self._term_by_value.get((codelist_conceptid, coded_value), "")

    def get_term_value(self, codelist_conceptid, coded_value_conceptid):
        row = self._term_by_conceptid.get((codelist_conceptid, coded_value_conceptid))
        return row["codedValue"] if row else ""

    def get_term_preferred_term(self, codelist_conceptid, coded_value_conceptid):
        row = self._term_by_conceptid.get((codelist_conceptid, coded_value_conceptid))
        return row["preferredTerm"] if row else ""

    def get_codelist_submissionvalue(self, codelist_conceptid):
        return self._codelist_submission_value.get(codelist_conceptid, "")

    def get_codelist_extensible(self, codelist_conceptid):
        return self._codelist_extensible.get(codelist_conceptid, "")
