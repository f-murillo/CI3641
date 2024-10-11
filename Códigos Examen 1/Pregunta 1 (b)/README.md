Pregunta 1 - Inciso b - Franco Murillo - 1610782

Los siguientes códigos fueron hechos en F#

- moduloPotencia.fs
    - Pide al usuario que ingrese 3 enteros a, b y c, e imprime el resultado de la operación (a^b) mod c
    - El programa asume que los valores ingresados por el usuario son correctos (tanto a como b y c son enteros no negativos)
    - Se llama al método modPot, el cual es un método recursivo
        - Si el valor de c es menor a 2, se imprime un mensaje de error y se retorna -1
        - Si b == 0, se retorna 1
        - En otro caso, se retorna ((a mod c) * (modPot a (b-1) c)) mod c

- matrizMagica.fs
    - Pide al usuario que ingrese el orden de la matriz, y luego pide que ingrese todos los valores que tendrá
    - El programa asume que los valores ingresados por el usuario son correctos (el orden de la matriz es un entero positivo, y los elementos de la matriz son enteros)
    - Se llama al método esMagico
        - Define métodos que calculan la suma de elementos de la matriz por fila, columna y diagonal
        - Se calcula las sumas
        - Se comparan las sumas y se retorna si son iguales o no

- Ejecución usando el intérprete de F# (teniendo instalado .NET Core SDK y ubicado en la carpeta donde se encuentra el archivo)
  > dotnet fsi --exec nombreDeArchivo.fs

        

