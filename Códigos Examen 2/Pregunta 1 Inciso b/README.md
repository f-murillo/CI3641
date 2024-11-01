Pregunta 1. Inciso b - Franco Murillo 1610782

Los siguientes códigos fueron hechos en MATLAB

- Count
  
    Sea la función:
    ```
    f(n) = { 
                n / 2, si n es par
                3n + 1, si n es impar
            }
    ```
    Y sea la función count(n), que cuenta el número de aplicaciones consecutivas de f sobre n hasta que el resultado sea 1

    - Dado un entero positivo, el programa calcula su count

    - Si se ingresa un entero menor o igual a 0, la función count aplicaría la función f sobre n de manera infinita sin obtener nunca 1

    - Métodos:
        - Count
            - Es el método "principal" (por decirlo de alguna manera)
            - Pide al usuario ingresar un número, y verifica si el número es menor o igual a cero, o si n mod 1 != 0 (si no es un entero). Si se cumple la condición, imprime un mensaje indicando que se debe ingresar un entero positivo, y sale del programa
            - Si no se cumple la condición calcula el count del número con la función c, e imprime el resultado
        - f:
            - Recibe un entero, y retorna n/2 si n es par, o 3*n + 1 si n es impar
        - c:
            - Recibe un entero n, y retorna el número de aplicaciones de f sobre n hasta llegar a 1
            - Inicializa las aplicaciones (a) en 0
            - Itera mientras n sea distinto de 1:
                - Aplica f a n
                - Incrementa en uno a la variable "a"

    - Complejidad temporal: Dada la naturaleza del problema, que trata sobre la Conjetura de Collatz, la complejidad temporal puede ser aproximada a O(T(n)), donde T(n) es el número de iteraciones necesarias para que n llegue a 1

- Mergesort
    - Ordena un arreglo de números usando el algoritmo de Mergesort, basado en Divide And Conquer

    - Métodos:
        - Mergesort
            - Es el método "principal" (por decirlo de alguna manera). Inicializa un arreglo de prueba, y llama a la función merge_sort que lo ordenará
        - merge_sort
            - Recibe el arreglo a ordenar
            - Caso base: si el arreglo es de tamaño 1, ya está ordenado, así que lo establece como arreglo ordenado y sale de la llamada
            - Si no se está en el caso base, divide el arreglo en 2 subarreglos, y procede a hacer llamadas recursivas a merge_sort sobre ambos subarreglos
            - Finalmente, llama a la función merge para mezclar los dos subarreglos ordenados
        - merge
            - Recibe dos subarreglos left y right para mezclarlos
            - Declara un arreglo de ceros llamado result, del tamaño de la suma de los tamaños de los subarreglos
            - Establece los indices para left, right y result (i,j, y k respectivamente)
            - Itera mientras los indices i y j sean menores al tamaño de left y rigth respectivamente:
                - Si left(i) es menor o igual a right(j), asigna a result(k) el elemento left(i), e incrementa el indice i
                - Y viceversa en caso contrario
                - Al final, incrementa el indice k, y pasa a la siguiente iteración
            - Luego, agrega a result los elementos  de left y right que no hayan sido agregados

    - Complejidad temporal: O(n*logn)

- Ejecución de los archivos

    Desde la terminal de MATLAB: 

```
    >> Count
    >> Mergesort
```
