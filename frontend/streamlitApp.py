import streamlit as st
import requests
import json
from predictor import predictor
from footer import fixed_footer
from study import show_study

st.set_page_config(
        page_title="GenderMe",
)

st.title("GenderMe")

st.markdown("A little demo by Briefgarde. Check out the <a href='https://github.com/Briefgarde/genderme'>GitHub</a>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Predictor", "Study"])

with tab1:
    predictor()

with tab2:
    show_study()

fixed_footer()