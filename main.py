import uvicorn
from fastapi import FastAPI
from banknote import BankNote
import numpy as np
import pickle
import pandas as pd

app = FastAPI()

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)
@app.get('/')
def home():
    return {"message": "Welcome to home page"}

@app.get('/first_page')
def first_page(name: str):
    return {"message": f"Wecolme to first page:{name}"}

@app.post('/prediction')
def predict_note(data: BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction = classifier.predict([variance, skewness, curtosis, entropy])

    if prediction[0]>0.5:
        prediction = "Fake Note"
    else:
        prediction = "Banke Note"
    
    return prediction

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
