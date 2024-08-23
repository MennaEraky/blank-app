import streamlit as st
import pickle 
st.title("🎈 Car CO2 Emssionm")
f1=st.number_input("Feature 1",min_value=1,max_value=10)
f2=st.number_input("Feature 2",min_value=1,max_value=10)
f3=st.number_input("Feature 3",min_value=1,max_value=100)

# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
