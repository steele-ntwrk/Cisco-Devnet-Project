import requests
import json
from prettytable import PrettyTable 
requests.packages.urllib3.disable_warnings()

key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
base_url = 'https://api.meraki.com/api/v1'

def get_orgs(cloud_url=base_url, key_in=key):
    key = key_in
    org_url = '{0}/organizations'.format(cloud_url)
    headers = {'X-Cisco-Meraki-API-Key': key}
    list_resp = requests.get(url=org_url,headers=headers, verify=False)
    list_resp.raise_for_status()
    
    json_list = list_resp.json()
    
    org_table = PrettyTable(['Id', 'Name'])
    org_table.align['Id'] = 'r'
    org_table.align['Name'] = 'l'
    org_table.sortby = 'Name'
    
    for item in json_list:
        org_table.add_row([item['id'],item['name']])
    
    print(org_table)
    
print(get_orgs)