import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

def delete_dns_entries():
    print("")
    print("<><><><><><><><><><><><><><><><><><><>")
    CLOUDFLARE_GLOBAL_API_KEY = os.environ.get('CLOUDFLARE_GLOBAL_API_KEY')
    CLOUDFLARE_EMAIL = os.environ.get('CLOUDFLARE_EMAIL')
    CLOUDFLARE_ZONE_ID = os.environ.get('CLOUDFLARE_ZONE_ID')
    keywords = os.environ.get('KEYWORDS', '').split(',')

    headers = {
        'X-Auth-Key': CLOUDFLARE_GLOBAL_API_KEY,
        'X-Auth-Email': CLOUDFLARE_EMAIL,
        'Content-Type': 'application/json'
    }

    url = f'https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/dns_records'
    params = {
        'per_page': 100,  # Maximum number of records per page
    }

    # Fetch all DNS records
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        dns_records = response.json().get('result', [])
        record_count = len(dns_records)
        if record_count == 0:
            print('No DNS records found.')
            return

        print(f'Found {record_count} DNS records.')

        # Filter DNS records based on keywords
        filtered_records = []
        for record in dns_records:
            record_name = record.get('name', '').lower()
            record_content = record.get('content', '').lower()
            for keyword in keywords:
                if keyword.lower() in record_name or keyword.lower() in record_content:
                    filtered_records.append(record)
                    break

        print(f'Filtered {len(filtered_records)} DNS records.')

        # Delete filtered DNS records
        deleted_records = []
        for record in filtered_records:
            record_id = record['id']
            delete_url = f'https://api.cloudflare.com/client/v4/zones/{CLOUDFLARE_ZONE_ID}/dns_records/{record_id}'
            delete_response = requests.delete(delete_url, headers=headers)

            if delete_response.status_code == 200:
                deleted_records.append(record['name'])

        deleted_count = len(deleted_records)
        if deleted_count > 0:
            print(f'Deleted {deleted_count} DNS records:')
            for name in deleted_records:
                print(name)
        else:
            print('No DNS records matched the keywords.')
    else:
        print('Failed to fetch DNS records.')
    print("<><><><><><><><><><><><><><><><><><><>")
    print("")


# Call the function to delete DNS entries
delete_dns_entries()
