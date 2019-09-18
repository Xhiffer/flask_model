from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
model = pickle.load( open( "save.p", "rb" ) )
app = Flask(__name__)

@app.route('/salaire.<numero>', methods=['GET', 'POST'])
def serveur(numero) :
    return jsonify({"numero":model.predict(int(numero))[0] })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)