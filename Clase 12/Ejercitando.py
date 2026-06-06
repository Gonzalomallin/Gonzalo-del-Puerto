datos_entrada = [
    "PUERTA_A;ABIERTA;18:03",
    "PUERTA_B;CERRADA;18:04",
    "PUERTA_A;ABIERTA;18:05"
]
contador_aperturas = {
    "PUERTA_A": 0,
    "PUERTA_B": 0
}

for dato_entrada in datos_entrada:
    datos = dato_entrada.split(";")
    nombre_puerta = datos[0]
    estado = datos[1]
    hora = datos[2]
    contador_aperturas[nombre_puerta] += 1
    
print(contador_aperturas)