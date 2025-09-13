import os
import argparse
from cdisc_library_client import CDISCLibraryClient
import requests
from ncievs_client import NCIEVSClient
from dotenv import load_dotenv
import logging
from rich.progress import track

# Load environment variables
load_dotenv()


def get_bc_list(client, cosmos_api_version):
    cosmos_api_version = "v2"
    all_bc_list = client.get_bc_latest_biomedicalconcepts(cosmos_api_version)
    return all_bc_list


def get_bcs(client, cosmos_api_version, all_bc_list):
    print(f"\nGetting {len(all_bc_list)} Biomedical Concepts from the CDISC Library")
    bc_list = []
    for bc in track(all_bc_list, description="Getting Biomedical Concepts ..."):
        href = bc['href']
        biomedicalConceptId = href.split("/")[-1]
        biomedicalConcept = client.get_bc_latest_biomedicalconcept(cosmos_api_version, biomedicalConceptId)
        bc_list.append(biomedicalConcept)
    return bc_list


def get_ncit_concept_status(client, concept_id):
    concept = client.get_api_json("/concept/ncit/" + concept_id + "?include=minimal")
    status = concept.get("conceptStatus", "")
    name = concept.get("name", "")
    return name, status


def process_biomedical_concepts(evs_client, bc_list):
    logger = logging.getLogger(__name__)
    print(f"\nChecking concept status of {len(bc_list)} Biomedical Concepts from the CDISC Library at NCIt")
    for bc in track(bc_list, description="Checking Biomedical Concepts ..."):
        bc_id = bc.get("conceptId", "")
        if bc_id[:3] != "NEW":
            name, status = get_ncit_concept_status(evs_client, bc_id)
            if status == "Retired_Concept":
                logger.warning(f"\nBiomedical Concept ID: {bc_id} - Status: {status} - name: {name}")
            # Process the biomedical concept as needed
            dec_list = bc.get("dataElementConcepts", [])
            for dec in dec_list:
                dec_id = dec.get("conceptId", "")
                # print (f"Processing Data Element Concept ID: {dec_id}")
                if dec_id[:3] != "NEW":
                    name, status = get_ncit_concept_status(evs_client, dec_id)
                    if status == "Retired_Concept":
                        logger.warning(f"\nData Element Concept ID: {dec_id} - Status: {status} - name: {name}")

    return


def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


def main():

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    # args = set_cmd_line_args()

    api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
    base_api_url = os.environ.get("CDISC_LIBRARY_API_URL")
    cosmos_api_version = "v2"

    client = CDISCLibraryClient(api_key=api_key, base_api_url=base_api_url)
    client._session.verify = False
    requests.urllib3.disable_warnings()

    evs_client = NCIEVSClient()

    all_bc_list = get_bc_list(client, cosmos_api_version)
    bc_list = get_bcs(client, cosmos_api_version, all_bc_list)

    process_biomedical_concepts(evs_client, bc_list)


if __name__ == "__main__":
    main()
