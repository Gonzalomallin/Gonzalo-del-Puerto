nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []

for nombre in nombres:
    nombre_limpio = nombre.strip().capitalize()
    nombres_normalizados.append(nombre_limpio)
    
print(nombres_normalizados)