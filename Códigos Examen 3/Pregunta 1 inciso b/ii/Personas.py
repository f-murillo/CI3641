from collections import Counter # Para contar las ocurrencia de nombres en el conjunto de personas

class Persona:
    """Clase que implementa una persona"""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        """Para mostrar el nombre y la edad de la persona"""
        return f"{self.nombre}, {self.edad} años"

class ConjuntoPersonas:
    """Clase que implementa conjuntos de personas"""
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        """Método que agrega una persona al conjunto"""
        self.personas.append(persona)

    def cantidad_personas(self):
        """Método que retorna la cardinalidad del conjunto"""
        return len(self.personas)

    def mayores_de_edad(self):
        """Método que retorna una lista con los mayores de edad del conjunto"""
        return [persona for persona in self.personas if persona.edad >= 18]

    def nombre_mas_comun(self):
        """Método que retorna el nombre más común del conjunto"""
        nombres = [persona.nombre for persona in self.personas]
        if not nombres: # Si no hay nombres (en caso de que no haya conjunto alguno)
            return None
        contador_nombres = Counter(nombres) # Se crea una instancia de Counter
        nombre_comun = contador_nombres.most_common(1)[0][0] # Se obtiene el nombre mas comun
        return nombre_comun