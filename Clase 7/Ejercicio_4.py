numeros = [2, 4, 5, 7, 9, 10, 12]

def sumar_pares(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n % 2 == 0:
            suma += n
    return suma

resultado = sumar_pares(numeros)
print(f"Lista original: {numeros}")
print(f"La suma de los números pares es: {resultado}")