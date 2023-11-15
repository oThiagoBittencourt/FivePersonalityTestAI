import joblib
from flask import Flask, request, jsonify
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

base = ['EXT', 'EST', 'AGR', 'CSN', 'OPN']

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

@app.route('/resultado', methods=['POST'])
@cross_origin()
def resultado():
    features = request.json

    X = []

    for item in base:
        for i in range(1,11):
            X.append(features[f'{item}{i}'])

    model = joblib.load('Models/model.joblib')
    y_pred = model.predict([X])
    
    return jsonify( {'personality' : str(y_pred[0])} )

# Páginas Respostas

@app.route('/0')
def pag_0():
    return render_template('0.html')

@app.route('/1')
def pag_1():
    return render_template('1.html')

@app.route('/2')
def pag_2():
    return render_template('2.html')

@app.route('/3')
def pag_3():
    return render_template('3.html')

@app.route('/4')
def pag_4():
    return render_template('4.html')

if __name__ == '__main__':
    app.run(debug=True)