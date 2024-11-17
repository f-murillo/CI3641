class TipoAtomico:
    """Clase que implementa los tipos atómicos"""
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = representacion
        self.alineacion = alineacion

class TipoCompuesto:
    """Clase que implementa los registros y los registro variantes"""
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos

class ManejadorTipos:
    """Clase que implementa el manejador de tipos de datos"""
    def __init__(self):
        self.tipos = {} # Diccionario para los tipos

    def agregar_tipo_atomico(self, nombre, representacion, alineacion):
        """Método que define un nuevo tipo atómico"""
        if nombre in self.tipos:
            print(f"Error: el tipo '{nombre}' ya existe.")
            return
        self.tipos[nombre] = TipoAtomico(nombre, representacion, alineacion)

    def agregar_tipo_compuesto(self, nombre, tipos_campos, es_union=False):
        """Método que define un nuevo registro o un nuevo registro variante"""
        if nombre in self.tipos:
            print(f"Error: el tipo '{nombre}' ya existe.")
            return
        for tipo in tipos_campos:
            if tipo not in self.tipos:
                print(f"Error: el tipo '{tipo}' no está definido.")
                return
        self.tipos[nombre] = TipoCompuesto(nombre, tipos_campos)

    def size_alineacion(self, tipo_nombre, es_union=False):
        """Método que calcula el tamaño y la alineación de un tipo"""

        tipo = self.tipos[tipo_nombre] # Se obtiene el tipo de dato del diccionario de tipos
        max_tamano = 0  # Tamaño máximo de los campos (usado para uniones)
        size_empaquetado = 0  # Tamaño del registro cuando los campos están empaquetados
        size_no_empaquetado = 0  # Tamaño del registro cuando los campos no están empaquetados
        max_alineacion = 0  # Alineación máxima requerida por los campos

        # Para cada campo del tipo compuesto
        for campo in tipo.campos:
            # Se obtiene los detalles del campo desde el diccionario de tipos
            campo_dato = self.tipos[campo]
            if isinstance(campo_dato, TipoAtomico):  # Si el campo es un tipo atómico
                representacion = campo_dato.representacion
                alineacion = campo_dato.alineacion
                # Se calcular el tamaño no empaquetado ajustado a la alineación
                no_empaquetado = ((representacion + alineacion - 1) // alineacion) * alineacion
            elif isinstance(campo_dato, TipoCompuesto):  # Si el campo es un tipo compuesto (struct o union)
                # Se hace la llamada recursiva para calcular tamaño y alineación del tipo compuesto
                representacion, no_empaquetado, _ = self.size_alineacion(campo, es_union)
                # Se determinar la alineación máxima de los campos del tipo compuesto
                alineacion = max(self.tipos[t].alineacion for t in campo_dato.campos)
            else:
                raise TypeError(f"Tipo no reconocido: {campo}")

            # Se actualizaa la alineación máxima requerida
            max_alineacion = max(max_alineacion, alineacion)
            
            if es_union:
                # Para uniones, el tamaño es el del campo más grande
                max_tamano = max(max_tamano, representacion)
                size_no_empaquetado = max(size_no_empaquetado, no_empaquetado)
            else:
                # Para estructuras, se suman los tamaños de representación y no empaquetados
                size_empaquetado += representacion
                size_no_empaquetado += no_empaquetado

        if es_union:
            # Para uniones, el tamaño empaquetado es el del campo más grande
            size_empaquetado = max_tamano
            size_optimo = size_no_empaquetado
        else:
            # Para estructuras, se añade el padding necesario para alinear el tamaño no empaquetado
            padding_optimo = (max_alineacion - (size_no_empaquetado % max_alineacion)) % max_alineacion
            size_optimo = size_no_empaquetado + padding_optimo

        return size_empaquetado, size_no_empaquetado, size_optimo

    def describir_tipo(self, nombre):
        """Método que proporciona la descripción de un tipo"""
        if nombre not in self.tipos:
            print(f"Error: el tipo '{nombre}' no está definido.")
            return
        tipo = self.tipos[nombre]
        if isinstance(tipo, TipoAtomico): # Si es atómico
            print(f"Tipo Atómico: {tipo.nombre}")
            print(f"Representación: {tipo.representacion} bytes")
            print(f"Alineación: {tipo.alineacion} bytes")
        elif isinstance(tipo, TipoCompuesto): # Si es compuesto
            es_union = self.es_union(nombre) # Se verifica si el tipo es union
            print(f"Tipo {'Union' if es_union else 'Struct'}: {tipo.nombre}")
            self.describir_registro(nombre, es_union)
        else:
            print(f"Tipo desconocido: {tipo}")

    def es_union(self, nombre):
        """Método que verifica si un tipo es union"""
        return nombre.startswith('union_')

    def describir_registro(self, nombre, es_union):
        """Método que proporciona la descripción de un registro"""
        size_empaquetado, size_no_empaquetado, size_optimo = self.size_alineacion(nombre, es_union)
        print(f"Tamaño empaquetado: {size_empaquetado} bytes")
        print(f"Tamaño no empaquetado: {size_no_empaquetado} bytes")
        print(f"Tamaño óptimo: {size_optimo} bytes")
        print(f"Bytes desperdiciados (empaquetado): {(size_empaquetado - size_optimo)*-1} bytes")
        print(f"Bytes desperdiciados (no empaquetado): {(size_no_empaquetado - size_optimo)*-1} bytes")

def main():
    """Método principal"""
    manejador = ManejadorTipos()
    while True:
        accion = input("Ingrese una acción: ")
        partes = accion.split() # Se separa en partes la acción ingresada 
        comando = partes[0]
        match comando:
            case "ATOMICO":
                if len(partes) != 4:
                    print("Error: faltan argumentos o hay argumentos de mas")
                    continue
                nombre = partes[1]
                representacion = int(partes[2])
                alineacion = int(partes[3])
                manejador.agregar_tipo_atomico(nombre, representacion, alineacion) 
            case "STRUCT":
                nombre = partes[1]
                tipos_campos = partes[2:]
                manejador.agregar_tipo_compuesto(nombre, tipos_campos)  
            case "UNION":
                nombre = partes[1]
                tipos_campos = partes[2:]
                manejador.agregar_tipo_compuesto(nombre, tipos_campos, es_union=True)
            case "DESCRIBIR":
                if len(partes) != 2:
                    print("Error: faltan argumentos o hay argumentos de mas")
                    continue
                nombre = partes[1]
                manejador.describir_tipo(nombre)
            case "SALIR":
                print("Saliendo")
                break
            case _:
                print(f"Accion {comando} desconocida")

if __name__ == "__main__":
    main()
