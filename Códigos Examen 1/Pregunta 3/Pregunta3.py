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
        # Diccionario para los programas, interpretes y traductores (más fácil para asociar valores con sus claves, y más eficiente para búsquedas)
        self.programas = {}
        self.interpretes = {}
        self.traductores = {}

    def definir_programa(self, nombre, lenguaje):
        """Método que define un programa con un nombre 'a' y un lenguaje 'b' dados"""
        # Si ya existe el programa
        if nombre in self.programas:
            print(f"Error: ya existe un programa con el nombre '{nombre}'")
            return
        self.programas[nombre] = Programa(nombre, lenguaje)
        print(f"Se definio el programa '{nombre}', ejecutable en '{lenguaje}'")

    def definir_interprete(self, lenguaje_base, lenguaje):
        """Método que define un intérprete de un lenguaje 'a' escrito en un lennguaje 'b' dados"""
        # Si ya el intérprete está definido
        if lenguaje in self.interpretes:
            print(f"Error: ya existe un interprete para '{lenguaje}', escrito en '{lenguaje_base}'")
            return
        self.interpretes[lenguaje] = Interprete(lenguaje_base, lenguaje)
        print(f"Se definio un interprete para '{lenguaje}', escrito en '{lenguaje_base}'")

    def definir_traductor(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        """Método que define un traductor de un lenguaje 'a' hacia un lenguaje 'b' escrito en un lenguaje 'c' """
        # Si ya el traductor está definido
        if lenguaje_origen in self.traductores:
            print(f"Error: ya existe un traductor de '{lenguaje_origen}', hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")
            return
        self.traductores[lenguaje_origen] = Traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)
        print(f"Se definio un traductor de '{lenguaje_origen}' hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")

    def ejecutable(self, nombre):
        """Método que verifica si un programa es ejecutable"""
        # Si el programa no está definido
        if nombre not in self.programas:
            print(f"Error: no existe un programa con el nombre '{nombre}'")
            return
        lenguaje = self.programas[nombre].lenguaje # Lenguaje en el que fue escrito el programa
        # Se llama al método recursivo ejecutableRec con el lenguaje
        if self.ejecutableRec(lenguaje):
            print(f"Si, es posible ejecutar el programa '{nombre}'")
        else:
            print(f"No es posible ejecutar el programa '{nombre}'")

    def ejecutableRec(self, lenguaje):
        """Método recursivo que determina si un programa es ejecutable, dado el lenguaje en el que fue escrito"""
        if lenguaje == "LOCAL": # Caso base
            return True
        # Si el lenguaje está entre los intérpretes y si el método recursivo sobre la base del lenguaje retorna true
        if lenguaje in self.interpretes and self.ejecutableRec(self.interpretes[lenguaje].lenguaje_base): 
            return True
        # Si el lenguaje está entre los traductores y si el método recursivo sobre la base del lenguaje retorna true
        if lenguaje in self.traductores and self.ejecutableRec(self.traductores[lenguaje].lenguaje_base):
            return True
        # Si no se cumple ninguna condición, el programa no es ejecutable
        return False

def main():
    """Método Principal"""
    sistema = Sistema()
    while True:
        accion = input("Introduce una accion: ")
        if accion == "SALIR":
            print("Saliendo del programa")
            break
        partes = accion.split()
        if partes[0] == "DEFINIR":
            tipo = partes[1]
            match tipo:
                case "PROGRAMA":
                    nombre, lenguaje = partes[2], partes[3]
                    sistema.definir_programa(nombre, lenguaje)
                case "INTERPRETE":
                    lenguaje_base, lenguaje = partes[2], partes[3]
                    sistema.definir_interprete(lenguaje_base, lenguaje)
                case "TRADUCTOR":
                    lenguaje_base, lenguaje_origen, lenguaje_destino = partes[2], partes[3], partes[4]
                    sistema.definir_traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)
                case _:
                    print(f"Error: no se reconoce el tipo '{tipo}'")  
                                    
        elif partes[0] == "EJECUTABLE":
            sistema.ejecutable(partes[1])
        else:
            print(f"Error: no se reconoce la accion '{partes[0]}'")    

if __name__ == "__main__":
    main()