import sys
import json
import requests
import os
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

DNAC=os.environ.get('DNAC','sandboxdnac.cisco.com')
DNAC_PORT=os.environ.get('DNAC_PORT',443)
DNAC_USER=os.environ.get('DNAC_USER','devnetuser')
DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','Cisco123!')

def get_auth_token(controller_ip=DNAC, username=DNAC_USER, password=DNAC_PASSWORD):
    """ Authenticates with controller and returns a token to be used in subsequent API invocations
    """

    login_url = "https://{0}:{1}/dna/system/api/v1/auth/token".format(controller_ip, DNAC_PORT)
    result = requests.post(url=login_url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)
    result.raise_for_status()

    token = result.json()["Token"]
    return {
        "controller_ip": controller_ip,
        "token": token
    }

def create_url(path, controller_ip=DNAC):
    """ Helper function to create a DNAC API endpoint URL
    """

    return "https://%s:%s/api/v1/%s" % (controller_ip, DNAC_PORT, path)

def get_create_network_device():
    cliTransport = input("Enter cliTransport method = ")
    enablePassword = input("Enter enablePassword: ")
    ipAddress = input("Enter ip address: ")
    password = input("Enter Password: ")
    snmpAuthPassphrase = input("Enter SNMP Auth Passphrase: ")
    snmpAuthProtocol = "v2"
    snmpMode = "AuthPriv"
    snmpPrivPassphrase = input("Enter SNMP Priv Passphrase: ")
    snmpPrivProtocol = "v2"
    snmpROCommunity = input("Enter SNMP RO Comm: ")
    snmpRWCommunity = input("Enter SNMP Rw Comm: ")
    
    get_body = {
        "cliTransport":cliTransport,
        "enablePassword":enablePassword,
        "ipAddress":[ipAddress],
        "password":password,
        "snmpAuthPassphrase":snmpAuthPassphrase,
        "snmpAuthProtocol":snmpAuthProtocol,
        "snmpMode":snmpMode,
        "snmpPrivPassphrase": snmpPrivPassphrase,
        "snmpPrivProtocol": snmpPrivProtocol,
        "snmpROCommunity": snmpROCommunity,
        "snmpRWCommunity": snmpRWCommunity,
    }
    
    return json.dumps(get_body)

body = get_create_network_device

def get_url(url):
    
    url = create_url(path=url)
    print(url)
    token = get_auth_token()
    headers = {'X-auth-token' : token['token']}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)

    return response.json()

def post_url(url):
    url = create_url(path=url)
    print(url)
    token = get_auth_token()
    headers = {'X-auth-token' : token['token']}
    try:
        response = requests.post(url, headers=headers, verify=False, body=get_create_network_device)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)
    
    return response.json()

def list_network_devices():
    return get_url("network-device")


    
    #datatype = type(json_body)
    
    #print(datatype)
    #print(body)



def main ():
    
    network_device = list_network_devices()
    
    #print(network_device)
  
    
    for device in network_device['response']: 
        print(device['id'], device['managementIpAddress'])

if __name__ == "__main__":
    main()