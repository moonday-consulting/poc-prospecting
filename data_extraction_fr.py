import requests

def fetch_api_data():
    url = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records?limit=20"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Erreur lors de l'accès à l'API : Code de statut", response.status_code)

if __name__ == "__main__":
    fetch_api_data()
