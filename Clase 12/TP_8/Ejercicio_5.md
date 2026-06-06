def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)

¿Qué hace el programa?
 El programa recorre una lista de nombres y, utilizando las dos funciones creadas, los limpia y los valida para guardarlos en una lista. 
¿Qué hace la función limpiar?
La función limpiar recibe un texto (en este caso, un nombre de la lista) y lo devuelve stripeado (sin caracteres vacíos al comienzo y al final) y
capitalizado, es decir, con la primer letra mayúscula.
¿Qué hace la función es_valido?
La función es_valido recibe un nombre (en este caso, el nombre ya limpio) y devuelve un valor booliano verdadero en función de si tiene
3 o mas letras. En caso contrario, arroja falso.
¿Qué nombres quedan almacenados en validos?
Los nombres se agregan a la lista validos si, al pasar por la función es_valido, cumplen la validación de 3 o mas letras.
¿Qué imprime el programa al finalizar?
El programa imprimera la lista validos. Es decir, los mismos nombres que hay en la lista nombres exceptuando a los que, una vez limpios,
no cumplen la validación. Deberia arrojar ["Bart", "Walter","Rick"] 
