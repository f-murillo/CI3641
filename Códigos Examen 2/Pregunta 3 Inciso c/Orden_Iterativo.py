def ins_ord(e, ls):
    """
    Método que inserta un elemento en su posición correcta dentro de una lista ordenada.
    """
    if not ls or e <= ls[0]:
        yield [e] + ls
    else:
        for rest in ins_ord(e, ls[1:]):
            yield [ls[0]] + rest

def ord(ls):
    """
    Método que ordena una lista de elementos utilizando inserciones recursivas
    """
    if ls:
        for sort_t in ord(ls[1:]):
            for sort_l in ins_ord(ls[0], sort_t):
                yield sort_l
    else:
        yield []

def it_ord(ls):
    """
    Método que itera y devuelve los elementos de una lista en orden ascendente.
    """
    for sort_l in ord(ls):
        for item in sort_l:
            yield item
