from zeep import Client
from zeep.transports import Transport
from zeep.cache import SqliteCache
from requests import Session
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv('simap_credentials.env')

# Replace these with your Simap credentials
username = os.getenv('SIMAP_USERNAME')
password = os.getenv('SIMAP_PASSWORD')



class Example:
    def __init__(self):
        pass

    def main(self, username, password):
        servername = "www.simap.ch"
        wsdl_url = f"https://{servername}/soapserver?wsdl"

        session = Session()
        session.auth = HTTPBasicAuth(username, password)
        transport = Transport(session=session, cache=SqliteCache())

        client = Client(wsdl_url, transport=transport)

        # Authentication
        successful_authentication = client.service.getAuthentication()
        if successful_authentication:
            print("Authentication successful!")
        else:
            print("Authentication not successful!")
            return

        # Making requests
        pageNo = 1
        recordsPerPage = 10
        timespanValue = "YEAR"
        searchXml = f"<search pageNo=\"{pageNo}\" recordsPerPage=\"{recordsPerPage}\">" \
                    f"<field name=\"TIMESPAN\"><value>{timespanValue}</value></field></search>"

        print(f"getSearchNoticeList(\"{searchXml}\")")
        count = client.service.getSearchNoticeCount(searchXml)
        print("count:", count)

        array_list = client.service.getSearchNoticeList(searchXml)
        for notice_id in array_list:
            print("id:", notice_id)
            xml = client.service.getNoticeXml(notice_id)
            print("xml:", xml)
            html = client.service.getNoticeHtml(notice_id)
            print("html:", html)

if __name__ == "__main__":
    example = Example()
    example.main(username, password)