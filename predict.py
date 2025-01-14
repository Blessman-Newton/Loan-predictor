from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle
from imblearn.over_sampling import SMOTE

app = Flask(__name__)

# Load model at startup
with open('credit_scoring.pkl', 'rb') as f:
    MODEL = pickle.load(f)

def prepare_features(data):
    df = pd.DataFrame([data])
    
    # Encode categorical variables
    le = LabelEncoder()
    df['loan_type_encoded'] = le.fit_transform(df['loan_type'])
    df['new_repeat_encoded'] = le.fit_transform(df['New_versus_Repeat'])
    
    features = [
        'Total_Amount', 
        'duration',
        'loan_type_encoded',
        'new_repeat_encoded',
        'Lender_portion_Funded',
        'Amount_Funded_By_Lender'
    ]
    
    return df[features]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Prepare features
        X = prepare_features(data)
        
        # Make prediction
        prediction = MODEL.predict(X)[0]
        probability = MODEL.predict_proba(X)[0][1]
        
        # Prepare response
        response = {
            'prediction': int(prediction),
            'probability': float(probability),
            'status': 'success'
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)