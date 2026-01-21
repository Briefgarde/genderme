from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from featureEngineering import getLastLetter, FeatureEngineering



# Define the data shape expected
class NameInput(BaseModel):
    name: str

app = FastAPI(title="Gender Inference API")

origins = [
    "http://localhost",       
    "http://localhost:8000",   
    "http://127.0.0.1:8000",  
    "https://YOUR_GITHUB_USERNAME.github.io", 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,     
    allow_methods=["*"],        
    allow_headers=["*"],       
)

MALE = 'Male'
FEMALE = 'Female'

def translatePredToGender(pred):
    p = pred[0]
    return MALE if p==0 else FEMALE


model = None
vectorizer = None

@app.on_event("startup")
def load_artifacts():
    global model, vectorizer
    import __main__
    setattr(__main__, "FeatureEngineering", FeatureEngineering)
    setattr(__main__, "getLastLetter", getLastLetter)
    model = joblib.load("modelWithPipeline.joblib")
    

@app.get("/")
def read_root():
    return {"message": "GenderMe Backend is running"}

@app.post("/predict")
def predict_gender(input_data: NameInput):
    if not input_data.name:
        raise HTTPException(status_code=400, detail="Name string is empty")
    
    clean_name = pd.DataFrame([input_data.name], columns=["firstName"])
    
    prediction = model.predict(clean_name)
    probability = model.predict_proba(clean_name)
    
    return {
        "name": input_data.name,
        "gender": translatePredToGender(prediction),
        "confidence": float(np.max(probability)) 
    }

if __name__ == "__main__":
    import uvicorn
    # This allows you to run 'python main.py' locally
    uvicorn.run(app, host="0.0.0.0", port=8000)