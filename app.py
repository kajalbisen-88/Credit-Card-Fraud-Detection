import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("Credit Card Fraud Detection")

amount = st.number_input("Enter Amount")

if st.button("Predict"):
    prediction = model.predict([[amount]])

    if prediction[0] == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Legitimate Transaction")
