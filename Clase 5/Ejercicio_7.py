def evaluar_energia(nivel = 0):
    if nivel > 7:
        print("Modo maquina activado")
    elif nivel > 4:
        print("Se puede laburar")
    else:
        print("Tomar cafe urgente")


evaluar_energia(9)
print(evaluar_energia())