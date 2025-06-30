import requests
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 502, 503, 504, 408],
    allowed_methods=["GET", "POST"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

class NCIEVSClient:

    def __init__(self):
        self.base_api_url = "https://api-evsrest.nci.nih.gov/api/v1"

    def get_api_json(self, href):
        headers = {
            'Accept': 'application/json',
            "User-Agent": "cdisc-cosmos"
        }
        raw_data = http.get(self.base_api_url+href, headers=headers)
        if raw_data.status_code == 200:
            return json.loads(raw_data.text)
        else:
            raise Exception(f"Request to {self.base_api_url+href} returned unsuccessful {raw_data.status_code} response")

    def get_raw_response(self, href):
        headers = {
            'Accept': 'application/json',
            'api-key': self.api_key,
            "User-Agent": "pipeline"
        }
        return http.get(self.base_api_url+href, headers=headers)
