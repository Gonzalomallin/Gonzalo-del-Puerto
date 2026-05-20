alumnos = [
    {
        "nombre": "Joaquin",
        "notas": [8, 4, 9],
        "materias": {"Programación", "Matemática"}
    },
    {
        "nombre": "Juan",
        "notas": [3, 5, 5],
        "materias": {"Programación"}
    },
    {
        "nombre": "Lucía",
        "notas": [9, 9, 8],
        "materias": {"Programación", "Inglés"}
    }    
]

for alumno in alumnos:
    print(alumno["nombre"])

for alumno in alumnos:        
    suma_notas = 0
    cantidad_notas = 0
    for nota in alumno["notas"]:
        suma_notas += nota
        cantidad_notas += 1
    print(suma_notas, cantidad_notas)
    promedio = suma_notas / cantidad_notas
    if promedio >= 4:
        print(alumno["nombre"], "aprobó", promedio)

for alumno in alumnos:
    if "Matemática" in alumno["materias"]:
        print(alumno["nombre"], " cursa matemática")

alumnos[0]["materias"].add("Laboratorio")
print(alumnos[0])









    
