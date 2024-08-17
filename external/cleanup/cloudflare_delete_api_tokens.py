import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

def remove_api_tokens():
    print("")
    print("<><><><><><><><><><><><><><><><><><><><><>")
    CLOUDFLARE_GLOBAL_API_KEY = os.environ.get('CLOUDFLARE_GLOBAL_API_KEY')
    CLOUDFLARE_EMAIL = os.environ.get('CLOUDFLARE_EMAIL')
    keywords = os.environ.get('KEYWORDS', '').split(',')
    print("Keywords: ",keywords)

    headers = {
        'X-Auth-Key': CLOUDFLARE_GLOBAL_API_KEY,
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'Content-Type': 'application/json'
    }

    url = 'https://api.cloudflare.com/client/v4/user/tokens'

    # Fetch all API tokens
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        api_tokens = response.json()['result']
        token_count = len(api_tokens)
        if token_count == 0:
            print('No API tokens found.')
            return

        # Filter API tokens based on keywords
        filtered_tokens = []
        for token in api_tokens:
            for keyword in keywords:
                if keyword in token['name']:
                    filtered_tokens.append(token)

        # Remove API tokens
        if len(filtered_tokens) == 0:
            print('No API tokens matching the keywords found.')
        else:
            print(f'Removing {len(filtered_tokens)} API tokens...')
            for token in filtered_tokens:
                delete_url = f'https://api.cloudflare.com/client/v4/user/tokens/{token["id"]}'
                delete_response = requests.delete(delete_url, headers=headers)
                if delete_response.status_code == 200:
                    print(f'Successfully removed API token: {token["id"]}')
                else:
                    print(f'Failed to remove API token: {token["id"]}')
    print("<><><><><><><><><><><><><><><><><><><><><>")
    print("")

# Remove API Tokens
remove_api_tokens()
