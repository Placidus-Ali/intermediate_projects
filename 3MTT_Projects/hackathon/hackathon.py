import streamlit as st
import joblib
import numpy as np
import os
import sklearn
print('Libraries Imported suuccessfully')

# Load the model and scaler
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, "gradient_boosting.joblib")
model = joblib.load(model_path)
print('Model Loaded Successfully')

scaler_path = os.path.join(script_dir, "scaler_object.joblib")
scaler = joblib.load(scaler_path)
print('Scaler Loaded Successfully')

# Streamlit App
st.title("Diabetes Prediction Model")
st.write("This model predicts the likelihood of having diabetes based on user inputs.")
print('Stream App Created')

# User inputs for prediction
st.header("Enter your information:")
print("Header Input Created")

# Feature inputs
high_bp = st.selectbox("Do you have high blood pressure? (1: Yes, 0: No)", options=[1, 0])
high_chol = st.selectbox("Do you have high cholesterol? (1: Yes, 0: No)", options=[1, 0])
chol_check = st.selectbox("Have you checked your cholesterol in the last 5 years? (1: Yes, 0: No)", options=[1, 0])
bmi = st.number_input("Body Mass Index (BMI)", value=25.0, step=0.1)
smoker = st.selectbox("Are you a smoker? (1: Yes, 0: No)", options=[1, 0])
stroke = st.selectbox("Any History of stroke? (1: Yes, 0: No)", options=[1, 0])
heart_disease = st.selectbox("Any History of heart disease or attack? (1: Yes, 0: No)", options=[1, 0])
fruits = st.selectbox("Do you consume fruits frequently? (1: Yes, 0: No)", options=[1, 0])
veggies = st.selectbox("Do you consume vegetables frequently? (1: Yes, 0: No)", options=[1, 0])
heavy_alcohol = st.selectbox("Do you consume alcohol heavily? (1: Yes, 0: No)", options=[1, 0])
any_healthcare = st.selectbox("Do you have access to healthcare? (1: Yes, 0: No)", options=[1, 0])
no_docbc_cost = st.selectbox("Couldn’t see a doctor due to cost? (1: Yes, 0: No)", options=[1, 0])
gen_health = st.selectbox("Rate your general health (1: Excellent, ..., 5: Poor)", options=[1, 2, 3, 4, 5])
mental_health = st.number_input("Number of days of poor mental health in the past month", value=0, step=1)
physical_health = st.number_input("Number of days of poor physical health in the past month", value=0, step=1)
diff_walk = st.selectbox("Difficulty walking or climbing stairs? (1: Yes, 0: No)", options=[1, 0])
sex = st.selectbox("Sex (1: Male, 0: Female)", options=[1, 0])
age = st.selectbox("Age category (1: 18–24, ..., 13: 80+)", options=list(range(1, 14)))
education = st.selectbox("Education level (1: No high school, ..., 6: College graduate)", options=list(range(1, 7)))
income = st.selectbox("Income level (1: <$10k, ..., 8: $75k+)", options=list(range(1, 9)))
print("Feature Input Created")

# Prepare input data for prediction
input_data = np.array([[high_bp, high_chol, chol_check, bmi, smoker, stroke, heart_disease,
                        fruits, veggies, heavy_alcohol, any_healthcare, no_docbc_cost,
                        gen_health, mental_health, physical_health, diff_walk, sex,
                        age, education, income]])
print("Input Data Created")

# Scale the input data
scaled_data = scaler.transform(input_data)
print("Scaler Data Created")

# Prediction
if st.button("Predict Diabetes"):
    prediction = model.predict(scaled_data)
    result = "You Are Likely to Have Diabetes, Please Consult a Doctor" if prediction[0] == 1 else "You Are Unlikely to Have Diabetes"
    st.success(f"Prediction: {result}")
print("Prediction Done")

# Additional Information
st.write("Note: This prediction is based on a model trained on historical data and should not replace medical advice.")

print("Model is Perfectly Working")