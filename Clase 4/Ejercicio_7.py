lista_de_super = ["Huevos","pan","coca","azucar","leche","fideos"]
print(type(lista_de_super))
print(lista_de_super)
print(len(lista_de_super))
for indice in range (len(lista_de_super)):
    print(indice)
    print(lista_de_super[indice])
lista_de_comida = ["pizza","hamburguesa","empanada"]

while True:
        indice_seleccionado = int(input("elegi la comida"))
        if indice_seleccionado < len(lista_de_comida):
            comida = lista_de_comida[indice_seleccionado]
            print(f"elegiste el indice {indice_seleccionado}: {comida}")
        else:
            print("elegiste una comida invalida")
            

















