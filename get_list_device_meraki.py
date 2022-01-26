import requests
import json
from prettytable import PrettyTable

requests.packages.urllib3.disable_warnings()

key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
base_url = "https://api.meraki.com/api/v1"

HEADERS = {
    "X-Cisco-Meraki-API-Key": key,
}


def get_orgs(cloud_url=base_url):
    """Returns list of orgs from Meraki Sandbox"""

    org_url = f"{cloud_url}/organizations"
    list_resp = requests.get(url=org_url, headers=HEADERS, verify=False)
    list_resp.raise_for_status()

    json_list = list_resp.json()

    org_table = PrettyTable(["Id", "Name"])
    org_table.align["Id"] = "r"
    org_table.align["Name"] = "l"
    org_table.sortby = "Name"

    for item in json_list:
        org_table.add_row([item["id"], item["name"]])

    print(org_table)


def get_networks(cloud_url=base_url):
    """Returns list of network for an organization"""

    input_org = input(
        "Please copy and paste a Org ID out of the table you would like to get networks for?\n"
    )

    # Create and Send HTTP GET Request
    network_url = f"{cloud_url}/organizations/{input_org}/networks"

    try:
        list_resp = requests.get(
            url=network_url, headers=HEADERS, verify=False)
        list_resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(">>>Reason code " + str(err))

    # Store response as JSON
    json_list = list_resp.json()

    network_table = PrettyTable(["Name", "ID"])
    network_table.align["Name"] = "l"

    for item in json_list:
        network_table.add_row([item["name"], item["id"]])

    print(network_table)


def get_devices(cloud_url=base_url, key_in=key):
    """Returns list of network devices in a network"""

    input_network = input(
        "Please copy and paste a Network ID out of the table you would  like to get networks for?\n"
    )
    device_url = f"{cloud_url}/networks/{input_network}/devices"

    try:
        list_resp = requests.get(url=device_url, headers=HEADERS, verify=False)
        list_resp.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f">>>Reason code {err}")

    json_list = list_resp.json()

    device_table = PrettyTable(["Model", "Serial", "MAC"])
    device_table.align["Model"] = "l"

    for item in json_list:
        device_table.add_row([item["model"], item["serial"], item["mac"]])

    print(device_table)


if __name__ == "__main__":

    print(
        "Hello and welcome to the Meraki Explorer.\n This tool will allow you navigate down the Meraki Org tree"
    )

    while True:

        get_orgs()

        get_networks()

        get_devices()

        again = input(
            'Would you like to look at another Meraki Org? Type "yes" if you would or "no" to quit\n'
        ).lower()

        if again == "no":
            break
