class Programa:
    """Clase que implementa los programas que se definirán en el sistema"""
    def __init__(self, nombre, lenguaje):
        self.nombre = nombre
        self.lenguaje = lenguaje

class Interprete:
    """Clase que implementa los intérpretes que se definirán en el sistema"""
    def __init__(self, lenguaje_base, lenguaje):
        self.lenguaje_base = lenguaje_base
        self.lenguaje = lenguaje

class Traductor:
    """Clase que implementa los traductores que se definirán en el sistema"""
    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino
        
class Sistema:
    """Clase que implementa el sistema en el que se definen los programas, intérpretes y traductores"""
    def __init__(self):
        # Diccionario para los programas, interpretes y traductores
        self.programas = {}
        self.interpretes = {}
        self.traductores = {}

    def definir_programa(self, nombre, lenguaje):
        """Método que define un programa con un nombre 'a', escrito en un lenguaje 'b'"""
        # Si el programa ya existe
        if nombre in self.programas:
            print(f"Error: ya existe un programa con el nombre '{nombre}'")
            return
        # Crear programa
        self.programas[nombre] = Programa(nombre, lenguaje)
        print(f"Se definio el programa '{nombre}', ejecutable en '{lenguaje}'")

    def definir_interprete(self, lenguaje_base, lenguaje):
        """Método que define un intérprete de un lenguaje, escrito en un lenguaje base"""
        # Si el lenguaje de origen no esta en el diccionario de interpretes
        if lenguaje not in self.interpretes:
            # Diccionario para poder tener varios interpretes para un mismo lenguaje de origen
            self.interpretes[lenguaje] = {} 
        # Si el lenguaje base ya esta definido para el lenguaje de origen
        if lenguaje_base in self.interpretes[lenguaje]:
            print(f"Error: ya existe un interprete para '{lenguaje}', escrito en '{lenguaje_base}'")
            return
        # Crear interprete
        self.interpretes[lenguaje][lenguaje_base] = Interprete(lenguaje_base, lenguaje)
        print(f"Se definio un interprete para '{lenguaje}', escrito en '{lenguaje_base}'")

    def definir_traductor(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        """Método que define un traductor de un lenguaje de origen a un lenguaje destino, escrito en un lenguaje base"""
        # Si el lenguaje de origen no esta en el diccionario de traductores
        if lenguaje_origen not in self.traductores:
            # Diccionario para poder tener varios traductores para un mismo lenguaje de origen
            self.traductores[lenguaje_origen] = {} 
        # Si el lenguaje base y destino ya estan definidos para el lenguaje de origen
        if lenguaje_destino in self.traductores[lenguaje_origen] and \
           self.traductores[lenguaje_origen][lenguaje_destino].lenguaje_base == lenguaje_base:
            print(f"Error: ya existe un traductor de '{lenguaje_origen}' hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")
            return
        # Crear traductor
        self.traductores[lenguaje_origen][lenguaje_destino] = Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)
        print(f"Se definio un traductor de '{lenguaje_origen}' hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")

    def ejecutable(self, nombre):
        """Método que verifica si un programa es ejecutable"""
        # Si el programa no existe
        if nombre not in self.programas:
            print(f"Error: no existe un programa con el nombre '{nombre}'")
            return
        # Obtener el lenguaje en el que esta escrito el programa
        lenguaje = self.programas[nombre].lenguaje
        # Llamar a ejecutableRec sobre el lenguaje
        if self.ejecutableRec(lenguaje):
            print(f"Si, es posible ejecutar el programa '{nombre}'")
        else:
            print(f"No es posible ejecutar el programa '{nombre}'")

    def ejecutableRec(self, lenguaje):
        """Método recursivo que determina si un programa es ejecutable, dado el lenguaje en el que fue escrito"""
        if lenguaje == "LOCAL":  # Caso base
            return True
        # Si el lenguaje está en el diccionario de intérpretes, y si para alguna base de algún intérprete del lenguaje el método recursivo retorna True
        if lenguaje in self.interpretes and any(self.ejecutableRec(base) for base in self.interpretes[lenguaje]):
            return True
        # Si el lenguaje está en el diccionario de traductores, y si para alguna base y destino de algún traductor del lenguaje el método recursivo retorna True
        if lenguaje in self.traductores and any(self.ejecutableRec(traductor.lenguaje_base) and \
                self.ejecutableRec(destino) for destino, traductor in self.traductores[lenguaje].items()):
            return True
        # Si no se cumple ninguna condición, el programa no es ejecutable
        return False 

def main():
    """Método Principal"""
    # Crear el sistema
    sistema = Sistema()
    while True:
        accion = input("Ingresa una accion: ")
        if accion == "SALIR":
            print("Saliendo del programa")
            break
        partes = accion.split()
        # Se verifica la accion ingresada
        if partes[0] == "DEFINIR":
            tipo = partes[1]
            # Switch para verificar el tipo de la accion 
            match tipo:
                case "PROGRAMA":
                    # Si el número de argumentos es distinto de 4
                    if len(partes) != 4:
                        print("Error: numero de argumentos incorrecto")
                        continue
                    # Se declara el nombre del programa y el lenguaje, y se llama al método que define el programa
                    nombre, lenguaje = partes[2], partes[3]
                    sistema.definir_programa(nombre, lenguaje)
                case "INTERPRETE":
                    # Si el número de argumentos es distinto de 4
                    if len(partes) != 4:
                        print("Error: numero de argumentos incorrecto")
                        continue
                    # Se declara el lenguaje base y el lenguaje, y se llama al método que define el interprete
                    lenguaje_base, lenguaje = partes[2], partes[3]
                    sistema.definir_interprete(lenguaje_base, lenguaje)
                case "TRADUCTOR":
                    # Misma idea que antes, pero si se define aun traductor, el numero de argumentos debe ser 5
                    if len(partes) != 5:
                        print("Error: numero de argumentos incorrecto")
                        continue
                    # Se declara el lenguaje base, lenguaje origen y lenguaje destino, y se llama al método que define el traductor
                    lenguaje_base, lenguaje_origen, lenguaje_destino = partes[2], partes[3], partes[4]
                    sistema.definir_traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)
                case _:
                    # Si el tipo es incorrecto
                    print(f"Error: no se reconoce el tipo '{tipo}'")  
                                    
        elif partes[0] == "EJECUTABLE":
            sistema.ejecutable(partes[1])
        else:
            # Si la accion ingresada es incorrecta
            print(f"Error: no se reconoce la accion '{partes[0]}'")    

if __name__ == "__main__":
    main()
