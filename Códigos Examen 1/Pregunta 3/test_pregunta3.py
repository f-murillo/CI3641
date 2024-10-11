import unittest
from unittest.mock import patch
import Pregunta3

class TestSistema(unittest.TestCase):
    """Clase para la prueba del Sistema"""
    def setUp(self):
        """Método que inicia el sistema para las pruebas"""
        self.sistema = Pregunta3.Sistema()

    @patch('builtins.input', side_effect=[
        'HOLA',
        'DEFINIR WTF holamundo C++',
        'DEFINIR PROGRAMA fibonacci LOCAL',
        'EJECUTABLE fibonacci',
        'DEFINIR PROGRAMA factorial Java',
        'DEFINIR INTERPRETE C Java',
        'DEFINIR TRADUCTOR C Java C',
        'EJECUTABLE factorial',
        'DEFINIR INTERPRETE LOCAL C',
        'EJECUTABLE factorial',
        'SALIR'
    ])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input): # Se agrega un parámetro adicional por el funcionamiento del patch (éste inyecta parámetros adicionales)
        """Método que realiza la prueba del método main"""
        # Llamar a la función main que usará las entradas simuladas
        Pregunta3.main()

        # Comprobar que las salidas esperadas se imprimieron
        mock_print.assert_any_call("Error: no se reconoce la accion 'HOLA'")
        mock_print.assert_any_call("Error: no se reconoce el tipo 'WTF'")
        mock_print.assert_any_call("Se definio el programa 'fibonacci', ejecutable en 'LOCAL'")
        mock_print.assert_any_call("Si, es posible ejecutar el programa 'fibonacci'")
        mock_print.assert_any_call("Se definio el programa 'factorial', ejecutable en 'Java'")
        mock_print.assert_any_call("Se definio un interprete para 'Java', escrito en 'C'")
        mock_print.assert_any_call("No es posible ejecutar el programa 'factorial'")
        mock_print.assert_any_call("Se definio un traductor de 'Java' hacia 'C', escrito en 'C'")
        mock_print.assert_any_call("Si, es posible ejecutar el programa 'factorial'")
        mock_print.assert_any_call("Saliendo del programa")

    def test_definir_programa(self):
        """Método para la prueba de definir_programa"""
        self.sistema.definir_programa('fibonacci', 'LOCAL')
        # Prueba en la que el programa ya existe
        self.sistema.definir_programa('fibonacci', 'C')
        # Aserción de que el programa efectivamente se agregó al diccionario de programas
        self.assertIn('fibonacci', self.sistema.programas)
        # Aserción de que la clave de 'fibonacci' efectivamente sea 'LOCAL'
        self.assertEqual(self.sistema.programas['fibonacci'].lenguaje, 'LOCAL')

    def test_definir_interprete(self):
        """Método para la prueba de definir_interprete"""
        self.sistema.definir_interprete('C', 'Java')
        # Prueba en la que el interprete ya fue definido 
        self.sistema.definir_interprete('C', 'Java')
        # Aserción de que el lenguaje efectivamente se agregó al diccionario de interpretes
        self.assertIn('Java', self.sistema.interpretes)
        # Aserción de que la clave de 'Java' efectivamente sea 'C'
        self.assertEqual(self.sistema.interpretes['Java'].lenguaje_base, 'C')

    def test_definir_traductor(self):
        """Método para la prueba de definir_traductor"""
        self.sistema.definir_traductor('C', 'Java', 'C')
        # Prueba en la que el traductor ya fue definido 
        self.sistema.definir_traductor('C', 'Java', 'C')
        # Aserción de que el lenguaje efectivamente se agregó al diccionario de interpretes
        self.assertIn('Java', self.sistema.traductores)
        # Aserción de que la clave de 'Java' efectivamente sea 'C'
        self.assertEqual(self.sistema.traductores['Java'].lenguaje_destino, 'C')

    def test_ejecutable_programa_local(self):
        """Método para probar el caso base de ejecutableRec"""
        self.sistema.definir_programa('fibonacci', 'LOCAL')
        self.sistema.ejecutable('fibonacci')
        self.assertTrue(self.sistema.ejecutableRec('LOCAL'))

    def test_ejecutable(self):
        """Método para probar ejecutable y ejecutableRec"""
        self.sistema.definir_programa('factorial', 'Java')
        self.sistema.definir_interprete('LOCAL', 'Java')
        # Asersión de que el programa factorial sea efectivamente ejecutable
        self.assertEqual(self.sistema.ejecutableRec('Java'), True)
        # Pruebas con programa y lenguaje que no están definidos
        self.sistema.ejecutable('hola')
        self.assertFalse(self.sistema.ejecutableRec('F'))

if __name__ == '__main__':
    unittest.main()
