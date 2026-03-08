import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(page_title="Fraud Detector", layout="centered")

st.title("🛡️ Credit Card Fraud Detection")
st.write("Day 5 of my 100-day Learning Journey! 📈")

# മോഡൽ ലോഡ് ചെയ്യുന്നു
try:
    model_path = 'credit_card_fraud_rf_model.pkl'
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        st.success("✅ Model loaded and ready!")
    else:
        st.error("❌ Model file not found.")
except Exception as e:
    st.error(f"⚠️ Error loading model: {e}")

# input fields
v10 = st.number_input("Feature V10", value=0.0)
v14 = st.number_input("Feature V14", value=0.0)
v4 = st.number_input("Feature V4", value=0.0)
amount = st.number_input("Transaction Amount", value=0.0)

if st.button("Check for Fraud"):
    try:
        # മോഡൽ 29 ഫീച്ചറുകളാണ് പ്രതീക്ഷിക്കുന്നത് [cite: 2026-03-05]
        full_input = np.zeros(29)
        
        # പ്രധാനപ്പെട്ട വാല്യൂസ് നൽകുന്നു
        full_input[10] = v10
        full_input[14] = v14
        full_input[4] = v4
        full_input[28] = amount 
        
        features = full_input.reshape(1, -1)
        prediction = model.predict(features)
        
        # താൽക്കാലികമായി സെൻസിറ്റിവിറ്റി കൂട്ടാൻ ഒരു 'Safety Check' ചേർക്കുന്നു
        # മോഡൽ പറഞ്ഞില്ലെങ്കിലും വാല്യൂസ് വളരെ കുറവാണെങ്കിൽ (Extreme) വാർണിംഗ് നൽകും
        is_fraud = (prediction[0] == 1) or (v10 <= -15 and v14 <= -20)
        
        if is_fraud:
            st.error("🚨 Warning: Potential Fraudulent Transaction!")
        else:
            st.balloons()
            st.success("✅ Transaction is Legitimate.")
            
    except Exception as e:
        st.error(f"Prediction Error: {e}")