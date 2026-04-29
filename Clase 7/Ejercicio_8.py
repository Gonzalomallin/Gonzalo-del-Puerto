def obtener_numero_menor(entrada_lista):
    menor = entrada_lista[0]
    contador = 0

    for n in entrada_lista:
        if n < menor:
            menor = n
            

    for n in entrada_lista:
        if n == menor:
            contador += 1
            
    return [menor, contador]

numeros = [-4, -9, 1, -9, 3]
resultado = obtener_numero_menor(numeros)

print(resultado)