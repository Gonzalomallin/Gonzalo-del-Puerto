nombre_alumno = []

for i in range(4):
    nombre = input("Ingrese aquí su nombre: ")
    if len(nombre) == 0:
        print("Error: no se ha escrito nada")
    else:
        nombre_alumno.append(nombre.capitalize())
        
print(nombre_alumno)

for nombre in nombre_alumno:
    nombre_archivo = open("alumnos.txt", "w")
    nombre_archivo.writelines("\n".join(nombre_alumno))               
    nombre_archivo.close()








