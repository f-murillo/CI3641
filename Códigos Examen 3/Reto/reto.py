import math

def trib(n):
    """Método que calcula el n-ésimo número de tribonacci"""    
    t1 = 0
    t2 = 1
    t3 = 2
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

# Prueba
n = int(input("Ingresa un número: "))
resultado = maldad(n)
print(f"maldad({n}) = {resultado}")
