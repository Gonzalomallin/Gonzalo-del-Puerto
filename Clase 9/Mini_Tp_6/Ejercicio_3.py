libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]

for titulo, autor, anio, genero in libros:
    if anio > 2010:
        print(f"Libros publicados después del 2010: {autor}, {anio}")

generos_unicos = {libro[3] for libro in libros}
print(f"Los géneros disponibles son: {generos_unicos}")

cant_genero = {}

for titulo, autor, anio, genero in libros:
    if genero not in cant_genero:
        cant_genero[genero] = 0
        cant_genero[genero] += 1

for genero, cantidad in cant_genero.items():
    print(f"La cantidad de unidades por género es: {genero}: {cantidad}")
