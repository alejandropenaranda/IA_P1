import pygame , sys
import random
import math
import numpy as np
from nodes import Nodo

# Aqui se abre el archivo de texto que contiene el mapa y se guarda en la variable board en forma de matriz
archivo = open("Prueba1.txt")
info = archivo.readlines()
#print(info)
archivo.close()

#funcion que le pregunta al usuario que algoritmo desea ejecutar
def escogerAlgoritmo():
    choice = input("ingrese el nombre del algoritmo de busqueda que desee ejecutar (costo, amplitud, profundidad, nombre, nombre):")
    if choice == "costo":
        return choice
    elif choice == "amplitud":
        return choice
    elif choice == "profundidad":
        return choice
    elif choice == "nombre":
        return choice
    elif choice == "nombre":
        return choice
    else:
        print("escoja un algoritmo de busqueda valido")
        sys.exit()

#__________________________________________definicion de variables globales

algoritmo = escogerAlgoritmo()
solucion  = []

#Creamos un nodo unicial, en donde se guardara el estado inicial
nodo_raiz= Nodo(costo=0, semillas=[], bolas=[], freezers=[], cells=[], kakaroto=[])
cola = [] #se guardaran los nodos en este array
board = []
count = 0

for i in info:
    fila = i.split()
    for h in range(len(fila)):
        fila[h] = int(fila[h])
    board.append(fila)

#Se crea una matriz de 10x10
mapa = np.zeros((10, 10), dtype=int)
#funcion que encuentra la posicion inicial de todos los elementos del tablero

def find_initial_positions(board):
    freezers = []
    cells = []
    balls = []
    seeds = []
    goku = []
    kakaroto = None
    for i in range(len(board)):
        for h in range(len(board)):
            if board[i][h] == 1:
                mapa[[i],[h]]=1
            elif board[i][h] == 2:
                goku.append([i,h])
                mapa[[i],[h]]=0
                kakaroto = [i,h]
            elif board[i][h] == 3:
                freezers.append([i,h])
                mapa[[i],[h]]=3
            elif board[i][h] == 4:
                cells.append([i,h])
                mapa[[i],[h]]=4
            elif board[i][h] == 5:
                seeds.append([i,h])
                mapa[[i],[h]]=5
            elif board[i][h] == 6:
                balls.append([i,h])
                mapa[[i],[h]]=6

    nodo_raiz.semillas=seeds
    nodo_raiz.bolas=balls
    nodo_raiz.freezers=freezers
    nodo_raiz.cells=cells
    nodo_raiz.kakaroto=kakaroto
    print("mapa:",mapa)
    print('board:', board)
    print("despues:")
    print("Semillas",nodo_raiz.showSemillas())
    print("Bolas",nodo_raiz.showBolas())
    print("freezers",nodo_raiz.showFreezers())
    print("Cells",nodo_raiz.showCells())
    print("Kakaroto",nodo_raiz.showKakaroto())

    print("----------------")
    cola.append(nodo_raiz)
    return goku,freezers,cells,seeds,balls

def puede_moverse(nodo):
    print("posicion inicial kakaroto:",nodo.showKakaroto())
    nodos_posibles = []
    #nodos_recorridos = nodo.recorrer_arbol_arriba()

    #----------arriba-------------
    fila_nueva = nodo.showKakaroto()[0] - 1

    #0,Si es un espacio vacio
    if fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 0:
        print("arriba espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #3,Si es un Frezzer
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 3:
        print("arriba Frezzer")
        nodo_aux = Nodo(nodo.costo+4, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Frezzer",nodo_aux.showFreezers())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
    
    #4,Si es un Cell
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 4:
        print("arriba Cell")
        nodo_aux = Nodo(nodo.costo+7, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Cell",nodo_aux.showCells())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #5,Si es una semilla, falta poner la logica para la semilla
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 5:
        semillas = nodo.showSemillas().copy()
        if [fila_nueva, nodo.showKakaroto()[1]] in nodo.showSemillas():
            print("arriba Semilla")
            print("semillas antes de eliminar", nodo.showSemillas())
            semillas.remove([fila_nueva,nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Semillas",nodo_aux.showSemillas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Semillas",nodo_aux.showSemillas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
        #nodo.semillas.append([fila_nueva,nodo.showKakaroto()[1]])#Se vuelve a agregar al nodo raiz la semilla que fue recolectada por kakaroto para el calculo de las demas posiciones

            

    #6,Si es una esfera, falta poner la logica para la esfera
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 6:
        bolas = nodo.showBolas().copy()
        if [fila_nueva, nodo.showKakaroto()[1]] in nodo.showBolas():
            print("arriba esfera")
            print("bolas antes de eliminar", nodo.showBolas())
            bolas.remove([fila_nueva,nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Esferas",nodo_aux.showBolas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Esferas",nodo_aux.showBolas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
        #nodo.bolas.append([fila_nueva,nodo.showKakaroto()[1]])#Se vuelve a agregar al nodo raiz la bola que fue recolectada por kakaroto para el calculo de las demas posiciones
    else:
        print("no arriba")


    print("--------")
    #----------------izquierda------------
    columna_nueva = nodo.showKakaroto()[1] - 1
    if columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 0:
        print("izquierda espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #3,Si es un Frezzer
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 3:
        print("izquierda Frezzer")
        nodo_aux = Nodo(nodo.costo+4, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Frezzer",nodo_aux.showFreezers())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #4,Si es un Cell
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 4:
        print("izquierda Cell")
        nodo_aux = Nodo(nodo.costo+7, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Cell",nodo_aux.showCells())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #5,Si es una semilla, falta poner la logica para la semilla
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 5:
        semillas = nodo.showSemillas().copy()
        if [nodo.showKakaroto()[0], columna_nueva] in nodo.showSemillas():
            print("izquierda semilla")
            print("semillas antes de eliminar", nodo.showSemillas())
            semillas.remove([nodo.showKakaroto()[0],columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Semillas",nodo_aux.showSemillas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Semillas",nodo_aux.showSemillas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
            #nodo.semillas.append([nodo.showKakaroto()[0],columna_nueva])#Se vuelve a agregar al nodo raiz la semilla que fue recolectada por kakaroto para el calculo de las demas posiciones

    #6,Si es una esfera, falta poner la logica para la esfera
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 6:
        bolas = nodo.showBolas().copy()
        if [nodo.showKakaroto()[0], columna_nueva] in nodo.showBolas():
            print("izquierda esfera")
            print("bolas antes de eliminar", nodo.showBolas()) 
            bolas.remove([nodo.showKakaroto()[0],columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Comparacion estado izquierda")
                print("Esferas",nodo_aux.showBolas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("No Comparacion estado izquierda")
            print("Esferas",nodo_aux.showBolas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
        #nodo.bolas.append([nodo.showKakaroto()[0],columna_nueva])#Se vuelve a agregar al nodo raiz la bola que fue recolectada por kakaroto para el calculo de las demas posiciones
    else:
        print("no izquierda")

    print("--------")
    #-----------abajo-----------
    fila_nueva = nodo.showKakaroto()[0] + 1

    if fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 0:
        print("abajo espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

#***
    #3,Si es un Frezzer
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 3:
        print("abajo Frezzer")
        nodo_aux = Nodo(nodo.costo+4, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Frezzer",nodo_aux.showFreezers())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
    
    #4,Si es un Cell
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 4:
        print("abajo Cell")
        nodo_aux = Nodo(nodo.costo+7, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Cell",nodo_aux.showCells())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #5,Si es una semilla, falta poner la logica para la semilla
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 5:
        semillas = nodo.showSemillas().copy()
        if [fila_nueva, nodo.showKakaroto()[1]] in nodo.showSemillas():
            print("abajo semilla")
            print("semillas antes de eliminar",nodo.showSemillas())
            semillas.remove([fila_nueva,nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo)
        #nodo.adicionarSemilla([fila_nueva,nodo.showKakaroto()[1]])
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Semillas",nodo_aux.showSemillas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Semillas",nodo_aux.showSemillas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
        #nodo.semillas.append([fila_nueva,nodo.showKakaroto()[1]])#Se vuelve a agregar al nodo raiz la semilla que fue recolectada por kakaroto para el calculo de las demas posiciones

    #6,Si es una esfera, falta poner la logica para la esfera
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 6:
        bolas = nodo.showBolas().copy()
        if [fila_nueva, nodo.showKakaroto()[1]] in nodo.showBolas():
            print("abajo esfera")
            print("bolas antes de eliminar",nodo.showBolas())
            bolas.remove([fila_nueva,nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo)
        print("INCREIBLE",nodo_aux.comparar_posicion())
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Hace la comparacion")
                print("Esferas",nodo_aux.showBolas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Las posiciones no son iguales")
            print("Esferas",nodo_aux.showBolas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
            print("---ESTADO DEL ABUELO---")
            print("Kakaroto",nodo.padre.showKakaroto())
            print("Bolas",nodo.padre.showBolas())
            print("freezers",nodo.padre.showFreezers())
            print("Cells",nodo.padre.showCells())
            print("Semillas",nodo.padre.showSemillas())
            print("---ESTADO DEL HIJO---")
            print("Kakaroto",nodo_aux.showKakaroto())
            print("Bolas",nodo_aux.showBolas())
            print("freezers",nodo_aux.showFreezers())
            print("Cells",nodo_aux.showCells())
            print("Semillas",nodo_aux.showSemillas())
            print("FIN")
        #nodo.bolas.append([fila_nueva,nodo.showKakaroto()[1]])#Se vuelve a agregar al nodo raiz la bola que fue recolectada por kakaroto para el calculo de las demas posiciones
#***

    else:
        print("no abajo")

    print("--------")
    #----------------------derecha----------------

    columna_nueva = nodo.showKakaroto()[1] + 1
    if columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 0:
        print("derecha espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
    
    #3,Si es un Frezzer
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 3:
        print("derecha Frezzer")
        nodo_aux = Nodo(nodo.costo+4, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Frezzer",nodo_aux.showFreezers())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #4,Si es un Cell
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 4:
        print("derecha Cell")
        nodo_aux = Nodo(nodo.costo+7, nodo.semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Cell",nodo_aux.showCells())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())

    #5,Si es una semilla, falta poner la logica para la semilla
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 5:
        semillas = nodo.showSemillas().copy()
        if [nodo.showKakaroto()[0], columna_nueva] in nodo.showSemillas():
            print("derecha semilla")
            print("semillas antes de eliminar", nodo.showSemillas())
            semillas.remove([nodo.showKakaroto()[0],columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, semillas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Semillas",nodo_aux.showSemillas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Semillas",nodo_aux.showSemillas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
        #nodo.semillas.append([nodo.showKakaroto()[0],columna_nueva])#Se vuelve a agregar al nodo raiz la semilla que fue recolectada por kakaroto para el calculo de las demas posiciones

    #6,Si es una esfera, falta poner la logica para la esfera
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 6:
        bolas = nodo.showBolas().copy()
        if [nodo.showKakaroto()[0], columna_nueva] in nodo.showBolas():
            print("derecha esfera")
            print("bolas antes de eliminar", nodo.showBolas())
            bolas.remove([nodo.showKakaroto()[0],columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo)
        if nodo_aux.comparar_posicion():
            if nodo_aux.nodo_puede_devolverse():
                nodos_posibles.append(nodo_aux)
                print("Esferas",nodo_aux.showBolas())
                print("Kakaroto",nodo_aux.showKakaroto())
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
                print("Costo",nodo_aux.showCosto())
        else:
            nodos_posibles.append(nodo_aux)
            print("Esferas",nodo_aux.showBolas())
            print("Kakaroto",nodo_aux.showKakaroto())
            for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
            print("Costo",nodo_aux.showCosto())
        print("---ESTADO DEL PADRE---")
        print("Kakaroto",nodo.showKakaroto())
        print("Bolas",nodo.showBolas())
        print("freezers",nodo.showFreezers())
        print("Cells",nodo.showCells())
        print("Semillas",nodo.showSemillas())
        print("---ESTADO DEL HIJO---")
        print("Kakaroto",nodo_aux.showKakaroto())
        print("Bolas",nodo_aux.showBolas())
        print("freezers",nodo_aux.showFreezers())
        print("Cells",nodo_aux.showCells())
        print("Semillas",nodo_aux.showSemillas())
        print("FIN")
        #nodo.bolas.append([nodo.showKakaroto()[0],columna_nueva])#Se vuelve a agregar al nodo raiz la bola que fue recolectada por kakaroto para el calculo de las demas posiciones
    else:
        print("no derecha")

    print("--------")
    print("posicion de los nodos:")

    for node in nodos_posibles:
        print(node.showKakaroto())
        print(count,"Array Bolas:",node.showBolas())
    #print('profundidad del nodo:',nodos_posibles[0].showProfundidad())

    print("----FINAL----")


    return nodos_posibles

#solo funciona para matrices nxn

#se crea el tablero, nota si se actualiza el tablero se debe de referenciar otra vez ya que no esta en el while del refresco
def create_board (matriz,size):
    i = -1 #desplazamiento en las columnas
    j = 0  #desplazamiento en las filas
    tamanho = len(matriz) #tamanho de la matriz
    aux = 0 #corrimiento de los cuadrados
    for rows in matriz:
        i = i+1
        for cells in rows:
            if (cells == 0):
                screen.blit(roadImage, ((j*size)+aux,(i*size)+aux))
            elif(cells == 1):
                screen.blit(wallImage, ((j*size)+aux,(i*size)+aux))
            else: 
                screen.blit(roadImage, ((j*size)+aux,(i*size)+aux))
            j = j+1
            if (j==tamanho):
                j = 0
                break
            if (i==tamanho):
                break
    return True
#-----------------

# tamaño de las filas y columnas 
# debe ser nxn
n = len(board)
m = len(board)
print(n)
#-----------------#
# llamdo de la funcion que obtiene las posiciones iniciales de los elementos
kakaroto,freezers,cells,seeds,balls = find_initial_positions(board)

#funcion que se encarga de expandir un nodo
def gestionarNodos(nodos):
    for i in nodos:
        agregarNodoCola(i)
    print('puta, que rika cola:', cola)
    print('primero: ',cola[0].showKakaroto())
    #print('segundo: ',cola[1].showKakaroto())


#____________________________________________________________________________________________________________
def iniciarGUI():
    #se inicia la aplicacion
    
    pygame.init()
    pintar_juego() #pinta el tablero

    #while para la logica o los eventos
    auxiliar=1
    movimientoGoku = [3,3,3,3,3,3,3,4,4,4,4,4] # se deben de ingresar la lista de los movimientos de la solucion encontrada
    while True:
        tiempo = math.floor(pygame.time.get_ticks()/1000)
        if tiempo == auxiliar:
            #if(auxiliar > len(movimientoGoku)): #se termina el juego cuando goku realizo todos los movimientos
                #sys.exit()
            moverGoku(movimientoGoku[auxiliar-1:auxiliar]) #se le ingresa de 1 en 1 los valores en movimientoGoku
            pintar_juego()          # Se debe de modificar esta funcion para pintar los valores que se le ingresan
                                    # el goku mata un freezer entonces debe de borrarse 
            auxiliar = auxiliar+1
        pygame.display.flip()
        pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
#____________________________________________________________________________________________________________

def expandirNodo(nodo):
    if nodo.esMeta():
        #solucion = -1
        solucion.append(True)
        print("posicion final goku:",nodo.showKakaroto())
        print("-------------------SOLUCION->",solucion)
        for node in nodo.recorrer_arbol_arriba():
            print("Camino",node.showKakaroto())
        iniciarGUI()
           #aqui se debe detener la busqueda y devolver el camino de la solucion
    else:
        gestionarNodos(puede_moverse(nodo))
        #costo,semillas,etc = funcionAcciones(nodo)
        #nuevoNodo=Nodo(costo,semillas,etc)
        #print(nuevoNodo.recorrer_arbol_arriba()) se muestra lista con los dos nodos creados
            #aqui se debe llamar a la funcion que genera los hijos del nodo y meterlos en la cola de nodos

def expandirCola():
    if algoritmo == "costo":
        pass
    elif algoritmo == "amplitud":
        nodo = cola.pop(0)   #remueve el primer elemento de la cola y lo expande
        expandirNodo(nodo) 
    elif algoritmo == "profundidad":
        pass
    elif algoritmo == "nombre":
        pass
    elif algoritmo == "nombre":
        pass

def crearNodos():
    #solucion=25
    while len(solucion) == 0:
        #solucion=solucion-1   
        expandirCola()     #aqui va la logica de crear todos los nodos
        #pass    

# funcion que le ingresa la lista de movimientos y actualiza la posicion de goku
# 1 = izquierda
# 2 = arriba
# 3 = derecha
# 4 = abajo

def moverGoku(lista):
    for i in lista:
        if i == 1:
            goku.update(col = goku['col'] - 1) # falta hacer que se vay pintando por iteracion
        elif i == 2:
            goku.update(row = goku['row'] + 1)
        elif i == 3:
            goku.update(col = goku['col'] + 1)
        elif i == 4:
            goku.update(row = goku['row'] - 1)



def agregarNodoCola(nodo):
    if algoritmo == "costo":
        cola.append(nodo) #agrega el nodo al final de la cola pero da igual el orden revisar si optimizamos esto
    elif algoritmo == "amplitud":
        cola.append(nodo) #agrega el nodo al final de la cola
    elif algoritmo == "profundidad":
        cola.insert(0,nodo) #agrega el nodo al principio de la cola
    elif algoritmo == "nombre":
        pass
    elif algoritmo == "nombre":
        pass

#expandirNodo(nodo_raiz)

#__________________________________________llamadas y definiciones de funciones que pintan la GUI
#------------
goku = {"row":kakaroto[0][1], "col":kakaroto[0][0]}

#------------
def pintar_freezers(freezers):
    for i in range(len(freezers)):
        row = freezers[i][0]
        col = freezers[i][1]
        screen.blit(freezerImg, ((col*imgsize),(row*imgsize)))
def pintar_cells(cells):
    for i in range(len(cells)):
        row = cells[i][0]
        col = cells[i][1]
        screen.blit(cellImg, ((col*imgsize),(row*imgsize)))
def pintar_seeds(seeds):
    for i in range(len(seeds)):
        row = seeds[i][0]
        col = seeds[i][1]
        screen.blit(seedImg, ((col*imgsize),(row*imgsize)))
def pintar_balls(balls):
    for i in range(len(balls)):
        row = balls[i][0]
        col = balls[i][1]
        screen.blit(ballImage, ((col*imgsize),(row*imgsize)))

# Comprueba si un nodo que se le ingrese es una meta    

def pintar_juego():
    #fondo blanco
    screen.fill(white)
    #pintar el tablero
    #create_board(tablero,imgsize)
    create_board(board,imgsize)
    #pintar las esferas
    pintar_balls(balls)
    #screen.blit(ballImage, ((queso.get('x')*imgsize),(queso.get('y')*imgsize)))
    #pintar un freezer test
    pintar_freezers(freezers)
    #screen.blit(freezerImg, ((2*imgsize),(0*imgsize)))
    #pintar un cell 
    pintar_cells(cells)
    #screen.blit(cellImg, ((2*imgsize),(5*imgsize)))
    #pintar una semilla
    pintar_seeds(seeds)
    #screen.blit(seedImg, ((1*imgsize),(0*imgsize)))
    #pintar a goku
    screen.blit(gokuImg, ((goku.get('row')*imgsize),(goku.get('col')*imgsize)))



#se carga la imagen del raton y demas
imgsize = 90
auxsize = 85
ballImage = pygame.transform.scale(pygame.image.load('imagenes/ball.png'), (auxsize,auxsize))
roadImage = pygame.image.load('imagenes/path.png')
wallImage = pygame.image.load('imagenes/muro.png')
gokuImg =  pygame.transform.scale(pygame.image.load('imagenes/goku.png'), (auxsize,auxsize))
freezerImg = pygame.transform.scale(pygame.image.load('imagenes/freezer.png'), (auxsize,auxsize))
cellImg = pygame.transform.scale(pygame.image.load('imagenes/cell.png'), (auxsize,auxsize))
seedImg = pygame.transform.scale(pygame.image.load('imagenes/semilla.png'), (auxsize,auxsize))

#Definir colores
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)

#tamanho de la GUI
aux1 = n*imgsize
aux2 = m*imgsize
size = (aux1,aux2)

#definicion de la GUI
screen = pygame.display.set_mode(size)

#generar la solucion del algoritmo inicial
crearNodos()


