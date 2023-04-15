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
        if len(self.bolas) == 2:
            return True
        else:
            return False    
    
    def showOperador(self):
        return self.operador
    
    def showProfundidad(self):
        return self.profundidad
    
    def same_state(self):
        if self.bolas == self.padre.bolas and self.frezzers == self.padre.freezers and self.cells == self.padre.cells and self.semillas == self.padre.semillas:
            return True
        else:
            return False