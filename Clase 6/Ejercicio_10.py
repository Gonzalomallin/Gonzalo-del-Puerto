lista_productos = []
suma_productos = 0

while True:
    productos = input("Ingrese su producto. En caso de salida, presione Fin:")
    if productos == "Fin":
        print("Gracias por su compra")
        break
    else:
        lista_productos.append(productos)
        suma_productos += 1

print(lista_productos)
print(f"Primero elemento de la lista: {lista_productos[0]}")
print(f"Último elemento de la lista: {lista_productos[-1]}")
print(f"Suma total de la lista: {suma_productos}")





