import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

# Retrieve the environment variables
ORGANIZATION = os.environ.get("ORGANIZATION")
TERRAFORM_IO_API_TOKEN = os.environ.get("TERRAFORM_IO_API_TOKEN")
VCS_IDENTIFIER = os.environ.get("VCS_IDENTIFIER")
TERRAFORM_OAUTH_TOKEN_ID = os.environ.get("TERRAFORM_OAUTH_TOKEN_ID")
REPO_TOKEN = os.environ.get("REPO_TOKEN")
BRANCH_NAME = os.environ.get("BRANCH_NAME")


def check_workspace_exists():
    url = "https://app.terraform.io/api/v2/organizations/{}/workspaces".format(ORGANIZATION)
    headers = {
        "Authorization": "Bearer {}".format(TERRAFORM_IO_API_TOKEN),
        "Content-Type": "application/vnd.api+json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        workspace_name = "homelab-external"
        workspaces = response.json().get("data")
        for workspace in workspaces:
            if workspace["attributes"]["name"] == workspace_name:
                print("")
                print("<><><><><><><><><><><><><><><><><><><><><><>")
                print("Workspace 'homelab-external' already exists.")
                print("<><><><><><><><><><><><><><><><><><><><><><>")
                print("")
                delete_confirmation = input("Do you want to delete it? (yes/no): ")
                
                if delete_confirmation.lower() == "yes":
                    delete_workspace(workspace_name)
                else:
                    print("")
                    print("<><><><><><><><><><>")
                    print("Cancelling deletion.")
                    print("<><><><><><><><><><>")
                    print("")
                    return
        create_workspace()
    else:
        print("")
        print("<><><><><><><><><><><><><><><><><><><><>")
        print("  No homelab-external workspace exists.")
        print("<><><><><><><><><><><><><><><><><><><><>")
        print("")


def delete_workspace(workspace_name):
    delete_url = "https://app.terraform.io/api/v2/organizations/{}/workspaces/{}".format(ORGANIZATION, workspace_name)
    headers = {
        "Authorization": "Bearer {}".format(TERRAFORM_IO_API_TOKEN),
        "Content-Type": "application/vnd.api+json"
    }
    delete_response = requests.delete(delete_url, headers=headers)

    if delete_response.status_code == 204:
        print("")
        print("><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("Workspace 'homelab-external' deleted successfully")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><")
        print("")
    else:
        print("")
        print("<><><><><><><><><><><><><><><>")
        print("Error deleting workspace: {}".format(delete_response.status_code))
        print("<><><><><><><><><><><><><><><>")
        print("")

def create_workspace():
    create_url = f"https://app.terraform.io/api/v2/organizations/{ORGANIZATION}/workspaces"
    headers = {
        "Authorization": f"Bearer {TERRAFORM_IO_API_TOKEN}",
        "Content-Type": "application/vnd.api+json"
    }

    create_payload = {
        "data": {
            "attributes": {
                "name": "homelab-external",
                "execution-mode": "local"
            },
            "type": "workspaces"
        }
    }

    # Conditionally add VCS repo information
    if VCS_IDENTIFIER and TERRAFORM_OAUTH_TOKEN_ID:
        create_payload["data"]["attributes"]["vcs-repo"] = {
            "identifier": VCS_IDENTIFIER,
            "oauth-token-id": TERRAFORM_OAUTH_TOKEN_ID,
            "branch": BRANCH_NAME
        }

    create_response = requests.post(create_url, headers=headers, json=create_payload)

    if create_response.status_code == 201:
        print("\n><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("Workspace 'homelab-external' created successfully")
        print("><><><><><><><><><><><><><><><><><><><><><><><><>\n")
    else:
        print("\n<><><><><><><><><><><><><><><>")
        print(f"Error creating workspace: {create_response.status_code}")
        print("Response: ", create_response.text)
        print("<><><><><><><><><><><><><><><>\n")


# Call the function to check and perform the necessary actions
check_workspace_exists()
