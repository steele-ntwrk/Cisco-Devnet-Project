import requests 
import json
from prettytable import PrettyTable

baseurl = 'https://sandboxapicdc.cisco.com/api/'
username = 'admin'
password = '!v3G@!4@Y'

requests.packages.urllib3.disable_warnings()

def get_auth(aci_url=baseurl, un=username, pw=password):
    auth_url = f"{aci_url}aaaLogin.json"
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
    
    token = auth_resp.json()["imdata"][0]['aaaLogin']['attributes']
    auth_token = token['token']
    
    cookies = {}
    cookies['APIC-Cookie'] = auth_token
    
    return cookies

def get_fabric(aci_url=baseurl,cookie=get_auth()):
    
    fabric_table = PrettyTable(["Fabric Name"])
    
    fabric_url = f"{aci_url}/node/class/fabricPod.json"

    fabric_resp = requests.get(url=fabric_url, cookies=cookie, verify=False)
    fabric_resp.raise_for_status
    
    fabric_json = fabric_resp.json()
    
    strip_top_level = fabric_json["imdata"]
    
    
    for item in strip_top_level:
        fabric_table.add_row([item['fabricPod']['attributes']['dn']])
    
    print(fabric_table)
    
def get_devices(aci_url=baseurl,cookie=get_auth()):
    
    device_table = PrettyTable(['Name', 'Inbound_MGMT', 'Outbound_MGMT','Uptime'])

    fabric_input = input(
                    'Copy and past the Fabric you wish to look at\n'
                         )
    
    device_url = f"{aci_url}/node/class/{fabric_input}/topSystem.json"
    
    device_resp = requests.get(url=device_url, cookies=cookie, verify=False)
    device_resp.raise_for_status
    
    device_json = device_resp.json()
    
    strip_top_level = device_json['imdata']
    
    for item in strip_top_level:
        device_table.add_row([item['topSystem']['attributes']['name'], 
                             item['topSystem']['attributes']['inbMgmtAddr'],
                             item['topSystem']['attributes']['oobMgmtAddr'],
                             item['topSystem']['attributes']['systemUpTime']])
        
    print(device_table)

if __name__ == "__main__":
    
    get_auth()
    
    get_fabric()
    
    get_devices()
    