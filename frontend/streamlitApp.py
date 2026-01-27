import streamlit as st
import requests
import json
from predictor import predictor
from footer import fixed_footer

st.title("GenderMe")

st.markdown("A little demo by Briefgarde. Check out the <a href='https://github.com/Briefgarde/genderme'>GitHub</a>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Predictor", "Study"])

with tab1:
    predictor()

with tab2:
    st.write("I love tabs")
    
fixed_footer()