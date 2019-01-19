class ArregloBinario(object):
    """
    """    

    def __init__(self, arry):
        self.arreglo = arry
    
    def Busqueda(self, item):
        pos = -1 #posicion inicia en -1
        inf = 0
        sup = len(self.arreglo) -1
        mitad = int((inf + sup +1) /2) 
        item_bin = item
        
        while (inf <= sup) and (pos == -1):
            if(item_bin == self.arreglo[mitad]):# si el elemento se encuentra en medio
                pos = mitad# la ubicaci�n es el elemento medio actual
            
            if(item_bin < self.arreglo[mitad]):
                sup = mitad - 1# elimina la mitad superior
            
            else:
                inf = mitad + 1# elimina la mitad inferior 

            mitad = int((inf + sup +1) / 2)# recalcula el elemento medio
 
        return pos #Retorna la poscicion


