from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize')
def visualize():
    df = pd.read_csv('data/protein_synthesis.csv')
    fig = px.scatter(df, x='protein_sequence', y='protein_structure', color='synthesis_pathway')
    return fig.to_html()

if __name__ == "__main__":
    app.run(debug=True)