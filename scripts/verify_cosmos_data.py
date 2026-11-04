import os
import requests
from dotenv import load_dotenv
from cdisc_library_client import CDISCLibraryClient
import argparse

load_dotenv()

PROD_DATA = {
    "bc_latest_package_date": "2026-11-02",
    "bc_packages": 19,
    "bc_biomedicalconcepts": 1588,
    "bc_categories": 455,
    "bc_latest_package_biomedicalconcepts": 140,
    "sdtm_latest_package_date": "2026-11-02",
    "sdtm_packages": 17,
    "sdtm_datasetspecializations": 1641,
    "sdtm_domains": 41,
    "sdtm_latest_package_datasetspecializations": 230,
}


# Expected values in the dev environment. Dev only holds a subset of the published
# packages, so package-history-based counts differ from prod.
DEV_DATA = {
    "bc_latest_package_date": "2026-11-02",
    "bc_packages": 4,
    "bc_biomedicalconcepts": 166,
    "bc_categories": 83,
    "bc_latest_package_biomedicalconcepts": 140,
    "sdtm_latest_package_date": "2026-11-02",
    "sdtm_packages": 4,
    "sdtm_datasetspecializations": 242,
    "sdtm_domains": 25,
    "sdtm_latest_package_datasetspecializations": 230,
}

RESPONSE_DATA = {"prod": PROD_DATA, "dev": DEV_DATA}

failures = []


def check(name, actual, expected):
    """Compare actual to expected, print the result, and record any mismatch."""
    if actual == expected:
        print(f"OK    {name}: {actual}")
    else:
        print(f"FAIL  {name}: expected {expected!r}, got {actual!r}")
        failures.append(name)


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        "--env",
        required=True,
        default="dev",
        help="Environment (dev/prod)",
        dest="env",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = set_cmd_line_args()

    if args.env.lower() not in ["dev", "prod"]:
        raise ValueError("Invalid input argument.")

    print(f"Running tests against the {args.env} environment")
    expected = RESPONSE_DATA[args.env.lower()]

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
    check(type, len(bc_packages), expected.get(type))

    # Get BCs in latest package
    type = "bc_latest_package_biomedicalconcepts"
    bc_latest_package_date = bc_packages[-1]["href"].split("/")[-2]
    bc_latest_package_biomedicalconcepts = client.get_bc_package_biomedicalconcepts(
        "v2", bc_latest_package_date
    )
    check(type, len(bc_latest_package_biomedicalconcepts), expected.get(type))
    check("bc_latest_package_date", bc_latest_package_date, expected.get("bc_latest_package_date"))

    # Get latest BCs
    type = "bc_biomedicalconcepts"
    bc_biomedicalconcepts = client.get_bc_latest_biomedicalconcepts("v2")
    check(type, len(bc_biomedicalconcepts), expected.get(type))

    # Get BC categories
    type = "bc_categories"
    bc_categories = client.get_bc_categories("v2")
    check(type, len(bc_categories), expected.get(type))

    # Get latest BCs in a category
    type = "bc_biomedicalconcepts"
    bc_biomedicalconcepts = client.get_bc_latest_biomedicalconcepts_category("v2", "")
    check(type, len(bc_biomedicalconcepts), expected.get(type))

    # Get SDTM Dataset Specialization Packages
    type = "sdtm_packages"
    sdtm_packages = client.get_sdtm_packages("v2")
    check(type, len(sdtm_packages), expected.get(type))

    # Get SDTM Dataset Specializations in latest package
    type = "sdtm_latest_package_datasetspecializations"
    sdtm_latest_package_date = sdtm_packages[-1]["href"].split("/")[-2]
    sdtm_latest_package_datasetspecializations = (
        client.get_sdtm_package_datasetspecializations("v2", sdtm_latest_package_date)
    )
    check(type, len(sdtm_latest_package_datasetspecializations), expected.get(type))
    check("sdtm_latest_package_date", sdtm_latest_package_date, expected.get("sdtm_latest_package_date"))

    # Get latest SDTM Dataset Specializations
    type = "sdtm_datasetspecializations"
    sdtm_datasetspecializations = client.get_sdtm_latest_sdtm_datasetspecializations(
        "v2"
    )
    check(type, len(sdtm_datasetspecializations), expected.get(type))

    # Get SDTM domains
    type = "sdtm_domains"
    sdtm_domains = client.get_sdtm_domains("v2")
    check(type, len(sdtm_domains), expected.get(type))

    # Get latest SDTM Dataset Specializations in a domain
    type = "sdtm_datasetspecializations"
    sdtm_datasetspecializations = (
        client.get_sdtm_latest_sdtm_datasetspecializations_domain("v2", "")
    )
    check(type, len(sdtm_datasetspecializations), expected.get(type))

    # Get latest SDTM Dataset Specializations that specialize a Biomedical Concept
    type = "sdtm_datasetspecializations"
    specializations = client.get_biomedicalconcept_latest_datasetspecializations(
        "v2", ""
    )
    sdtm_datasetspecializations = specializations["sdtm"]
    check(type, len(sdtm_datasetspecializations), expected.get(type))

    print()
    if failures:
        print(f"{len(failures)} check(s) failed: {', '.join(failures)}")
        raise SystemExit(1)
    print("All checks passed")
