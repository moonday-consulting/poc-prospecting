from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def display_csv():
    data = []
    total_rows = 0
    total_switzerland = 0
    total_france = 0
    displayed_rows = 0
    # Liste des fichiers CSV à lire
    csv_files = [
        'data/api_data_fusion_moonday.csv',
        'data/api_data_fusion_enedis.csv',
        'data/api_data_fusion_lingenheld.csv',
        'data/api_data_fusion_novartis.csv',
        'data/api_data_fusion_solocal.csv',
        'data/api_data_fusion_vinci.csv'
    ]

    for file_name in csv_files:
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                # Ajouter des conditions ici si certaines opérations doivent être
                # spécifiques à 'api_data_fusion_moonday.csv'
                if file_name == 'data/api_data_fusion_moonday.csv':
                                    # Mettre à jour le total des lignes pour tous les fichiers
                    total_rows += 1
                    # Mettre à jour les totaux pour la Suisse et la France basés sur les données de tous les fichiers
                    if row.get('country', '').upper() == 'SUISSE':
                        total_switzerland += 1
                    elif row.get('country', '').upper() == 'FRANCE':
                        total_france += 1
                    # Compter les lignes affichées pour tous les fichiers
                    if row.get('gpt_responses', '') == "True":
                        displayed_rows += 1
                    pass
                else:
                    # Ajouter les données à la liste 'data' pour tous les fichiers
                    data.append(row)

    return render_template('display.html', data=data, total_rows=total_rows, total_switzerland=total_switzerland, total_france=total_france, displayed_rows=displayed_rows)

if __name__ == '__main__':
    app.run(debug=True)
