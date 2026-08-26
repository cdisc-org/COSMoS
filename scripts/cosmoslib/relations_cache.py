"""
Linking-phrase / predicate-term lookup cache, replacing the get_predicateterm/
exists_predicaterm_linkingphrase/exists_predicateterm FCMP hash-lookup functions in
utilities/create_functions.sas, built from every published SDTM dataset specialization's
variable relationships (utilities/get_latest_relations_sdtm_api.sas).

Scope note: the SAS driver also builds several cross-check Excel/text reports (potential
subject/object linking-phrase inconsistencies across specializations, phrase/term usage
counts) for manual SME review. Per the port plan's decision to keep issue reporting to a
structured log rather than a full report replica, this port produces only the three cache
files the hash-lookup functions actually consume - not those audit reports.

sdtm_linkingphrases.json has no consumer anywhere in the current SAS source (grepped) - it's
produced anyway since the port plan's architecture explicitly calls for it and it costs
nothing extra (a strict subset of data already collected for the other two caches).
"""

import json
import os


def extract_relationships(specialization_json):
    """A dataset specialization's variables[] each optionally carry a single "relationship"
    dict with subject/linkingPhrase/predicateTerm/object keys (confirmed against the live
    shape already parsed by create_cosmos_sdtm_excel.py's get_sdtm_variable_data(), which
    SAS's JSON automap flattens into the `variables_relationship` table joined back to
    `variables` by `ordinal_variables`). Returns the list of those dicts for one
    specialization."""
    relationships = []
    for variable in specialization_json.get("variables", []):
        relationship = variable.get("relationship")
        if relationship:
            relationships.append(relationship)
    return relationships


def build_relation_caches(relationships):
    """Reduces every specialization's relationships to the three cache shapes:
    - linkingphrases_predterms: distinct (linkingPhrase, predicateTerm) pairs
    - predicateterms: distinct predicateTerm values
    - linkingphrases: distinct linkingPhrase values
    """
    pairs = set()
    predicate_terms = set()
    linking_phrases = set()
    for relationship in relationships:
        linking_phrase = relationship.get("linkingPhrase", "")
        predicate_term = relationship.get("predicateTerm", "")
        if linking_phrase and predicate_term:
            pairs.add((linking_phrase, predicate_term))
        if predicate_term:
            predicate_terms.add(predicate_term)
        if linking_phrase:
            linking_phrases.add(linking_phrase)

    return {
        "linkingphrases_predterms": sorted(pairs),
        "predicateterms": sorted(predicate_terms),
        "linkingphrases": sorted(linking_phrases),
    }


def save_relation_cache(path, values, fetched_at):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"values": values, "_meta": {"fetched_at": fetched_at}}, fh, indent=2, sort_keys=True)
        fh.write("\n")


def load_relation_cache(path):
    with open(path, "r", encoding="utf-8") as fh:
        payload = json.load(fh)
    return payload["values"]


class RelationsIndex:
    def __init__(self, linkingphrases_predterms, predicateterms):
        self._predterm_by_phrase = {}
        self._pairs = set()
        # SAS-QUIRK(preserved): the SAS hash is keyed on linkingPhrase alone even though
        # data.sdtm_linkingphrases_predterms can carry more than one predicateTerm per
        # linkingPhrase (it's deduplicated on the *pair*, not on linkingPhrase); declare
        # hash(dataset:) keeps the first-loaded value for a duplicate key. The dataset is
        # built sorted by (linkingPhrase, predicateTerm), so "first" means alphabetically
        # smallest predicateTerm - reproduced here by always sorting before iterating,
        # regardless of what order the cache file lists pairs in.
        for linking_phrase, predicate_term in sorted(linkingphrases_predterms):
            self._predterm_by_phrase.setdefault(linking_phrase, predicate_term)
            self._pairs.add((linking_phrase, predicate_term))
        self._predicate_terms = set(predicateterms)

    def get_predicateterm(self, linking_phrase):
        return self._predterm_by_phrase.get(linking_phrase, "")

    def exists_predicaterm_linkingphrase(self, linking_phrase, predicate_term):
        return (linking_phrase, predicate_term) in self._pairs

    def exists_predicateterm(self, predicate_term):
        return predicate_term in self._predicate_terms
