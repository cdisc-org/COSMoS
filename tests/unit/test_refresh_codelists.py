import json
import logging
from unittest.mock import patch

import responses
from cdisc_library_client import CDISCLibraryClient

from cosmoslib.cdisc_library_cache import load_codelist_cache
from refresh_codelists import main, refresh_one_package

BASE_URL = "https://library.cdisc.org/api"

PRODUCTS_JSON = {
    "_links": {
        "packages": [
            {"href": "/mdr/ct/packages/sdtmct-2025-03-28"},
            {"href": "/mdr/ct/packages/sdtmct-2026-06-26"},
        ]
    }
}

PACKAGE_JSON = {
    "version": "2026-06-26",
    "codelists": [
        {
            "conceptId": "C66742",
            "name": "No Yes Response",
            "submissionValue": "NY",
            "extensible": "false",
            "terms": [
                {"conceptId": "C49488", "submissionValue": "N", "preferredTerm": "No"},
            ],
        },
    ],
}


@responses.activate
def test_refresh_one_package_fetches_latest_and_writes_cache(tmp_path):
    responses.add(responses.GET, f"{BASE_URL}/mdr/products", json=PRODUCTS_JSON, status=200)
    responses.add(
        responses.GET, f"{BASE_URL}/mdr/ct/packages/sdtmct-2026-06-26", json=PACKAGE_JSON, status=200
    )

    client = CDISCLibraryClient(api_key="fake-key", base_api_url=BASE_URL)
    out_file = str(tmp_path / "sdtm_latest_codelist_package.json")

    row_count = refresh_one_package(client, "sdtmct", out_file, logging.getLogger(__name__))

    assert row_count == 1
    rows = load_codelist_cache(out_file)
    assert rows == [
        {
            "codelist_version": "2026-06-26",
            "codelist_conceptId": "C66742",
            "codelist_name": "No Yes Response",
            "codelist_submissionValue": "NY",
            "codelist_extensible": "No",
            "codedValue": "N",
            "codedValue_conceptId": "C49488",
            "preferredTerm": "No",
        }
    ]
    # requested the 2026 package, not the older 2025 one
    assert responses.calls[1].request.url == f"{BASE_URL}/mdr/ct/packages/sdtmct-2026-06-26"


@responses.activate
def test_refresh_one_package_skips_when_no_package_found(tmp_path):
    responses.add(responses.GET, f"{BASE_URL}/mdr/products", json={"_links": {"packages": []}}, status=200)

    client = CDISCLibraryClient(api_key="fake-key", base_api_url=BASE_URL)
    out_file = str(tmp_path / "ddf_latest_codelist_package.json")

    row_count = refresh_one_package(client, "ddfct", out_file, logging.getLogger(__name__))

    assert row_count == 0
    import os
    assert not os.path.exists(out_file)


def test_package_families_cover_all_four_ct_types():
    from refresh_codelists import PACKAGE_FAMILIES

    assert set(PACKAGE_FAMILIES) == {"sdtmct", "cdashct", "ddfct", "protocolct"}
    assert json.dumps(PACKAGE_FAMILIES)  # plain str values, JSON-serializable


def test_main_continues_past_one_failing_package_family():
    # One family raising must not stop the other three from being attempted.
    calls = []

    def fake_refresh(client, package_substring, out_file, logger):
        calls.append(package_substring)
        if package_substring == "cdashct":
            raise Exception("503 Service Unavailable")
        return 1

    with patch.dict("os.environ", {"CDISC_LIBRARY_API_KEY": "k", "CDISC_LIBRARY_API_URL": "u"}), \
         patch("refresh_codelists.refresh_one_package", side_effect=fake_refresh), \
         patch("refresh_codelists.set_cmd_line_args") as mock_args, \
         patch("refresh_codelists.CDISCLibraryClient"):
        mock_args.return_value.env = "prod"
        main()

    assert calls == ["sdtmct", "cdashct", "ddfct", "protocolct"]
