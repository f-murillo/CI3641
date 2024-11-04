def eval_pre(expr):
    """
    Método que Evalúa una expresión en notación prefija
    """
    stack = [] # Pila para guardar los números y operadores
    for e in reversed(expr):  # Leer de derecha a izquierda
        if e.isdigit():  # Si es un número, añadir a la pila
            stack.append(int(e))
        # Si es un operador, desempilar dos números, aplicar la operación y empilar el resultado
        else:
            a = stack.pop()
            b = stack.pop()
            match e:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(a // b) # Division entera

    return stack[0]  # El resultado está en el tope de la pila

def eval_post(expr):
    """
    Método que Evalúa una expresión en notación postfija
    """
    stack = []
    for e in expr:  # Leer de izquierda a derecha
        if e.isdigit():  # Si es un número, añadir a la pila
            stack.append(int(e))
        # Misma idea que en el método eval_pre
        else:
            b = stack.pop()
            a = stack.pop()
            match e:
                case '+':
                    stack.append(a + b)
                case '-':
                    stack.append(a - b)
                case '*':
                    stack.append(a * b)
                case '/':
                    stack.append(a // b) # Division entera

    return stack[0] # El resultado está en el tope de la pila

def precedencia(op):
    """
    Método que devuelve la precedencia de un operador
    """
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

def mostrar_pre(expr):
    """
    Método que muestra una expresión en notación infija 
    """
    stack = []
    for e in reversed(expr):  # Leer de derecha a izquierda
        if e.isdigit():  # Si es un número, empilar
            stack.append(e)
        else:  # Si es un operador, desempilar dos elementos y formar la expresión infija
            a = stack.pop()
            b = stack.pop()
            # Añadir paréntesis (si es necesario) para mantener la precedencia
            if precedencia(e) > precedencia('+'):
                a = f'({a})' if ' ' in a else a
                b = f'({b})' if ' ' in b else b
            # Empilar números y operación
            result = f'{a} {e} {b}'
            stack.append(result)
            
    return stack[0] # El resultado está en el tope de la pila

def mostrar_post(expr):
    """
    Muestra una expresión en notación infija 
    """
    stack = []
    for e in expr:  # Leer de izquierda a derecha
        if e.isdigit():  # Si es un número, empilar
            stack.append(e)
        else:  # Misma idea que en mostrar_pre, pero este caso para formar expresión postfija
            b = stack.pop()
            a = stack.pop()
            # Añadir paréntesis (si es necesario) para mantener la precedencia
            if precedencia(e) > precedencia('+'):
                a = f'({a})' if ' ' in a else a
                b = f'({b})' if ' ' in b else b
            # Empilar números y operación
            result = f'{a} {e} {b}'
            stack.append(result)
            
    return stack[0] # El resultado está en el tope de la pila

def main():
    """Método principal"""
    while True:
        action = input("Ingresa una acción (EVAL, MOSTRAR, SALIR): ")
        
        # Si la acción es EVAL o MOSTRAR
        if action.startswith("EVAL") or action.startswith("MOSTRAR"):
            # Separar la accion en partes y verificar que haya por lo menos 3 partes
            partes = action.split()
            if len(partes) < 3:
                print("Error: se debe ingresar una acción, un orden y una expresión")
                continue
            
            # Guardar las partes de la accion
            acc, order, *expr = partes
            # Verificar la validez de los elementos en la expresión
            if len(expr) < 3:
                print("Error: la expresión debe tener al menos 3 elementos")
                continue
            
            error_e_inv = False # Flag de error en algún elemento de la expresión
            num_count = 0 # Contador de enteros
            op_count = 0 # Contador de operadores
            # Para cada elemento de la expresión
            for e in expr:
                # Si el elemento es un entero
                if e.isdigit():
                    num_count += 1
                # Si es un operador
                elif e in ['+', '-', '*', '/']:
                    op_count += 1
                # Si se ingresó un elemento incorrecto
                else:
                    print(f"Error: se ingresó un elemento ({e}) inválido en la expresión")
                    error_e_inv = True
                    break
                
            # Si se encontró un elemento inválido en la expresión, saltar a la siguiente iteración del while
            if error_e_inv:
                continue
            
            # Verificar que haya al menos dos enteros y que el número de enteros sea uno más que el número de operadores
            if num_count < 2 or num_count != op_count + 1:
                print("Error: la expresión debe contener al menos dos enteros, y debe haber exactamente un entero más que operadores")
                continue
            
            # Si la accion es evaluar o mostrar usando notacion prefija
            if (acc == "EVAL" or acc == "MOSTRAR") and order == "PRE":
                # Si primero se ingresa un entero
                if expr[0].isdigit():
                    print("Error: en el orden prefijo primero se ingresan los operadores")
                    continue
                # Manejar accion
                match acc:
                    case "EVAL":
                        print(eval_pre(expr))
                    case "MOSTRAR":
                        print(mostrar_pre(expr))
                        
            # Si la accion es evaluar o mostrar usando notacion postfija
            if (acc == "EVAL" or acc == "MOSTRAR") and order == "POST":
                # Si primero se ingresa un operador
                if expr[0] in ['+', '-', '*', '/']:
                    print("Error: en el orden postfijo primero se ingresan los enteros")
                    continue
                # Manejar accion
                match acc:
                    case "EVAL":
                        print(eval_post(expr))
                    case "MOSTRAR":
                        print(mostrar_post(expr))
                        
            # Si el orden ingresado no es válido
            if order not in ["PRE", "POST"]:
                print(f"Error: orden ingresado ({order}) inválido")
                    
        # Si la acción es SALIR
        elif action == "SALIR":
            print("Saliendo")
            break
        
        # Si la acción no es correcta
        else:
            print(f"Error: no se reconoce la acción {action}")

if __name__ == "__main__":
    main()
