def f_3_3(n):
    """Método que calcula f_3_3 recursivamente (versión normal)"""
    if 0 <= n < 9:
        return n
    return f_3_3(n-3) + f_3_3(n-6) + f_3_3(n-9)

def f_3_3_cola(n):
    """Método que calcula f_3_3 usando recursividad de cola"""
    def f_3_3_aux(a0, a1, a2, a3, a4, a5, a6, a7, a8, i):
        if i == n:
            return a0
        return f_3_3_aux(a1, a2, a3, a4, a5, a6, a7, a8, a6+a3+a0, i+1) 
    return f_3_3_aux(0, 1, 2, 3, 4, 5, 6, 7, 8, 0)

def f_3_3_iterativo(n):
    """Método que calcula f_3_3 usando iteraciones, basado en la recursividad de cola"""
    # Inicializar los acumuladores para los últimos 9 valores y el acumulador actual
    a0, a1, a2, a3, a4, a5, a6, a7, a8 = 0, 1, 2, 3, 4, 5, 6, 7, 8
    actual = 0
    # Iterar desde 9 hasta n + 1
    for _ in range(9, n + 1):
        actual = a6 + a3 + a0 # Esta parte corresponde al argumento (a6 + a3 + a0) de la llamada recursiva a f_3_3_aux en la versión recursiva de cola
        # Actualizar los acumuladores
        a0, a1, a2, a3, a4, a5, a6, a7, a8 = a1, a2, a3, a4, a5, a6, a7, a8, actual
    return actual
