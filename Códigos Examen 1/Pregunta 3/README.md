Pregunta 3 - Franco Murillo - 1610782

Programa que simula programas, intérpretes y traductores basado en los diagramas T

El código para resolver el problema fue hecho en Python

Clases y Métodos

- Programa: representa los programas que se definirán en el sistema
    - Constructor (__init__):
        - Declara el nombre del programa y el lenguaje en el que está escrito

- Interprete: representa los intérpretes que se definirán en el sistema
    - Constructor (__init__):
        - Declara el nombre del lenguaje base en el que se hará el intérprete y el lenguaje que se interpretará

- Traductor: representa los traductores que se definirán en el sistema
    - Constructor (__init__):
        - Declara el nombre del lenguaje base en el que se hará el traductor, el lenguaje de origen, y el lenguaje destino al cual será traducido

- Sistema: integra el funcionamiento de las clases anteriores para el sistema
    - Constructor (__init__):
        - Declara un diccionario para los programas, los intérpretes y los traductores

    - definir_programa:
        - Recibe un nombre para el programa, y el lenguaje en el que será escrito
        - Si ya existe un programa con el nombre dado, imprime un mensaje de error y sale del método
        - Si no existe el programa, crea un objeto de tipo Programa con el nombre y el lenguaje dados, e imprime un mensaje de éxito de creación

    - definir_intérprete: 
        - Recibe un lenguaje inicial, y un lenguaje base sobre el cual se hará el intérprete
        - Si el lenguaje no está en el diccionario de intérpretes, se agrega, y como valor se le asigna otro diccionario
            - De esta forma, es posible definir varios intérpretes para un mismo lenguaje
        - Si el lenguaje base está en el diccionario del lenguaje inicial, imprime un mensaje de error y sale del método
        - Luego se crea un objeto de tipo Interprete con el lenguaje base y el lenguaje inicial, e imprime un mensaje de éxtito de creación

    - definir_traductor:
        - Recibe un lenguaje origen, un lenguaje base sobre el cual se escribirá el traductor, y un lenguaje destino al cual se hará la traducción del lenguaje origen
        - Si el lenguaje de origen no está en el diccionario de traductores, se agrega, y como valor se le asigna otro diccionario
            - De esta forma, es posible definir varios traductores para un mismo lenguaje
        - Si el lenguaje destino está en el diccionario del lenguaje de origen, y el lenguaje base (del lenguaje destino en el diccionario) es el ingresado por el usuario, imprime un mensaje de error y sale del método
        - Luego se crea un objeto de tipo Traductor con el lenguaje base, el lenguaje de origen y el lenguaje destino, e imprime un mensaje de éxito de creación

    - ejecutable:
        - Recibe programa, y retorna si es ejecutable o no (True o False)
        - Si el programa no se encuentra en el diccionario de programas, imprime un mensaje de error y sale del método
        - Si el programa está en el diccionario, se obtiene el lenguaje en el cual se escribió
        - Se llama al método recursivo ejecutableRec, y si éste retorna True, se imprime que el programa es ejecutable, o imprime que no en caso contrario
    
    - ejecutableRec:
        - Recibe un lenguaje y retorna si el programa escrito en el lenguaje dado es ejecutable 
        - Caso base: el lenguaje ingresado es LOCAL. En tal caso, retorna True
        - Si no, se hacen dos verificaciones
            - Si el lenguaje ingresado se encuentra en el diccionario de intérpretes, y si para algun lenguaje base (del lenguaje ingresado), el método ejecutableRec retorna True, el programa es ejecutable. Retorna True
            - Si el lenguaje ingresado se encuentra en el diccionario de traductores, y si para algun lenguaje base y destino (para el cual el lenguaje ingresado está traducido), el método ejecutableRec retorna True, el programa es ejecutable. Retorna True
        - Si ninguna condición se cumple, el programa no es ejecutable. Retorna False

    - main():
        - Declara un objeto de tipo Sistema 
        - Se crea un ciclo while (que siempre se cumplirá hasta que se desee salir)
            - Se pide al usuario que ingrese una acción (que puede comenzar con DEFINIR o EJECUTABLE, o directamente con SALIR para terminar el programa)
                - Si el usuario escribe DEFINIR, tiene para escoger 3 opciones:
                    - PROGRAMA, donde seguidamente se deberá ingresar el nombre del programa y el lenguaje sobre el que está escrito
                    - INTERPRETE, donde seguidamente se deberá ingresar el lenguaje base sobre el cual se hará el intérprete y luego el lenguaje que se interpretará
                    - TRADUCTOR, donde seguidamente se deberá ingresar el lenguaje base sobre el cual se hará el traductor, el lenguaje de origen que será traducido, y el lenguaje destino hacia donde se traducirá el lenguaje de origen
                    - Para cualquier otra opción ingresada, se imprimirá un mensaje de error, y se volverá a pedir una acción al usuario
                    - Si el usuario escribió DEFINIR, y el número total de argumentos es menor a 4 o mayor a 5, imprime un mensaje de error
                - Si el usuario escribe EJECUTABLE, debe ingresar el nombre del programa que quiere verificar si se puede ejecutar
                - Para cualquier otra acción ingresada, se imprimirá un mensaje de error, y se volverá a pedir una acción al usuario
                - 
NOTA: Las palabras clave (DEFINIR, PROGRAMA, INTERPRETE, TRADUCTOR, EJECUTABLE, SALIR) se deben escribir en mayúsculas; de lo contrario se imprimirá un mensaje de error.

Ejemplo de uso:
 ```
Introduce una accion: DEFINIR PROGRAMA hola LOCAL
Se definio el programa 'hola', ejecutable en 'LOCAL'
Introduce una accion: EJECUTABLE hola
Si, es posible ejecutar el programa 'hola'
Introduce una accion: DEFINIR PROGRAMA fizzbuzz Java
Se definio el programa 'fizzbuzz', ejecutable en 'Java'
Introduce una accion: EJECUTABLE fizzbuzz
No es posible ejecutar el programa 'fizzbuzz'
Introduce una accion: DEFINIR TRADUCTOR C Java LOCAL
Se definio un traductor de 'Java' hacia 'LOCAL', escrito en 'C'
Introduce una accion: EJECUTABLE fizzbuzz
No es posible ejecutar el programa 'fizzbuzz'
Introduce una accion: DEFINIR INTERPRETE LOCAL C
Se definio un interprete para 'C', escrito en 'LOCAL'
Introduce una accion: EJECUTABLE fizzbuzz
Si, es posible ejecutar el programa 'fizzbuzz'
Introduce una accion: SALIR
Saliendo del programa
 ```

 Ejecución del programa
 - Desde algún editor de código o IDE donde sea posible ejecutar código Python
- Desde la terminal (estando ubicado en el directorio donde se encuentra el archivo):
  
```
> python Pregunta3.py
```

Ejecución de las pruebas con cobertura (teniendo instalados unittest y coverage)
- Para las pruebas con cobertura

 ```
 > coverage run -m unittest test_pregunta3.py
 ```

- Para un reporte de la cobertura
```     
> coverage report -m
```

- Si se quiere un reporte de la cobertura hecho en HTML
```
> coverage html
```
