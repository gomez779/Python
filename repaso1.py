"""
Ejercicio: Gestión de Vehículos
Crea un sistema para gestionar vehículos en un concesionario. Debes implementar las siguientes clases:

Clase base Vehicle

Atributos: brand (marca), model (modelo), year (año), price (precio).

Método get_info(): devuelve una cadena con la información del vehículo.

Método apply_discount(discount): aplica un descuento en el precio.

Clase Car (hereda de Vehicle)

Atributo adicional: doors (cantidad de puertas).

Sobrescribe get_info() para incluir la cantidad de puertas.

Clase Motorcycle (hereda de Vehicle)

Atributo adicional: type (tipo de moto, ej. "deportiva", "crucero").

Sobrescribe get_info() para incluir el tipo de moto.

Crea una lista de vehículos y muestra la información de cada uno.

Aplica un descuento del 10% a todos los vehículos y muestra el precio actualizado.
Autor: German Cosano Torres
"""

class vehiculo:
    def __init__(self, marca, modelo, year, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__year = year
        self.__precio = precio


    def get_info(self):
        return f"Tu vehiculo: {self.__marca} {self.__modelo} del año {self.__year} vale {self.__precio} €"

    def descuento(self, descuento):
        total = self.__precio * (1 - descuento / 100)
        return total

class coche(vehiculo):
    def __init__(self, marca, modelo, year, precio, doors):
        super().__init__( marca, modelo, year, precio)
        self.__doors = doors

    def get_info(self):
        return super().get_info() + f", con {self.__doors} puertas."

    def __str__(self):
        return f"{self.get_info()}"



MiVehicule = vehiculo("ford", "focus", 2019, 3000)
MiCoche = coche("ford", "focus", 2019, 3000, 4)

print(MiVehicule.get_info())
print(f"El precio del coche con descuento es de {MiVehicule.descuento(20)} €")

print(MiCoche)
