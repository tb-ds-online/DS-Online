"""
API REST con FastAPI — predicción de supervivencia del Titanic.
"""
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from typing import Literal
import joblib
import pandas as pd
import os

pwd = os.path.dirname(os.path.abspath(__file__))
app = FastAPI(title="API de predicción de supervivencia del Titanic")
modelo = joblib.load(os.path.join(pwd, "modelo_titanic.joblib"))


class Pasajero(BaseModel):
    Pclass: int = Field(ge=1, le=3, description="Clase del billete: 1, 2 o 3")
    Sex: Literal["male", "female"]
    Age: float = Field(gt=0, le=120, description="Edad en años")
    Fare: float = Field(ge=0, description="Tarifa pagada")


class Prediccion(BaseModel):
    survived: int
    probabilidad_supervivencia: float


@app.get("/")
def home():
    return {
        "mensaje": "API de predicción de supervivencia del Titanic",
        "endpoints": {
            "/predict": "POST con JSON en el body --- devuelve la predicción",
            "/predict_get": "GET con query string ?Pclass=1&Sex=female&Age=29&Fare=100 --- devuelve la predicción",
            "/docs": "documentación interactiva",
        },
    }


@app.post("/predict", response_model=Prediccion)
def predict(pasajero: Pasajero):
    X = pd.DataFrame([pasajero.model_dump()])
    prediccion = int(modelo.predict(X)[0])
    probabilidad = float(modelo.predict_proba(X)[0][1])
    return Prediccion(survived=prediccion, probabilidad_supervivencia=round(probabilidad, 3))


@app.get("/predict_get", response_model=Prediccion)
def predict_get(pasajero: Pasajero = Depends()):
    X = pd.DataFrame([pasajero.model_dump()])
    prediccion = int(modelo.predict(X)[0])
    probabilidad = float(modelo.predict_proba(X)[0][1])
    return Prediccion(survived=prediccion, probabilidad_supervivencia=round(probabilidad, 3))

