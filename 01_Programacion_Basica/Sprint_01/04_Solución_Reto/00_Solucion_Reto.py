# Bridge SA · Operations — altas de la cohorte de marzo
#
# ALTAS_TEXTO ya esta cargado con el listado, tal cual.
# Cada linea util tiene la forma:  Nombre ; correo ; programa
#
# Deja preparadas estas tres cosas:
#   altas_limpias -> lista de listas [nombre, email, programa]
#   descartes     -> lista de listas [linea_original, motivo]
#   artefacto     -> el paquete que se lleva el Sprint 2
#
# Recuerda: linea en blanco se salta (no es descarte); correo sin @ o que
# no acabe en @bridge.example es descarte "email_invalido"; correo ya
# visto es descarte "duplicado". Y primero se limpia, despues se decide.
#
# Trucos: " ".join(t.split()) deja un solo espacio entre palabras;
#         "".join(t.split()) los quita todos;  t.title() pone la inicial
#         de cada palabra en mayuscula.

# altas_limpias = []
# descartes = []
# vistos = []

# for linea in ALTAS_TEXTO.split("\n"):
#    # tu codigo aqui
#    pass

# artefacto = {
#    "artefacto": "altas_limpias",
#    "fuente": "",          # <- de donde salen estos datos
#    "columnas": ["nombre", "email", "programa"],
#    "altas": altas_limpias,
#    "descartes": descartes,
#}

#print("Altas validas:", len(altas_limpias))
#print("Descartes:", len(descartes))




#------------------------------------------------
###################SOLUCIÓN##################
#------------------------------------------------
altas_limpias = []
descartes = []
vistos = []

for linea in ALTAS_TEXTO.split("\n"):
    # Línea en blanco: no existe, no es descarte
    if linea.strip() == "":
        continue

    partes = linea.split(";")

    # Primero se limpia
    nombre = " ".join(partes[0].split()).title()
    email = "".join(partes[1].split()).lower()
    programa = " ".join(partes[2].split())

    # Después se decide (se guarda la línea ORIGINAL, no la limpia)
    if "@" not in email or not email.endswith("@bridge.example"):
        descartes.append([linea, "email_invalido"])
    elif email in vistos:
        descartes.append([linea, "duplicado"])
    else:
        vistos.append(email)
        altas_limpias.append([nombre, email, programa])

artefacto = {
    "artefacto": "altas_limpias",
    "fuente": "Correo de Operations & Cohortes",
    "columnas": ["nombre", "email", "programa"],
    "altas": altas_limpias,
    "descartes": descartes,
}

print("Altas validas:", len(altas_limpias))
print("Descartes:", len(descartes))