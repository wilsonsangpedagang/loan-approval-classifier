# Loan Approval Prediction using XGBoost


## 🎯 Project Goal 
The goal of this project is to develop an intelligent web-based system that assists in predicting loan approval decisions based on a user's financial and personal information. By leveraging machine learning (specifically an XGBoost classifier), the app aims to provide quick, data-driven insights into whether a loan application is likely to be approved or denied helping both users and financial institutions make faster and more informed decisions.

## 🧾 Description
This project is a machine learning-powered web application built using Flask and XGBoost. It allows users to input key loan application features such as income, loan amount, credit score, education, and employment history through a user-friendly form. Once the form is submitted, the system processes the data, feeds it into a trained XGBoost model, and displays a prediction result showing the probability of loan approval.

## ✨ Features
🧾 User-Friendly Interface – A clean and intuitive frontend for easy data entry.
🔁 Backend Integration – Flask-powered backend to handle form submission and prediction requests.
🤖 Smart Prediction Engine – XGBoost model trained on historical loan data for accurate decision-making.
📊 Detailed Results – Displays loan approval status along with the exact approval probability.

## 📊 Dataset 
https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data
Synthetic Data for binary classification on Loan Approval
⚠️ Disclaimer:
This project uses synthetic data generated to simulate real-world loan application scenarios. The dataset does not contain any real personal or financial information. It is intended solely for educational and demonstration purposes

## ⚙️ Setup Instructions
1. 📁 Clone the Repository
```bash
git clone https://github.com/your-username/loan-approval-app.git
cd loan-approval-app
```

2. 🐍 Create a Virtual Environment
```bash
python -m venv venv
```

3. ▶️ Activate the Virtual Environment
```bash
venv\Scripts\activate
```

4. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

5. 🚀 Run the App
```bash
python app.py
```
Now app.py will be running in 
🌐 http://127.0.0.1:5000









