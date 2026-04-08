salir = True
i = 0
while salir:
    print(f"Hola mundo, estoy en la iteración: {i}")
    i += 1
    if input("Ir a la proxima iteración? [Si/no]") == "si":
      # salir = False
      # break
      continue
    if input("Desea salir? [si/no]") == "si":
        salir = False
    print(f"Estoy al final de la iteración: {i-1}")
