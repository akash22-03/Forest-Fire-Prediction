import pickle
import numpy

model = pickle.load(open('model.pkl','rb'))

temp = int(input('Enter Temperature : '))
oxygen = int(input('Enter Oxygen : '))
humid = int(input('Enter Humidity : '))

features = [temp,oxygen,humid]
val = [numpy.array(features)]
prediction = model.predict_proba(val)
result = '{0:.{1}f}'.format(prediction[0][1],2)

if result > str(0.5):
    print('Your Forest is in Danger.\nProbability of fire occuring is {}'.format(result))
else:
    print('Your Forest is safe.\nProbability of fire occuring is {}'.format(result))
