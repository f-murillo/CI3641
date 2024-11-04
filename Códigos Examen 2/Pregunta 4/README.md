Pregunta 4 - Franco Murillo 1610782

Implementación de función f_alpha_beta propuesta en el enunciado de la pregunta

Dado que en mi caso X = 7, Y = 8 y Z = 2, se tiene que:
alpha = ((7+8) mod 5) + 3 = 3 ; beta = ((8+2) mod 5) + 3 = 3

Por lo que f_alpha_beta = f_3_3, y es de la forma:
```
f_3_3 = {
    n                                        , si 0 <= n < 9
    f_3_3(n-3) + f_3_3(n-6) + f_3_3(n-9)     , si n >= 9
}
```


__Pregunta4.py__: Contiene los métodos para calcular f_3_3 de manera recursiva normal, recursiva de cola e iterativa.

Métodos de Pregunta4

__f_3_3__: calcula f_3_3 de un n. Es una traducción literal de la definición recursiva de f_3_3.
- Si n está en el intervalo [0,9), retorna n.
- Si no, quiere decir que n es mayor o igual que 9, retorna f_3_3(n-3) + f_3_3(n-6) + f_3_3(n-9).

__f_3_3_cola__: calcula f_3_3 de un n haciendo uso de recursión de cola.
- Usa una función auxiliar f_3_3_aux, que recibe 10 argumentos, (a0, a1, a2, a3, a4, a5, a6, a7, a8), y un i
  - Si i es igual a n, retorna a0.
  - Si no, retorna f_3_3_aux con los 8 primeros argumentos corridos una posición adelante, el 9no argumento como a6 + a3 + a0, y el último argumento como i+1.
- Finalmente retorna la función f_3_3_aux, donde los primeros 9 argumentos son los primeros 9 números por definición de f_3_3 (0, 1, 2, 3, 4, 5, 6, 7, 8), y como 10mo argumento a 0.

 __f_3_3_iterativo__: calcula f_3_3 de un n de manera iterativa, basado en la versión de recursión de cola.
- Inicializa los primeros 9 números de f_3_3 (a0, a1, a2, a3, a4, a5, a6, a7, a8), y una variable actual en cero.
- Itera desde 9 hasta n+1:
  - Reasigna todas las variables:
  - A la variable actual le asigna el valor de la suma a6 + a3 + a0.
  - Al resto de variables los corre una posición hacia adelante, a excepción de la última (a8), a la que le asigna el valor de actual.
- Finalmente retorna el valor de actual.

- La primera correlación entre la versión recursiva de cola e iterativa está en inicialización de los 9 primeros números de f_3_3 y actual, que corresponde a la primera llamada recursiva de f_3_3_aux, con los 9 primeros números de f_3_3 e i = 0. 
- La segunda correlación está en la asignación de a6 + a3 + a0 a actual, la cual corresponde al argumento (a6 + a3 + a0) de la llamada recursiva f_3_3_aux en la recursión de cola.


__Tiempos.py__: se encarga de calcular los tiempos de ejecución de cada método de f_3_3

- Se importaron las clases time y csv, así como los métodos de Pregunta4.py

- Se calculó el valor de f_3_3(n) desde 0 hasta 85 (se quiso llegar hasta 100, o incluso hasta 90, pero la versión recursiva normal se quedaba pegado)

- Se inicializa una lista con los números de 0 a 85, y las listas que tendrán los tiempos de cada método

- Para cada k en la lista de números:
    - Se guarda el tiempo del sistema antes y después de la ejecución de cada método aplicado sobre k, y se guarda su diferencia en la lista correspondiente

- Luego se crea un archivo CSV con los datos obtenidos, y se imprime un mensaje de éxito

__Análisis de los tiempos de ejecución__

- Se pudo observar que el método recursivo normal fue el más lento, mientras que las versiones de recursión de cola e iterativo prácticamente no tuvieron diferencia

- Al momento de ejecutarse las pruebas, es posible que para algún valor, alguno de los 3 métodos tenga un pico, es decir, que tarde más de lo esperado; esto puede tratarse a procesos en segundo plano por parte del procesador, memoria ocupada, detalles con el recolector de basura de Python, etc., pero a gran escala, los resutados son coherentes con lo esperado.

- Si se calcula individualmente el f_3_3 de números grandes (por ejemplo, 100), el método iterativo es el más rápido y eficiente, lo cual es esperado, pues solo hace reasignaciones

__Ejecución__
- Desde un IDE o un editor de código con extensiones que permitan correr programas escritos en Python.
- Desde la terminal (ubicado en el directorio donde se encuentra el archivo):
  ```
  > python Pregunta4.py 
  > python Tiempos.py
  ```
