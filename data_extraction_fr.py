import requests
import csv
def iterable_to_string(value):
    """
    Convertit une valeur itérable en une chaîne de caractères séparée par des points-virgules.
    Si la valeur n'est pas une liste, elle est convertie en chaîne de caractères.
    """
    if isinstance(value, list): 
        return ';'.join(value)
    else:
        return str(value)
def fetch_api_data_and_write_to_csv():
    url = "https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records?limit=100&order_by=dateparution DESC"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])

        with open('api_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'idweb', 'id', 'annonce_reference_schema_v110', 'objet', 'filename', 'famille',
                'code_departement', 'code_departement_prestation', 'famille_libelle', 'dateparution',
                'datefindiffusion', 'datelimitereponse', 'nomacheteur', 'titulaire', 'perimetre',
                'type_procedure', 'soustype_procedure', 'procedure_libelle', 'procedure_categorise',
                'nature', 'sousnature', 'nature_libelle', 'sousnature_libelle', 'nature_categorise',
                'nature_categorise_libelle', 'criteres', 'marche_public_simplifie',
                'marche_public_simplifie_label', 'etat', 'descripteur_code', 'dc', 'descripteur_libelle',
                'type_marche', 'type_marche_facette', 'type_avis', 'annonce_lie', 'annonces_anterieures',
                'annonces_anterieures_schema_v110', 'source_schema', 'GESTION', 'DONNEES', 'url_avis','url_pdf'
            ]
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

            csvwriter.writeheader()

            for result in results:
                row = {field: result.get(field, '') for field in fieldnames}

                row['code_departement'] = iterable_to_string(result.get('code_departement', ''))
                row['descripteur_code'] = iterable_to_string(result.get('descripteur_code', ''))
                row['dc'] = iterable_to_string(result.get('dc', ''))
                row['descripteur_libelle'] = iterable_to_string(result.get('descripteur_libelle', ''))
                row['type_marche'] = iterable_to_string(result.get('type_marche', ''))
                row['type_marche_facette'] = iterable_to_string(result.get('type_marche_facette', ''))
                row['type_avis'] = iterable_to_string(result.get('type_avis', ''))
                id_web = row['idweb']
                url_pdf = f"https://www.boamp.fr/telechargements/FILES/PDF/2024/02/{id_web}.pdf"
                row['url_pdf'] = url_pdf
                csvwriter.writerow(row)
    else:
        print("Erreur lors de l'accès à l'API : Code de statut", response.status_code)

if __name__ == "__main__":
    fetch_api_data_and_write_to_csv()
