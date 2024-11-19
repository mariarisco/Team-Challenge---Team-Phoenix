# Importar clase
from Hundir_la_flota_clases import Jugador

# Importar funciones
from Hundir_la_flota_funciones import disparo_aleatorio, disparo_manual, limpiar_pantalla

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
while declaracion_victoria == False:
                
        valid_options = ["1","2","3","4","5"]
        print("\n---Menu---")
        print("Introduce 1 para hacer un disparo")
        print("Introduce 2 para ver tu Tablero")
        print("Introduce 3 para ver tu historial de disparos (Tablero rival)")
        print("Introduce 4 para ver el numero de vidas del rival")
        print("Introduce 5 para ver tus vidas\n")
        menu = input("--> ").strip()
        limpiar_pantalla()
        
        while menu not in valid_options:
            print("Opcion introducida no valida.\n")
            print("\n---Menu---")
            print("Introduce 1 para hacer un disparo")
            print("Introduce 2 para ver tu Tablero")
            print("Introduce 3 para ver tu historial de disparos")
            print("Introduce 4 para ver el numero de vidas del rival")
            print("Introduce 5 para ver tus vidas\n")
            menu = input("--> ").strip()
            limpiar_pantalla()
            
        if menu == "1":
            while disparo_manual(jugador_objetivo=maquina) == True and maquina.vidas > 1:
                pass

            print("\n----Turno de la IA----\n")
            while disparo_aleatorio(jugador_objetivo=jugador) == True and jugador.vidas >1:
                pass
            
            print()

        elif menu == "2":
            print("\nEste es tu tablero: \n")
            jugador.mostrar_tablero()
            print()
        
        elif menu == "3":
            print("\nEste es el historial de tus disparos: \n")
            maquina.mostrar_historial_disparos()
            print()
        
        elif menu == "4":
            if maquina.vidas > 1:
                print(f"\nA tu rival le quedan {maquina.vidas} vidas.\n")
            if maquina.vidas == 1:
                print(f"\nA tu rival le queda una (1) vida.\n")
        
        elif menu =="5":
            if jugador.vidas > 1:
                print(f"\nTe quedan {maquina.vidas} vidas.\n")
            if jugador.vidas == 1:
                print(f"\nSólo te queda una (1) vida.\n")
        
if jugador.vidas == 0:
    print("\nNo te quedan más barcos. Has perdido")
    declaracion_victoria = True
if maquina.vidas == 0:
    print("\n¡A tu rival no le quedan más barcos! ¡Victoria!")
    declaracion_victoria = True