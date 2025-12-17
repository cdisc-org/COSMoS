import os
import requests
from cdisc_library_client import CDISCLibraryClient
import argparse

RESPONSE_DATA = {
    "bc_latest_package_date": "2025-12-16",
    "bc_packages": 15,
    "bc_biomedicalconcepts": 1127,
    "bc_categories": 410,
    "bc_latest_package_biomedicalconcepts": 46,
    "sdtm_latest_package_date": "2025-12-16",
    "sdtm_packages": 13,
    "sdtm_datasetspecializations": 1123,
    "sdtm_domains": 31,
    "sdtm_latest_package_datasetspecializations": 826
}


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--env", required=True, default="dev", help="Environment (dev/prod)", dest="env")
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = set_cmd_line_args()

    if args.env.lower() not in ["dev", "prod"]:
        raise ValueError("Invalid input argument.")

    print(f"Running tests against the {args.env} environment")

    if args.env.lower() == "dev":
        api_key = os.environ.get("CDISC_LIBRARY_API_KEY_DEV")
        base_api_url = os.environ.get("CDISC_LIBRARY_API_URL_DEV")
        client = CDISCLibraryClient(api_key=api_key, base_api_url=base_api_url)
        client._session.verify = False
        requests.urllib3.disable_warnings()
    else:
        api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
        base_api_url = os.environ.get("CDISC_LIBRARY_API_URL")
        client = CDISCLibraryClient(api_key=api_key, base_api_url=base_api_url)

    # Get BC packages
    type = "bc_packages"
    bc_packages = client.get_bc_packages("v2")
    assert len(bc_packages) == RESPONSE_DATA[type]

    # Get BCs in latest package
    type = "bc_latest_package_biomedicalconcepts"
    bc_latest_package_date = bc_packages[-1]['href'].split("/")[-2]
    bc_latest_package_biomedicalconcepts = client.get_bc_package_biomedicalconcepts("v2", bc_latest_package_date)
    assert len(bc_latest_package_biomedicalconcepts) == RESPONSE_DATA[type]
    assert bc_latest_package_date == RESPONSE_DATA["bc_latest_package_date"]

    # Get latest BCs
    type = "bc_biomedicalconcepts"
    bc_biomedicalconcepts = client.get_bc_latest_biomedicalconcepts("v2")
    assert len(bc_biomedicalconcepts) == RESPONSE_DATA[type]

    # Get BC categories
    type = "bc_categories"
    bc_categories = client.get_bc_categories("v2")
    assert len(bc_categories) == RESPONSE_DATA[type]

    # Get latest BCs in a category
    type = "bc_biomedicalconcepts"
    bc_biomedicalconcepts = client.get_bc_latest_biomedicalconcepts_category("v2", "")
    assert len(bc_biomedicalconcepts) == RESPONSE_DATA[type]

    # Get SDTM Dataset Specialization Packages
    type = "sdtm_packages"
    sdtm_packages = client.get_sdtm_packages("v2")
    assert len(sdtm_packages) == RESPONSE_DATA[type]

    # Get SDTM Dataset Specializations in latest package
    type = "sdtm_latest_package_datasetspecializations"
    sdtm_latest_package_date = sdtm_packages[-1]['href'].split("/")[-2]
    sdtm_latest_package_datasetspecializations = client.get_sdtm_package_datasetspecializations(
        "v2", sdtm_latest_package_date
    )
    assert len(sdtm_latest_package_datasetspecializations) == RESPONSE_DATA[type]
    assert sdtm_latest_package_date == RESPONSE_DATA["sdtm_latest_package_date"]

    # Get latest SDTM Dataset Specializations
    type = "sdtm_datasetspecializations"
    sdtm_datasetspecializations = client.get_sdtm_latest_sdtm_datasetspecializations("v2")
    assert len(sdtm_datasetspecializations) == RESPONSE_DATA[type]

    # Get SDTM domains
    type = "sdtm_domains"
    sdtm_domains = client.get_sdtm_domains("v2")
    assert len(sdtm_domains) == RESPONSE_DATA[type]

    # Get latest SDTM Dataset Specializations in a domain
    type = "sdtm_datasetspecializations"
    sdtm_datasetspecializations = client.get_sdtm_latest_sdtm_datasetspecializations_domain("v2", "")
    assert len(sdtm_datasetspecializations) == RESPONSE_DATA[type]

    # Get latest SDTM Dataset Specializations that specialize a Biomedical Concept
    type = "sdtm_datasetspecializations"
    specializations = client.get_biomedicalconcept_latest_datasetspecializations("v2", "")
    sdtm_datasetspecializations = specializations['sdtm']
    assert len(sdtm_datasetspecializations) == RESPONSE_DATA[type]
