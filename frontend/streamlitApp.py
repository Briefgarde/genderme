import streamlit as st
import requests
import json

def callAPI(name:str):
    import requests

    url = "http://127.0.0.1:8000/predict"

    payload = {"name": name}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "insomnia/12.2.0"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

st.title("GenderMe")

name = None
with st.form(key='form'):
    
    name = st.text_input('Enter a surname:')
    submit = st.form_submit_button()

if submit:
    if not name or not name.strip():
        st.warning('Please enter a surname')
    else: 
        try:
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
            

st.write("Do not use GenderMe for any kind of research or commercial use case", )