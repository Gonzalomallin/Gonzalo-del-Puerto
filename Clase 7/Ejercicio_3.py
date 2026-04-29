numeros = [-1, 1, -2, -3, 7, 10]
numeros_positivos = []
numeros_negativos = []
total = 0

for n in numeros:
    total += n
    if n > 0:
        numeros_positivos.append(n)
    else:
        numeros_negativos.append(n)

    print("Positivos: ", len(numeros_positivos))
    print("Negativos: ", len(numeros_negativos))
    print("Total: ", total)

