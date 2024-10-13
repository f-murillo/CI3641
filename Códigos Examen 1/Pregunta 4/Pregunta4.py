import math

class Cuaternion:
    """Clase que implementa el cuaternion y sus operaciones"""
    def __init__(self, a=0, b=0, c=0, d=0):
        """Constructor"""
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __eq__(self, other):
        """Método para redefinir el operador ==, para hacer comparables pares de cuaterniones"""
        if isinstance(other, Cuaternion):
            return (self.a == other.a and self.b == other.b and
                    self.c == other.c and self.d == other.d)
        # En caso de que se intente comparar un cuaternion con algo que no es un cuaternion
        return False

    def __add__(self, other):
        """Método que redefine el operador + para el contexto de la clase Cuaternion"""
        # Si lo que se está pasando es un cuaternion
        if isinstance(other, Cuaternion):
            return Cuaternion(
                self.a + other.a,
                self.b + other.b,
                self.c + other.c,
                self.d + other.d
            )
        # Si en cambio lo que se está pasando es un entero o un real
        elif isinstance(other, (int, float)):
            return Cuaternion(
                self.a + other,
                self.b,
                self.c,
                self.d
            )
        else:
            # Si no se pasa un cuaterion, un entero o un real, error
            raise TypeError(f"Error: la operacion no esta soportada para el tipo {type(other)}")

    def __radd__(self, other):
        """Método que implementa la suma del lado derecho"""
        return self.__add__(other)

    def __mul__(self, other):
        """Método que redefine el operador + para el contexto de la clase Cuaternion"""
        # Si lo que se está pasando es un cuaternion
        if isinstance(other, Cuaternion):
            return Cuaternion(
                self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d,
                self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c,
                self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b,
                self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a
            )
        # Si en cambio lo que se está pasando es un entero o un real
        elif isinstance(other, (int, float)):
            return Cuaternion(
                self.a * other,
                self.b * other,
                self.c * other,
                self.d * other
            )
        else:
            # Si no se pasa un cuaterion, un entero o un real, error
            raise TypeError(f"Error: la operacion no esta soportada para el tipo {type(other)}")

    def __rmul__(self, other):
        """Método que implementa la multiplicación del lado derecho"""
        return self.__mul__(other)

    def __invert__(self):
        """Método que redefine el operador ~ para el contexto de la clase Cuaternion"""
        return Cuaternion(self.a, -self.b, -self.c, -self.d)

    def __abs__(self):
        """Método que redefine el operador abs (modulo o valor absoluto) para el contexto de la clase Cuaternion"""
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)

    def __repr__(self):
        """Método que permite ver una representación del Cuaternion"""
        return f"{self.a} + {self.b}i + {self.c}j + {self.d}k"

# Uso
a = Cuaternion(1, 2, 3, 4)
b = Cuaternion(5, 6, 7, 8)
c = Cuaternion(9, 10, 11, 12)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"a + b = {a + b}")         # Suma de cuaterniones
print(f"~a = {~a}")               # Conjugada de un cuaternión
print(f"a * b = {a * b}")         # Producto de cuaterniones
print(f"abs(c) = {abs(c)}")       # Valor absoluto de un cuaternión
print(f"b + 3 = {b + 3}")         # Suma de un cuaternión con un entero
print(f"3 + b = {3 + b}")         # Al reves
print(f"a * 3.0 = {a * 3.0}")     # Producto de un cuaternión con un real
print(f"3.0 * a = {3.0 * a}")     # Al reves
print(f"(a + b) * (~c) = {(a + b) * (~c)}")  # Operaciones combinadas
