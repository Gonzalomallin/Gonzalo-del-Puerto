estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6], "asistencias": 9, "comision": "C1"},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencias": 6, "comision": "C1"},
    {"nombre": "Mora", "notas": [9, 8, 10], "asistencias": 10, "comision": "C2"},
    {"nombre": "Pedro", "notas": [2, 4, 3], "asistencias": 7, "comision": "C2"}
]

# 1- Para mostrar el promedio de cada estudiante, hay que sumar todas las notas que tiene cada
#alumno y, ese valor, dividirlo por la cantidad de notas que tienen. Las notas ocupan un lugar
#especifico dentro de la lista y dentro del diccionario, ocupando sus lugares de clave y valor.
# 2- Promociona si promedio >= 8 y asistencias >= 8
#Regulariza si promedio >= 4 y asistencias >= 6
#Recursa en otro caso

nota_comision = {}
est_en_riesgo = set()

for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    nota = estudiante["notas"]
    asistencia = estudiante["asistencias"]
    comision = estudiante["comision"]

    prom_notas = sum(nota) / len(nota)
    print(f"El promedio de {nombre} es de {prom_notas}")

    
    if prom_notas >= 8 and asistencia >= 8:
        print(f"{nombre} promociona")
    elif prom_notas >= 4 and asistencia >= 6:
        print(f"{nombre} regulariza")
    else:
        print(f"{nombre} recursa")
        est_en_riesgo.add(nombre)

