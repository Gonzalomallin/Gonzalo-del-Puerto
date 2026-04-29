def obtener_numero_mayor(lista_entrada):
    numero_mayor = lista_entrada[0]
    repeticion = 0

    for n in lista_entrada:
        if numero_mayor < n:
            numero_mayor = n
    for n in lista_entrada:
        if n == numero_mayor:
            repeticion += 1
    return [numero_mayor, repeticion]

numeros = [4, 9, 1, 9, 3, 10, 10, 10, 100]

print(obtener_numero_mayor(numeros))


