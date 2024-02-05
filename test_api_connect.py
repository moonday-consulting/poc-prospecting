import json

import requests

# Base URL for the TED API
base_url = "http://spendnetwork.com/api/ted_search/"

# If you need to apply filters, construct the query string
params = {
    "country_code": "UK",  # Example filter for UK country code
    "date_from": "01-03-2013",  # Example filter for date range start
    "format": "json",  # To get the response in JSON format
}

# Send a GET request with the specified parameters
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Now you can process the 'data' as per your requirements
    # For example, print the first record of tenders
    print(json.dumps(data[0], indent=2))
else:
    print(f"Failed to retrieve data: {response.status_code}")
import json

import requests

# Base URL for the TED API
base_url = "http://spendnetwork.com/api/ted_search/"

# If you need to apply filters, construct the query string
params = {
    "country_code": "SW",  # Example filter for UK country code
    "date_from": "01-03-2013",  # Example filter for date range start
    "format": "json",  # To get the response in JSON format
}

# Send a GET request with the specified parameters


response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:

    # Parse the JSON response
    data = response.json()

    # Now you can process the 'data' as per your requirements
    # For example, print the first record of tenders
    print(json.dumps(data[0], indent=2))
else:
    print(f"Failed to retrieve data: {response.status_code}")
