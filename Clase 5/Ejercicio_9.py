def pedir_comida(): 
    comida = ""
    while comida == "":
        comida = input("¿Que quiere pedir? ").lower()
    return comida
        

def obtener_precio(comida):
    precio = 0
    if comida == "hamburguesa":
        print("Hamburguesa 100")
        precio = 100
    elif comida == "pizza":
        print("Pizza 140")
        precio = 140
    elif comida == "milanesa":
        print("Milanesa 125")
        precio = 125

    if precio:
        print(f"Comida {comida} - Precio: {precio}$")
    else:
        print("No hay")
    return precio

comida = pedir_comida()
print(obtener_precio(comida))




  
