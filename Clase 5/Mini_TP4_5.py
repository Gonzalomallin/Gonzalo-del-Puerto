def obtener_estado():
    nota = int(input("¿Qué nota obtuviste?: "))

    if nota >= 8:
        print(f"Promocionaste! Te sacaste un {nota}")
    elif nota < 6:
        print(f"Desaprobaste. Te sacaste un {nota}")
    else:
        print(f"Aprobaste. Te sacaste un {nota}") 

obtener_estado()
