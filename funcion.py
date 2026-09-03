class Funcion:

    def __init__(self, fecha, hora, precio):
        self.__fecha = fecha
        self.__hora = hora
        self.__precio = precio

    def mostrar_datos(self):
        return f"Fecha: {self.__fecha}, Hora: {self.__hora}, Precio: {self.__precio}"

    def es_funcion_nocturna(self):
        if self.__hora >= 1900:
            return "es funcion nocturna"
        else:
            return "es funcion diurna"

    # hora = int(self.__hora.split(":"[0]))
    # return hora >= 20