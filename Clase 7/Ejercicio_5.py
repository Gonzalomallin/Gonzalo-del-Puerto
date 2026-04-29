lista_numeros = []

def suma_numeros(suma_pares):
    suma = 0
    for n in suma_pares:
                if n % 2 == 0:
                    suma += n
                return suma
    
    for i in range(5):
        while True:
            numero = int(input("Por favor, ingrese su numero: "))
            lista_numeros.append(numero)
            break

resultado = suma_numeros(lista_numeros)
print(lista_numeros)
print(f"La suma de los numeros pares es de {resultado}")
