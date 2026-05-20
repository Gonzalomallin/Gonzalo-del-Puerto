def datos_persona(nombre, edad):
    mayor_edad = False
    if edad >= 18:
        mayor_edad = True
    return (nombre, edad, mayor_edad)

resultado = datos_persona("Gonzalo", 37)


print(resultado)



