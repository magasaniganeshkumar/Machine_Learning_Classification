import numpy as np
from flask import Flask
from flask import request
from flask import render_template
import pickle

app = Flask(__name__)
sc = pickle.load(open('sc.pkl', 'rb'))
heart = pickle.load(open('heart.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    lst = []
    cp = int(request.form['chest pain type (4 values)'])
    if cp == 0:
        lst += [1, 0, 0, 0]
    elif cp == 1:
        lst += [0, 1, 0, 0]
    elif cp == 2:
        lst += [0, 0, 1, 0]
    elif cp >= 3:
        lst += [0, 0, 0, 1]  

    trestbps = int(request.form['requesting blood pressure'])
    lst += [trestbps]

    chol = int(request.form['serum cholestoral in mg/dl'])
    lst += [chol]

    fbs = int(request.form['fasting blood suger > 120 mg/dl'])
    if fbs == 0:
        lst += [1, 0]
    else:
        lst += [0, 1]
    
    restecg = int(request.form['resting electocardiographic results (values 0, 1, 2)'])
    if restecg == 0:
        lst += [1, 0, 0]
    elif restecg == 1:
        lst += [0, 1, 0]
    else:
        lst += [0, 0, 1]

    thalach = int(request.form['maximum heart rate achieved'])
    lst += [thalach]
    
    exang = int(request.form['exercise induced angina'])
    if exang == 0:
        lst += [1, 0]
    else:
        lst += [0, 1] 

    features = np.array([lst])  
    pred = heart.predict(sc.transform(features)) 
    print(pred)   
    return render_template('result.html', prediction = pred) 


if __name__ == '__main__':
    app.run(debug=True)    