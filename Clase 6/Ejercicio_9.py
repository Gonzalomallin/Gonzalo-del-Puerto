maximo = 0
minimo = 0

while True:
    numero = int(input("Ingrese un número. En caso de salida, presione 0: "))
    if numero == 0:
        break
    elif numero > maximo:
        maximo = numero
    elif numero < minimo:
        minimo = numero

print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

