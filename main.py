from pelicula import Pelicula
from funcion import Funcion
from sala import Sala

def main():

    pelicula_uno = Pelicula("Rapido y furioso", "accion", 123)
    print(pelicula_uno.mostrar_datos())

    #al ser un void, no debe usar print en el main ya que ya se uso en la clase pelicula, por lo tanto solo llamamos
    #pelicula_uno.mostrar_datos()
    funcion_uno = Funcion("02/20", 1600, 4500)
    print(funcion_uno.mostrar_datos())
    print(funcion_uno.es_funcion_nocturna())

    sala_1 = Sala(3, 150)
    sala_1.mostrar_datos()

    print(sala_1.hay_disponibilidad(145))



if __name__ == "__main__":
    main()