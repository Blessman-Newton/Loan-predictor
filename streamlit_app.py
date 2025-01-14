import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle

# Load model
with open('credit_scoring.pkl', 'rb') as f:
    MODEL = pickle.load(f)

def prepare_features(data):
    df = pd.DataFrame([data])
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

def main():
    st.title('Loan Default Prediction')
    
    # Input form
    total_amount = st.number_input('Loan Amount', min_value=0)
    duration = st.number_input('Duration (days)', min_value=1)
    loan_type = st.selectbox('Loan Type', ['Type_1', 'Type_5', 'Type_7'])
    new_repeat = st.selectbox('New or Repeat', ['New Loan', 'Repeat Loan'])
    lender_portion = st.slider('Lender Portion', 0.0, 1.0, 0.3)
    funded_amount = st.number_input('Funded Amount', min_value=0)

    if st.button('Predict'):
        data = {
            'Total_Amount': total_amount,
            'duration': duration,
            'loan_type': loan_type,
            'New_versus_Repeat': new_repeat,
            'Lender_portion_Funded': lender_portion,
            'Amount_Funded_By_Lender': funded_amount
        }
        
        X = prepare_features(data)
        prediction = MODEL.predict(X)[0]
        probability = MODEL.predict_proba(X)[0][1]
        
        st.subheader('Prediction Results:')
        st.write(f'Default Risk: {"High" if prediction == 1 else "Low"}')
        st.write(f'Default Probability: {probability:.2%}')

if __name__ == '__main__':
    main()