import os  # Para limpiar el terminal

from Hundir_la_flota_clases import Jugador, Jugador_v2
from Hundir_la_flota_funciones import disparo_aleatorio_v2,disparo_manual_v3,verificar_victoria

"""
Juego Hundir la Flota.
"""

# Mostrar mensajes iniciales
print("\n¡Empieza la batalla naval! 🌊")
print("Vas a jugar contra una máquina a Hundir la flota. \nCada jugador tiene una flota de 4 barcos. \n")
print("Si aciertas un disparo sobre el barco de tu rival, vuelves a disparar. \nSe lanzarán disparos por turnos hasta que uno de los jugadores hunda toda la flota del rival. \n")
print("Suerte!")

# Configuración inicial del juego
nombre_usuario = input("Introduce el nombre del jugador: ")
jugador = Jugador(id_jugador=nombre_usuario)
maquina = Jugador(id_jugador="IA")
declaracion_victoria = False

# Pausar para leer las instrucciones
input("\nPresiona Enter para comenzar el juego...")

# Bucle principal del juego
while not declaracion_victoria:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar terminal al inicio del bucle

    print("\n--- ESTADO DEL JUEGO ---")
    print("Tu tablero:")
    jugador.mostrar_tablero()
    print("\nTus disparos sobre el rival:")
    maquina.mostrar_historial_disparos()
    print(f"\nTus vidas: {jugador.vidas} | Vidas del rival: {maquina.vidas}")

    print("\n--- TU TURNO ---")
    while disparo_manual_v3(jugador_objetivo=maquina) and maquina.vidas > 0:
        # print("Tu disparo fue acertado. Aquí está el historial actualizado.")
        continue

    declaracion_victoria = verificar_victoria(jugador, maquina)
    if declaracion_victoria:
        break

    print("\n--- TURNO DE LA MÁQUINA ---")
    while disparo_aleatorio_v2(jugador_objetivo=jugador) and jugador.vidas > 0:
        continue

    declaracion_victoria = verificar_victoria(jugador, maquina)

    # Preguntar al jugador si quiere seguir jugando
    print("\n¿Quieres seguir jugando? (s/n)")
    continuar = input("--> ").strip().lower()
    if continuar == 'n':
        print("\nGracias por jugar. ¡Hasta la próxima! 😊")
        break
    elif continuar != 's':
        print("\nOpción inválida. Por favor, responde con 's' para sí o 'n' para no.")
        continue  # Vuelve a preguntar si la entrada es inválida

