import requests
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Retrieve the environment variables
CLOUDFLARE_ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
CLOUDFLARE_EMAIL = os.environ.get("CLOUDFLARE_EMAIL")
CLOUDFLARE_GLOBAL_API_KEY = os.environ.get("CLOUDFLARE_GLOBAL_API_KEY")

def get_tunnels():
    url = "https://api.cloudflare.com/client/v4/accounts/{}/cfd_tunnel".format(CLOUDFLARE_ACCOUNT_ID)
    headers = {
        "X-Auth-Email": CLOUDFLARE_EMAIL,
        "X-Auth-Key": CLOUDFLARE_GLOBAL_API_KEY,
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        tunnels = data["result"]
        non_deleted_tunnels = [tunnel for tunnel in tunnels if tunnel.get("deleted_at") is None]
        return non_deleted_tunnels
    else:
        print("Error: {}".format(response.status_code))
        sys.exit()

def delete_tunnel(tunnel):
    print("")
    print("<><><><><><><><><><><><><><><><><><><><><>")
    tunnel_id = tunnel["id"]
    tunnel_name = tunnel["name"]
    print("Selected tunnel: {} - Tunnel ID: {}".format(tunnel_name, tunnel_id))

    confirmation = input("Are you sure you want to delete this tunnel? (y/n): ")
    print("")
    if confirmation.lower() == "y":
        delete_url = "https://api.cloudflare.com/client/v4/accounts/{}/cfd_tunnel/{}".format(CLOUDFLARE_ACCOUNT_ID, tunnel_id)
        headers = {
            "X-Auth-Email": CLOUDFLARE_EMAIL,
            "X-Auth-Key": CLOUDFLARE_GLOBAL_API_KEY,
        }
        response = requests.delete(delete_url, headers=headers)

        if response.status_code == 200:
            print("Tunnel deleted successfully")
            print("<><><><><><><><><><><><><><><><><><><><><>")
            print("")
        else:
            print("Error deleting tunnel: {}".format(response.status_code))
            print("<><><><><><><><><><><><><><><><><><><><><>")
            print("")
    else:
        print("Deletion canceled")
        print("<><><><><><><><><><><><><><><><><><><><><>")
        print("")

def display_tunnels(tunnels):
    print("")
    print("<><><><><><><><><><><><><><><><><><><><><>")
    if not tunnels:
        print("            No Tunnels Found")
        print("<><><><><><><><><><><><><><><><><><><><><>")
        print("")
        sys.exit()

    print("Tunnels:")
    for i, tunnel in enumerate(tunnels):
        print("{}. Name: {} - Tunnel ID: {}".format(i + 1, tunnel["name"], tunnel["id"]))
    print("<><><><><><><><><><><><><><><><><><><><><>")
    print("")

# Get and display tunnels
tunnels = get_tunnels()
display_tunnels(tunnels)

# Delete the selected tunnel
selected_tunnel_index = input("Enter the tunnel number to delete: ")
try:
    selected_tunnel_index = int(selected_tunnel_index)
    print(" ")
    if 1 <= selected_tunnel_index <= len(tunnels):
        selected_tunnel = tunnels[selected_tunnel_index - 1]
        delete_tunnel(selected_tunnel)
    else:
        print("Invalid tunnel number")
except ValueError:
    print("Invalid input. Please enter a valid tunnel number.")
