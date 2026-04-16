
def pedir_comida():
    comida = ""
    while comida == "":
        comida = input("Bienvenido ¿Qué desea pedir?").lower()
    return comida


def obtener_precio(comida):
    precio = 0
    if comida == "Hamburguesa":
        precio = 100
        print("El precio es de 100")
    elif comida == "Pizza":
        precio = 75
        print("El precio es de 75")
    elif comida == "Milanesa":
        precio = 125
        print("El precio es de 125")

    if precio:
        print(f"Pediste {comida} - El precio es de: {precio}$")
    else:
        print("No hay")
    return precio


comida = pedir_comida()
print(obtener_precio(comida))



    



