import Utils as u
import random


tablero_j = u.crear_tablero()
tablero_m = u.crear_tablero()
tablero_mt = u.crear_tablero()

barco_1j = u.crear_barco_aleatorio(2)
barco_2j = u.crear_barco_aleatorio(2)
barco_3j = u.crear_barco_aleatorio(2)
barco_4j = u.crear_barco_aleatorio(3)
barco_5j = u.crear_barco_aleatorio(3)
barco_6j = u.crear_barco_aleatorio(4)

barcosj = [barco_1j, barco_2j, barco_3j,barco_4j,barco_5j,barco_6j]

barco_1m = u.crear_barco_aleatorio(2)
barco_2m = u.crear_barco_aleatorio(2)
barco_3m = u.crear_barco_aleatorio(2)
barco_4m = u.crear_barco_aleatorio(3)
barco_5m = u.crear_barco_aleatorio(3)
barco_6m = u.crear_barco_aleatorio(4)

barcosm = [barco_1m, barco_2m, barco_3m,barco_4m,barco_5m,barco_6m]

tablero_j = u.colocar_barcos(barcosj, tablero_j)
tablero_m = u.colocar_barcos(barcosm, tablero_m)

input("Bienvenid@s a HUNDIR LA FLOTA. Marca 1 para comenzar a jugar")


while 'O' in tablero_j and 'O' in tablero_m:
    tablero_m = u.disparar_a_maquina((int(input("fila")), int(input("columna"))), tablero_m,tablero_mt)
    tablero_j = u.disparar_a_jugador((random.randint(0,9), random.randint(0,9)), tablero_j)

    print("Tablero jugador\n", tablero_j)
    print("Tablero maquina\n", tablero_m)