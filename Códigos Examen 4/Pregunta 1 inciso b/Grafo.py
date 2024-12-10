from abc import ABC, abstractmethod
from collections import deque

class Grafo:
    """Clase Grafo (ya que no es especifica en el enunciado, se optó por trabajar con un grafo no dirigido)"""
    def __init__(self):
        """Constructor"""
        self.adjacencias = {} # Diccionario para guardar las adyacencias de cada nodo

    def agregar_arista(self, origen, destino):
        """Método que agrega una arista al grafo"""
        if origen not in self.adjacencias: # Si el nodo origen no está en el diccionario de adyacencias, se agrega, junto con una lista vacía de sus adyacentes
            self.adjacencias[origen] = []
        if destino not in self.adjacencias: # Lo mismo que para el nodo origen
            self.adjacencias[destino] = []
        # Se agrega cada nodo a la lista de adyacencias del otro
        self.adjacencias[origen].append(destino)
        self.adjacencias[destino].append(origen)
        
    def obtener_vecinos(self, nodo):
        """Método que obtiene los vecinos de un nodo"""
        return self.adjacencias.get(nodo, [])

class Busqueda(ABC):
    """Clase abstracta Busqueda"""
    def __init__(self, grafo):
        """Constructor"""
        self.grafo = grafo

    @abstractmethod
    def buscar(self, D, H):
        """Función abstracta buscar (se implementará en la subclase que herede de Busqueda)"""
  
class DFS(Busqueda):
    """Clase DFS"""
    def buscar(self, D, H):
        """Función que busca un nodo H a partir de un nodo D en un grafo por profundidad"""
        visitados = set() # Conjunto para llevar control de los nodos visitados
        stack = [(D, 0)]  # Pila para la búsqueda en profundidad

        while stack: # Mientras la pila no esté vacía
            nodo, profundidad = stack.pop() # Desempilamos el último nodo en la pila con su profundidad
            if nodo == H: # Si nodo es H, llegamos al destino
                return profundidad  # Retornamos la profundidad en la que se encontró

            if nodo not in visitados: # Si el nodo explorado no está en el conjunto de visitados, se agrega
                visitados.add(nodo)
                for vecino in self.grafo.obtener_vecinos(nodo): # Para cada vecino del nodo
                    if vecino not in visitados: # Si el vecino no ha sido visitado, se empila el vecino, junto con la profundidad en la que se encuentra
                        stack.append((vecino, profundidad + 1))

        # Si se llegó a este punto, no se puede llegar al nodo destino
        return -1

class BFS(Busqueda):
    def buscar(self, D, H):
        """Función que busca un nodo H a partir de un nodo D en un grafo por amplitud"""
        visitados = set() # Conjunto para llevar control de los nodos visitados
        queue = deque([(D, 0)])  # Cola para la búsqueda en amplitud

        while queue: # Mientras la cola no esté vacía
            nodo, capa = queue.popleft() # Desencolamos el primer nodo con su capa
            if nodo == H: # Si nodo es H, llegamos al destino
                return capa  # Retornamos la capa en la que se encontró

            if nodo not in visitados: # Si el nodo explorado no está en el conjunto de visitados, se agrega
                visitados.add(nodo)
                
                for vecino in self.grafo.obtener_vecinos(nodo): # Para cada vecino del nodo
                    if vecino not in visitados: # Si el vecino no ha sido visitado, se encola el vecino, junto con la capa en la que se encuentra
                        queue.append((vecino, capa + 1))

        # Si se llegó a este punto, no se puede llegar al nodo destino
        return -1