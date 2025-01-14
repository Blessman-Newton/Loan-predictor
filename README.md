# Credit Scoring System

A machine learning-based credit scoring system that predicts loan default risk using various loan application features.

## Overview

This project implements a loan default prediction system using Random Forest classification. It includes both API and web interface options for making predictions.

## Features

- Predicts loan default probability
- Handles multiple loan types
- Processes both new and repeat loan applications
- Provides REST API endpoint
- Includes interactive web interface using Streamlit
- Docker support for containerized deployment

## Tech Stack

- Python 3.12
- Flask (API Server)
- Streamlit (Web Interface) 
- Scikit-learn (Machine Learning)
- Pandas & NumPy (Data Processing)
- Docker (Containerization)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd Loan-predictor

2. Set up Virtual Environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

3. Install Dependencies
```bash
pip install -r requirements.txt

Running the Application
Using Streamlit (Web Interface)
```bash
streamlit run streamlit_app.py

<ol>
<li>API will be available at http://localhost:5000</li>
<li>Use /predict endpoint for predictions</li>
<li>Use /health endpoint to check server status</li>
</ol>

Using Docker
```bash 
# Build container
docker build -t loan-predictor .

# Run container
docker run -p 5000:5000 loan-predictor

API Usage Example
```bash
import requests

data = {
    "Total_Amount": 10000,
    "duration": 30,
    "loan_type": "Type_1",
    "New_versus_Repeat": "New Loan",
    "Lender_portion_Funded": 0.3,
    "Amount_Funded_By_Lender": 3000
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())


Model Information
Uses Random Forest Classifier
Features: loan amount, duration, type, borrower history
Includes SMOTE for handling class imbalance
Performance metrics available in