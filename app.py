import streamlit as st
import joblib
import pandas as pd

# Load model package
model_package = joblib.load("../models/final_model.pkl")
model = model_package["model"]
feature_order = model_package["features"]

st.title("🛒 Olist Review Risk Predictor")

st.write("Predict probability of a low customer review (1–2 stars)")

# Create input fields (adjust names to your real features)
price = st.number_input("Product Price", min_value=0.0)
delivery_time = st.number_input("Delivery Time (days)", min_value=0)
freight_value = st.number_input("Freight Value", min_value=0.0)

# Create input dataframe
input_data = pd.DataFrame([{
    "price": price,
    "delivery_time": delivery_time,
    "freight_value": freight_value
}])

# Ensure correct column order
input_data = input_data.reindex(columns=feature_order, fill_value=0)

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write(f"Probability of Low Review: {probability:.2f}")

    if prediction == 1:
        st.error("⚠ High Risk of Low Review")
    else:
        st.success("✅ Low Risk")