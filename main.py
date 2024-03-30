from fastapi import FastAPI, HTTPException
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import pymongo
from pydantic import BaseModel 
import numpy as np 

client = pymongo.MongoClient("mongodb+srv://namannanda0:smRf09oaMBDvJoxJ@cluster0.v5adu7w.mongodb.net/")
db = client["Heart_info"]  
collection = db["save"]
model = load("./heart.joblib")

class InputData(BaseModel):
     name: str
     age: str
     sex: str
     cp: str
     bp: str
     choles: str
     fbp: str
     recg: str
     mhr: str
     eia: str
     oldpeak: str
     slope: str
     major_vessels: str
     thal: str

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods="*",
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_numbers(input_data: InputData):
    lst = []
    lst.append(int(input_data.age))
    if input_data.sex =="Male":
        input_data.sex = 1
    else:
        input_data.sex = 0
    lst.append(input_data.sex)
    if input_data.cp =="No Pain":
        input_data.cp = 0
    elif input_data.cp =="Low Pain":
        input_data.cp = 1
    elif input_data.cp =="Medium Pain":
        input_data.cp = 2
    else: input_data.cp = 3
    lst.append(input_data.cp)
    lst.append(int(input_data.bp))
    lst.append(int(input_data.choles))
    if input_data.fbp =="More Than 120":
        input_data.fbp = 1
    else:
        input_data.fbp = 0
    lst.append(input_data.fbp)
    lst.append(int(input_data.recg))
    lst.append(int(input_data.mhr))
    if input_data.eia =="Yes":
        input_data.eia = 1
    else:
        input_data.eia = 0
    lst.append(input_data.eia)
    lst.append(int(input_data.oldpeak))
    lst.append(float(input_data.slope))
    lst.append(int(input_data.major_vessels))
    if input_data.thal =="Normal":
        input_data.thal = 1
    elif input_data.thal =="Fixed Defect":
        input_data.thal = 2
    else :
        input_data.thal = 3
    lst.append(input_data.thal)
    
    prediction = model.predict([lst])
    if int(prediction) == 1:
        prediction = "possible heart disease predicted"
    else: 
        prediction = "No heart Disease predicted"
    document = {
        "Patient_name": input_data.name,
        "patient_info": input_data.dict(),
        "prediction": prediction
    }
    collection.insert_one(document)

    return {"name": input_data.name,
            "prediction": prediction}

    
    

    

