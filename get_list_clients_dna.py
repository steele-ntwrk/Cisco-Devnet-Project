# Used to grab a list of clients from cisco dna

import sys
import os
import json
from tokenize import Token
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

dnac_username = 'devnetuser'
dna_password = 'Cisco123!'
base_url= 'sandboxdnac2.cisco.com'

def get_access_token(Controller_ip=base_url, username=dnac_username,password=dna_password):
    
    login_url = "https://{0}:443/dna/system/api/v1/auth/token".format(Controller_ip)
    auth_resp = requests.post(url=login_url,auth= HTTPBasicAuth(username,password), verify=False)
    auth_resp.raise_for_status()
    
    token = auth_resp.json()['Token']
    
    return token
    
def get_client_list(Controller_ip=base_url):
    client_api = 'https://{0}:443/dna/intent/api/v1/client-detail'.format(Controller_ip)
    token = get_access_token()
    headers = {'X-auth-token': token}
    
    client_list = requests.get(url=client_api, headers=headers, verify=False)

        
        
    return client_list.json()

print(get_client_list) 