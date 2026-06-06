lector_archivo = open("temperaturas.txt", "r")
lista_archivo = lector_archivo.readlines()
lector_archivo.close()

print(lista_archivo)

dic_temperaturas = {}

for linea in lista_archivo:
    partes = linea.split(";")
    if len(partes) == 2:
            ciudad = partes[0]
            temperatura = partes[1]

    if ciudad in dic_temperaturas:
        dic_temperaturas[ciudad].append(temperatura)
    else:
        dic_temperaturas[ciudad] = [temperatura]


print(dic_temperaturas)

    


