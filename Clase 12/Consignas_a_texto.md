EJ1: Un sensor registra eventos con este formato:

"PUERTA_A;ABIERTA;18:03"
"PUERTA_B;CERRADA;18:04"
"PUERTA_A;ABIERTA;18:05"
Se quiere contar cuántas veces aparece cada puerta.

Repuesta:
```python
Para contar cuantas veces aparece cada puerta tengo que normalizar usando un .split(";"), luego, crear una lista
y asignar variables para los elementos que voy a incluir en la lista. Ademas, agrego
variables como contador. Luego, con un iterador for puerta in lista_puerta: y, con condiciones que establezco a partir de if ,asigno que cuente las veces que aparece cada elemento.
```
```python
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
```

EJ2: Tenemos mediciones de voltaje:

[3.2, 3.4, 5.1, 2.9, 6.0, 3.3]

Mostrar cuántas mediciones están fuera del rango 3.0 a 5.0.

Repuesta:
```python
A partir de la lista de medicion de voltaje, la recorro con un for idx in lista: y condiciono, con if, esos valores a sólo los que se encuentran entre 3.0 < idx < 5.0.
```

EJ3: Un programa recibe comandos escritos por usuario:

Repuesta:
```python
Para normalizarlos, comienzo con validaciones de tipo .lower() y .strip(). Además, condiciono los comandos recibidos por el programa para que solo sean válidos los strings encender, apagar y estado.
```
" encender "
"APAGAR"
" estado "
"reiniciar"
Hay que normalizarlos y aceptar solo: encender, apagar, estado.