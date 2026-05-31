import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("Credit Card Fraud Detection")

amount = st.number_input("Enter Transaction Amount", min_value=0.0)

if st.button("Predict"):
    features = np.array([[amount]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("Fraud Transaction Detected")
    else:
        st.success("Legitimate Transaction")
