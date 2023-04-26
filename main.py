import sys
import numpy as np
import time
from nodes import Nodo
#Si al intentar expandir un nodo no tiene hijos, es porque esta en un camino sin salida, entonces hay que matar el programa

# Aqui se abre el archivo de texto que contiene el mapa y se guarda en la variable board en forma de matriz
#archivo = open("Prueba1.txt")
#info = archivo.readlines()
#print("info:",info)
#archivo.close()

def crear_mapa_desde_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        filas = archivo.readlines()
        mapa = []
        for fila in filas:
            mapa.append([int(x) for x in fila.split()])
        archivo.close()
        return np.array(mapa)

mapa = crear_mapa_desde_archivo('Prueba1.txt')
# print(mapa)
# print("len:",range(len(mapa)))

#funcion que le pregunta al usuario que algoritmo desea ejecutar
def escogerAlgoritmo():
    tipo = input("ingrese el tipo de busqueda deseado (informada/no informada) ")
    if tipo == "no informada":
        choice = input("ingrese el nombre del algoritmo de busqueda no informada que desee ejecutar (costo, amplitud, profundidad):")
        if choice == "costo":
            return choice
        elif choice == "amplitud":
            return choice
        elif choice == "profundidad":
            return choice
        else:
            print("escoja un algoritmo de busqueda no informada valido")
            sys.exit()
    elif tipo == "informada":
        choice = input("ingrese el nombre del algoritmo de busqueda informada que desee ejecutar (avara, a*):")
        if choice == "avara":
            return choice
        elif choice == "a*":
            return choice
        else:
            print("escoja un algoritmo de busqueda informada valido")
            sys.exit()
    else:
        print("escoja un tipo de busqueda valido")
        sys.exit()

# #__________________________________________definicion de variables globales

algoritmo = escogerAlgoritmo()
solucion  = []
camino = []
nodos_solucion = []
tiempo_inicial = time.time()
tiempo_final = 0
nodosExpandidos = 0
# #Creamos un nodo unicial, en donde se guardara el estado inicial
nodo_raiz= Nodo(costo=0, semillas=[],semillas_almacenadas=0, bolas=[], freezers=[], cells=[], kakaroto=[])
cola = [] #se guardaran los nodos en este array
#board = []

# for i in info:
#     fila = i.split()
#     for h in range(len(fila)):
#         fila[h] = int(fila[h])
#     board.append(fila)

# #Se crea una matriz de 10x10
#mapa = np.zeros((10, 10), dtype=int)
# #funcion que encuentra la posicion inicial de todos los elementos del tablero

def find_initial_positions(board):
    freezers = []
    cells = []
    balls = []
    seeds = []
    kakaroto = None
    for i in range(len(board)):
        for h in range(len(board)):
            if mapa[i][h] == 1:
                print("uwu")
            elif mapa[i][h] == 2:
                kakaroto = [i,h]
                mapa[i][h]=0
            elif mapa[i][h] == 3:
                freezers.append([i,h])
            elif mapa[i][h] == 4:
                cells.append([i,h])
            elif mapa[i][h] == 5:
                seeds.append([i,h])
            elif mapa[i][h] == 6:
                balls.append([i,h])

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
    print("Kakaroto",kakaroto[0])
    print("Kakaroto",kakaroto[1])

    print("----------------")
    cola.append(nodo_raiz)
    return kakaroto,freezers,cells,seeds,balls

def verificar_freezers(nodo, posicion):
    freezers = nodo.showFreezers().copy()
    semillas_almacenadas = nodo.showSemillasAlmacenadas()
    costo = nodo.showCosto()
    if posicion in nodo.showFreezers():
        if nodo.showSemillasAlmacenadas()>0:
            freezers.remove(posicion)
            semillas_almacenadas = semillas_almacenadas - 1
            costo = costo+1
        else:
            costo = costo+4
    else:
        costo = costo+1
    return freezers, semillas_almacenadas, costo

def verificar_cells(nodo, posicion):
    cells = nodo.showCells().copy()
    semillas_almacenadas = nodo.showSemillasAlmacenadas()
    costo = nodo.showCosto()
    if posicion in nodo.showCells():
        if nodo.showSemillasAlmacenadas()>0:
            cells.remove(posicion)
            semillas_almacenadas = semillas_almacenadas - 1
            costo = nodo.showCosto()+1
        else:
            costo = nodo.showCosto()+7
    else:
        costo = nodo.showCosto()+1
    return cells, semillas_almacenadas, costo

def verificar_semillas(nodo, posicion):
    semillas = nodo.showSemillas().copy()
    semillas_almacenadas = nodo.showSemillasAlmacenadas()
    if posicion in nodo.showSemillas():
        semillas.remove(posicion)
        semillas_almacenadas = semillas_almacenadas + 1
    return semillas, semillas_almacenadas

def verificar_bolas(nodo, posicion):
    bolas = nodo.showBolas().copy()
    if posicion in nodo.showBolas():
        bolas.remove(posicion)
    return bolas
    
def puede_moverse(nodo):
    print("posicion inicial kakaroto:",nodo.showKakaroto())
    print('valor heuristica:', nodo.heuristica())
    nodos_posibles = []
    nodos_recorridos = nodo.recorrer_arbol_arriba()
    for n in nodos_recorridos:
        print("Camino_principio:",n.showKakaroto())

    #----------arriba-------------
    fila_nueva = nodo.showKakaroto()[0] - 1
    print("MAPAAAAAAAAAAAAAAAA",mapa[0][1])
    print(mapa[fila_nueva][nodo.showKakaroto()[1]])
    #0,Si es un espacio vacio
    if fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 0:
        print("arriba espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]],padre=nodo, operador="arriba")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #3,Si es un Frezzer
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 3:
        print("arriba Frezzer")
        freezers, semillas_almacenadas, costo = verificar_freezers(nodo,[fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas, nodo.bolas, freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo, operador="arriba")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
    
    #4,Si es un Cell
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 4:
        print("arriba Cell")
        cells, semillas_almacenadas, costo = verificar_cells(nodo,[fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas, nodo.bolas, nodo.freezers, cells,kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo, operador="arriba")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #5,Si es una semilla, falta poner la logica para la semilla
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 5:
        semillas, semillas_almacenadas = verificar_semillas(nodo, [fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, semillas, semillas_almacenadas, nodo.bolas, nodo.freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo, operador="arriba")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

            

    #6,Si es una esfera, falta poner la logica para la esfera
    elif fila_nueva >= 0 and mapa[fila_nueva, nodo.showKakaroto()[1]] == 6:
        bolas = verificar_bolas(nodo, [fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas, bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]-1,nodo.showKakaroto()[1]], padre=nodo, operador="arriba")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
    else:
        print("no arriba")


    print("--------")
    #----------------izquierda------------
    columna_nueva = nodo.showKakaroto()[1] - 1
    if columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 0:
        print("izquierda espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo, operador="izquierda")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #3,Si es un Frezzer
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 3:
        print("izquierda Frezzer")
        freezers, semillas_almacenadas, costo = verificar_freezers(nodo,[nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas, nodo.bolas, freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo, operador="izquierda")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #4,Si es un Cell
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 4:
        print("izquierda Cell")
        cells, semillas_almacenadas, costo = verificar_cells(nodo,[nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas, nodo.bolas, nodo.freezers, cells,kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo, operador="izquierda")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #5,Si es una semilla, falta poner la logica para la semilla
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 5:
        semillas, semillas_almacenadas = verificar_semillas(nodo,[nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, semillas, semillas_almacenadas,nodo.bolas, nodo.freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo, operador="izquierda")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #6,Si es una esfera, falta poner la logica para la esfera
    elif columna_nueva >= 0 and mapa[nodo.showKakaroto()[0], columna_nueva] == 6:
        bolas = verificar_bolas(nodo, [nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas, bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] - 1], padre=nodo, operador="izquierda")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
    else:
        print("no izquierda")

    print("--------")
    #-----------abajo-----------
    fila_nueva = nodo.showKakaroto()[0] + 1

    if fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 0:
        print("abajo espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo, operador="abajo")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

#***
    #3,Si es un Frezzer
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 3:
        print("abajo Frezzer")
        freezers, semillas_almacenadas, costo= verificar_freezers(nodo,[fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas, nodo.bolas, freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo, operador="abajo")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
    
    #4,Si es un Cell
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 4:
        print("abajo Cell")
        cells, semillas_almacenadas, costo = verificar_cells(nodo,[fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas, nodo.bolas, nodo.freezers, cells,kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo, operador="abajo")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #5,Si es una semilla, falta poner la logica para la semilla
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 5:
        semillas, semillas_almacenadas = verificar_semillas(nodo, [fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, semillas, semillas_almacenadas, nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo, operador="abajo")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #6,Si es una esfera, falta poner la logica para la esfera
    elif fila_nueva < mapa.shape[0] and mapa[fila_nueva, nodo.showKakaroto()[1]] == 6:
        bolas = verificar_bolas(nodo, [fila_nueva, nodo.showKakaroto()[1]])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas,bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0]+1,nodo.showKakaroto()[1]], padre=nodo, operador="abajo")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
#***

    else:
        print("no abajo")

    print("--------")
    #----------------------derecha----------------

    columna_nueva = nodo.showKakaroto()[1] + 1
    if columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 0:
        print("derecha espacio vacio")
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas,nodo.bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo, operador="derecha")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
    
    #3,Si es un Frezzer
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 3:
        print("derecha Frezzer")
        freezers, semillas_almacenadas, costo = verificar_freezers(nodo,[nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas,nodo.bolas, freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo, operador="derecha")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #4,Si es un Cell
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 4:
        print("derecha Cell")
        cells, semillas_almacenadas, costo = verificar_cells(nodo,[nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(costo, nodo.semillas, semillas_almacenadas,nodo.bolas, nodo.freezers, cells,kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo, operador="derecha")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #5,Si es una semilla, falta poner la logica para la semilla
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 5:
        semillas, semillas_almacenadas = verificar_semillas(nodo, [nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, semillas, semillas_almacenadas,nodo.bolas, nodo.freezers, nodo.cells,kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo, operador="derecha")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)

    #6,Si es una esfera, falta poner la logica para la esfera
    elif columna_nueva < mapa.shape[1] and mapa[nodo.showKakaroto()[0], columna_nueva] == 6:
        bolas = verificar_bolas(nodo, [nodo.showKakaroto()[0], columna_nueva])
        nodo_aux = Nodo(nodo.costo+1, nodo.semillas, nodo.semillas_almacenadas,bolas, nodo.freezers, nodo.cells, kakaroto=[nodo.showKakaroto()[0],nodo.showKakaroto()[1] + 1], padre=nodo, operador="derecha")
        if algoritmo == "profundidad":
            if nodo_aux.nodo_valido(nodos_recorridos):
                nodos_posibles.append(nodo_aux)
                for node in nodo_aux.recorrer_arbol_arriba():
                    print("Camino",node.showKakaroto())
        else:
            if nodo_aux.comparar_posicion():
                if nodo_aux.nodo_puede_devolverse():
                    nodos_posibles.append(nodo_aux)
            else:
                nodos_posibles.append(nodo_aux)
    else:
        print("no derecha")

    print("--------")
    print("posicion de los nodos:")

    for node in nodos_posibles:
        print(node.showKakaroto())
        print("Array Bolas:",node.showBolas())
        print("Semillas almacendas:", node.showSemillasAlmacenadas())
        print("Freezers:",node.showFreezers())
        print("Cells:",node.showCells())
    #print('profundidad del nodo:',nodos_posibles[0].showProfundidad())

    print("----FINAL----")


    return nodos_posibles
#-----------------#
# llamdo de la funcion que obtiene las posiciones iniciales de los elementos
kakaroto,freezers,cells,seeds,balls = find_initial_positions(mapa)

#funcion que se encarga de expandir un nodo
def gestionarNodos(nodos):
    for i in nodos:
        agregarNodoCola(i)
    #print('puta, que rika cola:', cola)
    #print('primero: ',cola[0].showKakaroto())
    #print('segundo: ',cola[1].showKakaroto())

def expandirNodo(nodo):
    global nodosExpandidos
    nodosExpandidos = nodosExpandidos + 1
    if nodo.esMeta():
    #if False:
        tiempo_final=time.time()
        #solucion = -1
        solucion.append(True)
        print("posicion final goku:",nodo.showKakaroto())
        print("-------------------SOLUCION->",solucion)
        for node in nodo.recorrer_arbol_arriba():
            #print("Camino",node.showKakaroto())
            camino.append(node.showKakaroto())              #Verificar si se puede borrar
            nodos_solucion.append(node)
        print("Costo: ", nodo.showCosto())
           #aqui se debe detener la busqueda y devolver el camino de la solucion
        camino.reverse()
        nodos_solucion.reverse()
        print("CAMINO",camino)
        tiempo = round(tiempo_final - tiempo_inicial,5)
        print('incial',tiempo_inicial)
        print('final',tiempo_final)
        print('El tiempo de ejecucion del algoritmo de busqueda fue de: {} segundos'.format(tiempo))
        print("la cantidad de nodos que se expandieron es de: ", nodosExpandidos)
    else:
        gestionarNodos(puede_moverse(nodo))
        #costo,semillas,etc = funcionAcciones(nodo)
        #nuevoNodo=Nodo(costo,semillas,etc)
        #print(nuevoNodo.recorrer_arbol_arriba()) se muestra lista con los dos nodos creados
            #aqui se debe llamar a la funcion que genera los hijos del nodo y meterlos en la cola de nodos

def expandirCola():
    if algoritmo == "costo":
        nodo = cola.pop(nodoBarato())  # remueve el nodo que tenga el costo mas bajo
        expandirNodo(nodo)
    elif algoritmo == "amplitud":
        nodo = cola.pop(0)   #remueve el primer elemento de la cola y lo expande
        expandirNodo(nodo) 
    elif algoritmo == "profundidad":
        nodo = cola.pop(0)   #remueve el primer elemento de la cola y lo expande
        expandirNodo(nodo) 
    elif algoritmo == "avara":
        nodo = cola.pop(nodoMenorHeuristica())
        expandirNodo(nodo)
    elif algoritmo == "a*":
        nodo = cola.pop(nodoMenorCostoEstimado())
        expandirNodo(nodo)

def nodoBarato():
    menor = cola[0]
    indice = None
    for i in range(len(cola)):
        nuevo_costo = cola[i].showCosto()
        if menor.showCosto() >= nuevo_costo:
            menor = cola[i]
            indice = i
    return indice

def nodoMenorHeuristica():
    menor = cola[0]
    indice = None
    for i in range(len(cola)):
        nuevo_costo_estimado = cola[i].heuristica()
        if menor.heuristica() >= nuevo_costo_estimado:
            menor = cola[i]
            indice = i
    return indice

def nodoMenorCostoEstimado():
    menor = cola[0]
    indice = None
    for i in range(len(cola)):
        nuevo_costo_estimado = cola[i].heuristicaCosto()
        if menor.heuristicaCosto() >= nuevo_costo_estimado:
            menor = cola[i]
            indice = i
    return indice

def crearNodos():
    #solucion=25
    while len(solucion) == 0:
        #solucion=solucion-1   
        expandirCola()     #aqui va la logica de crear todos los nodos
        #pass    

def agregarNodoCola(nodo):
    if algoritmo == "costo":
        cola.append(nodo) #agrega el nodo al final de la cola pero da igual el orden revisar si optimizamos esto
    elif algoritmo == "amplitud":
        cola.append(nodo) #agrega el nodo al final de la cola
    elif algoritmo == "profundidad":
        cola.insert(0,nodo) #agrega el nodo al principio de la cola
    elif algoritmo == "avara":
        cola.append(nodo)
    elif algoritmo == "a*":
        cola.append(nodo)

#expandirNodo(nodo_raiz)

#generar la solucion del algoritmo inicial
crearNodos()


