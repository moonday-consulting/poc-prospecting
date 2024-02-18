import os
import xml.etree.ElementTree as ET
from datetime import datetime

from dotenv import load_dotenv
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

from xml.dom.minidom import parseString

import csv



# Load environment variables from .env file
load_dotenv("../.env")


# Replace these with your Simap credentials
username = os.getenv("SIMAP_USERNAME")
password = os.getenv("SIMAP_PASSWORD")


# Create a session for HTTP Basic Authentication
session = Session()
session.auth = HTTPBasicAuth(username, password)

# Create a Zeep transport using the authenticated session
transport = Transport(session=session)

# WSDL URL for the Simap SOAP service
wsdl_url = "https://www.simap.ch/soapserver?wsdl"


# Create a Zeep client with the authenticated transport
client = Client(wsdl=wsdl_url, transport=transport)

# Exemple de création d'une requête de recherche
# search_xml = """
# <search>
#   <field name="KEYWORDS"><value>Exemple de Mot-clé</value></field>
#   <field name="TYPE_CONTRACT_CD_OB"><value>WORKS</value></field>
# </search>
# """

# Définir la date de début pour la recherche (janvier 2024)
debut_annee = datetime(2024, 1, 1).strftime("%d.%m.%Y")

# Liste des codes des cantons
cantons = "ZH,GE,VD, BE, NE"  # Exemple avec Zurich, Genève, et Vaud

# Liste des keywords
keywords = "data"


search_xml = """
<search pageNo="1" recordsPerPage="1000">
  <field name="TIMESPAN"><value>YEAR</value></field>
  <field name="STAT_TM_1"><value>01.01.2023</value></field>
  <field name="STAT_TM_2"><value>31.12.2024</value></field>
</search>

"""


# Appel de l'API pour obtenir la liste des avis
try:
    response = client.service.getSearchNoticeXml(search_xml, "EN")
    # response = client.service.getSearchNoticeList(search_xml)
    # response = client.service.getSearchNoticeList(search_xml)
    # response = client.service.getSearchNoticeList(search_xml)
    # response = client.service.getSearchNoticeList(search_xml)
    dom = parseString(response)
    pretty_xml_as_string = dom.toprettyxml()
    print(pretty_xml_as_string)
except Exception as e:
    print(f"Une erreur s'est produite: {e}")


try:
    root = ET.fromstring(response)
    with open('../data/api_data_simap.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['id', 'description'])
        for item in root.findall(".//item"):
            project_id = item.find("projectid").text
            description = item.find("description").text
            description_cleaned = description.replace('\n', ' ').replace('\r', '')
            csvwriter.writerow([project_id, description_cleaned])

except ET.ParseError:
    print("Erreur lors de l'analyse de la réponse XML.")
