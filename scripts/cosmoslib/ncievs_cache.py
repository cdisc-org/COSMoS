"""
Read-through cache over NCI EVS REST lookups, replacing the embedded-Python FCMP
subroutines in utilities/create_functions.sas (get_definitions, get_shortname,
get_parent_code_shortname, get_synonyms, get_preferred_term, get_concept_status) that the
SAS macros call via a SAS-to-Python (MAS) bridge. Extends NCIEVSClient
(scripts/ncievs_client.py) rather than wrapping it, for the same reason NCIEVSClient itself
is a class: the requests.Session is naturally per-instance state.

NCit lookups are keyed by whatever codes appear in curation, not enumerable ahead of time
like a codelist package, so this cache is populated lazily during a converter/validator run
rather than by a dedicated refresh script. Entries are keyed f"{function_name}:{ncit_code}"
(not just by code) so that get_definitions/get_shortname (both `include=summary`) and
get_synonyms/get_preferred_term (both `include=synonyms`) cache independently, matching how
the SAS side issues one HTTP request per subroutine call.

SAS-QUIRK(fixed): the embedded Python for get_shortname/get_parent_code_shortname/
get_synonyms/get_concept_status wraps parsing in try/except and returns '' on any failure,
but get_definitions does not - it happens to degrade to '' anyway because it only checks
`if 'definitions' in concept_info`. NCIEVSClient.get_api_json() raises on a non-200 response
(unlike the SAS side's bare requests.get(), which never checks status_code), so a single
`_fetch()` helper here catches that for every method uniformly, restoring the "never crash
on a single bad/retired ncit code" behavior the SAS macros relied on.
"""

import json
import logging
import os
from datetime import datetime, timezone

from ncievs_client import NCIEVSClient

logger = logging.getLogger(__name__)


class NCIEVSCache(NCIEVSClient):
    def __init__(self, cache_path, use_cache=True, refresh_cache=False):
        super().__init__()
        self.cache_path = cache_path
        self.use_cache = use_cache
        self.refresh_cache = refresh_cache
        self.fetched_at = None
        self.dirty = False
        self._cache = self._load() if use_cache else {}

    def _load(self):
        if not os.path.isfile(self.cache_path):
            return {}
        with open(self.cache_path, "r", encoding="utf-8") as fh:
            payload = json.load(fh)
        meta = payload.pop("_meta", {})
        self.fetched_at = meta.get("fetched_at")
        return payload

    def save(self):
        if not self.use_cache or not self.dirty:
            return
        payload = dict(self._cache)
        payload["_meta"] = {"fetched_at": datetime.now(timezone.utc).isoformat()}
        os.makedirs(os.path.dirname(self.cache_path), exist_ok=True)
        with open(self.cache_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, sort_keys=True)
            fh.write("\n")

    def _fetch(self, href, default=None):
        try:
            return self.get_api_json(href)
        except Exception as exc:
            logger.warning(f"NCI EVS lookup failed for {href}: {exc}")
            return {} if default is None else default

    def _get_concept(self, ncit_code, include):
        return self._fetch(f"/concept/ncit/{ncit_code}?include={include}")

    def _cached(self, function_name, ncit_code, fetch):
        key = f"{function_name}:{ncit_code}"
        if self.use_cache and not self.refresh_cache and key in self._cache:
            return self._cache[key]
        result = fetch()
        if self.use_cache:
            self._cache[key] = result
            self.dirty = True
        return result

    def get_definitions(self, ncit_code):
        """Returns [definition_nci, definition_cdisc], replacing get_definitions()."""

        def fetch():
            definitions = self._get_concept(ncit_code, "summary").get("definitions", [])
            definition_cdisc = next((d["definition"] for d in definitions if d["source"] == "CDISC"), "")
            definition_nci = (
                next((d["definition"] for d in definitions if d["source"] == "NCI"), "")
                or definition_cdisc
                or next((d["definition"] for d in definitions if d["source"] == "NCI-GLOSS"), "")
                or next((d["definition"] for d in definitions if d["source"] == "CDISC-GLOSS"), "")
            )
            return [definition_nci, definition_cdisc]

        return self._cached("get_definitions", ncit_code, fetch)

    def get_shortname(self, ncit_code):
        """Returns the concept's preferred name, replacing get_shortname()."""

        def fetch():
            return self._get_concept(ncit_code, "summary").get("name", "")

        return self._cached("get_shortname", ncit_code, fetch)

    def get_parent_code_shortname(self, ncit_code):
        """Returns [parent_code, parent_shortname], ';'-joined across all parents,
        replacing get_parent_code_shortname()."""

        def fetch():
            parents = self._fetch(f"/concept/ncit/{ncit_code}/parents", default=[])
            return [";".join(v["code"] for v in parents), ";".join(v["name"] for v in parents)]

        return self._cached("get_parent_code_shortname", ncit_code, fetch)

    def get_synonyms(self, ncit_code):
        """Returns a ';'-joined, order-preserving deduplicated synonym list, replacing
        get_synonyms()."""

        def fetch():
            names = [v["name"] for v in self._get_concept(ncit_code, "synonyms").get("synonyms", [])]
            return ";".join(dict.fromkeys(names))

        return self._cached("get_synonyms", ncit_code, fetch)

    def get_preferred_term(self, ncit_code):
        """Returns the synonym entry of type 'Preferred_Name', replacing
        get_preferred_term()."""

        def fetch():
            for synonym in self._get_concept(ncit_code, "synonyms").get("synonyms", []):
                if synonym.get("type") == "Preferred_Name":
                    return synonym["name"]
            return ""

        return self._cached("get_preferred_term", ncit_code, fetch)

    def get_concept_status(self, ncit_code):
        """Returns the concept's status (e.g. "Retired_Concept"), replacing
        get_concept_status()."""

        def fetch():
            return self._get_concept(ncit_code, "minimal").get("conceptStatus", "")

        return self._cached("get_concept_status", ncit_code, fetch)
