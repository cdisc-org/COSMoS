import csv
import glob
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv
from cdisc_library_client import CDISCLibraryClient

package = "20261027_r19"

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

R = ROOT / "yaml" / package
bc = [yaml.safe_load(open(f)) for f in glob.glob(str(R / "bc" / "*.yaml"))]
sds = [yaml.safe_load(open(f)) for f in glob.glob(str(R / "sdtm" / "*.yaml"))]
old_bc = {
    r["bc_id"]
    for r in csv.DictReader(
        open(ROOT / "export/cdisc_biomedical_concepts_latest.csv", encoding="utf-8")
    )
}
old_sds = list(
    csv.DictReader(
        open(
            ROOT / "export/cdisc_sdtm_dataset_specializations_latest.csv",
            encoding="utf-8",
        )
    )
)

print("bc_latest_package_biomedicalconcepts", len(bc))
print("sdtm_latest_package_datasetspecializations", len(sds))
print("bc_biomedicalconcepts", len(old_bc | {b["conceptId"] for b in bc}))
print(
    "sdtm_datasetspecializations",
    len(
        {r["vlm_group_id"] for r in old_sds}
        | {s["datasetSpecializationId"] for s in sds}
    ),
)
print("sdtm_domains", len({r["domain"] for r in old_sds} | {s["domain"] for s in sds}))

# Categories: the API counts differently from the CSV (455 vs 408 for R18), so start from the live list
c = CDISCLibraryClient(
    api_key=os.environ["CDISC_LIBRARY_API_KEY"],
    # The client appends /cosmos/<version> itself, so the base URL must stop at /api
    base_api_url=os.environ.get(
        "CDISC_LIBRARY_API_URL", "https://api.library.cdisc.org/api"
    ).removesuffix("/cosmos/v2"),
)

live = {x["name"] for x in c.get_bc_categories("v2")}
print("bc_categories", len(live | {cat for b in bc for cat in b.get("categories", [])}))
