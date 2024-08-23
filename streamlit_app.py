import streamlit as st
import pickle

# Set the page configuration for a better appearance
st.set_page_config(page_title="Car CO2 Emission Predictor", page_icon="🚗", layout="centered")

# Main title on the main page
st.title("🚗 Car CO2 Emission Predictor")

# Subtitle with a brief description
st.markdown("""
This app predicts the CO2 emissions of a car based on its engine size, number of cylinders, and fuel consumption. 
Please provide the details in the sidebar.
""")

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Sidebar for input fields
st.sidebar.header("Input Features")

# Input fields in the sidebar
f1 = st.sidebar.number_input("Engine Size (L)", min_value=1, max_value=10, value=2, help="Enter the engine size in liters.")
f2 = st.sidebar.number_input("Cylinders", min_value=1, max_value=10, value=4, help="Enter the number of cylinders.")
f3 = st.sidebar.number_input("Fuel Consumption (L/100km)", min_value=1, max_value=100, value=10, help="Enter the fuel consumption in liters per 100 kilometers.")

# Prediction button in the sidebar
if st.sidebar.button("Predict CO2 Emission"):
    # Make prediction
    res = model.predict([[f1, f2, f3]])
    # Display the result on the main page
    st.markdown(f"### Predicted CO2 Emission: **{res[0]:.2f} g/km**")
else:
    st.markdown("### Please enter the car features in the sidebar to get a prediction.")

# Footer or additional information (optional)
st.markdown("""
---
This model is designed to help you understand the CO2 emissions based on simple car features. 
Adjust the values in the sidebar to see how they affect the emissions.
""")
