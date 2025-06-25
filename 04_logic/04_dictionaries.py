import os
os.system("clear")


persona = {
    "nombre": "jorge",
    "edad": 25,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9]
}

print(persona["nombre"])
print(persona["calificaciones"][1])

persona["calificaciones"][1] = 10
persona["nombre"] = "Juan"

print(persona)

del persona["edad"]
print(persona)

print(persona.pop("es_estudiante"))

print(persona)


persona.keys()

persona.value()

persona.items()