Reto - Franco Murillo 1610782

Implementación de la función maldad(n), de modo que funcione rápidamente para los mayores valores de n posibles

El código fue hecho en Python

Se aumentó el límite en la cantidad de dígitos que se puede manejar en las conversiones de cadenas de enteros (para poder manejar entradas grandes)

Observación: el código que calcula los números de la maldad fue implementado a partir del código escrito en Haskell para el reto del primer examen:

```haskell
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

- Para poder mejorar la eficiencia del programa en general, era necesario hacer esta función lo más eficiente posible. Primero se obtuvo la forma recursiva de cola:

```python
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

- Ya con esta versión recursiva de cola, aumentaba considerablemente la eficiencia de la función, pero fallaba para números muy grandes (por tener que hacer demasiadas llamadas recursivas). Por esto se obtuvo la versión iterativa a partir de esta versión, la cual mejora aún más la eficiencia

__narayana__: calcula el Narayana de n en k
- No cambia su funcionamiento con respecto a la versión en Haskell
- Hace uso de la función comb() del módulo math

__maldad__: calcula el número de la maldad
- No cambia su funcionamiento con respecto a la versión en Haskell
- Declara una función interna que calcula el piso del logaritmo base 2, donde se hace uso de la función bit_length() de la clase int, la cual devuelve el número de bits necesarios para representar el entero en binario (sin incluir el bit del signo), y a dicho número se le resta 1
- Hace uso de las funciones trib y narayana para el cálculo del número de la maldad

__OBSERVACION__
- Se asume que n >= 2, ya que:
  - Si n = 1, pisoLog2(1) = 0, y en la función narayana(n,k) se intentaría calcular combinatorio(1, -1) (BOOM, explotó el programa)
  - Si n = 0, pisoLog2(0) = -1 (por la manera en la que funciona pisoLog2), por lo que en narayana(n,k) se intentaría calcular combinatorio(0, -2) (BOOM, explotó el programa)
  - Si n es negativo, pisoLog2(n) retornaría el mismo resultado que para su versión positiva (por la manera en la que funciona pisoLog2), pero en narayana(n,k) se intentaría calcular combinatorio(n,k) con n negativo (BOOM, explotó el programa)  

Ejecución del programa
- Desde algún editor de código o IDE donde sea posible ejecutar código Python
- Desde la terminal (estando ubicado en el directorio donde se encuentra el archivo):
  
```
> python reto.py
```
- Desde un runner online: se recomienda ejecutarlo en ideone.com, indicando que el lenguaje a usar es Python 3. También se debe remover la importación y uso del módulo sys, el método main, e imprimir directamente maldad aplicado al número deseado. Esto es:

```python
import math

def trib(n):
    """Método que calcula el n-ésimo número de tribonacci"""    
    t1, t2, t3 = 0, 1, 2
    for _ in range(3, n + 1):
        t = t1 + t2 + t3
        t1, t2, t3 = t2, t3, t
    return t3

def narayana(n, k):
    """Método que calcula el Narayana de n en k"""
    return (math.comb(n, k) * math.comb(n, k - 1)) // n

def maldad(n):
    """Método que calcula el número de la maldad"""
    def pisoLog2(x):
        """Método que calcula el piso del logaritmo base 2"""
        return x.bit_length() - 1
    narayana_value = narayana(n, pisoLog2(n))
    trib_value = trib(pisoLog2(narayana_value) + 1)
    return trib_value

print(maldad(<numero>))
```
- OBSERVACION (luego de haberse evaluado ya el código): desgraciadamente, al eliminar el uso del módulo sys, se pierde por completo la capacidad de calcular números de maldad gigantes xd pero fue divertido e interesante poder implementar la función de tribonacci de forma iterativa. Además, se probó aumentando el número de dígitos máximo a 1.000.000.000, y efectivamente calculó números de maldad del orden de 1x10^200 (lo cual me pareció bastante genial).
