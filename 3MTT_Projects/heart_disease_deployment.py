import streamlit as st
import joblib
import numpy as np
import os
from PIL import Image
print("Libraries Imported Successfully")

# Load the model and scaler
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "random_forest.joblib")
model = joblib.load(model_path)

script_dir = os.path.dirname(os.path.abspath(__file__))
scaler_path = os.path.join(script_dir, "scaler.joblib")
scaler = joblib.load(scaler_path)
print('Model and Scaler Loaded Successfully')

image_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "heart_disease.jpg")
image = Image.open(image_path)

# Streamlit Title and Header
st.image(image, use_column_width=True)
st.title("Heart Disease Prediction Model")
st.write("This Model predicts the likelihood of heart disease based on user inputs.")
with st.expander("Documentation: Input Feature Descriptions"):
    st.write("**Age**: age in years")
    st.write("**Sex**: sex; 1 = male, 0 = female")
    st.write("**CP**: chest pain type; 0= typical angina, 1= atypical angina, 2= non-anginal pain, 3= asymptomatic")
    st.write("**Thalach**: maximum heart rate achieved")
    st.write("**Exang**: exercise induced angina; 1 = yes, 0 = no")
    st.write("**Oldpeak**: ST depression induced by exercise relative to rest(Min value=0.0, Max value=6.2)")
    st.write("**Slope**: the slope of the peak exercise ST segment; 0= upsloping, 1= flat, 2= downsloping")
    st.write("**CA**: number of major vessels (Min value=0, Max value=3) colored by flourosopy")
    st.write("**thal**: A categorical variable related to thallium stress test; 0 = error (in the original dataset 0 maps to NaN's), 1 = fixed defect, 2 = normal, 3 = reversable defect")
print('Streamlit Title and Header Set Successfully')

# Feature inputs
age = st.number_input("Age", min_value=29, max_value=77, value=50, step=1)
sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x== 1 else "No")
cp = st.number_input("Chest Pain Type", min_value=0, max_value=3, value=0, step=1)
thalach = st.number_input("Max Heart Rate Achieved", min_value=71, max_value=202, value=80, step=1)
exang = st.selectbox("Exercise Induced Angina", options=[1, 0], format_func=lambda x: "Yes" if x== 1 else "No")
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=6.2, value=0.0, step=0.1)
slope = st.number_input("Slope", min_value=0, max_value=2, value=1, step=1)
ca = st.number_input("CA", min_value=0.0, max_value=4.0, value=0.0, step=1.0)
thal = st.number_input("Thalassemia", min_value=0.0, max_value=3.0, value=0.0, step=1.0)
print("Feature Input Created")

# Prepare input data for prediction
input_data = np.array([[age, sex, cp, thalach, exang, oldpeak, slope, ca, thal]])
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