import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np
from predictt import *
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeMpdel.pkl", 'rb'))


@app.route('/')
def home():
    locations = sorted(data['location'].unique())
    return render_template('index1.html', locations=locations)
    
@app.route('/',methods=['POST'])
def index1():
    if request.method=='POST':
     location = request.form['location']
     bhk = request.form['bhk']
     bath = request.form['bath']
     sqft = request.form['total_sqft']
     bath = float(bath)
     bhk = float(bhk)

    df = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'bhk'])
    prediction = predict_price(location,sqft,bath,bhk)

    return render_template('index1.html',prediction=prediction)




if __name__ == "__main__":
    app.run(debug=True, port=5001)

