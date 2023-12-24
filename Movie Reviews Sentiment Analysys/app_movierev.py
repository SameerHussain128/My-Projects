import numpy as np
from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load Naive bayes model and TfidfVectorizer object from disk
filename = "Movies_Review_Classification.pkl"
classifier = pickle.load(open(filename, 'rb'))
cv = pickle.load(open("count-vectorizer.pkl", 'rb'))
app = Flask(__name__)

#@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=["POST"])
def predict():
  if request.method == 'POST':
    message = 

    
if __name__=='__main__':
    main()
    