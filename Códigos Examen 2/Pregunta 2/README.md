Pregunta 2 - Franco Murillo 16-10782

Programa que maneja expresiones aritméticas sobre enteros, tanto expresiones escritas en orden pre-fijo como post-fijo

__Métodos__

- __eval_pre__: Evalúa una expresión escrita en orden pre-fijo
        - Inicializa una pila vacía, en la cual se irán empilando los números y operadores
        - Para cada elemento la expresión leído de derecha a izquierda:
            - Si el elemento es un entero, se empila
            - Si no, quiere decir que el elemento es un operador, por lo que se desempilan dos números, se operan, y se empila el resultado
        - Al final, retorna el tope de la pila, que tendrá el resultado de la evaluación
        - Complejidad temporal: __O(len(expr))__, donde expr es la expresión a evaluar

- __eval_post__: Evalúa una expresión escrita en orden pre-fijo
        - Inicializa una pila vacía, en la cual se irán empilando los números y operadores
        - Para cada elemento de la expresión leído de izquierda a derecha:
            - Si el elemento es un entero, se empila
            - Si no, quiere decir que el elemento es un operador, por lo que se desempilan dos números, se operan, y se empila el resultado
        - Al final, retorna el tope de la pila, que tendrá el resultado de la evaluación
        - Complejidad temporal: __O(len(expr))__, donde expr es la expresión a evaluar

- __precedencia__: Retorna la precedencia de un operador
        - Si la operación es suma o resta, retorna 1
        - Si la operación es multiplicación o división, retorna 2
        - Si no es ninguna de las operaciones anteriores, retorna 0
        - Complejidad temporal: __O(1)__

- __mostrar_pre__: Muestra una expresión aritmética en notación infija
        - Declara una pila vacía
        - Para cada elemento de la expresión leído de derecha a izquierda:
            - Si el elemento es un entero, se empila
            - Si es un operador, desempila los dos últimos enteros y forma una subexpresión, agregando paréntesis (si es necesario) dependiendo de la precendencia del operador anterior y posterior. Luego empila la subexpresión formada
        - Finalmente, retorna el tope de la pila, que tendrá la expresión en notación infija
        - Complejidad temporal: __O(len(expr))__, donde expr es la expresión a mostrar

- __mostrar_post__: Muestra una expresión aritmética en notación postfija
        - Declara una pila vacía
        - Para cada elemento de la expresión leído de izquierda a derecha:
            - Si el elemento es un entero, se empila
            - Si es un operador, desempila los dos últimos enteros y forma una subexpresión, agregando paréntesis (si es necesario) dependiendo de la precendencia del operador anterior y posterior. Luego empila la subexpresión formada
        - Finalmente, retorna el tope de la pila, que tendrá la expresión en notación postfija
        - Complejidad temporal: __O(len(expr))__, donde expr es la expresión a mostrar

- __main__: Método principal
  - Declara un ciclo while que se ejecutará hasta que se desee salir
  - Pide al usuario que ingrese una opción, las cuales pueden ser EVAL, MOSTRAR o SALIR. La opción ingresada debe estar en mayúsculas
  - Si se ingresa EVAL, se deberá ingresar un orden de evaluación, el cual debe ser PRE o POST (debe ser ingresado en mayúsculas), seguido de la expresión a evaluar. Por ejemplo:
    ```
    EVAL PRE - * + 4 8 9 15 
    ```
    o:
    ```
    EVAL POST 20 3 * 4 2 7 - * + 
    ```

  - Si se ingresa MOSTRAR, al igual que antes, se deberá ingresar el orden de evaluación (PRE o POST, en mayúsculas), seguido de la expresión a evaluar. Por ejemplo:
    ```
    MOSTRAR PRE - * + 4 8 9 15 
    ```
    o:
    ```
    MOSTRAR POST 20 3 * 4 2 7 - * + 
    ```
- Tanto si se ingresa EVAL, como MOSTRAR, se verificará que efectivamente se ingrese una expresión y un orden, y que dicha expresión y orden sean correctos. Es decir, que el orden sea PRE o POST, que en la expresión haya al menos 3 elementos, y que únicamente tenga enteros y los símbolos '+', '-', '*' o '/'.
- Además, se verifica que en la expresión haya k enteros (con k >= 2), y k-1 operadores, y que si se trabaja con orden prefijo primero se ingresen los operadores, y que si se trabaja con postfijo primero se ingresen los enteros.
- Si se ingresa SALIR, mostrará un mensaje de salida, y saldrá del ciclo, terminando el programa
- Si se ingresa una acción incorrecta, se mostrará un mensaje de error, y volverá a otra iteración del ciclo
  

__Ejecución__
- Desde un IDE o un editor de código con extensiones que permitan correr programas escritos en Python
- Desde la terminal (ubicado en el directorio donde se encuentra el archivo):
  ```
  >python Pregunta2.py 
  ```

      
__Ejecución de las pruebas con cobertura__ (teniendo instalados unittest y coverage)
- Para las pruebas con cobertura

 ```
 > coverage run -m unittest test_pregunta2.py
 ```

- Para un reporte de la cobertura
```     
> coverage report -m
```

- Si se quiere un reporte de la cobertura hecho en HTML
```
> coverage html
```
    
