
# Importar librerías
import numpy as np
import random
import keyboard  # Para capturar la tecla Esc

# importar variables-constantes
from Hundir_la_flota_constantes import agua,tocado,coordenadas,tablero_agua,tablero_barco,tablero_dim

##### Función para crear el tablero #####
def crear_tablero(dimension_tablero):
    tablero = np.full((dimension_tablero, dimension_tablero), " ")
    return tablero

##### Función para crear barco de la maquina #####
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
        # jugador_objetivo.mostrar_tablero()
        return False
    elif jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_barco:
        print("El disparo ha tocado un barco")
        jugador_objetivo.reducir_vidas()
        jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
        # jugador_objetivo.mostrar_tablero()
        print("La IA dispara de nuevo.")
        return True

##### Función disparo aleatorio_v2 #####
def disparo_aleatorio_v2(jugador_objetivo):
    """
    Realiza un disparo aleatorio para la máquina.
    """
    indice_limite = jugador_objetivo.tablero.shape[0] - 1
    while True:
        coordenada_fila_disparo = random.randint(1, indice_limite)
        coordenada_columna_disparo = random.randint(1, indice_limite)

        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] in [agua, tocado]:
            continue

        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_agua:
            print("La máquina disparó y cayó en el agua.")
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = agua
            return False

        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_barco:
            print("La máquina disparó y tocó un barco tuyo.")
            jugador_objetivo.reducir_vidas()
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
            return True


##### Función disparo manual #####
def disparo_manual(jugador_objetivo):
    disparo_correcto = False
    while not disparo_correcto:
        disparo_correcto = True
        coordenada_fila_disparo = int(input("Coordenada fila (1-10): "))
        coordenada_columna_disparo = int(input("Coordenada columna (1-10): "))
        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_agua:
            print("El disparo ha caído en el agua")
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = agua
            jugador_objetivo.mostrar_historial_disparos()
            return False
        elif jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_barco:
            print("El disparo ha tocado un barco")
            jugador_objetivo.reducir_vidas()
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
            jugador_objetivo.mostrar_historial_disparos()
            return True

######## Función disparo manual v2 ########
def disparo_manual_v2(jugador_objetivo):
    disparo_correcto = False  # Inicializamos en False
    while not disparo_correcto:  # Mientras disparo_correcto sea False, el bucle se ejecuta
        # validar valores de entrada de las coordenadas
        try:
            # Solicitar coordenadas
            coordenada_fila_disparo = int(input("Coordenada fila (1-10): "))
            coordenada_columna_disparo = int(input("Coordenada columna (1-10): "))
        except ValueError:
            # Si el jugador ingresa algo que no es un número entero
            print("Entrada inválida. Por favor, ingresa un número entero entre 1 y 10.")
            continue  # Salta al siguiente ciclo del bucle
        
        # Verificar si las coordenadas están fuera del tablero
        if coordenada_fila_disparo > tablero_dim or coordenada_columna_disparo > tablero_dim:
            print("Coordenadas fuera del tablero. Por favor, ingresa coordenadas válidas (1-10).")
            continue  # Salta al siguiente ciclo del bucle
        
        # Verificar si las coordenadas ya fueron disparadas
        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] in [agua, tocado]:
            print("Ya disparaste a esa posición. Elige nuevas coordenadas.")
            continue  # Salta al siguiente ciclo del bucle
        
        # Disparo en agua
        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_agua:
            print("El disparo ha caído en el agua")
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = agua
            # jugador_objetivo.mostrar_historial_disparos()
            disparo_correcto = True  # Disparo válido, salimos del bucle
            return False  # Retorna False porque el disparo no impactó un barco
        
        # Disparo en barco
        elif jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_barco:
            print("El disparo ha tocado un barco")
            jugador_objetivo.reducir_vidas()
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
            print("\nTus disparos sobre el rival:")
            jugador_objetivo.mostrar_historial_disparos()
            disparo_correcto = True  # Disparo válido, salimos del bucle
            return True  # Retorna True porque el disparo impactó un barco


def disparo_manual_v3(jugador_objetivo):
    """
    Permite al jugador disparar manualmente. Muestra mensajes claros según el resultado del disparo.
    """
    disparo_correcto = False
    while not disparo_correcto:
        try:
            coordenada_fila_disparo = int(input("Coordenada fila (1-10): "))
            coordenada_columna_disparo = int(input("Coordenada columna (1-10): "))
        except ValueError:
            print("Entrada inválida. Ingresa un número entero entre 1 y 10.")
            continue

        if coordenada_fila_disparo < 1 or coordenada_columna_disparo < 1 or \
           coordenada_fila_disparo > tablero_dim or coordenada_columna_disparo > tablero_dim:
            print("Coordenadas fuera del tablero. Por favor, inténtalo de nuevo.")
            continue

        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] in [agua, tocado]:
            print("Ya disparaste a esta posición. Intenta otra coordenada.")
            continue

        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_agua:
            print("¡El disparo cayó en el agua!")
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = agua
            return False

        if jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] == tablero_barco:
            print("¡Tocaste un barco enemigo!. Aquí está tu historial de disparos actualizados:")
            jugador_objetivo.reducir_vidas()
            jugador_objetivo.tablero[coordenada_fila_disparo, coordenada_columna_disparo] = tocado
            jugador_objetivo.mostrar_historial_disparos()
            return True


# Función para verificar la victoria
def verificar_victoria(jugador, maquina):
    if jugador.vidas == 0:
        print("\nNo te quedan más barcos. Has perdido. 😔")
        return True
    elif maquina.vidas == 0:
        print("\n¡Has hundido todos los barcos del rival! ¡Victoria! 🎉")
        return True
    return False

# Función para manejar salida con Esc
def verificar_salida():
    if keyboard.is_pressed('esc'):
        print("\nHas presionado 'Esc'. ¿Estás seguro de que deseas salir? (s/n)")
        confirmar_salida = input("--> ").strip().lower()
        if confirmar_salida == 's':
            print("\nGracias por jugar. ¡Hasta la próxima! 😊")
            exit()  # Sale del programa