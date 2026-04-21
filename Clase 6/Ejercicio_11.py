lista_precios = ["Martillo: 3000", "Clavos: 500", "Destornillador: 1500"]

def obtener_precio(producto):
    
    return precios(producto)

lista_productos = []
total_dinero = 0

while True:
    nombre = input("Ingrese su producto (Fin para salir): ")
    
    if nombre == "Fin":
        print("Gracias por su compra. ")
        break
    
    precio = obtener_precio(nombre)
    
    if precio > 0:
        lista_productos.append(nombre)
        total_dinero += precio
        print(f"Agregado: {nombre} ($ {precio})")
    else:
        print("Producto no disponible o sin precio.") 




    
