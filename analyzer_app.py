import streamlit as st
import pickle
import numpy as np

sleep_model = pickle.load(open("sleep_model.pkl", "rb"))
productivity_model = pickle.load(open("productivity_model.pkl", "rb"))

st.title("Student Productivity & Sleep Analyzer")
st.write("This application predicts student productivity and sleep quality based on study habits and lifestyle factors.")

study_hours = st.number_input("Study Hours", 0.0, 12.0)
screen_time = st.number_input("Screen Time (hours)", 0.0, 10.0)
sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0)
caffeine = st.number_input("Caffeine Intake", 0.0, 10.0)
physical_activity = st.number_input("Physical Activity (minutes)", 0.0, 300.0)

def sleep_rating(score):
    if score < 6:
        return "Poor"
    elif score < 8:
        return "Average"
    else:
        return "Good"    

def productivity_rating(score):
    if score < 60:
        return "Low"
    elif score < 80:
        return "Moderate"
    else:
        return "High"    
   
if st.button("Predict"):
    features = np.array([[study_hours, screen_time, sleep_hours, caffeine, physical_activity]])
    
    sleep_pred = sleep_model.predict(features)[0]
    prod_pred = productivity_model.predict(features)[0]

    st.subheader("Prediction Results")

    st.success(f"Predicted Sleep Quality: {sleep_pred:.2f}")
    st.success(f"Predicted Productivity Score: {prod_pred:.2f}")

    st.write("Sleep Category:", sleep_rating(sleep_pred)) 
    st.write("Productivity Level:", productivity_rating(prod_pred))

    if sleep_pred < 6:
        st.warning("⚠️ Your sleep quality is low. Try to reduce screen time and avoid caffeine.")
    elif sleep_pred < 8:
        st.info("🙂 Your sleep quality is average. Maintain sleep time, it will help to be improve it.")
    else:
        st.success("💤 You have good sleep quality!. Try to maintain this routine.")

    if prod_pred < 60:
        st.warning("⚠️ Your productivity is low. Improve sleep, study routine and distractions.")
    elif prod_pred < 80:
        st.info("🙂 Your productivity is moderate. Time management can improve it.")
    else:
        st.success("🚀 Your have high productivity! Great routine. Maintain it.")

 



    