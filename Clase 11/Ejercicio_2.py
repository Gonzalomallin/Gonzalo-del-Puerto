
usuarios = [
    "ana,programacion",
    "juan,matematica",
    "lucia,fisica"
]

for linea in usuarios:
    datos = linea.split(",")
    nombre = datos[0].capitalize()
    materia = datos[1].capitalize()
#    print(nombre)
#    print(materia)
    print(f"Hola {nombre}, estás inscripto/a en {materia}")
