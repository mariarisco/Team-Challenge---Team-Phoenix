# Importar clase
from Hundir_la_flota_clases import Jugador

# Importar funciones
from Hundir_la_flota_funciones import disparo_aleatorio, disparo_manual

# Empieza el juego solicitando el nombre del jugador
nombre_usuario = input("Introduce el nombre del jugador: ")

# Se crean los jugadores
jugador = Jugador(id_jugador=nombre_usuario)
maquina = Jugador(id_jugador="IA")

# Se muestra el tablero del jugador
print("Este es tu tablero:")
jugador.mostrar_tablero()

# Variable de control para el bucle del juego
declaracion_victoria = False

# Bucle while para jugar la partida
while not declaracion_victoria:               
    print("\n--- Menú ---")
    print("1: Hacer un disparo")
    print("2: Ver tu Tablero")
    print("3: Ver tu historial de disparos")
    print("4: Ver vidas del rival")
    print("5: Ver tus vidas")

    menu = input("--> ").strip()
    if menu == "1":
        while disparo_manual(jugador_objetivo=maquina) and maquina.vidas > 1:
            pass
        print("\n---- Turno de la IA ----\n")
        while disparo_aleatorio(jugador_objetivo=jugador) and jugador.vidas > 1:
            pass            
    elif menu == "2":
        print("\nEste es tu tablero:")
        jugador.mostrar_tablero()
    elif menu == "3":
        print("\nHistorial de tus disparos:")
        maquina.mostrar_historial_disparos()
    elif menu == "4":
        print(f"\nA tu rival le quedan {maquina.vidas} vidas." if maquina.vidas > 1 else "\nA tu rival le queda una vida.")
    elif menu == "5":
        print(f"\nTe quedan {jugador.vidas} vidas." if jugador.vidas > 1 else "\nTe queda una vida.")
    
    if jugador.vidas == 0:
        print("\nNo te quedan más barcos. Has perdido")
        declaracion_victoria = True
    elif maquina.vidas == 0:
        print("\n¡Has hundido todos los barcos del rival! ¡Victoria!")
        declaracion_victoria = True
