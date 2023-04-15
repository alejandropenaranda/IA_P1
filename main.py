import pygame , sys
import random
import math
from nodes import Nodo

# Aqui se abre el archivo de texto que contiene el mapa y se guarda en la variable board en forma de matriz
archivo = open("Prueba1.txt")
info = archivo.readlines()
#print(info)
archivo.close()

board = []
for i in info:
    fila = i.split()
    for h in range(len(fila)):
        fila[h] = int(fila[h])
    board.append(fila)

#funcion que encuentra la posicion inicial de todos los elementos del tablero

def find_initial_positions(board):
    freezers = []
    cells = []
    balls = []
    seeds = []
    goku = []
    for i in range(len(board)):
        for h in range(len(board)):
            if board[i][h] == 2:
                goku.append([i,h])
            elif board[i][h] == 3:
                freezers.append([i,h])
            elif board[i][h] == 4:
                cells.append([i,h])
            elif board[i][h] == 5:
                seeds.append([i,h])
            elif board[i][h] == 6:
                balls.append([i,h])
    return goku,freezers,cells,seeds,balls

#funcion que le pregunta al usuario que algoritmo desea ejecutar
def escogerAlgoritmo():
    choice = input("ingrese el nombre del algoritmo de busqueda que desee ejecutar (costo, amplitud, profundidad, nombre, nombre):")
    if choice == "costo":
        pass
    elif choice == "amplitud":
        pass
    elif choice == "profundidad":
        pass
    elif choice == "nombre":
        pass
    elif choice == "nombre":
        pass
    else:
        print("escoja un algoritmo de busqueda valido")
        sys.exit()
"""
def movements_table (sensores, hq):
    left_sen = sensores[0]
    right_sen = sensores[1]
    down_sen = sensores[2]
    up_sen = sensores[3]

    # the movements will be represented by numbers  1 = up, 2 = left, 3 = down, 4 = right
    # when the mouse found the cheese, this will be represented by the number 5 = found cheese
    # when any sensor is true, it means that the mouse can go in that direction, otherwise he cant (false)
    action = 0
    if hq:
        action = 5
        return action
    elif (left_sen and up_sen and right_sen and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen and down_sen == False and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen == False and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen and right_sen == False and down_sen == False and hq == False): 
        action = 1
        return action
    
    elif (left_sen and up_sen == False  and right_sen and down_sen and hq == False): 
        action = 2
        return action
    
    elif (left_sen and up_sen == False and right_sen and down_sen == False and hq == False): 
        action = 4
        return action
    
    elif (left_sen and up_sen == False and right_sen == False and down_sen and hq == False): 
        action = 2
        return action
    
    elif (left_sen and up_sen == False and right_sen == False and down_sen == False and hq == False): 
        action = 2
        return action
    
    elif (left_sen == False and up_sen and right_sen and down_sen and hq == False): 
        action = 1
        return action
    
    elif (left_sen == False and up_sen and right_sen and down_sen == False and hq == False): 
        action = 4
        return action

    elif (left_sen == False and up_sen and right_sen == False and down_sen and hq == False): 
        action = 3
        return action
    
    elif (left_sen == False and up_sen and right_sen == False and down_sen == False and hq == False): 
        action = 1
        return action

    elif (left_sen == False and up_sen == False and right_sen and down_sen and hq == False): 
        action = 4
        return action
    
    elif (left_sen == False and up_sen == False and right_sen and down_sen == False and hq == False): 
        action = 4
        return action
    
    elif (left_sen == False and up_sen == False and right_sen == False and down_sen and hq == False): 
        action = 3
        return action
"""
"""
def huele_queso():
    if queso == mouse:
        return True
    else: 
        return False
"""
"""
def generate_matrix(n,m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for h in range(m):
            if i == mouse.get('y') and h == mouse.get('x'):
                matriz[i].append(1) 
            elif i == queso.get('y') and h == queso.get('x'):
                matriz[i].append(1) 
    return matriz
"""
"""
#funcion retorna 1 o 0 dependiendo del valor que se genere automaticamente
#se le da mas posibillidad de devolver 1 para que no hayan muchas paredes
#1 es un espacio libre para avanzar
#0 no es un espacio libre
def wall_generator():
    numero = random.randint(0,10)
    if numero == 0 or numero == 8:
        return 0
    else:
        return 1
"""

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
"""
def generate_rata():
    mouse = {'x':0, 'y':0}
    mouse.update({'x':random.randint(0,n-1), 'y':random.randint(0,m-1)})
    return  mouse
"""

"""
                                    # the movements will be represented by numbers  1 = up, 2 = left, 3 = down, 4 = right
                                    def move_mouse(action):
                                    if action == 1:
                                        mouse.update({'y':mouse.get('y')-1})
                                    elif action == 2:
                                        mouse.update({'x':mouse.get('x')-1})
                                    elif action == 3:
                                        mouse.update({'y':mouse.get('y')+1})
                                    elif action == 4:
                                        mouse.update({'x':mouse.get('x')+1})
                                    elif action == 5:
                                        print("huele a queso")
                                        sys.exit()
""" 
"""
def movement_rata(matriz):

    left_sen = False
    right_sen = False
    up_sen = False
    down_sen = False

    if mouse.get('x') == 0:
        left_sen = False
        if mouse.get('y') == 0:
            up_sen = False  
            if matriz[mouse.get('y')][mouse.get('x')+1] == 1:
                right_sen = True
            if matriz[mouse.get('y')+1][mouse.get('x')] == 1:
                down_sen = True
            return [left_sen,right_sen,down_sen,up_sen]
        elif mouse.get('y') == n-1:
            down_sen = False
            if matriz[mouse.get('y')][mouse.get('x')+1] == 1:
                right_sen = True
            if matriz[mouse.get('y')-1][mouse.get('x')] == 1:
                up_sen = True
            return [left_sen,right_sen,down_sen,up_sen]
        else:
            if matriz[mouse.get('y')][mouse.get('x')+1] == 1:
                right_sen = True
            if matriz[mouse.get('y')-1][mouse.get('x')] == 1:
                up_sen = True
            if matriz[mouse.get('y')+1][mouse.get('x')] == 1:
                down_sen = True
            return [left_sen,right_sen,down_sen,up_sen]
    if mouse.get('x') == n-1:
        right_sen = False
        if mouse.get('y') == 0:
            up_sen = False
            if matriz[mouse.get('y')][mouse.get('x')-1] == 1:
                left_sen = True
            if matriz[mouse.get('y')+1][mouse.get('x')] == 1:
                down_sen = True
            return [left_sen,right_sen,down_sen,up_sen]
        elif mouse.get('y') == n-1:
            down_sen = False
            if matriz[mouse.get('y')][mouse.get('x')-1] == 1:
                left_sen = True
            if matriz[mouse.get('y')-1][mouse.get('x')] == 1:
                up_sen = True
            return [left_sen,right_sen,down_sen,up_sen]
        else:
            if matriz[mouse.get('y')][mouse.get('x')-1] == 1:
                left_sen = True
            if matriz[mouse.get('y')-1][mouse.get('x')] == 1:
                up_sen = True
            if matriz[mouse.get('y')+1][mouse.get('x')] == 1:
                down_sen = True
            return [left_sen,right_sen,down_sen,up_sen]
    if mouse.get('y') == 0:
        up_sen = False
        if matriz[mouse.get('y')][mouse.get('x')-1] == 1:
            left_sen = True
        if matriz[mouse.get('y')][mouse.get('x')+1] == 1:
            right_sen = True
        if matriz[mouse.get('y')+1][mouse.get('x')] == 1:
            down_sen = True
        return [left_sen,right_sen,down_sen,up_sen]
    if mouse.get('y') == n-1:
        down_sen = False
        if matriz[mouse.get('y')][mouse.get('x')-1] == 1:
            left_sen = True
        if matriz[mouse.get('y')][mouse.get('x')+1] == 1:
            right_sen = True
        if matriz[mouse.get('y')-1][mouse.get('x')] == 1:
            up_sen = True
        return [left_sen,right_sen,down_sen,up_sen]
    else:
        if matriz[mouse.get('y')][mouse.get('x')-1] == 1:
            left_sen = True
        if matriz[mouse.get('y')][mouse.get('x')+1] == 1:
            right_sen = True
        if matriz[mouse.get('y')-1][mouse.get('x')] == 1:
            up_sen = True
        if matriz[mouse.get('y')+1][mouse.get('x')] == 1:
            down_sen = True
        return [left_sen,right_sen,down_sen,up_sen]
"""
# llamdo de la funcion que obtiene las posiciones iniciales de los elementos
kakaroto,freezers,cells,seeds,balls = find_initial_positions(board)

#funcion que se encarga de expandir un nodo

def expandirNodo(nodo):
    if nodo.esMeta():
        pass    #aqui se debe detener la busqueda y devolver el camino de la solucion
    else:
        pass    #aqui se debe llamar a la funcion que genera los hijos del nodo y meterlos en la cola de nodos


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
    #pintar la rata
    screen.blit(gokuImg, ((goku.get('row')*imgsize),(goku.get('col')*imgsize)))
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


#se inicia la aplicacion
pygame.init()

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

#pintar el tablero inicial

nodoInicial = Nodo(0,0,[0],0,0,0)
print(nodoInicial.esMeta())
print(nodoInicial.showOperador())
print(nodoInicial.showProfundidad())

pintar_juego()

"""
def aux():# se debe llamar la logica de movimiento del goku despues de haber encontado el la solucion
    movimiento_rata = movement_rata(tablero)
    move_mouse(movements_table(movimiento_rata,huele_queso()))
"""
#while para la logica o los eventos

auxiliar=1
while True:
    tiempo = math.floor(pygame.time.get_ticks()/1000)
    if tiempo == auxiliar:
        #aux()
        pintar_juego()
        auxiliar = auxiliar+1

    pygame.display.flip()
    pygame.display.update()
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
