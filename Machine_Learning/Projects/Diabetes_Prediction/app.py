import numpy as np
from flask import Flask
from flask import request
from flask import render_template
import pickle

app = Flask(__name__)
sc = pickle.load(open('sc.pkl', 'rb'))
heart = pickle.load(open('classifier.pkl', 'rb'))


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    float_features = [float(x) for x in request.form.values()]
    print(float_features)
    final_features = [np.array(float_features)]
    print(final_features)
    pred = heart.predict(sc.transform(final_features)) 
    print(pred)   
    return render_template('result.html', prediction = pred) 


if __name__ == '__main__':
    app.run(debug=True)    