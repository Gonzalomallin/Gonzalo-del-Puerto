lista_cargada = ["remeras", "buzos", "pantalon", "medias", "calzones"]
while True:
    item = input("¿Que hay en la lista?: ")
    if item in lista_cargada:
        print(f"el elemento {item} está en la lista")
    elif item == "fin":
        print("Gracias por tu busqueda.")
        break
    else:
        print(f"el elemento {item} no está en la lista")

