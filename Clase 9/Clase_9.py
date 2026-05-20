#Tuplas: class tuple
#mi_primera_tupla = ("Lautaro", "Linquiman")
#mi_segunda_tupla = (1, 2, 3)
#print(mi_primera_tupla)
#print(type(mi_primera_tupla))

#persona = ("Ana", 20)
#print(persona[0])
#print(persona[-1])
#nombre, edad = persona
#print(nombre)
#print(edad)

#for i in persona:
 #   print(i)

#persona[0] = "Fernando" ERROR

#coordenada = (-41.13, -71.31)
#fecha = (5, 5, 2026)
#def operacion(a, b):                        #la función devuelve una tupla
#    return (a + b, a - b)
#suma, resta = operacion(5, 10)

#print(suma, resta)

#Conjuntos: class set
# podriamos usar conjuntos para tener 1)Lista de asistentes únicos.2) DNI de Alumnos.
#No repite elementos. no sirve para contar o recorrer.
#mi_primer_conjunto = {1, 2, 3, 3, 4}
#print(mi_primer_conjunto)
#print(len(mi_primer_conjunto))

#nombres = {"Ana", "Juan", "Pedro"}
#print(nombres)
#nombres.add("Lucia")
#print(nombres)
#nombres.remove("Juan")
#print(nombres)
#print("Ana" in nombres)

#set para no repetir:
#lista_nombres = ["Ana", "Juan", "Ana", "Pedro"]
#nombres_unicos = set(lista_nombres)
#print(nombres_unicos)

#Con los sets operamos aplicando teoria de conjuntos:
#a = {"Ana", "Juan", "Pedro"}
#b = {"Juan", "Lucia"}
#print("Grupo A: ", a)
#print("Grupo B: ", b)

#print("Unión: ", a | b)
#print("Intersección: ", a & b)
#print("Diferencia a - b: ", a - b)
#print("Diferencia b - a: ", b - a)

#Diccionarios: estructura de datos que permite almacenar su contenido en forma de clave valor
#class dict
#puedo modificar o agregar elementos del diccionario
#mi_primer_diccionario = {
#    "clave_1": "valor_1",
#    "clave_2": "valor_2",
#}
#print(mi_primer_diccionario)
#print(type(mi_primer_diccionario))

#tuple vs dict:
#alumno_tupla = ("Paula", "Chavez", 8)
#print(alumno_tupla[2])
#alumno_dict = {
#    "nombre": "Paula",
#    "apellido": "Chavez",
#    "nota": 8
#}
#print(alumno_dict["nota"])

#persona = {
#    "nombre": "Martin",
#    "edad": 20
#}
#print(persona["nombre"])
#print(persona["edad"])
##Agregar un elemento
#persona["ciudad"] = "Bariloche"
#print("ciudad" in persona)
#keys = persona.keys()
#values = persona.values()
#print(keys)
#print(values)

#Para recorrer claves y valores del diccionario:
#for clave in persona:
#    print(clave)
#for clave in persona:
#    print(clave, persona[clave])

# Lista de diccionarios
#alumnos = [
#    {"nombre": "Paula", "nota": 8},
#    {"nombre": "Juan", "nota": 3},
#    {"nombre": "Pedro", "nota": 6}
#]
#alumnos.append({"nombre": "John", "nota": 2})
#for alumno in alumnos:
#    if alumno["nota"] >= 4:
#        print(alumno["nombre"], "aprobó")
#    else:
#        print(alumno["nombre"], "desaprobó")

#Diccionario con diccionario:
#alumno = {
#    "nombre": "Paula",
#    "contacto": {
#        "email": "paula@mail.com",
#        "telefono": "294499999"
#    }
#}

#curso = {
#    "nombre": "Programacion 1", 
#    "comision": 3
#}