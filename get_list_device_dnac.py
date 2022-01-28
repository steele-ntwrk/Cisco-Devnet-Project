
import sys
import os
import json
from pprint import pprint
from rich.console import Console
from rich.table import Table
from rich import box
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

dnac_username = 'devnetuser'
dna_password = 'Cisco123!'
base_url= 'https://sandboxdnac.cisco.com'



def get_access_token(username=dnac_username,password=dna_password):
    
    login_url = f"{base_url}:443/dna/system/api/v1/auth/token"
    auth_resp = requests.post(url=login_url,auth=HTTPBasicAuth(username,password), verify=False)
    auth_resp.raise_for_status()
    
    token = auth_resp.json()['Token']
    
    return token

def get_network_device_list():
    
    url = f"{base_url}/dna/intent/api/v1/network-device"
    token = get_access_token()
    headers = {'X-auth-token': token}
    list_resp = requests.get(url=url, headers=headers, verify=False)
    list_resp.raise_for_status()
    
    json_list = list_resp.json()
    
    device_table = Table(title='DNAC_Device_List',box=box.DOUBLE)
    device_table.add_column('Type',style="green")
    device_table.add_column('Hostname',style="blue")
    device_table.add_column('macAddress',style="green")
    device_table.add_column('MGMT IP',style="blue")
    device_table.add_column('Role',style="green")
    device_table.add_column('Serial Number',style="blue")
    #pprint(json_list) 
    
    for device in json_list['response']:
        device_table.add_row(device['type'],device['hostname'],device['macAddress'],
                             device['managementIpAddress'],device['role']
                             ,device['serialNumber'],device['upTime'])
        
    console = Console()
    console.print(device_table)
        
if __name__ == "__main__":
    
    print(get_access_token())
    
    get_network_device_list()