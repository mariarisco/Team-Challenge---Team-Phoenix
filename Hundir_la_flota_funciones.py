
# Importar librerías
import os
import numpy as np
import random

# importar variables-constantes
from Hundir_la_flota_constantes import agua,tocado,coordenadas,tablero_agua,tablero_barco

##### Función para crear el tablero #####
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
        orientacion = random.choice(coordenadas)
        # orientacion = random.choice(["N", "S", "E", "O"])
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

        if all(0 <= val <= indice_limite for val in [punto_origen_fila, punto_final_fila, punto_origen_columna, punto_final_columna]) and tablero_barco not in tablero[punto_origen_fila:punto_final_fila, punto_origen_columna:punto_final_columna]:
            valido = True
            tablero[punto_origen_fila:punto_final_fila, punto_origen_columna:punto_final_columna] = tablero_barco

##### Función disparo aleatorio #####
def disparo_aleatorio(jugador_objetivo):
    indice_limite = jugador_objetivo.tablero.shape[0] - 1
    coordenada_fila_disparo = random.randint(1, indice_limite)
    coordenada_columna_disparo = random.randint(1, indice_limite)
    while jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] in [agua, tocado]:
        coordenada_fila_disparo = random.randint(1, indice_limite)
        coordenada_columna_disparo = random.randint(1, indice_limite)

    if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_agua:
        print("El disparo ha caído en el agua")
        jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = agua
        jugador_objetivo.mostrar_tablero()
        return False
    elif jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_barco:
        print("El disparo ha tocado un barco")
        jugador_objetivo.reducir_vidas()
        jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
        jugador_objetivo.mostrar_tablero()
        print("La IA dispara de nuevo.")
        return True

##### Función disparo manual #####
def disparo_manual(jugador_objetivo):
    
    #Creamos esta variable para que entre en bucle. Despues la pasamos a True para salir. 
    #Solo se vuelve False y repite el bucle si el usuario dispara en una celda donde ya disparó
    #Ver ultimo if de esta funcion
    disparo_correcto = False
    while disparo_correcto == False:
        disparo_correcto = True

        check_flag = False
        while check_flag == False:

            #Primero comprobamos que no se introducen "Floats"
            coordenada_fila_disparo = input("Coordenada fila (1-10): ")
            while "," in coordenada_fila_disparo or "." in coordenada_fila_disparo:
                input("Coordenada incorrecta. Introduzca de nuevo. \nCoordenada fila: ")
            
            try:
                coordenada_fila_disparo = int(coordenada_fila_disparo)
                if 1 <= coordenada_fila_disparo <= 10:
                    check_flag = True
                else:
                    print("Coordenada fuera de los límites. Introduzca de nuevo.\n")
            except:
                print("Coordenada incorrecta. Introduzca de nuevo")
            
        check_flag = False
        while check_flag == False:

            #Primero comprobamos que no se introducen "Floats"
            coordenada_columna_disparo = input("Coordenada columna (1-10): ")
            while "," in coordenada_columna_disparo or "." in coordenada_columna_disparo:
                input("Coordenada incorrecta. Introduzca de nuevo. \nCoordenada columna: ")
            
            try:
                coordenada_columna_disparo = int(coordenada_columna_disparo)
                if 1 <= int(coordenada_columna_disparo) <= 10:
                    check_flag = True
                else:
                    print("Coordenada fuera de los límites. Introduzca de nuevo.\n")           
            except:
                print("Coordenada incorrecta. Introduzca de nuevo")
                
        #Si la coordenada coincide con una celda vacia, caerá en el agua
        if jugador_objetivo.tablero[coordenada_fila_disparo,coordenada_columna_disparo] == " ":
            print("El disparo ha caido en el agua \n")
            jugador_objetivo.tablero[coordenada_fila_disparo,coordenada_columna_disparo] = "-"
            jugador_objetivo.mostrar_historial_disparos()

            return False
        
        #Si coincide con una celda llena, caerá en un barco
        elif jugador_objetivo.tablero[coordenada_fila_disparo,coordenada_columna_disparo] == "O":
            print("El disparo ha tocado un barco \n")
            jugador_objetivo.reducir_vidas()
            jugador_objetivo.tablero[coordenada_fila_disparo,coordenada_columna_disparo] = "X"
            jugador_objetivo.mostrar_historial_disparos()
            print("Dispara de nuevo. \n")

            return True
        
        elif jugador_objetivo.tablero[coordenada_fila_disparo,coordenada_columna_disparo] == "-" or jugador_objetivo.tablero[coordenada_fila_disparo,coordenada_columna_disparo] == "X":
            print("Ya se ha disparado en esa celda. Prueba de nuevo \n")
            jugador_objetivo.mostrar_historial_disparos()
            disparo_correcto = False


#### Funcion para limpiar la consola de salida
def limpiar_pantalla():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS y Linux
        os.system('clear')