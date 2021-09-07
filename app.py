from flask import Flask, render_template, request
import pickle
import numpy
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template('ForestFire.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    tempvar = int(request.form['Temp'])
    oxyvar = int(request.form['Oxy'])
    humidvar = int(request.form['Humid'])

    inputvalues = [tempvar, oxyvar, humidvar]
    valarr = [numpy.array(inputvalues)]
    prediction = model.predict_proba(valarr)
    result = '{0:.{1}f}'.format(prediction[0][1], 2)
    if result > str(0.5):
        return render_template('ForestFire.html', pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(result))
    else:
        return render_template('ForestFire.html', pred='Your Forest is safe.\nProbability of fire occuring is {}'.format(result))


if __name__ == '__main__':
    app.run(debug=True)
