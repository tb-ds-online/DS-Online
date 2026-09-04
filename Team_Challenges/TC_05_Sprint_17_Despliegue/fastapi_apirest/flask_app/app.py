"""
API REST con Flask — predicción de supervivencia del Titanic.
"""
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

pwd = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
modelo = joblib.load(os.path.join(pwd, "modelo_titanic.joblib"))


@app.route("/")
def home():
    return jsonify({
        "mensaje": "API de predicción de supervivencia del Titanic",
        "endpoints": {
            "/predict": "POST con JSON {Pclass, Sex, Age, Fare} -> devuelve la predicción",
            "/predict_get": "GET con query string ?Pclass=1&Sex=female&Age=29&Fare=100 -> devuelve la predicción",
        },
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    return _predecir(data)


@app.route("/predict_get", methods=["GET"])
def predict_get():
    # En un GET no hay body de JSON — los datos van en la query string:
    # /predict_get?Pclass=1&Sex=female&Age=29&Fare=100
    # request.args es un diccionario de solo lectura con esos parámetros.
    data = {
        "Pclass": request.args.get("Pclass"),
        "Sex": request.args.get("Sex"),
        "Age": request.args.get("Age"),
        "Fare": request.args.get("Fare"),
    }
    return _predecir(data)


def _predecir(data):
    # Validación manual: hay que comprobar cada campo a mano
    campos_requeridos = ["Pclass", "Sex", "Age", "Fare"]
    faltantes = [c for c in campos_requeridos if not (data or {}).get(c)]
    if faltantes:
        return jsonify({"error": f"Faltan campos: {faltantes}"}), 400

    if data["Sex"] not in ("male", "female"):
        return jsonify({"error": "Sex debe ser 'male' o 'female'"}), 400

    try:
        pclass = int(data["Pclass"])
        age = float(data["Age"])
        fare = float(data["Fare"])
    except (ValueError, TypeError):
        return jsonify({"error": "Pclass, Age y Fare deben ser numéricos"}), 400

    if pclass not in (1, 2, 3):
        return jsonify({"error": "Pclass debe ser 1, 2 o 3"}), 400

    X = pd.DataFrame([{"Pclass": pclass, "Sex": data["Sex"], "Age": age, "Fare": fare}])
    prediccion = int(modelo.predict(X)[0])
    probabilidad = float(modelo.predict_proba(X)[0][1])

    return jsonify({"survived": prediccion, "probabilidad_supervivencia": round(probabilidad, 3)})


if __name__ == "__main__":
    app.run(port=5000, debug=False)
