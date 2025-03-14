class VirtualMethodTableHandler:
    """Clase que implementa el manejador de tablas de métodos virtuales"""
    def __init__(self):
        """Constructor"""
        self.classes = {} # Diccionario para las clases

    def define_class(self, definition):
        """Método que define una clase"""
        parts = definition.split() # Dividimos la definición
                
        if ":" in parts: # Si la definición tiene : , quiere decir que la clase hereda de otra
            class_name, super_name = parts[1], parts[3]
            methods = parts[4:]
        else: # Si no, no hereda de nadie
            class_name = parts[1]
            super_name = None
            methods = parts[2:]

        # Verificar si la clase ya existe
        if class_name in self.classes:
            print(f"Error: La clase {class_name} ya existe.")
            return
        
        # Verificar si la super clase existe
        if super_name and super_name not in self.classes:
            print(f"Error: La super clase {super_name} no existe.")
            return
        
        # Verificar métodos duplicados
        if len(methods) != len(set(methods)):
            print(f"Error: Hay definiciones de métodos repetidas en {class_name}.")
            return
        
        # Crear la tabla de métodos virtuales
        methods_table = {}
        if super_name: # Si la clase hereda de otra
            methods_table.update(self.classes[super_name]["metodos"])
        
        # Agregar métodos definidos
        for method in methods:
            methods_table[method] = f"{class_name} :: {method}"
        
        # Guardar la clase en el diccionario
        self.classes[class_name] = {
            "super": super_name,
            "metodos": methods_table
        }
        
        # Imprimir mensaje de exito
        print(f"Clase {class_name} creada exitosamente")

    def describe_class(self, class_name):
        """Método que describe una clase"""
        if class_name not in self.classes:
            print(f"Error: La clase {class_name} no existe.")
            return
        # Obtenemos la tabla de métodos de la clase
        methods_table = self.classes[class_name]["metodos"]
        for method, implementation in methods_table.items(): # Para cada método e implementación en la tabla
            print(f"{method} -> {implementation}")

def main():
    """Método principal"""
    handler = VirtualMethodTableHandler()
    while True:
        action = input("Ingresa una acción (CLASE, DESCRIBIR, SALIR): ")
        parts = action.split()
        command = parts[0] if parts else None
        
        match command:
            case "CLASE":
                if len(parts) > 2:
                    handler.define_class(action)
                else: # En caso de haber ingresado pocos argumentos
                    print("Error: número de argumentos erróneo")
            case "DESCRIBIR":
                if len(parts) == 2:
                    class_name = parts[1]
                    handler.describe_class(class_name)
                else: # En caso de haber ingresado pocos argumentos
                    print("Error: número de argumentos erróneo")
            case "SALIR":
                print("Saliendo del programa")
                break
            case _:
                print(f"Acción {action} no reconocida")

if __name__ == "__main__":
    main()
