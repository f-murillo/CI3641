class TipoAtomico:
    """Clase que implementa los tipos atómicos"""
    def __init__(self, nombre, representacion, alineacion):
        self.nombre = nombre
        self.representacion = representacion
        self.alineacion = alineacion

class TipoStruct:
    """Clase que implementa los registros"""
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos

class TipoUnion:
    """Clase que implementa los registro variantes"""
    def __init__(self, nombre, campos):
        self.nombre = nombre
        self.campos = campos

class ManejadorTipos:
    """Clase que implementa el manejador de tipos de datos"""
    def __init__(self):
        self.tipos = {}

    def agregar_tipo_atomico(self, nombre, representacion, alineacion):
        """Método que define un nuevo tipo atómico"""
        if nombre in self.tipos:
            print(f"Error: el tipo '{nombre}' ya existe.")
            return
        self.tipos[nombre] = TipoAtomico(nombre, representacion, alineacion)

    def agregar_tipo_struct(self, nombre, tipos_campos):
        """Método que define un nuevo registro"""
        if nombre in self.tipos:
            print(f"Error: el tipo '{nombre}' ya existe.")
            return
        for tipo in tipos_campos:
            if tipo not in self.tipos:
                print(f"Error: el tipo '{tipo}' no está definido.")
                return
        self.tipos[nombre] = TipoStruct(nombre, tipos_campos)

    def agregar_tipo_union(self, nombre, tipos_campos):
        """Método que define un nuevo registro variante"""
        if nombre in self.tipos:
            print(f"Error: el tipo '{nombre}' ya existe.")
            return
        for tipo in tipos_campos:
            if tipo not in self.tipos:
                print(f"Error: el tipo '{tipo}' no está definido.")
                return
        self.tipos[nombre] = TipoUnion(nombre, tipos_campos)

    def describir_tipo(self, nombre):
        """Método que proporciona información de un tipo"""
        if nombre not in self.tipos:
            print(f"Error: el tipo '{nombre}' no está definido.")
            return
        tipo = self.tipos[nombre]
        if isinstance(tipo, TipoAtomico): # Si el tipo es atómico
            print(f"Tipo Atómico: {tipo.nombre}")
            print(f"Representación: {tipo.representacion} bytes")
            print(f"Alineación: {tipo.alineacion} bytes")
        elif isinstance(tipo, TipoStruct): # Si el tipo es struct
            print(f"Tipo Struct: {tipo.nombre}")
            self.describir_registro(tipo.campos)
        elif isinstance(tipo, TipoUnion): # Si el tipo es union
            print(f"Tipo Union: {tipo.nombre}")
            self.describir_registro(tipo.campos)
        else:
            print(f"Error: Tipo desconocido: {tipo}")

    def describir_registro(self, tipos_campos):
        """Método que proporciona la información específica de un registro"""
        # Sizes empaquetados, no empaquedados, óptimo y alineación máxima
        size_empaquetado = 0
        size_no_empaquetado = 0
        size_optimo = 0
        max_alineacion = 0
        # Para cada tipo de los campos del registro
        for tipo in tipos_campos:
            tipo_dato = self.tipos[tipo]
            max_alineacion = max(max_alineacion, tipo_dato.alineacion) # Se actualiza la alineación máxima
            size_empaquetado += tipo_dato.representacion # Se incrementa el size empaquetado con la representación del tipo
            # Se calcula el size no empaquetado, asegurando que los datos esten alineados
            size_no_empaquetado += ((tipo_dato.representacion + tipo_dato.alineacion - 1) // tipo_dato.alineacion) * tipo_dato.alineacion

        # Se inicia el size optimo con el no empaquetado
        size_optimo = size_no_empaquetado
        # Se calcula el padding optimo para alinear el size del registro al bloque de alineacion maximo
        padding_optimo = (max_alineacion - (size_optimo % max_alineacion)) % max_alineacion
        # Se suma el padding obtenido al size optimo
        size_optimo += padding_optimo

        # Se imprimen los resultados
        print(f"Tamaño empaquetado: {size_empaquetado} bytes")
        print(f"Tamaño no empaquetado: {size_no_empaquetado} bytes")
        print(f"Tamaño óptimo: {size_optimo} bytes")
        print(f"Bytes desperdiciados (empaquetado): {(size_empaquetado - size_optimo)*-1} bytes")
        print(f"Bytes desperdiciados (no empaquetado): {(size_no_empaquetado - size_optimo)*-1} bytes")

def main():
    """Método Principal"""
    manejador = ManejadorTipos()
    while True:
        accion = input("Ingrese una acción: ")
        partes = accion.split() # Separar en partes la accion ingresada
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
                manejador.agregar_tipo_struct(nombre, tipos_campos)  
            case "UNION":
                nombre = partes[1]
                tipos_campos = partes[2:]
                manejador.agregar_tipo_union(nombre, tipos_campos)
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