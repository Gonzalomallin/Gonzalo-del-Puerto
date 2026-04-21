lista_productos = []

while "nombre" != "Fin":
    nombre = input("Ingrese su producto. En caso contrario, escriba Fin: ")
    if nombre in lista_productos:
        print(f"Lo siento, {nombre} ya está en la lista")
    elif nombre == "Fin":
        print("Hasta pronto")
        break
    else:
        lista_productos.append(nombre)
        print(f"Gracias. Seleccionaste {nombre}")

def productos():
    print(lista_productos)

productos()


