from flask import Blueprint, render_template, request
import numpy as np
from xgboost import XGBClassifier  # Required to load the model
import pandas as pd

# Create a Flask Blueprint for modular route organization
views = Blueprint("views", __name__)

# Load the trained XGBoost model from a JSON file
model = XGBClassifier()
model.load_model("loan_model.json")

# Route for the homepage
@views.route("/")
def index():
    return render_template("index.html")

# Route to render the input form
@views.route("/form", methods=["GET"])
def forms():
    return render_template("form.html")

# Route to handle prediction logic after form submission
@views.route("/predict", methods=["POST"])
def predict():
    try:
        # Define the feature names expected by the model
        feature_names = [
            'person_age',
            'person_education',
            'person_income',
            'person_emp_exp',
            'person_home_ownership',
            'loan_amnt',
            'loan_intent',
            'loan_int_rate',
            'loan_percent_income',
            'cb_person_cred_hist_length',
            'credit_score',
            'person_gender_male',
            'previous_loan_defaults_on_file_Yes'
        ]

        # Collect input values from the submitted form and convert them to the correct type
        data = [
            float(request.form["person_age"]),
            float(request.form["person_education"]),
            float(request.form["person_income"]),
            int(request.form["person_emp_exp"]),
            float(request.form["person_home_ownership"]),
            float(request.form["loan_amnt"]),
            float(request.form["loan_intent"]),
            float(request.form["loan_int_rate"]),
            float(request.form["loan_percent_income"]),
            float(request.form["cb_person_cred_hist_length"]),
            float(request.form["credit_score"]),
            float(request.form["person_gender_male"]),
            float(request.form["previous_loan_defaults_on_file_Yes"])
        ]

        # Create a DataFrame with the input data to match model's expected format
        x = pd.DataFrame([data], columns=feature_names)

        # Get the probability of the loan being approved (class 1)
        prob = model.predict_proba(x)[0][1]

        # If probability is 0.5 or higher, predict approval (1), otherwise rejection (0)
        prediction = int(prob >= 0.5)

        # Create a human-readable result message based on prediction
        result = (
            f"✅ Loan Approved! (Probability: {prob:.2%})"
            if prediction == 1
            else f"❌ Loan Denied. (Probability of approval: {prob:.2%})"
        )

        # Debug output to console
        print("Received input:", data)
        print("Prediction probability:", prob)

        # Render the result page with the prediction message
        return render_template("result.html", result=result)

    except Exception as e:
        # In case of error, render result page with the error message
        return render_template("result.html", result=f"⚠️ Error: {str(e)}")
