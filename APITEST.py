import dotenv
import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import os
import base64
from urllib.parse import quote

urllib3.disable_warnings(InsecureRequestWarning)

dotenv.load_dotenv()


GUARDIANS_USER = os.environ.get("GUARDIANS_DEV_API_USER")
GUARDIANS_KEY = os.environ.get("GUARDIANS_DEV_API_KEY")
GUARDIANS_URL = os.environ.get("GUARDIANS_DEV_URL_BASE")
LOCAL_API_URL = os.environ.get("API_URL_BASE")

# G_CREDENTIALS = f"{GUARDIANS_USER}:{GUARDIANS_KEY}"
# G_API_AUTH = os.environ.get("G_AUTH")
# API_AUTH = os.environ.get("API_AUTH")

API_USER = os.getenv("GUARDIANS_DEV_API_USER")
API_KEY = os.getenv("GUARDIANS_DEV_API_KEY")
AUTH = f"{API_USER}:{API_KEY}"
AUTH_ENCODED = base64.b64encode(AUTH.encode()).decode()
API_AUTH = f"Basic {AUTH_ENCODED}"
API_URL = os.getenv("GUARDIANS_DEV_URL_BASE")

headers = {
    "Authorization": API_AUTH,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

eppn = "http://cilogon.org/serverJ/users/1898@microsoft.cilogon.aaf.edu.au"
joel_eppn = "joel.seaman@aaf.edu.au"
sub = ('http://cilogon.org/serverJ/users/1898')
encoded_sub = quote(sub, safe='')


encoded_identifier = quote(joel_eppn, safe='')

print(encoded_identifier)


# person_url = f"{LOCAL_API_URL}/co_people.json?coid=3&search.identifier={encoded_identifier}"
tc_url = f"{GUARDIANS_URL}/co_t_and_c_agreements.json?coid=6"



# person_read = requests.get(person_url, headers=headers, verify=False)
# json_data = json.loads(person_read.text)
# CO_PERSON_ID = json_data['CoPeople'][0]['Id']
#
# print("GET status code", person_read.status_code)
# print("GET response text", person_read.text)
# print(CO_PERSON_ID)


terms_and_conditions = requests.get(f"{API_URL}/co_t_and_c_agreements.json?coid=6", headers=headers)
print(terms_and_conditions.text)
print(terms_and_conditions.status_code)


new_agreement = {
    "RequestType": "CoTAndCAgreements",
    "Version": "1.0",
    "CoTAndCAgreements": [
        {
            "Version": "1.0",
            "CoTermsAndConditionsId": 4,
            "Person": {"Type": "CO", "Id": 362}
        }
    ]
}


#url_read = f'https://registry-dev.biocommons.org.au/{eppn}'



# get_TC_metadata = requests.get(tc_url, headers=headers, verify=False)
# print("GET response text", get_TC_metadata.text)
#
# put_TC_update = requests.post(tc_url, headers=headers, verify=False, json=new_agreement)
# print("Put status code:", put_TC_update.status_code)
# print("Put response text:", put_TC_update.text)
#
# terms_and_conditions = requests.get(f"{API_URL}/co_t_and_c_agreements.json?coid=6", headers=headers)
# print(terms_and_conditions.text)
# print(terms_and_conditions.status_code)



#
# get_TC_metadata = requests.get(tc_url, headers=headers, verify=False)
# print("GET response text", get_TC_metadata.text)
#
# print("Put status code:", put_TC_update.status_code)
# print("Put response text:", put_TC_update.text)
