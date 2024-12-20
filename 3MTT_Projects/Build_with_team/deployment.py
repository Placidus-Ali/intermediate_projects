import streamlit as st
import joblib
import numpy as np
import os
print('Models Inported Successfully')

# Load the model and scaler
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Set the path to your model file relative to the script's location
model_path = os.path.join(script_dir, "random_forest_model.joblib")
# Load the model
model = joblib.load(model_path)

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the scaler file
scaler_path = os.path.join(script_dir, "scaler_object.joblib")
# Load the scaler
scaler = joblib.load(scaler_path)
# scaler = joblib.load(open("scaler_object.joblib", 'rb'))
print('Models Loaded Successfully')

# Streamlit App
st.title("Crop Yield Prediction Model")
st.write("This app uses a Random Forest model to predict crop yield based on crop type, year, rainfall, and temperature.")
print('Model Name Approved')

# Mapping for crop selection
crop_mapping = {1: "Cassava", 2: "Rice", 3: "Yam"}
print('Crop Mapping Done')

# User inputs for prediction
st.header("Enter the input values:")
print('Input Header Done Successfully')

# Crop selection
crop_type = st.selectbox("Crop Type", options=[1, 2, 3], format_func=lambda x: crop_mapping[x])
print('Crop Selection Done Successfully')

# Year input
year = st.number_input("Year", min_value=1960, max_value=2030, value=2020, step=1)
print('Year Input Done Successfully')

# Average Rainfall input
rainfall = st.number_input("Average Rainfall (mm)", min_value=0.0, max_value=2000.0, value=1000.0)
print('Average Rainfall Input Done Successfully')

# Average Temperature input
temperature = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
print('Average Temperature Done Successfully')

# Prepare input data for prediction
input_data = np.array([[crop_type, year, rainfall, temperature]])
print('Input Data For Prediction Done Successfully')

# Scale the input data (excluding Crop and Year if they weren't scaled during training)
scaled_data = scaler.transform(input_data)
print('Scaler Data Done Successfully')

# Prediction
if st.button("Predict Yield"):
    prediction = model.predict(scaled_data)
    st.success(f"The predicted crop yield is: {prediction[0]:.2f} kg/ha")
print('Prediction Done Successfully')

# Additional Information
st.write("Note: Ensure that the input values are within a realistic range for accurate predictions.")
print('Write-up Done Successfully')

print('Model Deployed Successfully')