
# importar librería
import numpy as np

# importar funciones
from Hundir_la_flota_funciones import crear_tablero,crear_barco  # Solo importar lo necesario

# importar variables-constantes
from Hundir_la_flota_constantes import tablero_dim,barcos,tablero_barco,tablero_agua

# Crear clase jugador
class Jugador():
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = self.crear_tablero_jugador()
        # Las vidas serán el número total de posiciones de barcos que se tiene inicialmente
        self.vidas = list(self.tablero.ravel()).count(tablero_barco)
    
    # función para colocar los barcos del jugador
    def crear_tablero_jugador(self):
        # Definimos aquí el método crear_tablero_jugador para evitar el import circular
        # tablero = crear_tablero(10)
        tablero = crear_tablero(tablero_dim)
        # lista_barcos = [[4, 1], [3, 2], [2, 3], [1, 4]]
        lista_barcos = barcos 
        for barco in lista_barcos:
            for _ in range(barco[0]):
                # from Hundir_la_flota_funciones import crear_barco
                crear_barco(tablero=tablero, longitud_barco=barco[1])
        tablero = np.vstack([np.arange(1, 11), tablero])
        tablero = np.hstack([np.arange(0, 11).reshape(11, 1), tablero])
        return tablero
    
    def reducir_vidas(self):
        self.vidas -= 1
        # print(f"Al jugador {self.id_jugador} le quedan {self.vidas} vidas.")
    
    def mostrar_tablero(self):
        print(self.tablero)
    
    # Devuelve los disparos que le han hecho al jugador pero oculta los barcos
    def mostrar_historial_disparos(self):
        copia = self.tablero.copy()
        shape = copia.shape
        copia = list(copia.ravel())
        for index, value in enumerate(copia):
            if value == tablero_barco:
                copia[index] = " "
        copia = np.array(copia).reshape(shape)
        print(copia)


# Crear clase jugador 2
class Jugador_v2():
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.tablero = self.crear_tablero_jugador()
        # Las vidas serán el número total de posiciones de barcos que se tiene inicialmente
        self.vidas = list(self.tablero.ravel()).count(tablero_barco)
    
    # función para colocar los barcos del jugador
    def crear_tablero_jugador(self):
        # Definimos aquí el método crear_tablero_jugador para evitar el import circular
        # tablero = crear_tablero(10)
        tablero = crear_tablero(tablero_dim)
        # lista_barcos = [[4, 1], [3, 2], [2, 3], [1, 4]]
        lista_barcos = barcos 
        for barco in lista_barcos:
            for _ in range(barco[0]):
                # from Hundir_la_flota_funciones import crear_barco
                crear_barco(tablero=tablero, longitud_barco=barco[1])
        tablero = np.vstack([np.arange(1, 11), tablero])
        tablero = np.hstack([np.arange(0, 11).reshape(11, 1), tablero])
        return tablero
    
    def reducir_vidas(self):
        self.vidas -= 1
        # print(f"Al jugador {self.id_jugador} le quedan {self.vidas} vidas.")
    
    def mostrar_tablero(self):
        """
        Imprime el tablero completo del jugador, incluidos los barcos.
        """
        print("\nTablero del jugador:")
        print(self.tablero)
    
    # Devuelve los disparos que le han hecho al jugador pero oculta los barcos
    def mostrar_historial_disparos(self):
        """
        Imprime el historial de disparos realizados sobre el jugador, ocultando los barcos intactos.
        """
        copia = self.tablero.copy()
        # Ocultar los barcos intactos
        copia = np.where(copia == tablero_barco, ".", copia)
        print("\nHistorial de disparos sobre este jugador:")
        for fila in copia:
            print(" ".join(fila))  # Imprimir fila por fila de manera legible


