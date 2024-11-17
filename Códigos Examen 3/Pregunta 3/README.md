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
  - __size_alineacion__: función recursiva que calcula el tamaño y la alineación de un tipo
    - Se obtiene el tipo de dato, y se inicializan el tamaño máximo, tamaño empaquetado, tamaño no empaquetado, y la alineación máxima
    - Para cada campo del tipo:
      - Se sacan los detalles del campo
      - Caso base: si el campo es de tipo atómico, calcula el tamaño y la alineación
      - Si el campo es compuesto (struct o union), se llama a size_alineacion sobre el campo, y se obtiene el máximo de las alineaciones calculadas
      - Si no es atómico ni compuesto, error (BOOM)
      - Se actualiza el valor de la máxima alineación
      - Si el campo es union, el tamaño máximo será el máximo del tamaño máximo hasta el momento y la representación del campo; y el tamaño no empaquetado será el máximo del tamaño no empaquetado hasta el momento, y el tamaño no empaquetado obtenido al hacer la llamada recursiva
      - Si el campo es struct, simplemente se suma al tamaño empaquetado la representación obtenida en la recursión; y al tamaño no empaquetado se suma el tamaño no empaquetado obtenida en la recursión
    - Si el campo es union, el tamaño empaquetado será el tamaño del campo más grande; y el tamaño óptimo será el tamaño no empaquetado
    - Si el campo es struct, se agrega el padding necesario para el tamaño no empaquetado
    - Se retornan el tamaño empaquetado, el tamaño no empaquetado y el tamaño óptimo
  - __es_union__: verifica si un tipo es union
  - __describir_tipo__: proporciona una descripción del tipo de datos
    - Verifica que el tipo esté definido
    - Si el tipo es atómico, obtiene e imprime su nombre, representación y alineación
    - Si el tipo es compuesto, verifica si es de tipo union o struct, imprime el tipo, y llama al método describir_registro
  - __describir_registro__: proporciona la descripción de un registro (struct o union)
    - Calcula el tamaño empaquetado, no empaquetado y óptimo con la función size_alineacion
    - Imprime los resultados, obteniendo también los bytes desperdiciados en el caso empaquetado y no empaquetado

__main__: método principal
  - Se crea una instancia del manejador de tipos
  - Se itera con un while True
    - Pide al usuario que ingrese una opción
    - Divide la opción en partes
    - Verifica el valor de la primera parte (el comando)
      - Si es "ATOMICO" se verifica que la acción tenga 4 partes (el comando, el nombre, la representación y la alineación); si no es así, imprime un mensaje de error, y se da otra vuelta al ciclo
        - Obtiene el resto de partes de la acción, y llama al método que agrega el tipo atómico
       - Si es "STRUCT" se obtiene el resto de partes de la acción, y llama al método que agrega el tipo compuesto (como solo se agregaron dos parámetros, por defecto se sabe que no será un tipo union)
       - Si es "UNION" se obtiene el resto de partes de la acción, y llama al método que agrega el tipo compuesto (agregando como parámetro que si se trata de un tipo union)
       - Si es "DESCRIBIR" se verifica que la acción tenga 2 partes (el comando y el nombre del tipo); si no es así, imprime un mensaje de error, y se da otra vuelta al ciclo
         - Obtiene la otra parte de la acción y llama al método que describe al tipo
       - Si es "SALIR" imprime un mensaje de finalización del programa, y sale del ciclo
 
