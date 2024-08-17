import requests
import json
import os

from dotenv import load_dotenv
from requests.exceptions import RequestException

# Load environment variables from .env file
load_dotenv(override=True)

# Retrieve the environment variables
ZEROTIER_API_TOKEN = os.environ.get("ZEROTIER_API_TOKEN")

def check_network_exists():
    url = "https://api.zerotier.com/api/v1/network"
    headers = {
        "Authorization": "Bearer {}".format(ZEROTIER_API_TOKEN)
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            networks = response.json()

            if len(networks) == 0:
                print("")
                print("<><><><><><><><><")
                print("No networks found")
                print("<><><><><><><><><")
                print("")
                return

            select_network(networks)
        else:
            print("")
            print("<><><><><><>")
            print("Error: {}".format(response.status_code))
            print("<><><><><><>")
            print("")

    except RequestException as e:
        print("")
        print("<><><><><><>")
        print("Error: {}".format(str(e)))
        print("<><><><><><>")
        print("")

def select_network(networks):
    print("")
    print("<><><><><><><><><><><><><><>")
    print("Select a network to delete:")
    for i, network in enumerate(networks, start=1):
        print("{}. {} - {}".format(i, network["config"]["name"], network["id"]))
    print("<><><><><><><><><><><><><><>")
    print("")

    selection = int(input("Enter the network number: "))
    print(" ")

    if selection < 1 or selection > len(networks):
        print("")
        print("**********************")
        print("Invalid network number")
        print("**********************")
        print("")
    else:
        network_id = networks[selection - 1]["id"]
        delete_network(network_id)

def delete_network(network_id):
    url = "https://api.zerotier.com/api/v1/network/{}".format(network_id)
    headers = {
        "Authorization": "Bearer {}".format(ZEROTIER_API_TOKEN),
        "Content-Type": "application/json"
    }

    try:
        response = requests.delete(url, headers=headers)

        if response.status_code == 200:
            print("")
            print("<><><><><><><><><><><><><><>")
            print("Network deleted successfully")
            print("<><><><><><><><><><><><><><>")
            print("")

        else:
            print("")
            print("<><><><><><><><><><><><><><>")
            print("Error deleting network: {}".format(response.status_code))
            print("<><><><><><><><><><><><><><>")
            print("")

    except RequestException as e:
        print("")
        print("<><><><><><>")
        print("Error: {}".format(str(e)))
        print("<><><><><><>")
        print("")

# Call the function to check and perform the necessary actions
check_network_exists()
