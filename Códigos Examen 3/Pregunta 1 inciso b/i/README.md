Pregunta 1 - Inciso b - i - Franco Murillo 1610782

# Implementación de los numerales de Church, así como las funciones que suman y multiplican pares de numerales de Church

# __Clases__

Church
  - Es una clase base vacía que se usa para definir la jerarquía de tipo.
  - No tiene métodos ni propiedades.
  - Se usa principalmente para agrupar las clases Cero y Suc bajo un mismo tipo base

Cero
  - Clase que representa el primer numeral de Church
  - __init__: constructor. Inicializa una instancia de la clase Cero
  - __str__: Devuelve el String "Cero" cuando se quiera imprimir una instancia de la clase Cero

Suc
  - Clase que representa el sucesor de un numeral de Church
  - __init__: constructor. Inicializa una instancia de Suc con un predecesor, el cual es otro numeral de Church
  - __str__: Devuelve el String "Suc(<pred>)", donde <pred> es una representación del predecesor

# __Funciones__

suma
  - Suma dos numerales de Church a y b recursivamente
  - Si a es Cero, retorna b (0 + b = b)
  - Si no (significa que a es sucesor de algún otro numeral de Church) llama a suma con el predecesor de a, y b
  - La función asume que las entradas son correctas (dos numerales de Church)

multiplicacion
  - Multiplica dos numerales de Church a y b recursivamente
  - Si a es Cero, retorna Cero (0 * b = 0)
  - Si no (significa que a es sucesor de algún otro numeral de Church) llama a la función suma con b como primer parámetro, y la función multiplicacion con el predecesor de a y b como segundo parámetro
  - La función asume que las entradas son correctas (dos numerales de Church)

