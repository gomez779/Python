class persona():
    def __init__(self, pelo, estatura, talla, nombre, dni, sexo):
        self.__pelo = pelo
        self.__estatura = estatura
        self.__talla = talla
        self.__nombre = nombre
        self.__dni = dni
        self.sexo = sexo

    def accion(self):
        if self.sexo == "hombre":
            print(f"{self.__nombre} Se esta preparando para la maratón")
        else:
            print(f"{self.__nombre} Esta aprendiendo a cocinar")

    @property
    def get_pelo(self):
        return self.__pelo

    @property
    def get_nombre(self):
        return self.__nombre

    @get_pelo.setter
    def get_pelo(self, nuevo_pelo):
        self.__pelo = nuevo_pelo

    def tennirse(self):
        nuevo_pelo = input(f"¿De qué color quieres que se tiña {self.__nombre}? ")
        self.get_pelo = nuevo_pelo


class hombre(persona):
    def __init__(self, pelo, estatura, talla, nombre, dni):
        super().__init__(pelo, estatura, talla, nombre, dni, sexo="hombre")

class mujer(persona):
    def __init__(self, pelo, estatura, talla, nombre, dni):
        super().__init__(pelo, estatura, talla, nombre ,dni, sexo="mujer")


juan = hombre("negro", 190, 45, "juan", "04663762Y")
maria = mujer("rubio", 165, 36, "maria", "12839145O")

maria.accion()
juan.accion()
maria.tennirse()
juan.tennirse()
print(f"{juan.get_nombre} tiene el pelo de color {juan.get_pelo}")
print(f"{maria.get_nombre} tiene el pelo de color {maria.get_pelo}")
