lineas = [
    " AnA ;8;7;9",
    " JuAn;4;5;3",
    " LucIA;10;9;10"
]

lineas_limpia = []

for idx, linea in enumerate(lineas):
    datos = linea.split(";")
    nombre = datos[0].strip().capitalize()
#    print(f"Alumno: '{nombre}'")
    lineas_limpia.append(nombre)
    idx += 1

for idx, linea in enumerate(lineas):
    datos = linea.split(";")
    notas = [datos[1], datos[2], datos[3]]
    notas_txt = " - ".join(notas)
#    print(f"Notas: '{notas_txt}'")
    idx += 1
    lineas_limpia.append(notas_txt)
    print(f"Alumno: '{nombre[idx]}' - Notas: '{notas_txt}'")
    

print(lineas_limpia)
    