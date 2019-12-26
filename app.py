import flask
from flask import Flask, render_template
from flask_frozen import Freezer

# app = Flask(__name__)

app = Flask('__name__')
freezer = Freezer(app)

import pandas as pd
import numpy as np
import seaborn as sns
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PowerTransformer

import pickle

with open('article_classifier.pkl', 'rb') as picklefile:
    c = pickle.load(picklefile)

with open('score_predictor.pkl', 'rb') as picklefile:
    predictor = pickle.load(picklefile)

#-------- ROUTES GO HERE -----------#

@app.route("/classify", methods=['POST', 'GET'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':

        inputs = flask.request.form

        # name = inputs['name']
        article = inputs['article']
        sentiment = TextBlob(article, classifier = c).sentiment

        classification = c.classify(article)
        sentiment = predictor.predict([sentiment])

        if (classification == 'neg'):
            result = 'negative'
        else:
            result = 'positive'

        # return render_template('blog.html', r=result, s = (sentiment[0]*10)/10)
    with open("build/classify.html", 'r') as viz_file:
        return viz_file.read()

    # return render_template('blog.html', r=result, s = sentiment[0])

#put site content here

@app.route('/page')
def page():
   with open("build/VideoGameWebscraping.html", 'r') as viz_file:
       return viz_file.read()

@app.route('/')
def home():
    with open("build/index.html", 'r') as viz_file:
       return viz_file.read()
    # return render_template('home.html')

@app.route('/data')
def notebook():
    return render_template('Scraping_Itch_2.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    # freezer.freeze()
    app.run(debug=True)
    '''Connects to the server'''

    # HOST = '127.0.0.1'
    # PORT = 4000
    # app.run(HOST, PORT, debug=True)