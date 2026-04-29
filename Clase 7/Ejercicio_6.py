lista_ingresados = []
suma_negativo = 0
suma_positivo = 0
suma_total = 0

while True:
    numero = int(input("Ingrese su número. Para salir, presione 0: "))
    if numero == 0:
        print("Hasta pronto")
        break
    elif numero < 0:
        lista_ingresados.append(numero)
        suma_negativo += 1
        suma_total += 1
    elif numero > 0:
        lista_ingresados.append(numero)
        suma_positivo += 1
        suma_total += 1

print(f"Los numeros negativos suman {suma_negativo}")
print(f"Los numeros positivos suman {suma_positivo}")
print(f"La suma total es de {suma_total}")

