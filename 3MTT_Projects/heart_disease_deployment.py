import streamlit as st
import joblib
import numpy as np
import os
print("Libraries Imported Successfully")

# Load the model and scaler
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Set the path to your model file relative to the script's location
model_path = os.path.join(script_dir, "random_forest.joblib")
# Load the model
model = joblib.load(model_path)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the scaler file
scaler_path = os.path.join(script_dir, "scaler.joblib")
# Load the scaler
scaler = joblib.load(scaler_path)
# scaler = joblib.load(open("scaler_object.joblib", 'rb'))
print('Model and Scaler Loaded Successfully')


# Streamlit App
st.title("Heart Disease Prediction Model")
st.write("This Model predicts the likelihood of heart disease based on user inputs.")
print('Stream App Created')

# User inputs for prediction (without min and max constraints)
st.header("Enter your information:")
print("Header Input Created")

# Feature inputs
age = st.number_input("Age", value=50)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", options=[1, 0])
cp = st.number_input("Chest Pain Type (0-3)", value=0)
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol Level", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", options=[1, 0])
restecg = st.number_input("Resting ECG Results (0-2)", value=1)
thalach = st.number_input("Max Heart Rate Achieved", value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", options=[1, 0])
oldpeak = st.number_input("ST Depression Induced by Exercise", value=1.0, step=0.1)
slope = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", value=1)
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", value=0)
thal = st.number_input("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", value=1)
print("Feature Input Created")

# Prepare input data for prediction
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
print("Input Data Created")

# Scale the input data
scaled_data = scaler.transform(input_data)
print("Scaler Data Created")

# Prediction
if st.button("Predict Heart Disease"):
    prediction = model.predict(scaled_data)
    result = "You Are Likely To Have Heart Disease, Please See A Doctor" if prediction[0] == 1 else "You Are Likely Not To Have Heart Diseased"
    st.success(f"Prediction: {result}")
print("Prediction Done")

# Additional Information
st.write("Note: This prediction is based on a model trained on historical data and should not replace medical advice.")

print("Model is Perfectly Working")