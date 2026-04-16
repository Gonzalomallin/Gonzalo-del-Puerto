def calcular_precio():
    total = int(input("¿Cuanto va a pagar?: " ))

    if total > 10000:
        descuento = total * 0.1
        final = total - descuento
        print(f"El total es {final}")
    elif total <= 10000:
        no_descuento = total
        print(f"El total es {total}")
        


calcular_precio()



