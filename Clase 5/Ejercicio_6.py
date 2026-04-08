
def trae_documento():
    return input("Trae documento [si/no]: ") == "si"

def ingresar_edad():
    return int(input("Ingresar edad: "))

def puede_pasar(documento, edad):
    return documento == True and edad >= 18

documento = trae_documento()
edad = ingresar_edad()
if puede_pasar(documento, edad):
    print("Puede pasar")
else:
    print("No puede pasar")

