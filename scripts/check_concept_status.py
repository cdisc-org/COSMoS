import os
import argparse
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment, Font, Border, Side
from cdisc_library_client import CDISCLibraryClient
import pandas as pd
import requests
from ncievs_client import NCIEVSClient

def get_bc_list(client, cosmos_api_version):
    cosmos_api_version = "v2"
    all_bc_list = client.get_bc_latest_biomedicalconcepts(cosmos_api_version)
    return all_bc_list

def get_bcs(client, cosmos_api_version, all_bc_list, count=1000):
    print(f"\nGetting {len(all_bc_list)} Biomedical Concepts from the CDISC Library")
    bc_list = []
    for bc in all_bc_list:
        href = bc['href']
        biomedicalConceptId = href.split("/")[-1]
        biomedicalConcept = client.get_bc_latest_biomedicalconcept(cosmos_api_version, biomedicalConceptId)
        bc_list.append(biomedicalConcept)
        if len(bc_list) == count:
            break
    return bc_list

def get_ncit_concept_status(client, concept_id):
    concept = client.get_api_json("/concept/ncit/"+concept_id+"?include=minimal")
    status = concept.get("conceptStatus", "")
    name = concept.get("name", "")
    return name, status

def process_biomedical_concepts(evs_client, bc_list):
  for bc in bc_list:
    bc_id = bc.get("conceptId", "")
    if bc_id[:3] != "NEW":
        name, status = get_ncit_concept_status(evs_client, bc_id)
        if status == "Retired_Concept":
            print(f"Processing Biomedical Concept ID: {bc_id} - Status: {status} - name: {name}")
        # Process the biomedical concept as needed
        dec = bc.get("dataElementConcepts", [])
        for d in dec:
            dec_id = d.get("conceptId", "")
            # print (f"Processing Data Element Concept ID: {dec_id}")
            if dec_id[:3] != "NEW":
                    name, status = get_ncit_concept_status(evs_client, dec_id)
                    if status == "Retired_Concept":
                        print(f"Processing DEC ID: {dec_id} - Status: {status} - name: {name}")
  return

def set_cmd_line_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args

def main():

    args = set_cmd_line_args()

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
