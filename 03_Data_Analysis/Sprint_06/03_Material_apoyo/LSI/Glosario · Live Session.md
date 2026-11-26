# Glosario · Live Session

Al final de cada bloque tenéis enlaces para ampliar. Los de los bloques 01 y 02 son herramientas que se usan hoy en las empresas; los fundamentos que hay debajo los veréis con calma en el LAB.

## Inicio y bloque 01 · así se trabaja hoy · diapositivas 1–6

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 1 | Base de datos | Un sistema para guardar datos de forma organizada, que muchas personas y programas pueden consultar y modificar a la vez sin estropearlos. |
| 1 | LAB | La plataforma del curso con la teoría, los vídeos y los ejercicios de cada sprint. |
| 4 | Base de datos de la aplicación | La que guarda cada operación de una web o una app en el momento: un pedido, un alta, un pago. También se llama base de datos operacional. |
| 4 | PostgreSQL, MySQL, SQL Server, Oracle | Gestores de bases de datos relacionales. PostgreSQL es hoy el más usado por desarrolladores. |
| 4 | Ingesta | Copiar datos de su origen (la aplicación, una API, ficheros de un proveedor) al sitio donde se analizan. |
| 4 | Almacén de datos (data warehouse) | Una base de datos pensada para analizar millones de filas de toda la empresa. BigQuery, Snowflake, Databricks y Redshift son los más conocidos. |
| 4 | Transformación | Convertir los datos en bruto en tablas limpias y útiles para el negocio, normalmente con consultas SQL que se guardan y se repiten. |
| 4 | dbt | Una herramienta para escribir, versionar y ejecutar en orden esas consultas de transformación. |
| 4 | Dashboard | Un panel con gráficos y cifras que se actualiza solo. Power BI, Looker y Tableau son los más habituales. |
| 4 | Data engineer · analytics engineer | Quien construye las tuberías que mueven los datos · quien prepara las tablas limpias para analizar. |
| 5 | SQL | Structured Query Language: el lenguaje para consultar bases de datos relacionales. Es casi igual en todos los gestores. |
| 5 | Motor o gestor de base de datos | El programa que guarda los datos y ejecuta las consultas: SQLite, PostgreSQL, BigQuery, DuckDB… |
| 5 | SQLite | Una base de datos que cabe en un solo fichero, sin servidor. Es la del LAB. |
| 5 | SQLAlchemy · `create_engine` | La librería que conecta Python (y pandas) con casi cualquier base de datos · la función que crea esa conexión a partir de una dirección. |
| 5 | Cadena de conexión | La dirección de una base de datos con su tipo, usuario, clave, servidor y nombre: `postgresql+psycopg://usuario:clave@servidor/bd`. |
| 5 | BigQuery | El almacén de datos en la nube de Google. Se paga según los datos que lee cada consulta. |
| 5 | DuckDB | Una base de datos de análisis que funciona dentro de Python y consulta con SQL ficheros CSV y Parquet directamente. |
| 5 | Variable de entorno | Un valor guardado fuera del código, como una clave o una dirección. Se lee con `os.environ`. |
| 6 | Consulta (query) | Una instrucción en SQL que pide datos. |
| 6 | `JOIN` | Junta dos tablas emparejando filas por una columna común. Es el `merge` de pandas. |
| 6 | `SUM` · `GROUP BY` | Suma · agrupa las filas para calcular por grupo. |
| 6 | MCP | Model Context Protocol: un estándar para conectar asistentes de IA con herramientas y datos, por ejemplo una base de datos. |

Para ampliar: el [tutorial de SQL de W3Schools](https://www.w3schools.com/sql/), con ejemplos que se pueden ejecutar en el navegador, y la [documentación de DuckDB](https://duckdb.org/docs/), las dos en inglés.

## Bloque 02 · datos de fuera, hoy · diapositivas 7–9

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 7 | HTTP | El protocolo con el que se piden y se sirven las páginas web y las APIs. |
| 8 | API | Una puerta para pedir datos a otro programa o servicio. Suele responder en JSON. |
| 8 | API key | Una clave que os identifica ante una API. Es personal: no se comparte ni se sube a GitHub. |
| 8 | `requests` | La librería de Python para hacer peticiones a webs y APIs. |
| 8 | `requests.get` · `requests.post` | Pedir datos · enviar datos, por ejemplo una pregunta a un modelo de IA. |
| 8 | SDK | Una librería que da un proveedor para usar su API sin escribir las peticiones a mano. |
| 8 | Cabecera (header) | Información que viaja con la petición pero no en la URL, como la clave de acceso. |
| 8 | Error 429 | La respuesta de una API cuando se hacen demasiadas peticiones en poco tiempo. |
| 8 | Scraping | Sacar datos de una web leyendo su HTML. |
| 8 | Condiciones de uso | Las reglas que pone una web sobre lo que se puede hacer con su contenido. |
| 8 | RGPD | Reglamento General de Protección de Datos: la ley europea sobre datos personales. |
| 9 | HTML | El lenguaje en el que están escritas las páginas web: etiquetas que contienen otras etiquetas. |
| 9 | JavaScript | El lenguaje que se ejecuta en el navegador. Muchas webs lo usan para pedir sus datos después de cargar la página. |
| 9 | Web dinámica | Una web cuyo contenido no viene en el HTML inicial, sino que lo añade JavaScript. Con `requests` llega vacía. |
| 9 | Pestaña Red (Network) | La parte del inspector del navegador que muestra cada petición que hace la página, incluidos los JSON con sus datos. |
| 9 | Playwright | Una librería que controla un navegador real desde Python. Sirve para webs dinámicas. Selenium hace lo mismo. |
| 9 | Selector CSS | Una forma de señalar elementos de una página: `.producto` son los que tienen la clase «producto». |

Para ampliar: la [documentación de Requests](https://requests.readthedocs.io/en/latest/user/quickstart/) y la [de Playwright para Python](https://playwright.dev/python/docs/intro), las dos en inglés.

## Bloque 03 · lo que vais a aprender · diapositivas 10–13

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 11 | `sqlite3` | El módulo de Python para trabajar con SQLite. Viene instalado con Python. |
| 11 | `pd.read_sql` | Lanza una consulta SQL y devuelve el resultado como DataFrame. Funciona con SQLite y con cualquier base de datos conectada con SQLAlchemy. |
| 11 | `to_sql` | Guarda un DataFrame como tabla en una base de datos. |
| 11 | Pipeline | Una cadena de pasos automáticos (sacar, limpiar, cargar) que se ejecuta sola, por ejemplo cada noche. |
| 11 | BeautifulSoup | La librería que convierte el HTML en un árbol en el que se puede buscar. |
| 11 | JSON | Texto con claves y valores, listas y objetos anidados. Es el formato de las APIs y de las respuestas estructuradas de los LLM. |
| 11 | pydantic | Una librería que comprueba que unos datos tienen la forma esperada (campos y tipos) y da error si no. |
| 11 | Validar | Comprobar que algo cumple lo que se espera antes de usarlo. |
| 12 | API REST | Una API que se usa con direcciones web (endpoints) y los métodos de HTTP. Es el tipo más habitual. |
| 12 | `merge` | El método de pandas para juntar DataFrames por una clave, como un `JOIN`. |
| 13 | `RIGHT JOIN` · `FULL OUTER JOIN` | Se queda todo lo de la tabla de la derecha · todo lo de las dos tablas. SQLite los admite desde 2022. |
| 13 | `UNION ALL` | Pone el resultado de una consulta debajo del de otra, sin quitar repetidos. |
| 13 | Inyección SQL | Colar código SQL dentro de un dato para que la base de datos lo ejecute. Se evita con `?`. |
| 13 | f-string | Un texto de Python con valores dentro: `f"Hola {nombre}"`. No sirve para montar consultas SQL. |

Para ampliar: [Comparison with SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html), de la documentación de pandas, traduce cada consulta SQL a pandas. En inglés.

## Para cuando veáis los vídeos · diapositivas 14–27

| Diapositiva | Término | Qué es |
| --- | --- | --- |
| 15 | Base de datos relacional | Guarda la información en varias tablas relacionadas por claves. |
| 15 | Redundancia · normalizar | Guardar el mismo dato varias veces · repartir los datos en tablas para que cada dato se guarde una sola vez. |
| 15 | Clave primaria · clave foránea | La columna que identifica cada fila y no se repite · la columna que apunta a la clave primaria de otra tabla. |
| 16 | Chinook | La base de datos de ejemplo de los vídeos: una tienda de música online con 11 tablas. |
| 16 | Modelo de datos | El mapa de una base de datos: sus tablas, sus columnas y cómo se relacionan. |
| 16 | Tabla puente | Une otras dos cuando la relación es de muchos a muchos, como `playlist_track`. |
| 17 | Conexión · cursor | El enlace con la base de datos · el intermediario que envía consultas y recoge resultados. |
| 17 | `execute` · `fetchall` | Envía una consulta · recoge todas las filas que quedan. |
| 18 | `WHERE` | Qué filas queréis. Es la máscara de pandas. |
| 18 | `LIKE` y `%` | Busca por patrón: `'A%'` empieza por A. |
| 18 | `IS NULL` | Comprueba si el valor está vacío. Con `= NULL` no funciona. |
| 19 | `HAVING` | Filtra grupos después de agrupar. `WHERE` filtra filas antes. |
| 19 | `ORDER BY` · `LIMIT` · `DISTINCT` | Ordenar · cuántas filas como máximo · quitar repetidos. |
| 20 | `LEFT` · `INNER JOIN` | Se quedan todas las filas de la tabla de la izquierda · solo las que cruzan en las dos. |
| 20 | `NULL` | Un valor vacío en SQL. En pandas aparece como `NaN`. |
| 21 | `CREATE TABLE` · `INSERT` · `UPDATE` · `DELETE` | Crear una tabla · añadir filas · modificarlas · borrarlas. |
| 21 | `commit` | Guarda los cambios en la base de datos. |
| 22 | Endpoint · `params` | Cada dirección de una API · los parámetros de la petición, que `requests` añade a la URL. |
| 22 | Código de estado | El número con el que responde el servidor: 200 bien, 4xx error vuestro, 5xx error suyo. |
| 22 | `.env` · `.gitignore` | Un fichero con claves privadas · la lista de ficheros que Git no debe subir. |
| 23 | `find` · `find_all` | El primer elemento que encaja · todos los que encajan. |
| 23 | Atributo | Información dentro de la etiqueta: `href` en un enlace, `id` o `class` en un bloque. |
| 24 | `.string` · `.text` | El texto directo de una etiqueta · todo el texto de dentro. |
| 24 | Inspector del navegador | Clic derecho, «Inspeccionar»: el HTML de cualquier parte de una página. |
| 25 | `OperationalError` | El error de `sqlite3` cuando la consulta falla: tabla que no existe, SQL mal escrito… |
| 26 | Chuleta | Resumen de lo mínimo para consultar mientras practicáis. |

Para ampliar: [sqlite3](https://docs.python.org/3/library/sqlite3.html), de la documentación de Python; la [documentación de Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), y los [datos abiertos de la AEMET](https://opendata.aemet.es/).

## Fuentes

- [SQL Tutorial](https://www.w3schools.com/sql/), W3Schools
- [DuckDB documentation](https://duckdb.org/docs/)
- [Requests: Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Playwright for Python](https://playwright.dev/python/docs/intro)
- [Comparison with SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html), documentación de pandas
- [sqlite3](https://docs.python.org/3/library/sqlite3.html), documentación de Python
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [AEMET OpenData](https://opendata.aemet.es/)
- [Stack Overflow Developer Survey 2025 · Technology](https://survey.stackoverflow.co/2025/technology/)
