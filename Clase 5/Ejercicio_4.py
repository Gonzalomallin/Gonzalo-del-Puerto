def saludarI():
    print("Hola")
saludarI()

def bienvenida():
    nombre = input("ingrese su nombre: ")
    print(f"hola {nombre} :)")
    print("Bienvenido a mi programa")
bienvenida ()

def saludarII(nombre):
    print(f"Hola {nombre} :)")
    print("Bienvenido vos tmb a mi programa")
saludarII("juan")

def saludarIII(nombre_1, nombre_2):
    print(f"Hola {nombre_1} y {nombre_2} :)")
saludarIII("Juan", "Pedro")

def sumar(a = 0, b = 0):
    print(f"la suma es: {a} + {b} = {a + b}")
sumar(1, 2)
sumar(a=1)
sumar(b=2)
