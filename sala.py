class Sala:

    def __init__(self, numero, capacidad):
        self.__numero = numero
        self.__capacidad = capacidad

    def mostrar_datos(self):
        print(f"numero: {self.__numero} - capacidad: {self.__capacidad} asientos")
        

    def hay_disponibilidad(self, entradas_vendidas):
        if entradas_vendidas < self.__capacidad:
            return "Hay Disponibilidad"
        return "No Hay Disponibilidad"