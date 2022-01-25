import requests 
import json

baseurl = 'https://sandboxapicdc.cisco.com/api/'
username = 'admin'
password = '!v3G@!4@Y'
requests.packages.urllib3.disable_warnings()

def get_auth(aci_url=baseurl, un=username, pw=password):
    auth_url = '{0}aaaLogin.json'.format(aci_url)
    body = {
        "aaaUser":{
            "attributes": {
                'name': un,
                'pwd': pw
            }
        }
    }
    
    body_json = json.dumps(body)
    
    auth_resp = requests.post(url=auth_url, data=body_json, verify=False)
    auth_resp.raise_for_status()
    
    token = auth_resp.json()['imdata'][0]['aaaLogin']['attributes']['token']
    
    return token

