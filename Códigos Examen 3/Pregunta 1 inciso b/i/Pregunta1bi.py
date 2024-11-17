class Church:
    """Clase que representa el numeral de Church"""
    pass

class Cero(Church):
    """Clase que representa el cero en el contexto de los nuemrales de Church"""
    def __init__(self):
        """Constructor"""
        pass
    def __str__(self):
        """Para representarlo con String"""
        return "Cero"

class Suc(Church):
    """Clase que representa al sucesor de un nuemral de Church"""
    def __init__(self, pred):
        """Constructor"""
        self.pred = pred
    def __str__(self):
        """Para representarlo con String"""
        return f"Suc({self.pred})"

def suma(a, b):
    """Método que suma dos numerales de Church"""
    if isinstance(a, Cero): # Si a es Cero
        return b
    # Si a es sucesor de otro numeral de Church
    return Suc(suma(a.pred, b))

def multiplicacion(a, b):
    """Método que multiplica dos numerales de Church"""
    if isinstance(a, Cero): # Si a es Cero
        return Cero()
    # Si a es sucesor de otro numeral de Church
    return suma(b, multiplicacion(a.pred, b))
