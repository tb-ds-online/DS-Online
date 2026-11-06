# # Bridge SA · Operations — el registro de cohortes
# #
# # Ya tienes cargado:
# #   ALTAS_PREVIAS  lista de dicts {"nombre", "email", "programa"} (viene del S1)
# #   HOJA_NUEVAS    el texto de la hoja de esta semana: "nombre ; correo ; programa"
# #   COHORTES       dict {programa: codigo} con las cohortes abiertas
# #   ORIGEN_ALTAS   de donde salen las altas previas (para el artefacto, no lo cambies)
# #
# # Deja preparado esto, con estos nombres exactos:
# #   normalizar_email(texto)    -> str, sin espacios y en minusculas
# #   parsear_hoja(texto)        -> list de dicts {"nombre", "email", "programa"}
# #   class Cohorte(codigo, programa) -> self.codigo, self.programa,
# #                                 self.miembros (dict correo -> persona),
# #                                 self.rechazos (list de {"email", "motivo"}),
# #                                 alta(persona) -> True / False,
# #                                 emails() -> set, total() -> int, y __str__
# #   registro                   -> dict {codigo: Cohorte}, uno por cohorte abierta
# #   inscribir(registro, altas) -> (registradas, sin_cohorte)
# #   sin_cohorte, programas_sin_cohorte, artefacto


# def normalizar_email(texto):
#     # sin espacios (tampoco los de en medio) y en minusculas
#     return ""


# def parsear_hoja(texto):
#     # una linea = "nombre ; correo ; programa"
#     # una linea en blanco no es nadie: no crea ninguna fila
#     filas = []
#     for linea in texto.split("\n"):
#         pass
#     return filas


# class Cohorte:
#     def __init__(self, codigo, programa):
#         pass

#     def alta(self, persona):
#         # motivos de rechazo: "duplicado" y "otro_programa"
#         return False


# def inscribir(registro, altas):
#     registradas = []
#     fuera = []
#     # cada alta va a la cohorte de SU programa; si no hay ninguna abierta
#     # para ese programa, no es un rechazo: es que no hay donde meterla
#     return registradas, fuera


# registro = {}
# todas = list(ALTAS_PREVIAS) + parsear_hoja(HOJA_NUEVAS)
# registradas, sin_cohorte = inscribir(registro, todas)
# programas_sin_cohorte = set()

# artefacto = {
#     "artefacto": "registro_cohortes",
#     "fuente": "",            # <- de donde sale esto
#     "origen": ORIGEN_ALTAS,  # <- la procedencia no te la inventas: se arrastra
#     "cohortes": {},          # <- {codigo: {"programa", "miembros", "total"}}
#     "rechazos": [],          # <- los de todas las cohortes, juntos
#     "sin_cohorte": sin_cohorte,
# }

# print("Miembros:", sum(c.total() for c in registro.values()),
#       "· Sin cohorte:", len(sin_cohorte))



#------------------------------------------------
###################SOLUCIÓN##################
#------------------------------------------------

def normalizar_email(email):
    return "".join(email.split()).lower()


def parsear_hoja(texto):
    personas = []
    for linea in texto.split("\n"):
        if linea.strip() == "":
            continue
        partes = linea.split(";")
        personas.append({
            "nombre": " ".join(partes[0].split()).title(),
            "email": normalizar_email(partes[1]),
            "programa": " ".join(partes[2].split()),
        })
    return personas


class Cohorte:
    def __init__(self, codigo, programa):
        self.codigo = codigo
        self.programa = programa
        self.miembros = {}          # correo -> persona
        self.rechazos = []

    def emails(self):
        return set(self.miembros)

    def total(self):
        return len(self.miembros)

    def alta(self, persona):
        email = normalizar_email(persona["email"])
        if email in self.miembros:
            self.rechazos.append({"email": email, "motivo": "duplicado"})
            return False
        if persona["programa"] != self.programa:
            self.rechazos.append({"email": email, "motivo": "otro_programa"})
            return False
        self.miembros[email] = {
            "nombre": persona["nombre"],
            "email": email,
            "programa": persona["programa"],
        }
        return True

    def __str__(self):
        return f"{self.codigo} ({self.programa}): {self.total()} miembros, {len(self.rechazos)} rechazos"


registro = {}
for programa, codigo in COHORTES.items():
    registro[codigo] = Cohorte(codigo, programa)

sin_cohorte = []
programas_sin_cohorte = set()


def inscribir(persona):
    programa = persona["programa"]
    if programa in COHORTES:
        return registro[COHORTES[programa]].alta(persona)
    sin_cohorte.append(persona)
    programas_sin_cohorte.add(programa)
    return False


for persona in ALTAS_PREVIAS + parsear_hoja(HOJA_NUEVAS):
    inscribir(persona)

rechazos = []
for c in registro.values():
    for r in c.rechazos:
        rechazos.append({"cohorte": c.codigo, "email": r["email"], "motivo": r["motivo"]})

artefacto = {
    "artefacto": "registro_cohortes",
    "fuente": "Altas limpias del Sprint 1 (ALTAS_PREVIAS) + hoja semanal de Operations & Cohortes (HOJA_NUEVAS), repartidas en las cohortes abiertas este trimestre (COHORTES)",
    "origen": ORIGEN_ALTAS,
    "cohortes": {
        codigo: {
            "programa": c.programa,
            "miembros": list(c.miembros.values()),
            "total": c.total(),
            "rechazos": c.rechazos,
        }
        for codigo, c in registro.items()
    },
    "rechazos": rechazos,
    "sin_cohorte": sin_cohorte,
    "programas_sin_cohorte": sorted(programas_sin_cohorte),
}

for c in registro.values():
    print(c)
print("Miembros:", sum(c.total() for c in registro.values()))
print("Rechazos:", len(rechazos))
print("Sin cohorte:", len(sin_cohorte))