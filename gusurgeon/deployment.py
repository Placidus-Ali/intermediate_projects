import streamlit as st
import os
import joblib
import pandas as pd
print("Libraries Loading Successfully")

# Load trained model
with open("random_forest_model.pkl", "rb") as model_file:
    model = joblib.load(model_file)
print("Model Loading Successfully")

st.title("EHR Software Price Prediction")

# Display an image
st.image("ehr.jpg", use_column_width=True)

# User input fields
pricing_model = st.selectbox("Pricing Model", ["Subscription", "Perpetual License"])
deployment_type = st.selectbox("Deployment Type", ["Cloud-based", "On-premise"])
num_users = st.number_input("Number of Users", min_value=1, step=1)

features_customization = st.multiselect("Features & Customization", ["Basic", "Advanced", "Customized"])
integration_requirements = st.multiselect("Integration Requirements", ["Standard", "Full Interoperability"])

department_selected = st.multiselect("Department Selected", ["HIS-PACs Basic", "Ophthalmology", "ENT", "Oral Surgery"])
financial_management = st.selectbox("Financial Management System", ["Simple", "Advanced"])

# Numerical input fields
training_cost = st.number_input("Training Cost ($)", min_value=0, step=1)
security_cost = st.number_input("Security & Compliance Cost ($)", min_value=0, step=1)
support_cost = st.number_input("Support & Maintenance ($)", min_value=0, step=1)
scalability_cost = st.number_input("Scalability Cost ($)", min_value=0, step=1)
contract_fees = st.number_input("Contract Fees ($)", min_value=0, step=1)
print("Input Field Created Successfully")


# Convert categorical inputs to appropriate format
features_customization = ",".join(features_customization) if features_customization else "None"
integration_requirements = ",".join(integration_requirements) if integration_requirements else "None"
department_selected = ",".join(department_selected) if department_selected else "None"
print("Categorical Input Created Successfully")

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    "Pricing Model": [pricing_model],
    "Deployment Type": [deployment_type],
    "Number of Users": [num_users],
    "Features & Customization": [features_customization],
    "Integration Requirements": [integration_requirements],
    "Training Cost": [training_cost],
    "Security & Compliance Cost": [security_cost],
    "Support & Maintenance": [support_cost],
    "Scalability Cost": [scalability_cost],
    "Contract Fees": [contract_fees],
    "Department Selected": [department_selected],
    "Financial Management System": [financial_management]
})

# Ensure categorical columns are encoded properly
input_data = pd.get_dummies(input_data)

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated EHR Price: ${prediction[0]:,.2f}")
print("Deployment Was Done Successfully")

