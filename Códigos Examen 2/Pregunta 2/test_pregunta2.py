import unittest
from unittest.mock import patch
from Pregunta2 import eval_pre, eval_post, mostrar_pre, mostrar_post, main


class TestPregunta2(unittest.TestCase):
    """Clase para la prueba del Sistema"""
    def setUp(self):
        """Método que inicia el sistema para las pruebas"""
        #self.sistema = Pregunta3.Sistema()

    @patch('builtins.input', side_effect=[
        'HOLA',
        'EVAL',
        'EVAL EPA - * + 4 8 9 15',
        'EVAL PRE - * jaweno 4 8 9 15',
        'MOSTRAR PRE - * + 4 8 9 15',
        'EVAL PRE 1 2 +',
        'MOSTRAR POST 20 3 * 4 2 7 - * +',
        'EVAL POST + 1 2',
        'EVAL PRE / 4 0',
        'SALIR'
    ])
    
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input): # Se agrega un parámetro adicional por el funcionamiento del patch (éste inyecta parámetros adicionales)
        """Método que realiza la prueba del método main"""
        # Llamar a la función main que usará las entradas simuladas
        main()
        # Comprobar que las salidas esperadas se imprimieron
        mock_print.assert_any_call("Error: no se reconoce la acción HOLA")
        mock_print.assert_any_call("Error: se debe ingresar una acción, un orden y una expresión")
        mock_print.assert_any_call("Error: orden ingresado (EPA) inválido")
        mock_print.assert_any_call("Error: se ingresó un elemento (jaweno) inválido en la expresión")
        mock_print.assert_any_call("(4 + 8) * 9 - 15")
        mock_print.assert_any_call("Error: en el orden prefijo primero se ingresan los operadores")
        mock_print.assert_any_call("20 * 3 + 4 * (2 - 7)")
        mock_print.assert_any_call("Error: en el orden postfijo primero se ingresan los enteros")
        mock_print.assert_any_call("Error: No se puede dividir entre cero")
        mock_print.assert_any_call("Saliendo")

    def test_eval_pre(self):
        """Método que prueba la evaluación prefija"""
        self.assertEqual(eval_pre(['-', '*', '+', '4', '8', '9', '15']), 93)
        self.assertEqual(eval_pre(['-', '10', '2']), 8)
        self.assertEqual(eval_pre(['+', '1', '2']), 3)
        self.assertEqual(eval_pre(['*', '2', '3']), 6)
    
    def test_eval_post(self):
        """Método que prueba la evaluación postfija"""
        self.assertEqual(eval_post(['8', '3', '-', '8', '4', '4', '+', '*', '+']), 69)
        self.assertEqual(eval_post(['10', '2', '-']), 8)
        self.assertEqual(eval_post(['1', '2', '+']), 3)
        self.assertEqual(eval_post(['2', '3', '*']), 6)
    
    def test_mostrar_pre(self):
        """Método que prueba mostrar una expresión en prefija"""
        self.assertEqual(mostrar_pre(['-', '*', '+', '4', '8', '9', '15']), '(4 + 8) * 9 - 15')
        self.assertEqual(mostrar_pre(['-', '10', '2']), '10 - 2')
        self.assertEqual(mostrar_pre(['+', '1', '2']), '1 + 2')
        self.assertEqual(mostrar_pre(['*', '2', '3']), '2 * 3')
    
    def test_mostrar_post(self):
        """Método que prueba mostrar una expresión en postfija"""
        self.assertEqual(mostrar_post(['8', '3', '-', '8', '4', '4', '+', '*', '+']), '8 - 3 + 8 * (4 + 4)')
        self.assertEqual(mostrar_post(['10', '2', '-']), '10 - 2')
        self.assertEqual(mostrar_post(['1', '2', '+']), '1 + 2')
        self.assertEqual(mostrar_post(['2', '3', '*']), '2 * 3')
           

if __name__ == '__main__':
    unittest.main()
