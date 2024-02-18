import requests
import csv

def fetch_api_data_and_write_to_csv(number_of_results=100):
    records_fetched = 0
    start = 0
    limit = 100
    results_to_fetch = min(number_of_results, 1000)
    
    with open('data/api_data_boamp.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'idweb', 'id', 'annonce_reference_schema_v110', 'objet', 'filename', 'famille',
            'code_departement', 'code_departement_prestation', 'famille_libelle', 'dateparution',
            'datefindiffusion', 'datelimitereponse', 'nomacheteur', 'titulaire', 'perimetre',
            'type_procedure', 'soustype_procedure', 'procedure_libelle', 'procedure_categorise',
            'nature', 'sousnature', 'nature_libelle', 'sousnature_libelle', 'nature_categorise',
            'nature_categorise_libelle', 'criteres', 'marche_public_simplifie',
            'marche_public_simplifie_label', 'etat', 'descripteur_code', 'dc', 'descripteur_libelle',
            'type_marche', 'type_marche_facette', 'type_avis', 'annonce_lie', 'annonces_anterieures',
            'annonces_anterieures_schema_v110', 'source_schema', 'GESTION', 'DONNEES', 'url_avis', 'url_pdf'
        ]
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        csvwriter.writeheader()

        while records_fetched < results_to_fetch:
            url = f"https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records?limit={min(limit, results_to_fetch - records_fetched)}&start={start}&order_by=dateparution DESC"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                records = data.get("results", [])
                for record in records:
                    row = {field: (record.get(field, '').replace('\n', ' ').replace('\r', ' ') if isinstance(record.get(field, ''), str) else record.get(field, '')) for field in fieldnames}
                    id_web = row['idweb']
                    url_pdf = f"https://www.boamp.fr/telechargements/FILES/PDF/2024/02/{id_web}.pdf"
                    row['url_pdf'] = url_pdf
                    csvwriter.writerow(row)
                    records_fetched += 1

                start += limit
            else:
                print("Erreur lors de l'accès à l'API : Code de statut", response.status_code)
                break

if __name__ == "__main__":
    fetch_api_data_and_write_to_csv(1000)
