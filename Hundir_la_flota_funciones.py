
# Importar librerías
import numpy as np
import random

# importar variables-constantes
from Hundir_la_flota_constantes import coordenadas,tocado,agua

##### Función para crear el tablero #####
# Esta función no se está utilizando
def crear_tablero(dimension_tablero):
    tablero = np.full((dimension_tablero, dimension_tablero), " ")
    return tablero

##### Función para crear barco #####
def crear_barco(tablero, longitud_barco):
    indice_limite = tablero.shape[0] - 1
    valido = False
    contador = 0
    while not valido and contador < 1000:
        contador += 1
        # orientacion = random.choice(["N", "S", "E", "O"])
        orientacion = random.choice(coordenadas)
        punto_origen_fila = random.randint(0, indice_limite)
        punto_origen_columna = random.randint(0, indice_limite)
        punto_final_fila, punto_final_columna = punto_origen_fila, punto_origen_columna

        if orientacion == "N":
            punto_origen_fila -= longitud_barco
            punto_final_columna += 1
        elif orientacion == "S":
            punto_final_fila += longitud_barco
            punto_final_columna += 1
        elif orientacion == "O":
            punto_origen_columna -= longitud_barco
            punto_final_fila += 1
        elif orientacion == "E":
            punto_final_columna += longitud_barco
            punto_final_fila += 1

        if all(0 <= val <= indice_limite for val in [punto_origen_fila, punto_final_fila, punto_origen_columna, punto_final_columna]) and "O" not in tablero[punto_origen_fila:punto_final_fila, punto_origen_columna:punto_final_columna]:
            valido = True
            tablero[punto_origen_fila:punto_final_fila, punto_origen_columna:punto_final_columna] = "O"

##### Función disparo aleatorio #####
def disparo_aleatorio(jugador_objetivo):
    indice_limite = jugador_objetivo.tablero.shape[0] - 1
    coordenada_fila_disparo = random.randint(1, indice_limite)
    coordenada_columna_disparo = random.randint(1, indice_limite)
    while jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] in ["-", "X"]:
        coordenada_fila_disparo = random.randint(1, indice_limite)
        coordenada_columna_disparo = random.randint(1, indice_limite)

    if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == " ":
        print("El disparo ha caído en el agua")
        # jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = "-"
        jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = agua
        jugador_objetivo.mostrar_tablero()
        return False
    elif jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == "O":
        print("El disparo ha tocado un barco")
        jugador_objetivo.reducir_vidas()
        # jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = "X"
        jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
        jugador_objetivo.mostrar_tablero()
        print("La IA dispara de nuevo.")
        return True

##### Función disparo manual #####
def disparo_manual(jugador_objetivo):
    disparo_correcto = False
    while not disparo_correcto:
        disparo_correcto = True
        coordenada_fila_disparo = int(input("Coordenada fila (1-10): "))
        coordenada_columna_disparo = int(input("Coordenada columna (1-10): "))
        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == " ":
            print("El disparo ha caído en el agua")
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = "-"
            jugador_objetivo.mostrar_historial_disparos()
            return False
        elif jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == "O":
            print("El disparo ha tocado un barco")
            jugador_objetivo.reducir_vidas()
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = "X"
            jugador_objetivo.mostrar_historial_disparos()
            return True
