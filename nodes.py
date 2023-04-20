class Nodo:
    def __init__(self,costo,semillas,bolas,frezzers,cells,kakaroto,padre=None,operador=None):
        self.costo = costo
        self.padre = padre
        self.operador = operador # operador utilizado para que goku llegara a esta posicion
        self.bolas = bolas
        self.frezzers = frezzers
        self.cells = cells
        self.kakaroto = kakaroto # posicion actual del goku
        self.semillas = semillas
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
    
    def showBolas(self):
        return self.bolas
    
    def showFrezzers(self):
        return self.frezzers
    
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
        elif self.bolas != self.padre.bolas or self.frezzers != self.padre.freezers or self.cells != self.padre.cells or self.semillas != self.padre.semillas:
            return True
        else:
            return False

    def comparar_posicion(self):
        if self.padre==None:
            return True
        elif self.showKakaroto == self.padre.showKakaroto():
            return True
        else:
            return False

    def eliminarSemilla(self, semilla):
        self.semillas.remove(semilla)
        return self.semillas

    def eliminarBola(self, bola):
        self.bolas.remove(bola)
        return self.bolas