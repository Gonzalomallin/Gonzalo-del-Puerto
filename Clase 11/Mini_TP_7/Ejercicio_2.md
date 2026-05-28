```python
linea = " mara ; programacion ; 8 "

partes = linea.split(";")
nombre = partes[0].strip().capitalize()
materia = partes[1].strip().capitalize()
nota_texto = partes[2].strip()

if nota_texto.isnumeric():
    nota = int(nota_texto)
    print(f"{nombre} cursa {materia} y obtuvo {nota}")
else:
    print("La nota no es valida")
```
```python
Es un programa que contiene una variable "linea" con un texto. A partir de una nueva variable "partes" con su función .split(";"), transformo el texto de "linea" en 3 elementos distintos e identificados a partir de 3 nuevas variables con sus respectivas ubicaciones (por ejemplo, partes[0]). Nuevas variables las cuales normalizo con funciones como .strip()(primero ésta para que la función que le sigue no interprete el espacio como la primer letra a capitalizar) y .capitalize(). Luego, valido una de estas variables (nota_texto) para que sólo sea aceptada como un numero entero con la función .isnumeric().
Si esa variable se encontrara con un "ocho" en vez del numero 8, imprimiría "La nota no es valida"
```
