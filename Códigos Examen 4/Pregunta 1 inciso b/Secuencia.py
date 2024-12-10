from abc import ABC, abstractmethod

class Secuencia(ABC):
    """Clase abstracta Secuencia"""
    @abstractmethod # Decorator que indica que el método es abstracto (debe ser instanciado por clases que hereden de Secuencia)
    def agregar(self, elemento):
        """Método abstracto agregar (se implementará en la subclase de Secuencia)"""
    
    @abstractmethod
    def remover(self):
        """Método abstracto remover (se implementará en la subclase de Secuencia)"""
    
    @abstractmethod
    def vacio(self):
        """Método abstracto vacio (se implementará en la subclase de Secuencia)"""

class Pila(Secuencia):
    """Clase Pila"""
    def __init__(self):
        """Constructor"""
        self.elementos = []
    
    def agregar(self, elemento):
        """Método que agrega un elemento al final de la pila"""
        self.elementos.append(elemento)
    
    def remover(self):
        """Función que elimina y retorna el último elemento de la pila"""
        if self.vacio():
            raise IndexError("La pila está vacía")
        return self.elementos.pop()
    
    def vacio(self):
        """Función que verifica si la pila está vacía"""
        return len(self.elementos) == 0

class Cola(Secuencia):
    """Clase Cola"""
    def __init__(self):
        self.elementos = []
    
    def agregar(self, elemento):
        """Método que agrega un elemento al final de la cola"""
        self.elementos.append(elemento)
    
    def remover(self):
        """Función que elimina y retorna el primer elemento de la cola"""
        if self.vacio():
            raise IndexError("La cola está vacía")
        return self.elementos.pop(0)
    
    def vacio(self):
        """Función que verifica si la cola está vacía"""
        return len(self.elementos) == 0
