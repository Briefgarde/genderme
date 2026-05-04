import streamlit as st 
import json
import requests

def callAPI(name:str):
    base_url = st.secrets["RENDER_BACKEND_URL"]
    url = base_url + "/predict"
    payload = {"name": name}
    response = requests.request("POST", url, json=payload)
    return response.text


def predictor():
    name = None
    with st.form(key='form'):
        
        st.markdown(
            """
            <style>
            /* Target the container of the input */
            div[data-baseweb="input"] {
                background-color: #f0f0f0;
                border-radius: 5px;
            }
            
            /* Target the actual input field to ensure it inherits the color */
            input {
                background-color: #f0f0f0 !important;
                color: #333 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

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
                                        
                    if gender.lower() == 'female':
                        r = int(240 + (confidence * 16))
                        g = int(240 - (confidence * 58))
                        b = int(240 - (confidence * 47))
                    elif gender.lower() == 'male':
                        r = int(240 - (confidence * 64))
                        g = int(240 - (confidence * 16))
                        b = int(240 - (confidence * 10))
                    else:
                        r, g, b = 240, 240, 240

                    st.markdown(
                        f'<div style="background-color: rgb({r},{g},{b}); padding: 15px; border-radius: 10px; border: 1px solid rgba(0,0,0,0.05);">'
                        f'<span style="color: #333; font-weight: 500;">{text}</span>'
                        f'</div>', 
                        unsafe_allow_html=True
                    )                
                else:
                    st.error("API returned incomplete data.")
            except Exception as e:
                st.error(f"An error occurred: {e}")