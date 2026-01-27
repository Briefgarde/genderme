import streamlit as st
from predictor import predictor
from footer import fixed_footer
from study import show_study

st.set_page_config(
        page_title="GenderMe",
)

st.title("GenderMe")

st.markdown("A little demo by Briefgarde. Check out the [GitHub](https://github.com/Briefgarde/genderme)")

tab1, tab2 = st.tabs(["Predictor", "Study"])

with tab1:
    predictor()

with tab2:
    show_study()

fixed_footer()