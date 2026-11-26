# Glosario · Ficheros para la IA

Los términos de la sesión, ordenados por bloque y diapositiva y explicados en una o dos frases. Al final tenéis enlaces para ampliar.


## Inicio y bloque 01 · diapositivas 1–4

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 4 | Separador y decimal | En España, Excel exporta los CSV con `;` entre columnas porque la coma se usa para los decimales. pandas, por defecto, espera lo contrario. |
| 4 | API | Un servicio al que un programa le pide datos y que responde, casi siempre, en JSON. |
| 4 | Respuesta estructurada de un LLM | Cuando se le pide a un LLM que conteste con un JSON con campos fijos, para poder usar la respuesta desde código. |
| 4 | Batch API | Una forma de mandar a un LLM muchas peticiones de golpe en un fichero, más barata que hacerlo una a una. En OpenAI, ese fichero es un `.jsonl`. |
| 4 | Fine-tuning | Reentrenar un modelo con ejemplos propios para ajustarlo a una tarea. Los ejemplos se entregan en un `.jsonl`. |
| 4 | Hugging Face | La plataforma donde se publican modelos y datasets de IA. Convierte muchos datasets a Parquet, y se pueden consultar con DuckDB. |
| 4 | Logs | El registro de lo que hace un sistema: cada pregunta al chatbot, su respuesta, cuánto tardó. Crecen muy rápido. |

## Bloque 02 · formatos · diapositivas 5–8

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 6 | CSV | Comma-separated values: texto plano, una fila por línea y un separador entre columnas. No guarda tipos. |
| 6 | JSON | Texto con pares clave-valor, que admite listas y objetos dentro de otros. Es el formato de las APIs. |
| 6 | JSONL | JSON Lines: un objeto JSON por línea. Se lee con `pd.read_json(..., lines=True)`. |
| 6 | Parquet | Formato binario que guarda los datos por columnas, con su tipo y comprimidos. pandas necesita `pyarrow` para usarlo. |
| 6 | Binario | Un fichero que no está pensado para leerse como texto. Si se abre con un editor, se ven símbolos sin sentido. |
| 6 | Esquema | La lista de columnas de un fichero con el tipo de cada una. Parquet lo guarda; CSV no. |
| 6 | `large_string` | Cómo llama `pyarrow` al texto dentro de un Parquet. Al leerlo, pandas lo convierte en `str`. |
| 6 | Inferencia de tipos | Lo que hace `read_csv`: mira los valores y adivina si son números, texto o booleanos. Con `1.10` adivina número y lo deja en `1.1`. |
| 7 | Almacenamiento por columnas | Guardar juntos todos los valores de una columna, en vez de fila a fila. Comprime mejor y deja leer solo las columnas que se piden. |
| 7 | Compresión | Guardar los datos ocupando menos. Una columna con pocos valores distintos se comprime muchísimo. |
| 7 | Leer solo unas columnas | `pd.read_parquet(f, columns=[...])`. En CSV existe `usecols`, pero el fichero se recorre entero igualmente. |
| 8 | Excel y `openpyxl` | `pd.read_excel` necesita la librería `openpyxl` para los `.xlsx`. Con `sheet_name` se elige la hoja. |
| 8 | `pyarrow` | La librería que usa pandas para leer y escribir Parquet. Se instala aparte: `uv add pyarrow`. |
| 8 | Data lake | Un almacén donde una empresa guarda grandes cantidades de ficheros, casi siempre en Parquet, para analizarlos después. |

## Bloque 03 · demo en el notebook · diapositivas 9–12

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 10 | Prompt | La instrucción que se le da al modelo. En la demo, el equipo lo va cambiando y numera cada versión. |
| 10 | Versión del prompt | Un nombre para cada cambio del prompt: `1.1`, `1.2`, `1.10`. Es texto, no un número: la `1.10` va después de la `1.9`, no es igual que la `1.1`. |
| 10 | Tasa de acierto | El porcentaje de respuestas correctas. Como `correcta` vale 1 o 0, es la media de la columna. |
| 10 | Tokens | Los trozos de texto que procesa un LLM. Se paga por token, así que un prompt más corto sale más barato. |
| 10 | `json.loads` | Convierte una línea de texto JSON en un diccionario de Python. Con un JSONL se usa una vez por línea. |
| 10 | `pd.json_normalize` | Aplana un JSON anidado: cada campo de dentro pasa a ser una columna. Con `sep="_"` los nombres quedan como `respuesta_version_prompt`. |
| 10 | `with open(...) as f` | Abre un fichero y lo cierra solo al terminar el bloque. `encoding="utf-8"` evita problemas con tildes y eñes. |
| 10 | `merge` | Junta dos tablas por una columna común, aquí `id_conversacion`. Lo vieron con pandas. |
| 10 | `how="left"` | Conserva todas las filas de la tabla de la izquierda, aunque no encuentren pareja en la otra. Las que no la encuentran quedan con huecos. |
| 11 | SQL | El lenguaje para hacer preguntas a tablas. Se lee casi como una frase en inglés. |
| 11 | DuckDB | Una base de datos que funciona dentro de Python, sin servidor. Lanza SQL directamente sobre ficheros CSV, Parquet o sobre DataFrames. |
| 11 | `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY` | Qué columnas, de dónde, qué filas, por qué agrupar y cómo ordenar. Cada una tiene su equivalente en pandas en la tabla de la diapositiva. |
| 11 | `AS` | Pone un nombre nuevo a una columna del resultado: `avg(correcta) AS acierto`. |
| 11 | `duckdb.sql(...).df()` | Lanza la consulta y devuelve el resultado como un DataFrame de pandas. |
| 11 | Comillas simples y dobles | En SQL, los textos y los ficheros van con comillas simples (`'Pagos'`). Las dobles son para nombres de columna: por eso `"Pagos"` da error. |
| 11 | Replacement scan | Lo que permite escribir `FROM datos` con un DataFrame: DuckDB busca una variable con ese nombre en el notebook. |
| 12 | Error silencioso | Un fallo que no da error y produce un resultado falso. Es el más peligroso, porque nadie lo revisa. |

## Bloque 04 · para practicar · diapositivas 13–14

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 14 | `pd.read_excel` | Lee un `.xlsx`. Con `engine="openpyxl"` se evita el aviso de pandas 3 sobre el motor que usará en el futuro. |
| 14 | Coste frente a calidad | La decisión típica al poner un LLM en producción: un prompt más corto gasta menos tokens, pero puede acertar menos. |
| 14 | Tamaño de muestra | Cuántos datos sostienen un número. Con unas 80 conversaciones por versión, una diferencia pequeña puede ser casualidad. |

## Para repasar · diapositivas 15–18

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 16 | `encoding` | Cómo se guardan las letras en un fichero. Casi todo es `utf-8`; los Excel antiguos de Windows suelen ser `latin-1`. |
| 17 | `UnicodeDecodeError` | Error al leer un fichero con una codificación distinta de la que se esperaba. Se arregla con `encoding="latin-1"`. |
| 17 | Ruta relativa | Una ruta que se cuenta desde la carpeta del notebook. `Path.cwd()` dice cuál es. |
| 17 | `Binder Error` | El error de DuckDB cuando no encuentra una columna. Casi siempre es una errata o unas comillas dobles donde iban simples. |

## Fuentes

- pandas, guía de lectura y escritura de ficheros: https://pandas.pydata.org/docs/user_guide/io.html
- DuckDB, documentación: https://duckdb.org/docs/
- DuckDB y Hugging Face, consultas con `hf://`: https://huggingface.co/docs/hub/en/datasets-duckdb
- Hugging Face, conversión automática de datasets a Parquet: https://huggingface.co/blog/sql-console
- OpenAI, Batch API (fichero `.jsonl`): https://developers.openai.com/api/docs/guides/batch

