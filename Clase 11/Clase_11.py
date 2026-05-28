#Extraer información de un texto de manera prolija

#Función split nos permite convertir una cadena de texto en una lista.
# STRING.split(delimitador, MAX_SPLIT=-1) ejemplo: "Buenos dias estrellita".split(" ") - ['Buenos', 'dias', 'estrellita']
#ejemplo = "Buenos dias estrellita".split(" ")
#print(ejemplo)
#En el problema del pdf el delimitador es ";"

#funcion strip nos permite eliminar caracteres vacioes e invisibles de una cadena de texto al principio y al final
# " Hola Mundo ".strip() - "Hola Mundo". o strip("$") etc
#ejemplo_2 = " Hola mundo ".strip() 
#print(ejemplo_2)

#función capitalize. transforma el texto para que solo la primer letra sea mayuscula.
#STRING.capitalize()
#ejemplo_3 = "HOLA".capitalize()
#print(ejemplo_3)
#ejemplo_4 = " hola".strip().capitalize()
#print(ejemplo_4)

#función join nos permite unir listas de string mediante un caracter y convertirlo en string
# " - ".join(['8', '7', '9']) - '8 - 7 - 9'

# Slicing de listas: para manipular el acceso al contenido de las listas

#validacion de datos: revisar los datos antes de usarlos. sobre todo si lo ingresa un usuario
#ayuda a construir programas mas seguros, claros y confiables para que no se rompan.
#ejemplo: 1996.isnumeric(); len("1996") == 4; Maria.isalpha(); 
# Pedro, Martinez, 19, 2004.count(",") == 3; carlos234.isalnum()