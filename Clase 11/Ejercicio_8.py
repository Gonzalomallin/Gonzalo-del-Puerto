#Usar un for para recorrer los elementos

lista_productos = []
while True:
    producto = input("Ingrese producto A, producto B. Para salir, FIN: ")
    if producto == "FIN":
        print("Hasta pronto")
        break
    elif producto == "":
        lista_productos.append(producto)
        for producto in lista_productos:
            if len(lista_productos) == 2 and producto.isalpha():
                print("Gracias por ingresar sus productos")
                print(lista_productos)
                break
            else:
                print("Intentar otra vez")

    