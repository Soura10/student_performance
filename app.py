from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

application= Flask(__name__) #entry point where you need to execute it

app=application

##Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    # Probably doing getting the data and do the prediction inside this method

    if request.method=='GET':
        return render_template('home.html')
    else:
         ##in the POST part i have to capture the data
             ##the i have to do standard scaling or feature scaling
             ##then only do the prediction.
             data=CustomData