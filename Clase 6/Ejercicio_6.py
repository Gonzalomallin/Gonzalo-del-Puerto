def saludo():
    print("Bienvenido")

def retorno():
    return "Bienvenido"

def personal(nombre = ""):
    if (nombre == ""):
        return "Hola!"
    return f"Bienvenido {nombre}"
    
saludo()
print(retorno())
print(personal("Gonza"))
print(personal())




