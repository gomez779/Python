class Libro:
    """Clase que representa un libro con título, autor, ISBN y estado de disponibilidad."""

    def __init__(self, titulo, autor, isbn):
        """
        Inicializa un nuevo libro.
        
        Parámetros:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        isbn (int): El número ISBN del libro.
        """
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True


    def prestar(self):
        """
        Marca el libro como no disponible.
        
        Lanza:
        FileExistsError: Si el libro ya está prestado.
        """
        if self.__disponible:
            self.__disponible = False
        else:
            raise FileExistsError("El libro esta prestado")

    def devolver(self):
        if self.__disponible:
            raise FileExistsError("El libro esta disponible")
        else:
            self.__disponible = True

    def __str__(self):
        if self.__disponible:
            return f"{self.__titulo} esta Disponible, su autor: {self.__autor}"
        else:
            return f"{self.__titulo} esta Ocupado"
    @property
    def get_titulo(self):
        return self.__titulo

    @property
    def get_disponible(self):
        return self.__disponible

class Usuario:

    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni
        self.__libros_prestados = []

    def prestarLibro(self, libro):
        if len(self.__libros_prestados) <= 3:
            if libro.get_disponible:
                self.__libros_prestados.append(libro)
                libro.prestar()
            else:
                raise FileExistsError("El libro ya esta prestado")
        else:
            raise ValueError("El numero máximo de libros prestados es de 3")

    def DevolverLibro(self, libro):
        if libro.get_disponible:
            raise FileExistsError("El libro ya esta prestado")
        else:
            self.__libros_prestados.remove(libro)
            libro.devolver()
    @property
    def get_librosPrestados(self):
        if self.__libros_prestados:#Esto comprueba si la lista está vacía
            return [libro.get_titulo for libro in self.__libros_prestados]
        return f"Ningún libro prestado"

    def __str__(self):
        return f"{self.__nombre} con DNI: {self.__dni} tiene estos libros prestados {self.get_librosPrestados}"

MiLibro = Libro("Quijote", "yo", 3020 )
MiLibro2 = Libro("Quijote2", "tu", 4020 )
MiLibro3 = Libro("Quijote3", "elOtro", 5020 )
MiUsuario = Usuario("German",  51184115J)

print(MiLibro)

MiUsuario.prestarLibro(MiLibro)
MiUsuario.prestarLibro(MiLibro2)
MiUsuario.prestarLibro(MiLibro3)
print(MiUsuario.get_librosPrestados)

MiUsuario.DevolverLibro(MiLibro3)
print(MiUsuario.get_librosPrestados)