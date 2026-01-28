import streamlit as st
from predictor import predictor
from footer import fixed_footer
from study import show_study
from critic import show_critic

st.set_page_config(
        page_title="GenderMe",
)

st.title("GenderMe")

st.markdown("A little demo by Briefgarde. Check out the [GitHub](https://github.com/Briefgarde/genderme)")

tab1, tab2, tabs3= st.tabs(["Predictor", "Study", "Critics"])

with tab1:
    predictor()

with tab2:
    show_study()

with tabs3:
    show_critic()

fixed_footer()