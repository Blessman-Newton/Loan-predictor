# Credit Scoring System

A machine learning-powered credit scoring system designed to predict loan default risk using various loan application features.

## Overview

This project implements a loan default prediction system using a **Random Forest Classifier**. The system supports both a **REST API** and an interactive **web interface** built with Streamlit for making predictions.

## Features

- Predicts the probability of loan defaults.
- Supports multiple loan types.
- Handles both new and repeat loan applications.
- REST API endpoints for seamless integration.
- Interactive web interface for user-friendly predictions.
- Docker support for containerized deployment.

## Tech Stack

- **Python** 3.12
- **Flask** (API Server)
- **Streamlit** (Web Interface)
- **Scikit-learn** (Machine Learning)
- **Pandas** & **NumPy** (Data Processing)
- **Docker** (Containerization)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone [<your-repository-url>](https://github.com/Blessman-Newton/Loan-predictor.git)
   cd Loan-predictor
   ```

2. **Set up a virtual environment**:
   ```bash
   # Create a virtual environment
   python -m venv .venv

   # Activate the virtual environment
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

### Using Streamlit (Web Interface)
To launch the web interface:
```bash
streamlit run streamlit_app.py
```

### Using Flask (API Server)
To run the API:
```bash
python app.py
```
- **API Endpoints**:
  1. `/predict` – Submit loan data for prediction.
  2. `/health` – Check the server status.
- The API will be available at: [http://localhost:5000](http://localhost:5000).

### Using Docker
To deploy the application using Docker:
1. **Build the Docker container**:
   ```bash
   docker build -t loan-predictor .
   ```
2. **Run the container**:
   ```bash
   docker run -p 5000:5000 loan-predictor
   ```

---

## API Usage Example

Here’s how to make a prediction using the API:

```python
import requests

# Sample loan application data
data = {
    "Total_Amount": 10000,
    "duration": 30,
    "loan_type": "Type_1",
    "New_versus_Repeat": "New Loan",
    "Lender_portion_Funded": 0.3,
    "Amount_Funded_By_Lender": 3000
}

# Send a POST request to the API
response = requests.post("http://localhost:5000/predict", json=data)

# Print the prediction result
print(response.json())
```

---

## Model Information

- **Algorithm**: Random Forest Classifier
- **Features**:
  - Loan amount
  - Loan duration
  - Loan type
  - Borrower history (new vs. repeat loan)
  - Portion funded by the lender
- **Class Imbalance Handling**: SMOTE (Synthetic Minority Oversampling Technique)
- **Performance Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-score

