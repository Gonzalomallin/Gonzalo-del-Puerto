x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]
maximo = 0
minimo = 0

for i in x:
    if i > maximo:
        maximo = i
    elif i < minimo:
        minimo = i

print(f"El número máximo de la lista es {maximo}")
print(f"El número minimo de la lista es {minimo}")

