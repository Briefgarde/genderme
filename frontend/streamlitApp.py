import streamlit as st
import requests
import json

def callAPI(name:str):
    base_url = st.secrets["RENDER_BACKEND_URL"]
    url = base_url + "/predict"
    payload = {"name": name}
    response = requests.request("POST", url, json=payload)
    return response.text

def fixed_footer():
    footer_style = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #ffffff;
        color: black;
        text-align: center;
        padding: 10px;
        z-index: 999; /* Ensures it stays on top of other elements */
    }
    </style>
    """
    st.markdown(footer_style, unsafe_allow_html=True)


    text_footer = """
        <div class="footer">
            <p>Do not use GenderMe for any kind of research or commercial purpose.</p>
            <p>App hosted on StreamLit, backend on Render.com.</p>
        </div>
    """

    st.markdown(
        text_footer,
        unsafe_allow_html=True
    )

st.title("GenderMe")

st.markdown("A little demo by Briefgarde. Check out the <a href='https://github.com/Briefgarde/genderme'>GitHub</a>", unsafe_allow_html=True)

name = None
with st.form(key='form'):
    
    name = st.text_input('Enter a surname:')
    submit = st.form_submit_button()

if submit:
    if not name or not name.strip():
        st.warning('Please enter a surname')
    else: 
        try:
            with st.spinner("Wait for it... (Backend is asleep, the cons of the free plan)", show_time=True):
                prediction = json.loads(callAPI(name)) 
            
            gender = prediction.get('gender')
            confidence = prediction.get('confidence')
            used_name = prediction.get('name')

            if gender and confidence:
                text = f"We think {used_name} is {str.lower(gender)} with {round(confidence*100, 2)}% confidence"
                st.write(text)
            else:
                st.error("API returned incomplete data.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
# st.subheader("Disclaimer")
# st.markdown("GenderMe is not a state of the art gender predictor. Based on my testing, it reaches around 85% accuracy, lower than the ~93% accuracy that professional apps like [Genderize](https://genderize.io/) or [Namsor](https://namsor.app/) can reach. Still, as a side project put together in a little more than a month, I believe it is capable. ")

fixed_footer()