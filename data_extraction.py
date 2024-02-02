import zeep
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('simap_credentials.env')

# Replace these with your Simap credentials
username = os.getenv('SIMAP_USERNAME')
password = os.getenv('SIMAP_PASSWORD')

# Create a session for HTTP Basic Authentication
session = Session()
session.auth = HTTPBasicAuth(username, password)

# Create a Zeep transport using the authenticated session
transport = Transport(session=session)

# WSDL URL for the Simap SOAP service
wsdl_url = 'https://www.simap.ch/soapserver?wsdl'

# Create a Zeep client with the authenticated transport
client = Client(wsdl=wsdl_url, transport=transport)



# Example method and parameters
method_name = 'getNoticesByCategory'
parameters = {'category': 'OB'}  # Public procurement category

# Call the API method
try:
    notice_ids = client.service[method_name](**parameters)

    # Process the notice IDs
    for notice_id in notice_ids:
        # You might need to call another operation to get detailed information about each notice
        # Example: notice_details = client.service.getNoticeDetails(notice_id=notice_id)
        # print(notice_details)

except Exception as e:
    print(f"An error occurred: {e}")