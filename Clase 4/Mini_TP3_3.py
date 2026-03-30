lista_vacia = []
while True:
    item = input("¿Que agregas a la lista: ")
    if item == "fin":
        break
    lista_vacia.append(item)
    print("La lista es: ",lista_vacia)
    print(len(lista_vacia))
    