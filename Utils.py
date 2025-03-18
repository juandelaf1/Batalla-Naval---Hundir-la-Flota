import numpy as np
import random
import time as t


def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, '_')


def crear_barco_aleatorio(eslora):
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    barco_aleatorio = [(fila, columna)]

    orientacion = random.choice(["Horizontal", "Vertical"])
    while len(barco_aleatorio) < eslora:
        if orientacion == "Horizontal":
            columna = columna + 1
            if  0 <= columna <= 9:
                barco_aleatorio.append((fila, columna))
            else:
                return crear_barco_aleatorio(eslora)    
        else:
            fila = fila + 1
            if  0 <= fila <= 9:
                barco_aleatorio.append((fila, columna))            
            else:
                return crear_barco_aleatorio(eslora)   
    return barco_aleatorio

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


def colocar_barcos(barcos, tablero):
    for barco in barcos:
        tablero = colocar_barco(barco, tablero)
    return tablero


def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Acertaste")
        tablero[casilla] = "X"
        print(tablero)

    else:
        print("Fallaste")
        tablero[casilla]  = "A"
        print(tablero)
    return tablero



def disparar_a_maquina(casilla,tablero_m,tablero_mt):
    print("\n")
    if tablero_m[casilla]=="O":
        tablero_m[casilla]="X"
        tablero_mt[casilla]="X"
        print("\n")
        print(tablero_mt)
        print("TE TENGO!, AQUI VOY  DE NUEVO...")
        print("\n")
        return disparar_a_maquina((int(input("ingrese una posicion en la fila")), int(input("ingrese una posicion en la columna"))), tablero_m, tablero_mt)    
    else:
        tablero_m[casilla]="A"
        tablero_mt[casilla]="A"
        print("OH NO!! HE FALLADO, TU TURNO")
        print("\n")
        print(tablero_mt)
        print("\n")
        return tablero_m
    

def disparar_a_jugador(casilla,tablero_j):
    t.sleep(2)
    if tablero_j[casilla]=="O":
        tablero_j[casilla]="X"   
        print("\n") 
        print(tablero_j)
        print("\n") 
        print("TE ENCONTRE, MI TURNO NUEVAMENTE")
        return disparar_a_jugador((random.randint(0,9), random.randint(0,9)), tablero_j)
    else: 
        tablero_j[casilla]="A"
        print("\n")
        print(tablero_j)
        print("\n")
        print("POR POCO... VENGA, TE TOCA")
        return tablero_j