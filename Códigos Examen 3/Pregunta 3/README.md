Pregunta 3 - Franco Murillo 1610782

# Programa que simula un manejador de tipos de datos

El programa fue hecho en Python

# Clases

__TipoAtomico__: implementa los tipos atómicos, con un nombre, una representación y una alineación

__TipoCompuesto__: implementa los tipos de registros (struct) o registros variantes (union), con un nombre y sus campo

__ManejadorTipos__: implementa el manejador de tipos
  - __init__: constructor. Inicializa un diccionario para los tipos
  - __agregar_tipo_atomico__: agrega un nuevo tipo atómico. Verifica que el tipo no haya sido agregado antes
  - __agregar_tipo_compuesto__: agrega un nuevo tipo de registro (struct o union). Verifica que el tipo no haya sido agregado antes, y que los campos estén definidos
  - __agregar_tipo_union__: agrega un nuevo tipo de registro variante. Verifica que el tipo no haya sido agregado antes, y que los campos estén definidos
  - __size_alineacion__: calcula el tamaño y la alineación de un tipo
    - Se obtiene el tipo de dato, y se inicializan el tamaño máximo, tamaño empaquetado, tamaño no empaquetado, y la alineación máxima
  - __describir_tipo__: proporciona una descripción del tipo de datos
    - Verifica que el tipo esté definido
    - Si el tipo es atómico, obtiene e imprime su nombre, representación y alineación
    - Si el tipo es struct, imprime su nombre, y llama a describir_registro con los campos del registro
 
