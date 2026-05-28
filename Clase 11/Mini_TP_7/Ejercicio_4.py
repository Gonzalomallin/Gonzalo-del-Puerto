edad_ingresada = ""
while True:
    edad_ingresada = input("Ingrese su edad. Para salir, escriba Fin: ")
    if edad_ingresada.strip().isnumeric() and 0 < int(edad_ingresada) <= 120:
        print(f"Edad registrada: {edad_ingresada} ")
    elif edad_ingresada == "Fin".lower():
        print("Gracias, hasta pronto. ")
        break
    else:
        print("Comando incorrecto, vuelva a intentar. ")
        