lista_vacia_2 = []
while True:
    item = input("¿Que agregas a la lista: ")
    if item == "fin":
        break
    elif len(lista_vacia_2) >= 5:
        break
    lista_vacia_2.append(item)
print("La lista es: ",lista_vacia_2)
print(len(lista_vacia_2))
