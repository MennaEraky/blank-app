import streamlit as st
import pickle

# Set the title of the app
st.title("🎈 Car CO2 Emission Predictor")

# Add a brief description
st.markdown("""
Welcome to the Car CO2 Emission Predictor. 
Use the inputs below to predict the CO2 emissions based on car features.
""")

# Create three columns for the inputs to keep them aligned
col1, col2, col3 = st.columns(3)

with col1:
    f1 = st.number_input("Engine Size (L)", min_value=1, max_value=10, value=2)
with col2:
    f2 = st.number_input("Cylinders", min_value=1, max_value=10, value=4)
with col3:
    f3 = st.number_input("Fuel Consumption (L/100km)", min_value=1, max_value=100, value=10)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Add a button to trigger the prediction
if st.button("Predict CO2 Emission"):
    # Make prediction
    res = model.predict([[f1, f2, f3]])
    # Display the result with some styling
    st.markdown(f"### Predicted CO2 Emission: **{res[0]:.2f} g/km**")
