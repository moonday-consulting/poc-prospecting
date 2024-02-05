import os
import xml.etree.ElementTree as ET
from datetime import datetime

from dotenv import load_dotenv
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport

# Load environment variables from .env file
load_dotenv("simap_credentials.env")


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
<search pageNo="1" recordsPerPage ="50" >
 <field name ="KEYWORD"><value>informatique</value></field>
 <field name="STAT_TM_1"><value>01.01.2024</value></field>
</search>
"""


# Appel de l'API pour obtenir la liste des avis
try:
    response = client.service.getSearchNoticeXml(search_xml, "FR")
    # response = client.service.getSearchNoticeList(search_xml)
    # response = client.service.getSearchNoticeList(search_xml)
    # response = client.service.getSearchNoticeList(search_xml)
    # response = client.service.getSearchNoticeList(search_xml)
    # print(response)
except Exception as e:
    print(f"Une erreur s'est produite: {e}")


try:
    # Analyser la réponse XML
    root = ET.fromstring(response)

    # Parcourir tous les éléments 'item' et extraire les ID et descriptions
    for item in root.findall(".//item"):
        project_id = item.find("projectid").text
        deadline = item.find("deadline").text
        description = item.find("description").text
        print(
            f"ID: {project_id}, Description: {description}, Deadline: {deadline}",
        )


except ET.ParseError:
    print("Erreur lors de l'analyse de la réponse XML.")
