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