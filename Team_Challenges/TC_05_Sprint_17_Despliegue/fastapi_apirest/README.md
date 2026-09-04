# Flask vs FastAPI — comparativa con salidas reales

Las dos apps de esta carpeta hacen exactamente lo mismo: sirven el mismo modelo
(`modelo/modelo_titanic.joblib`) con un endpoint `/predict`. Todo lo que ves aquí
abajo son respuestas **reales**, capturadas arrancando ambos servidores y
haciéndoles las mismas peticiones — no está inventado.

## Cómo probarlas vosotros mismos

```bash
# 1. Entrenar el modelo (una vez) — deja el .joblib en modelo/
cd modelo && python train_model.py && cd ..

# 2. Copiar el modelo dentro de cada app (cada una lleva su propia copia,
#    para que funcione igual en local que ya desplegada en Render)
cp modelo/modelo_titanic.joblib flask_app/
cp modelo/modelo_titanic.joblib fastapi_app/

# 3. Flask
cd flask_app && pip install -r requirements.txt && python app.py
# → http://127.0.0.1:5000

# 4. FastAPI (en otra terminal)
cd fastapi_app && pip install -r requirements.txt && uvicorn app:app --reload
# → http://127.0.0.1:8000
# → http://127.0.0.1:8000/docs  (documentación interactiva, gratis)
```

> 💡 **Por qué cada app lleva su propio `.joblib`, en vez de compartir el de `modelo/`**:
> cuando despliegues en Render normalmente solo subes la carpeta de la app concreta
> (`flask_app/` o `fastapi_app/`), no el repositorio entero. Si el código dependiera
> de una ruta como `../modelo/modelo_titanic.joblib`, funcionaría en tu ordenador pero
> **rompería en producción**, porque esa carpeta hermana no existiría en el entorno
> desplegado. Cada app debe poder valerse por sí misma con lo que hay dentro de su
> propia carpeta.

---

## La misma petición válida, en las dos

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" \
  -d '{"Pclass": 1, "Sex": "female", "Age": 29, "Fare": 100}'
```

| | Respuesta |
|---|---|
| **Flask** | `{"survived": 1, "probabilidad_supervivencia": 1.0}` |
| **FastAPI** | `{"survived": 1, "probabilidad_supervivencia": 1.0}` |

Idéntica — para el caso feliz, da igual cuál uséis.

---

## Donde de verdad se nota la diferencia: datos mal formados

### Caso 1 — Falta un campo (`Age`)

**Flask** — hay que haber escrito a mano la comprobación de campos faltantes:
```json
{"error": "Faltan campos: ['Age']"}
```
HTTP 400 (código que también hay que poner a mano).

**FastAPI** — nadie escribió código para este caso, lo genera Pydantic solo:
```json
{"detail":[{"type":"missing","loc":["body","Age"],"msg":"Field required","input":{"Pclass":1,"Sex":"female","Fare":100}}]}
```
HTTP 422 automático, y encima te dice **exactamente qué campo falta y dónde** (`loc`).

### Caso 2 — Valor de `Sex` inválido (`"otro"` en vez de `"male"`/`"female"`)

**Flask**:
```json
{"error": "Sex debe ser 'male' o 'female'"}
```

**FastAPI**:
```json
{"detail":[{"type":"literal_error","loc":["body","Sex"],"msg":"Input should be 'male' or 'female'","input":"otro","ctx":{"expected":"'male' or 'female'"}}]}
```

### Caso 3 — `Age` como texto (`"treinta"` en vez de un número)

**Flask** — hay que capturar la excepción de conversión a mano:
```json
{"error": "Pclass, Age y Fare deben ser numéricos"}
```

**FastAPI**:
```json
{"detail":[{"type":"float_parsing","loc":["body","Age"],"msg":"Input should be a valid number, unable to parse string as a number","input":"treinta"}]}
```

### Caso 4 — `Pclass` fuera de rango (4, cuando solo existen 1/2/3)

**Flask**:
```json
{"error": "Pclass debe ser 1, 2 o 3"}
```

**FastAPI**:
```json
{"detail":[{"type":"literal_error","loc":["body","Pclass"],"msg":"Input should be 1, 2 or 3","input":4,"ctx":{"expected":"1, 2 or 3"}}]}
```

---

## Lo que esto demuestra, en números

| | Flask | FastAPI |
|---|---|---|
| Líneas de código de validación escritas a mano | ~15 | **0** |
| Campos con validación de tipo real (no solo "existe") | 0 | 4 de 4 |
| `/docs` con interfaz interactiva | No existe, hay que montarlo aparte | **Sí, gratis**, en `/docs` |
| Esquema OpenAPI (`/openapi.json`) | No existe | Se genera solo |
| Código del endpoint `/predict` | 20 líneas | **9 líneas** |

El código de validación de Flask (comprobar que existan los campos, que `Sex`
sea uno de dos valores, intentar convertir a número y capturar la excepción,
comprobar el rango de `Pclass`...) **desaparece entero en FastAPI** — se
sustituye por la definición de la clase `Pasajero` una sola vez, y Pydantic se
encarga del resto en cada petición.

## Lo que Flask hace mejor aquí

- Menos que aprender: no hace falta entender type hints, Pydantic ni `async`
- Un archivo menos (no hace falta declarar el modelo de respuesta aparte)
- Si el equipo ya lo conoce de los talleres en vivo, hay menos fricción para
  llegar a tener algo desplegado dentro del tiempo del challenge

## La conclusión que os pedimos que saquéis vosotros

Ninguna opción es "la correcta" — la tabla del enunciado ya lo decía. Lo que
esta comparación debería dejar claro es **por qué** cada ventaja existe, no
solo que existe: FastAPI no es "mejor", es que mueve el trabajo de validación
del código de cada endpoint a una definición declarativa que se escribe una
vez y se aplica siempre. Esa es la decisión real que estáis tomando al elegir
uno u otro.
