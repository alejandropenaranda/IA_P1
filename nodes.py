class Nodo:
    def __init__(self,costo,semillas,semillas_almacenadas,bolas,freezers,cells,kakaroto,padre=None,operador=None):
        self.costo = costo
        self.padre = padre
        self.operador = operador # operador utilizado para que goku llegara a esta posicion
        self.bolas = bolas
        self.freezers = freezers
        self.cells = cells
        self.kakaroto = kakaroto # posicion actual del goku
        self.semillas = semillas
        self.primerobjetivo = 0
        self.val_heuristica = 0
        self.semillas_almacenadas = semillas_almacenadas
        if padre is None:
            self.profundidad = 0
        else:
            self.profundidad = padre.profundidad + 1

    # Recorre el arbol desde el nodo actual hasta su padre y luego hacia la raíz.
    def recorrer_arbol_arriba(self, nodos_recorridos=None):
        if nodos_recorridos is None:
            nodos_recorridos = []
        nodos_recorridos.append(self)#Agrega el nodo actual a la lista de nodos recorridos
        if self.padre is not None:
            self.padre.recorrer_arbol_arriba(nodos_recorridos)
        return nodos_recorridos
    
    def esMeta(self):
        if len(self.bolas) == 0:
            return True
        else:
            return False    
    
    def showCosto(self):
        return self.costo
    
    def showSemillas(self):
        return self.semillas

    def showSemillasAlmacenadas(self):
        return self.semillas_almacenadas

    def showBolas(self):
        return self.bolas
    
    def showFreezers(self):
        return self.freezers
    
    def showCells(self):
        return self.cells
    
    def showKakaroto(self):
        return self.kakaroto
    
    def showOperador(self):
        return self.operador
    
    def showProfundidad(self):
        return self.profundidad
    
    def nodo_puede_devolverse(self):
        if self.padre==None:
            return True
        elif self.padre.padre == None:
            return True
        elif self.bolas != self.padre.padre.bolas or self.freezers != self.padre.padre.freezers or self.cells != self.padre.padre.cells or self.semillas != self.padre.padre.semillas:
            return True
        else:
            return False
    
    def nodo_valido(self, lista_nodos):
        count = 0
        if self.padre==None:
            return True
        for n in lista_nodos:
            #if self.showKakaroto() in lista_nodos:
            #print("self_kakaroto:",self.showKakaroto())
            if self.bolas == n.bolas and self.freezers == n.freezers and self.cells == n.cells and self.semillas == n.semillas and self.kakaroto == n.kakaroto:
                #print("nodoInvalido",n.kakaroto)
                count = count+1
        if count>0:
            return False
        else:
            return True
            # else:
            #     return True

    def comparar_posicion(self):
        if self.padre==None:
            return True
        elif self.padre.padre == None:
            return True
        elif self.showKakaroto() == self.padre.padre.showKakaroto():
            return True
        else:
            return False

    def eliminarSemilla(self, semilla):
        self.semillas.remove(semilla)
        return self.semillas

    def eliminarBola(self, bola):
        self.bolas.remove(bola)
        return self.bolas

    def definir_primer_objetivo(self,objetivo):
        self.primerobjetivo = objetivo

    def showValHeuristica(self):
        return self.val_heuristica

    def heuristica(self):
        if len(self.bolas)==2:
            aux = abs(self.bolas[0][0]-self.kakaroto[0]) + abs(self.bolas[0][1]-self.kakaroto[1])
            for i in range(len(self.bolas)):
                aux2 = abs(self.bolas[i][0]-self.kakaroto[0]) + abs(self.bolas[i][1]-self.kakaroto[1])
                if aux>aux2:
                    self.definir_primer_objetivo(i)
                else:
                    self.definir_primer_objetivo(0)

            if self.primerobjetivo == 0:
                distancia1 = abs(self.bolas[0][0]-self.kakaroto[0]) + abs(self.bolas[0][1]-self.kakaroto[1])
                distancia2 = abs(self.bolas[0][0]-self.bolas[1][0]) + abs(self.bolas[0][1]-self.bolas[1][1])
                self.val_heuristica = distancia1 + distancia2
                return self.showValHeuristica()
            else:
                distancia1 = abs(self.bolas[1][0]-self.kakaroto[0]) + abs(self.bolas[1][1]-self.kakaroto[1])
                distancia2 = abs(self.bolas[0][0]-self.bolas[1][0]) + abs(self.bolas[0][1]-self.bolas[1][1])
                self.val_heuristica = distancia1 + distancia2
                return self.showValHeuristica()
        elif len(self.bolas) == 1:
            aux =  abs(self.bolas[0][0]-self.kakaroto[0]) + abs(self.bolas[0][1]-self.kakaroto[1])
            self.val_heuristica = aux
            return self.showValHeuristica()
        else:
            self.val_heuristica = 0
            return self.showValHeuristica()