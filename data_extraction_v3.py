import os
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport


# Function to fetch data
def fetch_data(keyword, start_date, cantons):
    load_dotenv("simap_credentials.env")

    username = os.getenv("SIMAP_USERNAME")
    password = os.getenv("SIMAP_PASSWORD")

    session = Session()
    session.auth = HTTPBasicAuth(username, password)

    transport = Transport(session=session)

    wsdl_url = "https://www.simap.ch/soapserver?wsdl"

    client = Client(wsdl=wsdl_url, transport=transport)

    search_xml = f"""
    <search pageNo="-1" recordsPerPage ="50" >
    <field name="KEYWORD"><value>{keyword}</value></field>
    <field name="STAT_TM_1"><value>{start_date}</value></field>
    <field name="KANTON_CD_OB"><value>{cantons}</value></field>
    </search>
    """

    try:
        response = client.service.getSearchNoticeXml(search_xml, "DE")
    except Exception as e:
        return f"Une erreur s'est produite: {e}"

    try:
        root = ET.fromstring(response)
        projects = []
        canton_counts = Counter()
        for item in root.findall(".//item"):
            project_id = item.find("projectid").text
            deadline = item.find("deadline").text
            description = item.find("description").text
            canton = (
                item.find("contLoc").text
                if item.find("contLoc") is not None
                else "Unknown"
            )
            projects.append((project_id, description, deadline, canton))
            canton_counts[canton] += 1
        return projects, canton_counts
    except ET.ParseError:
        return "Erreur lors de l'analyse de la réponse XML.", None


# Streamlit app
st.title("SIMAP Tenders Display with Filters")
# Input for keyword filtering
filter_keyword = st.text_input("Filter Keyword", value="")
start_date = st.date_input("Start Date", value=datetime.now())
cantons = st.text_input("Cantons (comma-separated)", value="ZH, GE, VD, BE, NE")

if st.button("Fetch Data"):
    data = fetch_data(filter_keyword, start_date.strftime("%d.%m.%Y"), cantons)
    if isinstance(data, str):
        st.error(data)
    else:

        # # Filter the data based on the keyword in description
        # filtered_data = [d for d in data if filter_keyword.lower() in str(d[1]).lower()]

        st.write(f"Total Offers Found: {len(data)}")

        for project_id, description, deadline in data:
            st.markdown(f"**ID:** {project_id}")
            st.text(f"Description: {description}")
            st.text(f"Deadline: {deadline}")
            st.write("---")
