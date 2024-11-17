import unittest
from unittest.mock import patch
from Pregunta3 import TipoAtomico, TipoCompuesto, ManejadorTipos, main 

class TestManejadorTipos(unittest.TestCase):

    def setUp(self):
        """Método que inicializa un manejador de tipos para usar en las pruebas"""
        self.manejador = ManejadorTipos()

    @patch('builtins.input', side_effect=[
        'ATOMICO char 1 2',
        'ATOMICO char 1 5',
        'ATOMICO int 4 4',
        'DESCRIBIR wenas',
        'STRUCT wenas char int',
        'ATOMICO atomico',
        'DESCRIBIR wenas hellou',
        'DESCRIBIR wenas',
        'SALIR'
    ])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        """Método que realiza la prueba del método main"""
        # Llamamos a la función main que usará las entradas simuladas
        main()

        # Capturamos toda la salida generada
        output = [call.args[0] for call in mock_print.call_args_list]

        # Salidas esperadas
        expected_output = [
            "Error: el tipo 'char' ya existe.",
            "Error: el tipo 'wenas' no está definido.",
            "Error: faltan argumentos o hay argumentos de mas",
            "Tipo Struct: wenas",
            "Tamaño empaquetado: 5 bytes",
            "Tamaño no empaquetado: 6 bytes",
            "Tamaño óptimo: 8 bytes",
            "Bytes desperdiciados (empaquetado): 3 bytes",
            "Bytes desperdiciados (no empaquetado): 2 bytes",
            "Saliendo"
        ]

        # Comprobamos que las salidas esperadas se imprimieron
        for expected in expected_output:
            self.assertIn(expected, output)

    def test_agregar_tipo_atomico(self):
        """Método que prueba la adición de un tipo atómico"""
        self.manejador.agregar_tipo_atomico("char", 1, 2)
        self.assertIn("char", self.manejador.tipos)
        self.assertIsInstance(self.manejador.tipos["char"], TipoAtomico)
        self.assertEqual(self.manejador.tipos["char"].representacion, 1)
        self.assertEqual(self.manejador.tipos["char"].alineacion, 2)

    def test_agregar_tipo_compuesto_struct(self):
        """Método que prueba la adición de un tipo compuesto (struct)"""
        self.manejador.agregar_tipo_atomico("char", 1, 2)
        self.manejador.agregar_tipo_atomico("int", 4, 4)
        self.manejador.agregar_tipo_compuesto("foo", ["char", "int"])
        self.assertIn("foo", self.manejador.tipos)
        self.assertIsInstance(self.manejador.tipos["foo"], TipoCompuesto)

    def test_agregar_tipo_compuesto_union(self):
        """Método que prueba la adición de un tipo compuesto (union)"""
        self.manejador.agregar_tipo_atomico("char", 1, 2)
        self.manejador.agregar_tipo_atomico("int", 4, 4)
        self.manejador.agregar_tipo_compuesto("union_foo", ["char", "int"], es_union=True)
        self.assertIn("union_foo", self.manejador.tipos)
        self.assertIsInstance(self.manejador.tipos["union_foo"], TipoCompuesto)

    def test_size_alineacion_struct(self):
        """Método que prueba el cálculo de tamaño y alineación para un struct"""
        self.manejador.agregar_tipo_atomico("char", 1, 2)
        self.manejador.agregar_tipo_atomico("int", 4, 4)
        self.manejador.agregar_tipo_compuesto("foo", ["char", "int"])
        size_empaquetado, size_no_empaquetado, size_optimo = self.manejador.size_alineacion("foo")
        self.assertEqual(size_empaquetado, 5)
        self.assertEqual(size_no_empaquetado, 6)
        self.assertEqual(size_optimo, 8)

    def test_size_alineacion_union(self):
        """Método que prueba el cálculo de tamaño y alineación para una union"""
        self.manejador.agregar_tipo_atomico("char", 1, 2)
        self.manejador.agregar_tipo_atomico("int", 4, 4)
        self.manejador.agregar_tipo_compuesto("union_foo", ["char", "int"], es_union=True)
        size_empaquetado, size_no_empaquetado, size_optimo = self.manejador.size_alineacion("union_foo", es_union=True)
        self.assertEqual(size_empaquetado, 4)
        self.assertEqual(size_no_empaquetado, 4)
        self.assertEqual(size_optimo, 4)

    def test_describir_tipo(self):
        """Método que prueba la descripción de un tipo compuesto"""
        self.manejador.agregar_tipo_atomico("char", 1, 2)
        self.manejador.agregar_tipo_atomico("int", 4, 4)
        self.manejador.agregar_tipo_compuesto("foo", ["char", "int"])
        self.manejador.describir_tipo("foo")

if __name__ == '__main__':
    unittest.main()
