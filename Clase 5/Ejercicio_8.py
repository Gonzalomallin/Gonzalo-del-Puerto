def pedir_comida(): 
    opcion = ""
    while opcion == "":
        opcion = input("¿Que quiere pedir? ")
    return opcion
        
print(pedir_comida())
