alumno = {
    "nombre": "Federico",
    "apellido": "Gimenez",
    "edad": 36
}
print(f"Nombre y Apellido: {alumno["nombre"]} {alumno["apellido"]}")

alumno["edad"] += 1
alumno["Activo"] = True

print(alumno)