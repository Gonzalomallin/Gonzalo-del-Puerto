# Escribir una funcion que convierta una frase en:
# "pedro MARTINEZ sEgundo" -> "pedro Martinez Segundo"

def camel_case():
    datos = "pedro MARTINEZ sEgundo".split()
    datos_1 = datos[0].lower()
    datos_2 = datos[1].capitalize()
    datos_3 = datos[2].capitalize()
    print(f"'{datos_1} {datos_2} {datos_3}'")

camel_case()
