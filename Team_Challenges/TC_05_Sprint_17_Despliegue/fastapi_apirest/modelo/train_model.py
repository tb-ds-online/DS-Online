"""Entrena un modelo mínimo de supervivencia del Titanic para la demo de despliegue."""
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

pwd = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(pwd, "titanic_train.csv"))

features = ["Pclass", "Sex", "Age", "Fare"]
X, y = df[features], df["Survived"]

preprocessing = ColumnTransformer([
    ("num", Pipeline([("imputar", SimpleImputer(strategy="median")), ("escalar", StandardScaler())]), ["Age", "Fare"]),
    ("cat", OneHotEncoder(drop="if_binary", handle_unknown="ignore"), ["Sex"]),
], remainder="passthrough")

pipeline = Pipeline([("preprocesado", preprocessing), ("modelo", RandomForestClassifier(random_state=42))])
pipeline.fit(X, y)

ruta_salida = os.path.join(pwd, "modelo_titanic.joblib")
joblib.dump(pipeline, ruta_salida)

print(f"Modelo guardado en: {ruta_salida}")
print("Ejemplo de predicción:", pipeline.predict(pd.DataFrame([{"Pclass": 1, "Sex": "female", "Age": 29, "Fare": 100}])))


