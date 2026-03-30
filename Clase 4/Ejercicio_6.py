opcion = ""
Total = 0
print("Selecciona la comida para llevar")
while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: ").lower()
    if opcion == "pizza":
        Total += 25
        print("Excelente! Agregamos una pizza a tu pedido")
        print("¿alguna cosa mas para pedir?")
    elif opcion == "terminar pedido":
        print("cerrando pedido...")
    elif opcion == "hamburguesa":
        Total += 20
        print("Excelente, agregamos una hamburguesa a tu pedido")
        print("¿alguna cosa mas para pedir?")
    else:
        print(f"lo siento, no tenemos {opcion}, prueba con otra cosa")
    print(f"Gracias por tu compra, el total es {Total} $")
    







    







