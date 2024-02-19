from flask import Flask, render_template, request
import csv
from collections import Counter

app = Flask(__name__)

def load_csv_data_and_count_relevance(filename):
    data = []
    relevances = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['relevance'] = int(row['relevance'].replace('%', ''))
            data.append(row)
            relevances.append(row['relevance'])
    sorted_data = sorted(data, key=lambda x: x['relevance'], reverse=True)

    relevance_counts = Counter(relevances)
    return  sorted_data, dict(relevance_counts)

@app.route('/')
def index():
    data, relevance_counts = load_csv_data_and_count_relevance('../data/api_data_fusion_moonday_test_relevance.csv')
    true_positives = ['24-14728', '24-15217', '24-15222', '274039', '24-14766']
    false_positives = ['24-15828', '272874']
    return render_template('display.html', data=data, relevance_counts=relevance_counts, true_positives=true_positives, false_positives=false_positives)


if __name__ == '__main__':
    app.run(debug=True)
