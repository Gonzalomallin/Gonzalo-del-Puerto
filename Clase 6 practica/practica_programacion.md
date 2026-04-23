# Práctica - Programación 1

**REGLA:** No utilizar Python para realizar estos ejercicios. El parcial será en papel y no habrá ayuda del intérprete.  
Responder en este mismo documento.

---

## Ejercicio 1 - Tipos de datos

Indicar qué tipo de dato devuelve cada expresión:

```
8 < 2: ____False______  
"perro" != "gato": _____True_____  
"Hola" * 2: ______Hola Hola____  
9 / 2: ______4.5____  
9 // 2: ______4____  
```

---

## Ejercicio 2 - Lectura de código

Explicar con tus palabras qué hace el siguiente código:

```
numeros = [2, 4, 6, 8]
contador = 0

for numero in numeros:
    if numero > 4:
        contador = contador + 1

print(contador)
```

Explicar el comportamiento general, no línea por línea.

---Es un contador que suma la cantidad de números mayor a 4 que hay dentro de la lista "numeros". E imprime esa información.

## Ejercicio 3 - Análisis

¿El siguiente código funciona correctamente?  
En caso de que no funcione, explicar por qué.

```
valores = [10, 20, 30]
print(valores[2])
print(valores[3])
```

---No funciona porque no existe el valor "valores[3]" para imprimir.

## Ejercicio 4 - Desarrollo

Se pide desarrollar un sistema de registro de números:

1. Pedir números al usuario hasta que ingrese 0.  
2. Guardarlos en una lista.

Luego, crear una función que:

- Reciba la lista.  
- Muestre:
  - Cantidad total de números ingresados (sin usar `len`).


lista_numeros = []
cantidad = 0


while True:
    numero = input("Ingrese un numero. Para salir, presione 0: ")
    if numero == 0:
        break
    else:
        lista_numeros.append(numero)
        cantidad += 1 
        print(f"La suma total de numeros ingresados es: {cantidad}")



def funcion(lista_numeros):
    print(f"La suma total de numeros ingresados es: {cantidad}")

funcion(lista_numeros)