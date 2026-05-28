while True:
    nota_parcial = input("Ingrese su nota. Para salir, FIN: ")
    if nota_parcial.strip().isnumeric() and int(nota_parcial) >= 0 and int(nota_parcial) <= 10:
        print(f"Gracias, su nota es {nota_parcial}")
    elif nota_parcial == "FIN":
        break
    else:
        print("Siga intentando")



