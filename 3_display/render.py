from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def display_csv():
    displayed_rows = {
        'moonday': 0,
        'lingenheld': 0,
        'novartis': 0,
        'solocal': 0,
        'vinci': 0,
    }
    data_by_file = {
        'moonday': [],
        'lingenheld': [],
        'novartis': [],
        'solocal': [],
        'vinci': [],
    }
    file_labels = {
        'data/api_data_fusion_moonday.csv': 'moonday',
        'data/api_data_fusion_lingenheld.csv': 'lingenheld',
        'data/api_data_fusion_novartis.csv': 'novartis',
        'data/api_data_fusion_solocal.csv': 'solocal',
        'data/api_data_fusion_vinci.csv': 'vinci',
    }

    for file_name, label in file_labels.items():
        with open(file_name, 'r', encoding='utf-8') as file:
            csv_file = csv.DictReader(file)
            total_rows = 0
            total_switzerland = 0
            total_france = 0
            for row in csv_file:
                total_rows += 1
                if row.get('country', '').upper() == 'SUISSE':
                    total_switzerland += 1
                elif row.get('country', '').upper() == 'FRANCE':
                    total_france += 1
                if row.get('gpt_responses', '') == "true":
                    displayed_rows[label] += 1
                pass
                data_by_file[label].append(row)

    return render_template('display.html', data_by_file=data_by_file, total_rows=total_rows, total_switzerland=total_switzerland, total_france=total_france, displayed_rows=displayed_rows)

if __name__ == '__main__':
    app.run(debug=True)
