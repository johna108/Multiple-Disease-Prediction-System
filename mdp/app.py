import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('diabetes.html', active_page='diabetes')

@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    prediction = None
    if request.method == 'POST':
        # getting the input data from the form
        features = [
            float(request.form['Pregnancies']),
            float(request.form['Glucose']),
            float(request.form['BloodPressure']),
            float(request.form['SkinThickness']),
            float(request.form['Insulin']),
            float(request.form['BMI']),
            float(request.form['DiabetesPedigreeFunction']),
            float(request.form['Age'])
        ]
        
        # making prediction
        prediction = diabetes_model.predict([features])
        prediction = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
    
    return render_template('diabetes.html', prediction=prediction, active_page='diabetes')

@app.route('/heart', methods=['GET', 'POST'])
def heart():
    prediction = None
    if request.method == 'POST':
        # getting the input data from the form
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]
        
        # making prediction
        prediction = heart_disease_model.predict([features])
        prediction = 'The person is having heart disease' if prediction[0] == 1 else 'The person does not have any heart disease'
    
    return render_template('heart.html', prediction=prediction, active_page='heart')

@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    prediction = None
    if request.method == 'POST':
        # getting the input data from the form
        features = [
            float(request.form['fo']),
            float(request.form['fhi']),
            float(request.form['flo']),
            float(request.form['Jitter_percent']),
            float(request.form['Jitter_Abs']),
            float(request.form['RAP']),
            float(request.form['PPQ']),
            float(request.form['DDP']),
            float(request.form['Shimmer']),
            float(request.form['Shimmer_dB']),
            float(request.form['APQ3']),
            float(request.form['APQ5']),
            float(request.form['APQ']),
            float(request.form['DDA']),
            float(request.form['NHR']),
            float(request.form['HNR']),
            float(request.form['RPDE']),
            float(request.form['DFA']),
            float(request.form['spread1']),
            float(request.form['spread2']),
            float(request.form['D2']),
            float(request.form['PPE'])
        ]
        
        # making prediction
        prediction = parkinsons_model.predict([features])
        prediction = 'The person has Parkinsons disease' if prediction[0] == 1 else 'The person does not have Parkinsons disease'
    
    return render_template('parkinsons.html', prediction=prediction, active_page='parkinsons')

if __name__ == '__main__':
    app.run(debug=True)
