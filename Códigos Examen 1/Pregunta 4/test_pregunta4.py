import math
import unittest
from Pregunta4 import Cuaternion

class TestCuaternion(unittest.TestCase):
    """Clase que implementa las pruebas para la clase Cuaternion"""
    def setUp(self):
        """Método que inicializa los cuaterniones para las pruebas"""
        self.a = Cuaternion(1, 2, 3, 4)
        self.b = Cuaternion(5, 6, 7, 8)
        self.c = Cuaternion(9, 10, 11, 12)

    def test_eq(self):
        """Método que prueba el funcionamiento del método __eq__"""
        # Caso en el que son iguales
        self.assertTrue(self.a == Cuaternion(1,2,3,4))
        # Caso en el que no son iguales
        self.assertFalse(self.a == Cuaternion(4,3,2,1))
        # Caso en el que se compara un cuaternion con algo de otro tipo
        self.assertFalse(self.a == 5)
        
    def test_add(self):
        """Método que prueba el funcionamiento del método __add__"""
        # Casos con los tipos correctos
        resultado = self.a + self.b
        self.assertEqual(resultado, Cuaternion(6, 8, 10, 12))
        self.assertEqual(self.a + 3, Cuaternion(4, 2, 3, 4))
        self.assertEqual(3 + self.a, Cuaternion(4, 2, 3, 4))
        
        # Casos con tipos incorrectos
        with self.assertRaises(TypeError):
            resultado = self.a + "string"
        with self.assertRaises(TypeError):
            resultado = self.a + []

    def test_mul(self):
        """Método que prueba el funcionamiento del método __mul__"""
        # Casos con los tipos correctos
        resultado = self.a * self.b
        self.assertEqual(resultado, Cuaternion(-60, 12, 30, 24))
        self.assertEqual(self.a * 3, Cuaternion(3, 6, 9, 12))
        self.assertEqual(3 * self.a, Cuaternion(3, 6, 9, 12))
        
        # Casos con valores incorrectos
        with self.assertRaises(TypeError):
            resultado = self.a * "string"
        with self.assertRaises(TypeError):
            resultado = self.a * []

    def test_invert(self):
        """Método que prueba el funcionamiento del método __invert__ (conjudado de un cuaternion)"""
        resultado = ~self.a
        self.assertEqual(resultado, Cuaternion(1, -2, -3, -4))

    def test_abs(self):
        """Método que prueba el funcionamiento del método __abs__ (valor absoluto de un cuaternion)"""
        resultado = abs(self.a)
        self.assertEqual(resultado, math.sqrt(1**2 + 2**2 + 3**2 + 4**2))
        self.assertEqual(abs(self.a), math.sqrt(30))

    def test_combinado(self):
        """Método que prueba el funcionamiento de los métodos combinados"""
        resultado = (self.a + self.b) * ~self.c
        esperado = Cuaternion(6, 8, 10, 12) * Cuaternion(9, -10, -11, -12)
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
