# Glosario · Live Session V

Los términos de la sesión, ordenados por bloque y diapositiva y explicados en una o dos frases. Al final de cada bloque tenéis enlaces para ampliar. Muchos los veréis con calma en los vídeos del sprint: aquí basta con reconocerlos.

## Inicio y bloque 01 · antes de analizar · diapositivas 1–5

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 1 | Datos limpios | Datos con el tipo correcto, sin duplicados, escritos siempre igual y con los huecos tratados. Es el punto de partida para analizar o entrenar un modelo. |
| 2 | Formato de fichero | La forma en que se guardan los datos en disco: CSV, Excel, JSON, XML, Parquet… Cada uno se lee de una manera. |
| 4 | Hipótesis | La pregunta que queremos responder con los datos. Marca qué datos hacen falta y qué análisis tiene sentido. |
| 4 | EDA | Exploratory Data Analysis: el análisis exploratorio. Mirar los datos (tipos, valores, huecos, relaciones) antes de sacar conclusiones o entrenar un modelo. |
| 4 | ETL | Extract, Transform, Load: sacar los datos de donde estén, limpiarlos y transformarlos, y guardarlos listos para usar. |
| 4 | Extract | Obtener los datos: de ficheros, bases de datos, APIs o webs. |
| 4 | Transform | Corregir tipos, limpiar textos, tratar huecos y crear columnas nuevas. |
| 4 | Load | Guardar el resultado: un CSV limpio, un Parquet o una tabla en una base de datos. |
| 4 | API | Una puerta para pedir datos a otro programa o servicio por internet. Suele responder en JSON. |
| 5 | Datos estructurados | Filas y columnas con un esquema fijo, como un CSV o una tabla de una base de datos. |
| 5 | Datos semiestructurados | Datos con etiquetas o claves que separan cada valor, pero sin forma de tabla fija, como un JSON o un XML. |
| 5 | Datos desestructurados | Texto libre, imágenes, audio o vídeo. Hay que procesarlos antes de poder analizarlos. |
| 5 | Variable categórica | Una columna con pocos valores posibles que funcionan como etiquetas: compañía, país, tipo de avión. |
| 5 | Cardinalidad | En el curso, el porcentaje de valores distintos de una columna: `df["col"].nunique() / len(df) * 100`. Si es baja, la columna suele ser categórica. |
| 5 | OCR | Optical Character Recognition: sacar el texto de una imagen, como la foto de un ticket. |

Para ampliar: [Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html), de la documentación de pandas, en inglés. Incluye `dtypes`, `nunique` y `value_counts`.

## Bloque 02 · limpiar y transformar · diapositivas 6–9

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 7 | `dtypes` | El tipo de cada columna. Si una columna de números sale como `str`, todavía no se puede operar con ella. |
| 7 | `str` | El tipo de las columnas de texto en pandas 3. En los vídeos aparece como `object`. |
| 7 | `.str` | La puerta a los métodos de texto de pandas: se aplican a todos los valores de la columna a la vez, como `df["Destino"].str.strip()`. |
| 7 | `strip` | Quita los espacios del principio y del final. `" ginebra"` y `"ginebra"` son valores distintos hasta que se quitan. |
| 7 | `title` | Pone en mayúscula la primera letra de cada palabra: `"nueva york"` → `"Nueva York"`. |
| 7 | `astype` | Cambia el tipo de una columna, por ejemplo de texto a `float`. Falla si algún valor no se puede convertir. |
| 7 | `pd.to_datetime` | Convierte texto en fecha. Con `format=` le decís cómo está escrita y no tiene que adivinarlo. |
| 7 | `datetime64` | El tipo de fecha de pandas. Permite filtrar por mes, ordenar en el tiempo o calcular diferencias. |
| 7 | `.dt` | La puerta a las partes de una fecha: `.dt.hour`, `.dt.month`, `.dt.day_of_week`. |
| 7 | `contains` | Comprueba si cada texto contiene algo. Con `case=False` no distingue mayúsculas y minúsculas. |
| 7 | `~` | Invierte una máscara: los `True` pasan a `False` y al revés. |
| 7 | `fillna` | Rellena los huecos con un valor o con otra Series. |
| 7 | `transform("mean")` | Calcula la media de cada grupo y la devuelve en cada fila de ese grupo. Sirve para rellenar con la media de los vuelos parecidos. |
| 8 | Expresión regular (regex) | Un patrón que describe la forma de un texto, como «uno o más dígitos seguidos de "rojas"». Sirve para buscar, extraer o sustituir. |
| 8 | `str.extract` | Aplica una expresión regular a cada valor y devuelve lo que hay entre paréntesis. Si no encuentra nada, deja `NaN`. |
| 8 | LLM | Large Language Model: un modelo de lenguaje como ChatGPT o Claude. |
| 8 | Determinista | Que con la misma entrada da siempre la misma salida. Una regex lo es; un LLM, no siempre. |
| 9 | Nulo, hueco o missing | Un dato que falta. pandas lo muestra como `NaN`. |
| 9 | `dropna` | Quita las filas con huecos. Con `subset=` solo mira esas columnas. |
| 9 | Imputar | Rellenar un hueco con un valor estimado, como la media. El dato rellenado no es real. |
| 9 | Variable indicadora | Una columna `True`/`False` que apunta qué filas tenían un hueco antes de rellenarlo. |

Para ampliar: [Working with text data](https://pandas.pydata.org/docs/user_guide/text.html) y [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html), de la documentación de pandas, y [regex101](https://regex101.com/) para probar expresiones regulares (elegid *Python* en *Flavor*).

## Bloque 03 · ficheros · diapositivas 10–12

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 11 | CSV | Comma-Separated Values: texto plano con una fila por línea y los valores separados por comas, punto y coma u otro carácter. |
| 11 | Separador (`sep`) | El carácter que separa las columnas en un CSV. Si no es la coma, hay que decírselo a `read_csv`. |
| 11 | `decimal` | El carácter de los decimales. En España suele ser la coma: `decimal=","`. |
| 11 | Excel (`.xlsx`) | El formato de las hojas de cálculo de Excel: varias hojas, formato y fórmulas en un fichero. pandas lo lee con `read_excel`. |
| 11 | `openpyxl` | La librería que usa pandas para leer y escribir ficheros `.xlsx`. Hay que instalarla aparte. |
| 11 | JSON | JavaScript Object Notation: texto con claves y valores, listas y objetos unos dentro de otros. Es el formato habitual de las APIs. |
| 11 | Anidado | Un dato dentro de otro: un diccionario dentro de un diccionario o una lista dentro de un registro. |
| 11 | `json.loads` | Convierte un texto con JSON en diccionarios y listas de Python. `json.load` hace lo mismo leyendo un fichero. |
| 11 | `pd.json_normalize` | Convierte JSON anidado en una tabla y aplana los diccionarios internos en columnas como `destino.ciudad`. |
| 11 | JSON Lines (`.jsonl`) | Un objeto JSON por línea. Se lee con `pd.read_json(ruta, lines=True)`. |
| 11 | XML | eXtensible Markup Language: datos entre etiquetas, organizados en forma de árbol. |
| 11 | Parquet | Un formato que guarda la tabla por columnas, comprimida y con los tipos. Es binario: no se abre con un editor de texto. |
| 11 | Almacén de datos | El sistema donde una empresa guarda grandes volúmenes de datos para analizarlos. Se suele llamar data warehouse o data lake. |
| 12 | `pd.read_xml` | Lee un XML sencillo directamente como DataFrame. |
| 12 | `JSONDecodeError` | El error de Python cuando el texto no es JSON válido, por ejemplo si un LLM añade una frase antes del JSON. |
| 12 | Salida estructurada | Una opción de las APIs de LLM para que la respuesta sea siempre JSON válido con los campos que pedís. |

Para ampliar: [IO tools](https://pandas.pydata.org/docs/user_guide/io.html), de la documentación de pandas: todos los formatos que lee y escribe, con sus parámetros.

## Bloque 04 · el sprint · diapositivas 13–15

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 14 | Binning | Convertir un número en tramos, como «baja», «media» y «alta». Lo veréis en el vídeo de números. |
| 14 | `open` | La función de Python para abrir un fichero y leerlo o escribirlo como texto. |
| 14 | Ruta (path) | El camino hasta un fichero. Relativa (`./data/ventas.xlsx`) si parte de donde está el notebook; absoluta si empieza en la raíz del disco. |
| 14 | Spam | Correo no deseado. En la práctica, cada correo trae un veredicto de si lo es y con qué confianza. |
| 15 | pandas 3 | La versión de enero de 2026. Los vídeos se grabaron con una anterior, por eso algunas salidas no coinciden. |
| 15 | NumPy 2 | La versión de NumPy que ha eliminado `np.NaN`. Se escribe `np.nan`. |
| 15 | `AttributeError` | El error que da Python cuando pedís algo que no existe en un objeto o una librería, como `np.NaN`. |
| 15 | `total_seconds` | La duración entera de una diferencia de tiempo en segundos, contando los días. |
| 15 | regex101 | Una web para probar expresiones regulares paso a paso con vuestros propios textos. |

## Para cuando veáis los vídeos · diapositivas 16–25

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 17 | `re` | El módulo de Python para expresiones regulares. |
| 17 | `re.findall` | Devuelve una lista con todo lo que encaja con el patrón. Si el patrón tiene paréntesis, solo lo de dentro. |
| 17 | `\d`, `\s`, `\w` | Un dígito; un espacio, tabulador o salto de línea; una letra, un dígito o `_`. |
| 17 | `{4}`, `+`, `?` | Exactamente 4 veces; 1 o más; 0 o 1. |
| 17 | `[A-Z]` | Cualquier mayúscula de la A a la Z, sin tildes ni ñ. |
| 17 | Grupo `( )` | La parte del patrón que queréis sacar. |
| 17 | Escapar | Poner `\` delante de un carácter especial para buscarlo tal cual: `\$`, `\.`. |
| 18 | `strftime` / `strptime` | Pasar de fecha a texto / de texto a fecha, con un patrón como `"%Y-%m-%d %H:%M"`. |
| 18 | `%Y`, `%m`, `%d`, `%H`, `%M` | Año, mes, día, hora y minutos en el patrón de una fecha. |
| 18 | `timedelta` | Una duración: la diferencia entre dos fechas o lo que se suma a una fecha. |
| 19 | `pd.cut` | Hace tramos con los cortes que elegís vosotros. |
| 19 | `pd.qcut` | Hace tramos con el mismo número de filas en cada uno. |
| 19 | `np.inf` | Infinito. Sirve como último corte para que el tramo superior no tenga techo. |
| 20 | MCAR | Missing Completely At Random: el dato falta por accidente, sin relación con nada. |
| 20 | MAR | Missing At Random: falta más en unos grupos que en otros, y eso se ve en otra columna. |
| 20 | MNAR | Missing Not At Random: falta por el propio valor que no vemos, como el sueldo de quien gana mucho. |
| 20 | Sesgo | Un error sistemático: los datos o el modelo se desvían siempre hacia el mismo lado. |
| 21 | `encoding` | Cómo están guardados los caracteres en el fichero. Si salen errores con tildes o eñes, probad `encoding="latin-1"`. |
| 21 | `header` · `names` | En qué fila están los nombres de columna (`None` si no hay) · qué nombres poner. |
| 21 | `sheet_name` | Qué hoja del Excel leer. Con `None` lee todas y devuelve un diccionario. |
| 21 | `usecols` · `skiprows` | Qué columnas leer · qué filas saltarse. |
| 21 | `index=False` | Al guardar con `to_csv` o `to_excel`, no escribe el índice como columna. |
| 21 | `uv add` | El comando para añadir una librería a vuestro proyecto con uv. |
| 22 | `with open(...) as f` | Abre un fichero y lo cierra solo al terminar el bloque. |
| 22 | `json.dump` | Guarda diccionarios o listas en un fichero JSON. Con `ensure_ascii=False` las tildes se guardan tal cual. |
| 23 | ElementTree (`ET`) | La librería de Python para leer XML como un árbol. |
| 23 | Raíz | El nodo de arriba del todo de un XML, del que cuelga todo lo demás. |
| 23 | `.tag`, `.attrib`, `.text` | El nombre de la etiqueta, sus atributos y el texto que tiene dentro. |
| 23 | `.find` · `.findall` | El primer hijo · todos los hijos con una etiqueta. |
| 23 | `lxml` | Una librería para procesar XML que `pd.read_xml` usa por defecto. |
| 24 | `FileNotFoundError` | La ruta no lleva a ningún fichero. |
| 24 | `os.getcwd()` · `os.listdir()` | La carpeta desde la que se ejecuta el notebook · los ficheros que hay en una carpeta. |
| 24 | `UnicodeDecodeError` | El fichero no está guardado en la codificación que espera Python. |
| 25 | Chuleta | Resumen de lo mínimo para consultar mientras practicáis. |

Para ampliar: [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html) de pandas, [re](https://docs.python.org/3/library/re.html), [json](https://docs.python.org/3/library/json.html) y [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) de la documentación de Python, y la [guía de lectura y escritura de ficheros de Real Python](https://realpython.com/read-write-files-python/), todas en inglés.

## Fuentes

- [Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html), documentación de pandas
- [Working with text data](https://pandas.pydata.org/docs/user_guide/text.html), documentación de pandas
- [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html), documentación de pandas
- [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html), documentación de pandas
- [IO tools](https://pandas.pydata.org/docs/user_guide/io.html), documentación de pandas
- [re](https://docs.python.org/3/library/re.html), [json](https://docs.python.org/3/library/json.html) y [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html), documentación de Python
- [regex101](https://regex101.com/)
- [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/), Real Python
