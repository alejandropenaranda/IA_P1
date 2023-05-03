import pygame , sys
from pygame.locals import *
import math
from main import (nodos_solucion , mapa, tiempo, nodosExpandidos)

final = nodos_solucion[-1]
pygame.font.init()

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
n = len(mapa)
m = len(mapa)
#-----------------#
#____________________________________________________________________________________________________________
def iniciarGUI(nodo):
    #se inicia la aplicacion
    
    pygame.init()

    #Configuracion para el texto
    nodos_lista=nodos_solucion
    auxiliar=1
    pintar_juego(nodo) #pinta el tablero

    #while para la logica o los eventos
    #while auxiliar < len(nodos_lista):
    aux = True
    while aux:
        tiempo = math.floor(pygame.time.get_ticks()/1000)

        if auxiliar < len(nodos_lista):
            if tiempo == auxiliar:
                pintar_juego(nodos_lista[auxiliar])
                auxiliar = auxiliar+1
            pygame.display.flip()
            pygame.display.update()
        else:
            screen.fill(white)
            pintarEstadisticas()
            pygame.display.update()
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
#____________________________________________________________________________________________________________
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

def pintar_juego(nodo):
    
    freezers = nodo.showFreezers()
    cells = nodo.showCells()
    bolas = nodo.showBolas()
    semillas = nodo.showSemillas()
    kakaroto = nodo.showKakaroto()
    #fondo blanco
    screen.fill(white)
    #pintar el tablero
    create_board(mapa,imgsize)

    pintar_freezers(freezers)
    pintar_cells(cells)
    pintar_balls(bolas)
    pintar_seeds(semillas)

    screen.blit(gokuImg, ((kakaroto[1]*imgsize),(kakaroto[0]*imgsize)))

#Definir colores
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
    
fuente = pygame.font.SysFont('Segoe UI',28)
fuente2 = pygame.font.SysFont('Segoe UI', 40)
texto = fuente.render("prueba de texto",True,black)

def pintarEstadisticas():
    title = fuente2.render('Estadisticas', True,black)
    nodos = fuente.render('La cantidad de nodos que se expandieron es de: '+str(nodosExpandidos),True,black )
    profundidad = fuente.render('Profundidad del arbol de busqueda: '+str(final.showProfundidad()),True, black)
    time = fuente.render('El tiempo de ejecucion del algoritmo de busqueda fue de: '+str(tiempo)+' s',True,black)
    costo = fuente.render('El costo de la solucion encontrada es de: '+str(final.showCosto()),True,black)
    screen.blit(title,(25,60))
    screen.blit(nodos,(25,120))
    screen.blit(profundidad,(25,160))
    screen.blit(time,(25,200))
    screen.blit(costo,(25,240))

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

#tamanho de la GUI
aux1 = n*imgsize
aux2 = m*imgsize
size = (aux1,aux2)

#definicion de la GUI
screen = pygame.display.set_mode(size)

iniciarGUI(nodos_solucion[0])