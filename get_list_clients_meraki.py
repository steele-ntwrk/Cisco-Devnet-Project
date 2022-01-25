import requests
import json
from prettytable import PrettyTable 
requests.packages.urllib3.disable_warnings()

key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
base_url = 'https://api.meraki.com/api/v1'

def get_orgs(cloud_url=base_url, key_in=key):
    '''Returns list of orgs from Meraki Sandbox'''
    
    org_url = '{0}/organizations'.format(cloud_url)
    headers = {'X-Cisco-Meraki-API-Key': key_in}
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
    
def get_networks(cloud_url=base_url, key_in=key):
    '''Returns list of network for an organization'''
    
    input_org = input("Please copy and paste a Org ID out of the table you would like to get networks for?\n")
    
    #Create and Send HTTP GET Request
    network_url = '{0}/organizations/{1}/networks'.format(cloud_url, input_org)
    headers = {'X-Cisco-Meraki-API-Key': key_in}
    
    try:
        list_resp = requests.get(url=network_url,headers=headers, verify=False)
        list_resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(">>>Reason code " + str(err))
        
    #Store response as JSON
    json_list = list_resp.json()
    
    network_table = PrettyTable(['Name', 'ID'])
    network_table.align['Name'] = 'l'
    
    for item in json_list:
        network_table.add_row([item['name'],item['id']])
    
    print(network_table)
    
def get_devices(cloud_url=base_url, key_in=key):
    '''Returns list of network devices in a network'''
    
    input_network = input("Please copy and paste a Network ID out of the table you would  like to get networks for?\n")
    device_url = '{0}/networks/{1}/devices'.format(cloud_url, input_network)
    headers = {'X-Cisco-Meraki-API-Key': key_in}
    
    try:
        list_resp = requests.get(url=device_url,headers=headers, verify=False)
        list_resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(">>>Reason code " + str(err))
    
    json_list = list_resp.json()
    
    device_table = PrettyTable(['Model','Serial','MAC'])
    device_table.align['Model'] = 'l'
    
    for item in json_list:
        device_table.add_row([item['model'],item['serial'],item['mac']])
    
    print(device_table)
 
if __name__ == "__main__":

    print ('Hello and welcome to the Meraki Explorer.\n This tool will allow you navigate down the Meraki Org tree')

again = 'yes'
    
while again == 'yes':
        
    get_orgs()
    
    get_networks()
    
    get_devices()
    
    again = input('Would you like to look at another Meraki Org? Type "yes" if you would or "no" to quit\n')
    
    if again != 'no':
        again = input('Invalid choice, please choose yes or no\n')
