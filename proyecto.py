class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.calificacion = None

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_leidos = []

    def agregar_libro_leido(self, libro, calificacion):
        libro.calificacion = calificacion
        self.libros_leidos.append(libro)

    def recibir_recomendacion(self, genero_interes):
        recomendaciones = [libro for libro in biblioteca if libro.genero == genero_interes and libro not in self.libros_leidos]
        return recomendaciones

biblioteca = [
    Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Romance"),
    Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico"),
    Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía")
]


usuario1 = Usuario("Andrea")


libro_leido = biblioteca[0]
usuario1.agregar_libro_leido(libro_leido, 4.5)


recomendaciones_usuario1 = usuario1.recibir_recomendacion("Romance")

print(f"Recomendaciones para {usuario1.nombre}:")
for libro in recomendaciones_usuario1:
    print(f"- {libro.titulo} by {libro.autor}")

