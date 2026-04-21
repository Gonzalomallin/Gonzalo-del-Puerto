suma = 0
total = 0
maximo = 0
minimo = 0

while True:
    numero = int(input("Ingrese un número. En caso de salida, presione 0: "))
    if numero != 0:
        suma += suma + numero
        total += 1
    else:
         break

print(suma)
print(total)
print(suma/total)
