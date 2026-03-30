lista_comidas = []
opcion = ""
print("Haga su pedido.")
while opcion != "terminar pedido":
    opcion = input("Escribí la comida que quieras pedir: ")
    if opcion == "pizza":
        print("Gracias ¿Algo más?")
    elif opcion == "hamburguesa":
        print("Gracias ¿Algo más?")
    elif opcion == "empanadas":
        print("Gracias ¿Algo más?")
    else:
        print("No tenemos ¿Algo más?")
    lista_comidas.append(opcion)
print("Gracias por tu pedido")
print(lista_comidas)

