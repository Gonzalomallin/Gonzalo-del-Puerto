libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("1984", "George Orwell", 1949, "Novela"),
    ("Rayuela", "Julio Cortázar", 1963, "Novela"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Armas, gérmenes y acero", "Jared Diamond", 1997, "Historia"),
    ("Historia mínima de América Latina", "Carlos Malamud", 2014, "Historia"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Cosmos", "Carl Sagan", 1980, "Ciencia"),
    ("Una breve historia del tiempo", "Stephen Hawking", 1988, "Ciencia"),
    ("El arte de la guerra", "Sun Tzu", -500, "Estrategia"),
    ("Pensar rápido, pensar despacio", "Daniel Kahneman", 2011, "Psicología")
]

# 1- Para mostrar los géneros disponibles sin repetir tengo que crear un set e ir agregando los géneros que 
# no están en ese set. Los géneros ocupan un lugar especifico dentro de la lista que contiene varias tuplas.
# 2- Pedir un input al usuario, sujeto a condiciones, para que aparezcan los géneros que busca, los que no y
# tambien la opción de salir del input.

genero_disponible = {libro[3] for libro in libros}
print(f"Los géneros disponibles son {genero_disponible}")

while True:
    busqueda = input("Ingrese un género: ")
    if busqueda == "salir":
        print(f"Gracias, hasta pronto. ")
        break
    elif busqueda in genero_disponible:
        print(f"Libros del género: {genero_disponible}")
        for titulo, autor, anio, genero in libros:
            if genero == busqueda:
                print(f"{titulo}, ({autor}, {anio})")
    else:
        print(f"El género {busqueda} no está disponible")