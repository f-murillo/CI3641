Reto - Franco Murillo 1610782

Implementación de la función maldad(n), de modo que funcione rápidamente para los mayores valores de n posibles

El código fue hecho en Python

Observación: el código fue implementado a partir del código del programa escrito en Haskell para el reto del primer examen:

```
import Math.Combinatorics.Exact.Binomial(choose)
import Data.Bits(shiftR)

trib :: Integer -> Integer
trib n = if n<3 then n else tribs!!fromIntegral n where tribs=0:1:2:zipWith3(\a b c->a+b+c)tribs(tail tribs)(drop 2 tribs)

narayana :: Integer -> Integer -> Integer
narayana n k=(choose(fromIntegral n)(fromIntegral k)*choose(fromIntegral n)(fromIntegral(k-1)))`div`n

maldad :: Integer -> Integer
maldad n = let pisoLog2 x=fromIntegral(length(takeWhile(>0)(iterate(`shiftR`1)x))-1) in trib(pisoLog2(narayana n(pisoLog2 n))+1)
```

El cambio más significativo entre el código Haskell y el de Python, fue la implementación de la función trib

Funciones

__trib__: calcula el n-ésimo número de tribonacci

- Para poder mejorar la eficiencia del programa en general, era necesario hacer esta función lo más eficiente posible, para lo cual se adaptó la función recursiva. Primero se obtuvo la forma recursiva de cola:

```
def trib_cola(n):
    def trib_aux(t1, t2, t3, i):
        if i == n:
            return t3 + t2 + t1
        return trib_aux(t2, t3, t1 + t2 + t3, i + 1)
    return trib_aux(0, 1, 2, 3)
```

__trib_cola(n)__
- Declara una función recursiva auxiliar que lleva por parámetros t1, t2, t3 (acumuladores) e i (iterador)
  - Si i es igual a n, se retorna la suma de los últimos 3 valores acumulados (ya que al momento de que i sea igual a n, aún no se ha hecho esa última suma)
  - Si no, retorna la función auxiliar con t2, t3, t1+t2+t3 e i+1 como parámetros
- Finalmente retorna la función auxiliar con los 3 primeros valores de tribonacci y el iterador i en 3 como argumentos

- Ya con esta versión recursiva de cola, aumentaba considerablemente la eficiencia de la función, pero fallaba para números muy grandes por tener que hacer demasiadas llamadas recursivas. Por esto se obtuvo la versión iterativa a partir de esta versión, la cual mejora aún más la eficiencia

__narayana__: calcula el Narayana de n en k
- No cambia su funcionamiento con respecto a la versión en Haskell
- Hace uso de la función comb() del módulo math

__maldad__: calcula el número de la maldad
- No cambia su funcionamiento con respecto a la versión en Haskell
- Declara una función interna que calcula el piso del logaritmo base 2, la cual hace uso de la función bit_length() de la clase int
- Hace uso de las funciones trib y narayana para el cálculo del número de la maldad
