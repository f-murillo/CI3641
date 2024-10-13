Reto - Franco Murillo - 1610782

Programa que calcula los números de la maldad. El problema se resolvió usando Haskell

Se asume que el número ingresado para su cálculo es mayor a cero

NOTA: el código está lo más compacto posible para poder calificar para el reto (que el código resolviera el problema y contuviera la menor cantidad de caracteres posibles)

Métodos 
- trib n: Calcula el n-ésimo número de Tribonacci
    - Caso base: si n es menor que 3, retorna n
    - En otro caso, se crea una lista infinita (tribs) y se calcula su n-ésimo número (con el !!). La función fromIntegral n transforma el n de Integer a Int, ya que la función !! trabaja con Int
        - tribs se inicializa con 0,1,2 (los primeros 3 números de Tribonacci). Luego se genera el resto de la lista con zipWith3, el cual recibe una función lambda (que toma 3 elementos y retorna su suma) y tres listas:
            - tribs: la lista original de números de Tribonacci 
            - tail tribs: la lista tribs menos el primer elemento
            - drop 2 tribs: la lista tribs menos los dos primero elementos
            - zipWith3 aplica la función lambda sobre las 3 listas, generando una nueva lista

- narayana n, k: Calcula Narayana de n en k
    - Aplica la fórmula: (1/n) * combinatorio(n,k) * combinatorio(n,k-1)
    - Para el calculo del combinatorio, se importó la función __choose__ del módulo __Math.Combinatorics.Exact.Binomial__
- Para importar el módulo y sus funciones, es necesario tenerlo instalado:

        > cabal install --lib exact-combinatorics

    - La función (choose) espera como argumento un Int, por eso se transforman n, k y k-1 de Integer a Int con fromIntegral

- maldad n: Calcula el n-ésimo número de la maldad
    - Se declara una función interna que calcula el piso del logaritmo base 2 de x (pisoLog2)
        - Para ello, se crea una lista (con el interate), en la que se almacena el resultado de hacer bit shifting a la derecha de x (lo cual divide a x entre 2), mientras el resultado sea mayor a 0 (con el takeWhile (>0)); se obtiene la longitud de la lista, y se le resta 1 para obtener el resultado final (ya que inicialmente se agrega a la lista el propio x, el cual no cuenta para el cálculo del logaritmo base 2). Con esto, se obtiene efectivamente el piso del logaritmo base 2 de x
        - Para realizar el bit shifting a la derecha, se importó la función __shiftR__ del módulo __Data.Bits__
        - La función (choose) espera como argumento un Int, por eso se transforman n y k de Integer a Int 
    - Se calcula el piso del logaritmo base 2 de n (pisoLog2 n)
    - Se calcula el Narayana de n en el resultado anterior (narayana n (pisoLog2))
    - Se calcula el piso del logaritmo base 2 del resultado anterior (pisoLog2 (narayana n (pisoLog2))) 
    - Finalmente, se devuelve la función trib aplicada al resultado anterior + 1 (trib(pisoLog2(narayana n(pisoLog2 n))+1))

Ejecución

- Dado que el programa está escrito en Haskell, se puede ejecutar desde el intérprete de Haskell (ghci):

- Estando ubicado en el directorio donde está el archivo: 
        
        > ghci reto.hs

- Desde el interprete, se llama a la función maldad:

        ghci> maldad <número>

- Ya que se está en el intérprete, también se puede ejecutar las funciones trib y narayana:

        ghci> trib <número>

        ghci> narayana <número1> <número2>

NOTA: se decidió trabajar con Integer en lugar de Int, ya que el entero de precisión de Haskell (Integer) permite calcular números de maldad grandes sin overflow, a diferencia del entero del procesador (Int), y la diferencia de tiempo de ejecución entre usar Int o Integer no fue significativo
