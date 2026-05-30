from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("fraud_model.pkl")

@app.route("/")
def home():
    return """
    <h2>Credit Card Fraud Detection</h2>
    <form action="/predict" method="post">
        <input type="text" name="amount" placeholder="Transaction Amount" required>
        <button type="submit">Predict</button>
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    amount = float(request.form["amount"])

    # Example input (modify according to your model features)
    features = np.array([[amount]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "Fraud Transaction Detected"
    else:
        result = "Legitimate Transaction"

    return f"<h3>{result}</h3><a href='/'>Try Again</a>"

if __name__ == "__main__":
    app.run(debug=True)