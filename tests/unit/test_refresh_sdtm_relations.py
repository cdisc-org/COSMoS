import logging

import responses
from cdisc_library_client import CDISCLibraryClient

from refresh_sdtm_relations import collect_all_relationships

BASE_URL = "https://library.cdisc.org/api"

LIST_JSON = {
    "_links": {
        "datasetSpecializations": [
            {"href": "/cosmos/v2/mdr/specializations/sdtm/datasetspecializations/PASI03HEADEDEMA"},
            {"href": "/cosmos/v2/mdr/specializations/sdtm/datasetspecializations/PASI03HEADERYTH"},
        ]
    }
}

SPEC_1 = {
    "datasetSpecializationId": "PASI03HEADEDEMA",
    "variables": [
        {"name": "AEDECOD", "relationship": {
            "subject": "AEDECOD", "linkingPhrase": "is decoded by the value in",
            "predicateTerm": "decodes", "object": "AETERM",
        }},
    ],
}

SPEC_2 = {
    "datasetSpecializationId": "PASI03HEADERYTH",
    "variables": [
        {"name": "X"},  # no relationship on this one
    ],
}


@responses.activate
def test_collect_all_relationships_crawls_every_specialization():
    responses.add(
        responses.GET,
        f"{BASE_URL}/cosmos/v2/mdr/specializations/sdtm/datasetspecializations",
        json=LIST_JSON, status=200,
    )
    responses.add(
        responses.GET,
        f"{BASE_URL}/cosmos/v2/mdr/specializations/sdtm/datasetspecializations/PASI03HEADEDEMA",
        json=SPEC_1, status=200,
    )
    responses.add(
        responses.GET,
        f"{BASE_URL}/cosmos/v2/mdr/specializations/sdtm/datasetspecializations/PASI03HEADERYTH",
        json=SPEC_2, status=200,
    )

    client = CDISCLibraryClient(api_key="fake-key", base_api_url=BASE_URL)
    relationships = collect_all_relationships(client, "v2", logging.getLogger(__name__))

    assert relationships == [
        {"subject": "AEDECOD", "linkingPhrase": "is decoded by the value in",
         "predicateTerm": "decodes", "object": "AETERM"}
    ]
    assert len(responses.calls) == 3


@responses.activate
def test_collect_all_relationships_skips_a_failing_specialization_and_continues():
    responses.add(
        responses.GET,
        f"{BASE_URL}/cosmos/v2/mdr/specializations/sdtm/datasetspecializations",
        json=LIST_JSON, status=200,
    )
    responses.add(
        responses.GET,
        f"{BASE_URL}/cosmos/v2/mdr/specializations/sdtm/datasetspecializations/PASI03HEADEDEMA",
        status=500,
    )
    responses.add(
        responses.GET,
        f"{BASE_URL}/cosmos/v2/mdr/specializations/sdtm/datasetspecializations/PASI03HEADERYTH",
        json=SPEC_2, status=200,
    )

    client = CDISCLibraryClient(api_key="fake-key", base_api_url=BASE_URL)
    # A failed fetch must not raise out of collect_all_relationships - the crawl continues
    # to the remaining specializations (SPEC_2, which has no relationships of its own).
    relationships = collect_all_relationships(client, "v2", logging.getLogger(__name__))
    assert relationships == []
