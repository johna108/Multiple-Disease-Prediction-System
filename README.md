# Multiple Disease Prediction System

A machine learning-based web application that predicts multiple diseases using trained models. The application is built with Flask and provides predictions for:
- Diabetes
- Heart Disease
- Parkinson's Disease

## Features

- Clean, responsive UI built with Bootstrap
- Easy-to-use forms for entering patient data
- Real-time predictions using pre-trained machine learning models
- Navigation sidebar for switching between different disease predictions
- Input validation and clear result display

## Project Structure

```
mdp/
├── app.py                 # Main Flask application
├── templates/            # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── diabetes.html     # Diabetes prediction form
│   ├── heart.html        # Heart disease prediction form
│   └── parkinsons.html   # Parkinson's prediction form
├── colab_files_to_train_models/  # Training notebooks
├── dataset/              # Source datasets
├── saved_models/         # Trained ML models
└── requirements.txt      # Dependencies
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Multiple-Disease-Prediction-System
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:
```bash
cd mdp
```

2. Run the Flask application:
```bash
python app.py
```

3. Open your web browser and visit:
```
http://localhost:5000
```

## Disease Prediction Features

### 1. Diabetes Prediction
- Input parameters include:
  - Number of Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin Level
  - BMI
  - Diabetes Pedigree Function
  - Age

### 2. Heart Disease Prediction
- Input parameters include:
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Serum Cholesterol
  - Fasting Blood Sugar
  - Resting ECG Results
  - Maximum Heart Rate
  - Exercise Induced Angina
  - ST Depression
  - Slope of ST Segment
  - Number of Major Vessels
  - Thal Value

### 3. Parkinson's Disease Prediction
- Uses various voice measurement parameters:
  - Fundamental Frequency (Fo)
  - Frequency Variations (Fhi, Flo)
  - Jitter Measurements
  - Shimmer Measurements
  - And other acoustic parameters

## Model Training

The `colab_files_to_train_models` directory contains Jupyter notebooks used to train the machine learning models. Each disease has its own dedicated notebook:
- `Multiple disease prediction system - diabetes.ipynb`
- `Multiple disease prediction system - heart.ipynb`
- `Multiple disease prediction system - Parkinsons.ipynb`

## Dependencies

- Flask 3.0.2
- NumPy 1.26.3
- scikit-learn 1.3.2
- Flask-WTF 1.2.1
- Werkzeug 3.0.1

## Note

This application is intended for educational and demonstration purposes only. Medical diagnoses should always be performed by qualified healthcare professionals.
