import pygame , sys
import math
from main import (nodos_solucion , mapa)

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
n = len(mapa)
m = len(mapa)
print("n:",n)
#-----------------#
#____________________________________________________________________________________________________________
def iniciarGUI(nodo):
    #se inicia la aplicacion
    
    pygame.init()
    nodos_lista=nodos_solucion
    auxiliar=1
    print("nodos_lista:",nodos_lista)
    print("0",nodo.showKakaroto())
    pintar_juego(nodo) #pinta el tablero

    #while para la logica o los eventos
    while auxiliar < len(nodos_lista):
        #print("aux",auxiliar)
        #print("len",len(nodos_lista))
        tiempo = math.floor(pygame.time.get_ticks()/1000)
        if tiempo == auxiliar:
            pintar_juego(nodos_lista[auxiliar])
            auxiliar = auxiliar+1
        pygame.display.flip()
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

iniciarGUI(nodos_solucion[0])