#Ejercicio 20D:
#codigo 1:
#  
Lista = [1, 2, 3]
total = 0

for numero in lista:
    total = total + numero

print(f"{total}")

Este codigo imprime la variable total que suman los numeros dentro de la lista.

codigo 2:

def funcion(lista):
    contador = 0
    for numero in lista:
        if numero > 0:
            contador += 1
    return contador

Este codigo llama a una funcion que devuelve el contador con respecto a la cantidad de 
elementos que hay en la lista.
