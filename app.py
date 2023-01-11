from flask import Flask,render_template,request,url_for

import numpy as np
import pandas as pd
import requests
import pickle
import io
import config
heart_stroke_prediction_path='models/test1.pkl'
heart_stroke_prediction=pickle.load(open(heart_stroke_prediction_path,'rb'))

app=Flask(__name__)




@ app.route('/')
def home():
    title = 'HeartStroke Prediction - Home'
    return render_template('homepage.html',title=title)

'''@ app.route('/homepage.html',methods=['POST','GET'])
def Homepage():
    title = 'HeartStroke Prediction - Home'
    return render_template('homepage.html',title=title)'''

@ app.route('/about')
def about():
    title = 'HeartStroke Prediction - About'
    return render_template('about.html',title=title)

@ app.route('/heartstrokeprediction')
def heartstrokeprediction():
    title='HeartStroke Prediction - Prediction'
    return render_template("prediction.html",title=title)

@ app.route('/Prediction',methods=["POST"])
def Prediction():
    title="HeartStroke Prediction"
    if request.method == 'POST':
        Name = request.form['name']
        Gender = request.form['gender']
        Age = int(request.form['age'])
        Hypertension = request.form['hypertension']
        Heart_disease = request.form['heartdisease']
        Married_Status = request.form['marriedstatus']
        Employment=request.form['employment']
        Residence=request.form['residencetype']
        GlucoseLevel=float(request.form['glucoselevel'])
        BMI=float(request.form['bmi'])
        Smoking=request.form['smoking']
        gen={"Male":0,"Female":1,"Others":2}
        ht={"yes":1,"No":0}
        hd={"yes":1,"No":0}
        ms={"married":0,"notmarried":1}
        emp={'private':0, 'selfemployed':1, 'govt_job':2 ,'children':3, 'neverworked':4}
        rt={"urban":0,"rural":1}
        st={'formerly':0, 'Never':1, 'smokes':2 ,'unknown':3}
        data = np.array([[gen[Gender],Age, ht[Hypertension], hd[Heart_disease],emp[Employment],ms[Married_Status], rt[Residence], 
        GlucoseLevel,BMI,st[Smoking]]])
        my_prediction = heart_stroke_prediction.predict(data)
        final_prediction = my_prediction[0]
        if final_prediction==0:
            final_prediction='No'
        else:
            final_prediction='Yes'
        return render_template('results.html',Name=Name, prediction=final_prediction, title=title)
if __name__=='__main__':
    app.run(debug=True)