Pregunta 3 - Franco Murillo 1610782

# Programa que simula un manejador de tablas de métodos virtuales

El código del programa fue hecho en Python

## Clases y Métodos

### VirtualMethodTableHandler 

    - Implementa el manejador
    
    - ____init____: Constructor. Crea un diccionario para las clases
    
    - __define_clas__: Define una clase, dadas una definición, que incluye el nombre de la clase, y los métodos que contendrá

        - Obtiene las partes de la definición dada

        - Si la definición lleva ":", quiere decir que la clase heredará de otra; obtiene los nombres de la clase y de la super clase, y los métodos para la clase

        - Si no, establece como None a la super clase, y obtiene el nombre y los métodos de la clase

        - Verifica si ya existe la clase

        - En caso de que la definición lleve ":", verifica si existe la super clase

        - Verifica que no haya métodos duplicados en la definición

        - Verifica que no se forme un ciclo de jerarquía de herencia entre la clase y la super clase

        - Crea un diccionario para la tabla de métodos para la clase

        - Si la clase a definir hereda de otra, se actualiza la tabla de métodos de la super clase (en caso de que se sobreescriban métodos)

        - Se agregan los métodos a la tabla de métodos de la clase

        - Se guarda la clase en el diccionario de clases

        - Se imprime un mensaje de éxito

    - __describe__: Describe una clase

        - Verifica si la clase dada existe

        - Obtiene la tabla de métodos de la clase

        - Imprime cada método e implementación de la tabla

    - ___cicle_exists__: Verifica si existen ciclos de jerarquía de herencia de clases

        - Mientras exista una super clase (en algún momento, debería llegar a None):

            - Si la super clase tiene el mismo nombre de la clase, hay un ciclo de jerarquía; retorna True

            - Si no, pasa a la siguiente super clase
        
        - Si se llegó a este punto, no hay ciclo; retorna False

### main
    - Método principal

    - Se crea una instancia del manejador

    - Se usa un while(True)

        - Se pide al usuario que ingrese una acción (CLASE, DESCRIBIR o SALIR)

        - Se divide las partes de la acción ingresada, y se obtiene la primera parte, que será el comando

        - Se usa un match case sobre el comando

            - Si el comando es CLASE, verifica que el número de argumentos sea mayor a 2, y llama a __define_class__. Si el número de argumentos es menor a 2, imprime un mensaje de error, y da otra vuelta al ciclo

            - Si el comando es DESCRIBIR, verifica que el número de argumentos sea exactamente 2, y llama a __describe_class__. Si el número de argumentos es distinto de 2, imprime un mensaje de error, y da otra vuelta al ciclo

            - Si el comando es SALIR, imprime un mensaje de salida, sale del ciclo while, y termina el programa

            - Para cualquier otro valor del comando, imprimirá un mensaje de error, y dará otra vuelta al ciclo

## Ejemplos de uso

```
Ingresa una acción (CLASS, DESCRIBIR, SALIR): CLASS A wenas hellou
Clase CLASS A wenas hellou creada exitosamente
Ingresa una acción (CLASS, DESCRIBIR, SALIR): CLASS B : A a lo
Clase CLASS B : A a lo creada exitosamente
Ingresa una acción (CLASS, DESCRIBIR, SALIR): DESCRIBIR A
wenas -> A :: wenas
hellou -> A :: hellou
Ingresa una acción (CLASS, DESCRIBIR, SALIR): DESCRIBIR B
wenas -> A :: wenas
hellou -> A :: hellou
a -> B :: a
lo -> B :: lo
Ingresa una acción (CLASS, DESCRIBIR, SALIR): CLASS C : B ch a o
Clase CLASS C : B ch a o creada exitosamente
Ingresa una acción (CLASS, DESCRIBIR, SALIR): DESCRIBIR C
wenas -> A :: wenas
hellou -> A :: hellou
a -> C :: a
lo -> B :: lo
ch -> C :: ch
o -> C :: o
Ingresa una acción (CLASS, DESCRIBIR, SALIR): SALIR
Saliendo del programa
```

## Ejecución del programa

- Desde algún editor de código o IDE donde sea posible ejecutar código Python
- Desde la terminal (estando ubicado en el directorio donde se encuentra el archivo):
  
```
> python pregunta3.py
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