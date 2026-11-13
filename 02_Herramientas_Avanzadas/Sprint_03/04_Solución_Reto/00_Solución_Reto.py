# Bridge SA · Product — el cuestionario de satisfaccion de la cohorte de enero
#
# Ya tienes cargado (numpy esta importado como np):
#   RESPUESTAS_CSV   el volcado del formulario: email;p01;...;p40, separador ";"
#   REGISTRO         el registro de cohortes: lista de dicts con nombre, email,
#                    programa y cohorte
#   PREGUNTAS        los 40 identificadores en orden: ["p01", ..., "p40"]
#   BLOQUES          {"Contenido": [10 preguntas], "Docencia": [...], ...}
#   ORIGEN_REGISTRO  de donde sale el registro (para el artefacto, no lo cambies)
#
# Deja preparado esto, con estos nombres exactos:
#   M                 matriz (respuestas de la cohorte x 40), float, NaN en los huecos
#   emails            un correo por fila de M, en el mismo orden
#   medias_pregunta   (40,)   la media de cada pregunta
#   medias_por_bloque(X)      funcion: de una matriz (n, 40) a una (n, 4)
#   normalizar(X)             funcion: de una matriz (n, 40) a su z-score POR PREGUNTA
#   bloques           (n, 4)  = medias_por_bloque(M)
#   medias_bloque     (4,)    la media de cada columna de bloques
#   Z                 (n, 40) = normalizar(M)
#   peor_pregunta     int, indice (base 0) de la pregunta con la media mas baja
#   peor_bloque       str, el nombre del bloque con la media mas baja
#   artefacto         el paquete que se llevan el Sprint 09 y el Sprint 14
#
# Cuatro avisos que valen puntos:
#   · Ni un bucle de Python dentro de las dos funciones. Leer el CSV puede
#     llevarlos; el calculo, no. Lo comprobamos sobre el bytecode, asi que una
#     comprension de lista tambien cuenta como bucle.
#   · En el volcado hay celdas vacias. Un hueco NO es un cero.
#   · Hay una pregunta que ha contestado todo el mundo igual: su desviacion es 0.
#   · En el volcado hay correos que no estan en el registro de cohortes.

# import io

# crudo = np.genfromtxt(io.StringIO(RESPUESTAS_CSV), delimiter=";", skip_header=1,
#                      usecols=range(1, 41))
# correos = np.genfromtxt(io.StringIO(RESPUESTAS_CSV), delimiter=";", skip_header=1,
#                        usecols=0, dtype=str)
# genfromtxt deja un NaN donde la celda venia vacia: esa es tu senal de hueco.

# M = crudo                 # <- quedate solo con las filas que son de la cohorte
# emails = correos.tolist()  # <- y con sus correos, en el mismo orden

# medias_pregunta = np.zeros(40)   # <- la media de cada pregunta


# def medias_por_bloque(X):
    # <- de (n, 40) a (n, 4). Pista: los cuatro bloques son diez preguntas
    #    seguidas cada uno, asi que reshape los separa sin mover un dato.
    # return np.zeros((X.shape[0], len(BLOQUES)))


# def normalizar(X):
    # <- (valor - media de su pregunta) / desviacion de su pregunta.
    #    Los huecos siguen siendo huecos. Una pregunta plana no se divide.
    # return X


# bloques = medias_por_bloque(M)
# medias_bloque = bloques.mean(axis=0)
# Z = normalizar(M)

# peor_pregunta = 0    # <- indice de la pregunta con la media mas baja
# peor_bloque = ""     # <- nombre del bloque con la media mas baja

# artefacto = {
#    "artefacto": "matriz_satisfaccion",
#    "fuente": "",                  # <- de donde sale esto
#    "origen": ORIGEN_REGISTRO,     # <- la procedencia se arrastra
#    "n_respuestas": 0,
#    "n_preguntas": 0,
#    "preguntas": [],
#    "bloques": {},
#    "emails": [],
#    # OJO: un NaN no es JSON valido. Los huecos tienen que viajar como None, o
#    # el Sprint 09 no puede leer esto. El atajo, sin bucles:
#    #   np.where(np.isnan(M), None, M).tolist()
#    "matriz": [],
#    "medias_pregunta": [],
#    "medias_bloque": {},
#    "peor_pregunta": "",
#    "peor_bloque": "",
#}

# print("M:", M.shape, "| huecos:", int(np.isnan(M).sum()))

# ---------------- SOLUCIÓN ----------------
import io
import numpy as np

crudo = np.genfromtxt(io.StringIO(RESPUESTAS_CSV), delimiter=";", skip_header=1,
                      usecols=range(1, 41))
correos = np.genfromtxt(io.StringIO(RESPUESTAS_CSV), delimiter=";", skip_header=1,
                        usecols=0, dtype=str)

correos_registro = [persona["email"] for persona in REGISTRO]
en_registro = np.isin(correos, correos_registro)

M = crudo[en_registro]
emails = correos[en_registro].tolist()

medias_pregunta = np.nanmean(M, axis=0)


def medias_por_bloque(X):
    n_bloques = len(BLOQUES)
    return np.nanmean(X.reshape(X.shape[0], n_bloques, -1), axis=2)


def normalizar(X):
    media = np.nanmean(X, axis=0)
    desv = np.nanstd(X, axis=0)
    desv = np.where(desv == 0, 1, desv)
    return (X - media) / desv


bloques = medias_por_bloque(M)
medias_bloque = bloques.mean(axis=0)
Z = normalizar(M)

nombres_bloques = list(BLOQUES)
peor_pregunta = int(np.argmin(medias_pregunta))
peor_bloque = nombres_bloques[int(np.argmin(medias_bloque))]

artefacto = {
    "artefacto": "matriz_satisfaccion",
    "fuente": "Volcado del cuestionario de satisfacción de Product (RESPUESTAS_CSV), filtrado con los miembros del registro de cohortes del Sprint 2 (REGISTRO)",
    "origen": ORIGEN_REGISTRO,
    "n_respuestas": int(M.shape[0]),
    "n_preguntas": int(M.shape[1]),
    "preguntas": PREGUNTAS,
    "bloques": BLOQUES,
    "emails": emails,
    "matriz": np.where(np.isnan(M), None, M).tolist(),
    "medias_pregunta": medias_pregunta.tolist(),
    "medias_bloque": dict(zip(nombres_bloques, medias_bloque.tolist())),
    "peor_pregunta": PREGUNTAS[peor_pregunta],
    "peor_bloque": peor_bloque,
}

print("M:", M.shape, "| huecos:", int(np.isnan(M).sum()))
print("Medias por bloque:", artefacto["medias_bloque"])
print("Peor pregunta:", PREGUNTAS[peor_pregunta], "| Peor bloque:", peor_bloque)