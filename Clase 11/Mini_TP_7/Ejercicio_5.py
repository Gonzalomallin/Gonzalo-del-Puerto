lista_codigo = []
while True:
    codigo_materia = input("Ingrese su código de materia. Ejemplo: PROG-101. Para salir, Fin: ")
    if codigo_materia == "Fin".lower():
        print("Gracias, hasta pronto. ")
        break
    codigo_valido = codigo_materia.strip().split("-")
    izquierda, derecha = codigo_valido
    if len(codigo_valido) == 2 and izquierda.isalpha() and derecha.isnumeric():
          lista_codigo.append(codigo_valido)
          print(lista_codigo) 
    else:
        print("Formato incorrecto, vuelva a intentar. ")

# sé que no esta terminando de funcionar acorde a la consigna pero no logro entender como 
# terminar de resolverlo :).