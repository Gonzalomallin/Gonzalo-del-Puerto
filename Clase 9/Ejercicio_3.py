#persona["edad"] -= 1
mi_diccionario = {
    "nombre": "Martillo",
    "precio": 9500,
    "stock": 50
}

print(mi_diccionario)

mi_diccionario["precio"] = 9500 + 9500 * 0.1    # *= 1.1 
print(mi_diccionario["precio"])
mi_diccionario["stock"] -= 1
print(mi_diccionario["stock"])
print("Mensaje Final: ")
print("Producto: ", mi_diccionario["nombre"])
print("Precio actualizado: ", mi_diccionario["precio"])
print("Stock restante: ", mi_diccionario["stock"])
# alternativa:
#print(f"Producto: {mi_diccionario["nombre"]}, etc etc)
