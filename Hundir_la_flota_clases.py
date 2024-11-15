
# importar librería
import numpy as np
from Hundir_la_flota_funciones import crear_tablero  # Solo importar lo necesario
from Hundir_la_flota_funciones import crear_barco

# Crear clase jugador
class Jugador():
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = self.crear_tablero_jugador()
        # Las vidas serán el número total de posiciones de barcos que se tiene inicialmente
        self.vidas = list(self.tablero.ravel()).count("O")
    
    def reducir_vidas(self):
        self.vidas -= 1
        print(f"Al jugador {self.id_jugador} le quedan {self.vidas} vidas.")
    
    def mostrar_tablero(self):
        print(self.tablero)
    
    # Devuelve los disparos que le han hecho al jugador pero oculta los barcos
    def mostrar_historial_disparos(self):
        copia = self.tablero.copy()
        shape = copia.shape
        copia = list(copia.ravel())
        for index, value in enumerate(copia):
            if value == "O":
                copia[index] = " "
        copia = np.array(copia).reshape(shape)
        print(copia)

    def crear_tablero_jugador(self):
        # Definimos aquí el método crear_tablero_jugador para evitar el import circular
        tablero = crear_tablero(10)
        lista_barcos = [[4, 1], [3, 2], [2, 3], [1, 4]]
        for barco in lista_barcos:
            for _ in range(barco[0]):
                # from Hundir_la_flota_funciones import crear_barco -> Lo metemos arriba
                crear_barco(tablero=tablero, longitud_barco=barco[1])
        tablero = np.vstack([np.arange(1, 11), tablero])
        tablero = np.hstack([np.arange(0, 11).reshape(11, 1), tablero])
        return tablero
