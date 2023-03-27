from typing import Union
import pickle
import numpy as np
import pandas as pd
import uvicorn
import asyncio
from fastapi import FastAPI

from main import CustomerChurn

app = FastAPI()

##load Model
model = pickle.load(open('rf_clf_smoteenn.pkl', 'rb'))

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict")
def predict(data:CustomerChurn):
     # Features
    CustomerChurn = data.dict()
    Churn = pd.DataFrame(CustomerChurn, index = [0])
    # predictions
    predictions = model.predict(Churn)

    proba = model.predict_proba(Churn)
    proba_nochurn = np.round((proba[0][0])*100, 2)
    proba_churn = np.round((proba[0][1])*100, 2)

    if predictions == 1:
        return {f"The probability that the customer leaves the company is {proba_churn} percent"}
    elif predictions == 0:
        return {f"The probability that the customer stays in the company is {proba_nochurn} percent"}
 
if __name__ == '__main__':
     uvicorn.run(app, host='127.0.0.1', port=8000)
 
 if __name__ == "__main__":
            config = uvicorn.Config(app)
            server = uvicorn.Server(config)
await server.serve()
   #uvicorn app:app --reload