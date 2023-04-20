# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:37:04 2023

@author: shivs
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel #Formats of input
import pickle
import json

app = FastAPI()
origins=[*]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure : int
    SkinThickness : int
    Insulin :int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
    
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

@app.post('/diabetes_prediction') #endpoint
def diabetes_pred(input_parameters:model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    #Extracting all values.Here 'Pregnancies' is the key and dictonary[key] will give values
    preg  = input_dictionary['Pregnancies']
    glu  = input_dictionary['Glucose']
    bp  = input_dictionary['BloodPressure']
    skin  = input_dictionary['SkinThickness']
    insulin  = input_dictionary['Insulin']
    bmi  = input_dictionary['BMI']
    dpf  = input_dictionary['DiabetesPedigreeFunction']
    age  = input_dictionary['Age']
    
    
    
    
    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age]
    prediction = diabetes_model.predict([input_list]) #enclosing within a list we can avoid reshape
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    
    
    
    