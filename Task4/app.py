import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\souha\Downloads\task4\models\RF.pkl")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient information to predict the risk of heart disease.")

# Input fields
age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3, 4])
resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Serum Cholesterol", 100, 1000, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Result", [0, 1, 2])
max_hr = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2, 3,4,5,6,7])

# Convert sex to numeric
sex = 1 if sex == "Male" else 0

# Prepare input for prediction
input_data = np.array([[age, sex, cp, resting_bp, chol, fbs, restecg,
                        max_hr, exang, oldpeak, slope, ca, thal]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ No Heart Disease Detected.")
    else:
        st.error("⚠️ Risk of Heart Disease Detected!")
       