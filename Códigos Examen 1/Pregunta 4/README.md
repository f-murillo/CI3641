Pregunta 4 - Franco Murillo - 1610782

Programa que implementa los cuaterniones y sus operaciones

El código para resolver el problema fue hecho en Python

Clases y Métodos
- Cuaternion: representa los cuaterniones con sus operaciones
    - __init__ : constructor que inicializa los componentes del cuaternion

    - Se redefinieron los operadores ==, +, *, ~ y abs dentro del contexto de los cuaterniones
        - __eq__ : Permite comparar pares de cuaterniones
            - Retorna si cada componente de cada cuaternion es igual
            - Si se intenta comparar un cuaternion con cualquier otra cosa, retorna False
        - __add__ : Permite aplicar sumas sobre cuaterniones 
            - Si ambos sumandos son cuaterniones, retorna un cuaternion cuyas componentes son la suma definida de cuaterniones
            - Si el sumando de la derecha es un entero o un real, únicamente suma el primer componente del cuaternion con el sumando; el resto de componentes se mantienen
            - Si el sumando de la derecha no es un cuaternion, ni un entero ni un real, retorna un error de tipo
        - __radd__ : Permite aplicar suma sobre cuaterniones, cuando el sumando de la izquierda es un entero o real, y el sumando de la derecha es un cuaternion
        - __mul__ : Permite aplicar multiplicaciones sobre cuaterniones 
            - Si ambos miembros de la multiplicación son cuaterniones, retorna un cuaternion cuyas componentes son el producto definido de cuaterniones
            - Si el miembro de la derecha es un entero o un real, únicamente multiplica el primer componente del cuaternion con el miembro; el resto de componentes se mantienen
            - Si el miembro de la derecha no es un cuaternion, ni un entero ni un real, retorna un error de tipo
        - __rmul__ : Permite aplicar multiplicación sobre cuaterniones, cuando el miembro de la izquierda es un entero o real, y el miembro de la derecha es un cuaternion
        - __invert__ : Permite aplicar el inverso (conjugado) a cuaterniones
            - Retorna un cuaternion cuyo primer componente es el mismo del cuaternion original, y el resto de componentes son el negativo del resto de las componentes del cuaternion original
        - __abs__ : Permita aplicar el valor absoluto de un cuaternion
            - Retorna la raíz cuadrada de la suma de los componentes al cuadrado
        - __rep__ : Permite tener una representación en String del cuaternion
       
    - NOTA: no fue posible redefinir "&" para su uso en el programa, por lo que se usa "abs"

Ejecución del programa
- Desde algún editor de código o IDE donde sea posible ejecutar código Python
- Desde la terminal (estando ubicado en el directorio donde se encuentra el archivo):
        
        > python Pregunta4.py

Ejecución de las pruebas con cobertura (teniendo instalados unittest y coverage)
- Para las pruebas con cobertura
      
        > coverage run -m unittest test_pregunta4.py

- Para un reporte de la cobertura
      
        > coverage report -m

- Si se quiere un reporte de la cobertura hecho en HTML
      
        > coverage html
        

