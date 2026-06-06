# Interpretando consignas

## Verificaciones

1. Se pide verificar que un dato es un número?

**RESPUESTA: 
```python
if dato.isnumeric():
    #Código
```
Si el numero es negativo:
```python
dato = -1
if dato[0] == "-":
    dato = dato[1:]
```
2. Se pide verificar que tiene N cantidad de caracteres?

**RESPUESTA:** 
```python
if len(dato) == 10:
    # código

if len(dato) > 4:
    # código
```


3. Se pide verificar que no sea un dato vacío?

**RESPUESTA:** 
```python
if len(datos) == 0:
    # código
if len(datos) == False:
    # código
if datos == "":
    # código
```

4. Se pide verificar que un elemento más exista más de N veces?

**RESPUESTA:** 
```python
datos = "nombre, edad, género"
if datos.count(",") == 2:
    # código
```



5. Si tenemos que verificar que un texto contenga otro texto?

**RESPUESTA:** 
```python
dato = "Hola Mundo"
if "Hola" in dato:
    # código
#en diccionarios o listas o set o tuplas:
datos = {cacao{}}
if cacao in datos:
    # código
```


## Repeticiones

1. Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?

**RESPUESTA:** 
```python
datos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for dato in datos:
    if dato.isnumeric():
        # Código
```

2. Hay que pedirle 5 nombres al usuario. ¿Que hacemos?
```python
lista_nombres = []
nombre = input("Ingrese su nombre: ")
for idx in range(5):
    lista_nombres.append(nombre)
```

**RESPUESTA:** 

3. Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?

**RESPUESTA:** 
```python
datos = ""
while datos != "Fin":
    datos = input("Ingrese aquí su dato: ")
    # código

while True:
    datos = input("Ingrese aquí su dato: ")
    if datos == "Fin":
        break
```

## Archivos

1. Hay que leer un archivo: 

**RESPUESTA:** 
```python
f = open("archivo.txt", r)
contenido = f.read()
contenido_lista = f.readlines() #separado por salto de línea
```


2. Hay que escribir un archivo:

**RESPUESTA:** 
```python
f = open("archivo.txt", w)
f.write("Hola Mundo")
```

3. ¿Hay que cerrar un archivo?

**RESPUESTA:** 
```python
# Sí, se cierra siempre un archivo despues de leerlo y de escribirlo
f.close()
```

## Otros
1. Tenemos que solicitarle al usuario que ingrese 25 nombres, apellidos y año de nacimientos ¿Que hacemos? 
```python
datos = []
for idx in range(25):
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    anio_nacimiento = input("Ingrese su año de nacimiento: ")
    #Cuando validamos las variables, usamos input.strip(). Tambien #podemos validar con un input.isalpha() y un input.isnumeric()#o un count() de 4 digitos (para el año de nacimiento.)
    datos.append({
        "nombre": nombre,
        "apellido": apellido,
        "anio_nacimiento": anio_nacimiento
    })

```
2. Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible.
```python
La estructura ideal sería un diccionario.
```

