from flask import Flask, render_template
import pandas as pd 

app = Flask(__name__) #create /initiating the app

# Read the CSV file
df = pd.read_csv('data.csv')

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/assist')
def assist():
    return render_template('assist.html')

@app.route('/type')
def type():
    return render_template('type.html')

@app.route('/goal')
def goal():
    return render_template('goal.html')

@app.route('/home_away')
def home_away():
    return render_template('home_away.html')

@app.route('/match')
def match():
    return render_template('match.html')

@app.route('/opponent')
def opponent():
    return render_template('opponent.html')

@app.route('/scoring_trends')
def scoring_trends():
    return render_template('scoring_trends.html')

@app.route('/timing')
def timing():
    return render_template('timing.html')
# Add more routes for other charts if needed


@app.route('/data')
def get_data():
    # Convert DataFrame to JSON
    data_json = df.to_json(orient='records')
    return data_json


if __name__ == '__main__':
    app.run(debug=True)
