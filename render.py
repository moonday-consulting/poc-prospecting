from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def display_csv():
    data = []
    with open('api_data_with_responses.csv', 'r', encoding='utf-8') as file:
        csv_file = csv.DictReader(file, delimiter=';')
        for row in csv_file:
            data.append(row)
    return render_template('display.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
