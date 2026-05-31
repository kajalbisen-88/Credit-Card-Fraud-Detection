from flask import Flask, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("fraud_model.pkl")

@app.route("/")
def home():
    return """
    <h2>Credit Card Fraud Detection</h2>
    <form action="/predict" method="post">
        <input type="number" step="0.01" name="amount" placeholder="Enter Amount" required>
        <button type="submit">Predict</button>
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    try:
        amount = float(request.form["amount"])

        # Input for prediction
        features = np.array([[amount]])

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "⚠️ Fraud Transaction Detected"
        else:
            result = "✅ Legitimate Transaction"

        return f"""
        <h2>{result}</h2>
        <a href="/">Check Another Transaction</a>
        """

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
