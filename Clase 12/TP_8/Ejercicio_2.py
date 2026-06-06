mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

diccionario_mediciones = {
    "aula_1": ["temp", 18.5, "humedad", 40, "presion", 0],
    "aula_2": ["temp", 0, "humedad", 55, "presion", 0],
    "laboratorio": ["temp", 21.0, "humedad", 0, "presion", 1012]
}

for valor in diccionario_mediciones.values():
    conjunto_mediciones = set(valor[::2])

print(diccionario_mediciones)
print(conjunto_mediciones)

