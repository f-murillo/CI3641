import unittest
from unittest.mock import patch
import pregunta3

class TestManejador(unittest.TestCase):
    """Clase para los tests del manejador"""
    def setUp(self):
        """Método que inicializa el manejador"""
        self.handler = pregunta3.VirtualMethodTableHandler()
        
    @patch('builtins.input', side_effect=[
        'HOLA',
        'CLASE A',
        'CLASE A wenas hellou',
        'CLASE A jaweno',
        'CLASE B : A a lo',
        'DESCRIBIR A',
        'CLASE C : F w e p a',
        'CLASE F t t',
        'DESCRIBIR H',
        'DESCRIBIR A JAMON Y QUESO',
        'SALIR'
    ])
    
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input): # Se agrega un parámetro adicional por el funcionamiento del patch (éste inyecta parámetros adicionales)
        """Método que realiza la prueba del método main"""
        # Llamar a la función main que usará las entradas simuladas
        pregunta3.main()

        # Capturamos toda la salida generada
        output = [call.args[0] for call in mock_print.call_args_list]

        # Salidas esperadas
        expected_output = [
            "Acción HOLA no reconocida",
            "Error: número de argumentos erróneo",
            "Clase A creada exitosamente",
            "Error: La clase A ya existe.",
            "Clase B creada exitosamente",
            "wenas -> A :: wenas",
            "hellou -> A :: hellou",
            "Error: La super clase F no existe.",
            "Error: Hay definiciones de métodos repetidas en F.",
            "Error: La clase H no existe.",
            "Error: número de argumentos erróneo",
            "Saliendo del programa"
        ]

        # Comprobamos que las salidas esperadas se imprimieron
        for expected in expected_output:
            self.assertIn(expected, output)
            
    def test_define_class_no_inheritance(self):
        """Prueba para definir una clase sin herencia"""
        self.handler.define_class("CLASE A metodo1 metodo2")
        self.assertIn("A", self.handler.classes)
        self.assertEqual(self.handler.classes["A"]["super"], None)
        self.assertDictEqual(self.handler.classes["A"]["metodos"], {
            "metodo1": "A :: metodo1",
            "metodo2": "A :: metodo2"
        })
    
    def test_define_class_inheritance(self):
        """Prueba para definir una clase con herencia"""
        self.handler.define_class("CLASE A metodo1 metodo2")
        self.handler.define_class("CLASE B : A metodo3")
        self.assertIn("B", self.handler.classes)
        self.assertEqual(self.handler.classes["B"]["super"], "A")
        self.assertDictEqual(self.handler.classes["B"]["metodos"], {
            "metodo1": "A :: metodo1",
            "metodo2": "A :: metodo2",
            "metodo3": "B :: metodo3"
        })
    
    def test_define_existing_class(self):
        """Prueba para definir una clase que ya existe"""
        self.handler.define_class("CLASE A metodo1 metodo2")
        with patch('builtins.print') as mock_print:
            self.handler.define_class("CLASE A metodo3")
            mock_print.assert_called_with("Error: La clase A ya existe.")
    
    def test_define_class_no_superclass(self):
        """Prueba para definir una clase con una superclase que no existe"""
        with patch('builtins.print') as mock_print:
            self.handler.define_class("CLASE B : A metodo1 metodo2")
            mock_print.assert_called_with("Error: La super clase A no existe.")
    
    def test_define_class_duplicate_methods(self):
        """Prueba para definir una clase con métodos duplicados"""
        with patch('builtins.print') as mock_print:
            self.handler.define_class("CLASE A metodo1 metodo1")
            mock_print.assert_called_with("Error: Hay definiciones de métodos repetidas en A.")
    
    def test_describe_existing_class(self):
        """Prueba para describir una clase existente"""
        self.handler.define_class("CLASE A metodo1 metodo2")
        with patch('builtins.print') as mock_print:
            self.handler.describe_class("A")
            mock_print.assert_any_call("metodo1 -> A :: metodo1")
            mock_print.assert_any_call("metodo2 -> A :: metodo2")
    
    def test_describe_no_class(self):
        """Prueba para describir una clase que no existe"""
        with patch('builtins.print') as mock_print:
            self.handler.describe_class("A")
            mock_print.assert_called_with("Error: La clase A no existe.")
            

if __name__ == '__main__':
    unittest.main()
