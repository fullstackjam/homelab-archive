import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

def prompt_user(variable, prompt_msg):
    current_value = os.getenv(variable, "")
    print(f"Current value for {variable}: {current_value if current_value else '<<NULL>>'}")
    new_value = input(f"{prompt_msg} (Leave blank to keep current value): ").strip()
    return new_value if new_value else current_value

def update_env_file(variables):
    with open(".env", "w") as env_file:
        for var, value in variables.items():
            if value:
                env_file.write(f"{var}={value}\n")

variables = {
    "CLOUDFLARE_GLOBAL_API_KEY": "Enter Cloudflare Global API Key: ",
    "CLOUDFLARE_EMAIL": "Enter Cloudflare Email: ",
    "CLOUDFLARE_ACCOUNT_ID": "Enter Cloudflare Account ID: ",
    "CLOUDFLARE_ZONE_ID": "Enter Cloudflare Zone ID: ",
    "ZEROTIER_API_TOKEN": "Enter ZeroTier API Token: ",
    "TERRAFORM_IO_API_TOKEN": "Enter Terraform IO API Token: ",
    "TERRAFORM_OAUTH_TOKEN_ID": "Enter Terraform OAuth Token ID: ",
    "VCS_IDENTIFIER": "Enter VCS Identifier: ",
    "REPO_TOKEN": "Enter Repo Token: ",
    "ORGANIZATION": "Enter Organization: ",
    "KEYWORDS": "Enter keywords (comma-separated): ",
}

env_vars = {var: os.getenv(var, "") for var in variables}

if any(env_vars.values()):
    print("\nVariables and Current Values:")
    for var, value in env_vars.items():
        print(f"- {var}: {value if value else '<<NULL>>'}")

    while True:
        print("\nChoose a variable to edit:")
        for i, var in enumerate(variables, 1):
            print(f"{i}. {var}")
        choice = input("\nEnter the number (or press Enter to skip): ").strip()
        if not choice:
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(variables):
                selected_var = list(variables)[index]
                env_vars[selected_var] = prompt_user(selected_var, variables[selected_var])
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Invalid choice, try again.")
else:
    for var, prompt_msg in variables.items():
        env_vars[var] = prompt_user(var, prompt_msg)

update_env_file(env_vars)

print("\nFinal Environment Variable Values:")
for var, value in env_vars.items():
    print(f"- {var}: {value if value else '<<NULL>>'}")
