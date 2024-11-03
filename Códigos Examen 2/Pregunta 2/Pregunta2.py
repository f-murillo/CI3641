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

def precedence(op):
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
    Método que muestra una expresión en notación infija a partir de una expresión en notación prefija
    """
    stack = []
    for e in reversed(expr):  # Leer de derecha a izquierda
        if e.isdigit():  # Si es un número, empilar
            stack.append(e)
        else:  # Si es un operador, desempilar dos elementos y formar la expresión infija
            a = stack.pop()
            b = stack.pop()
            # Añadir paréntesis (si es necesario) para mantener la precedencia
            if precedence(e) > precedence('+'):
                a = f'({a})' if ' ' in a else a
                b = f'({b})' if ' ' in b else b
            # Empilar números y operación
            result = f'{a} {e} {b}'
            stack.append(result)
            
    return stack[0] # El resultado está en el tope de la pila

def mostrar_post(expr):
    """
    Muestra una expresión en notación infija a partir de una expresión en notación postfija
    """
    stack = []
    for e in expr:  # Leer de izquierda a derecha
        if e.isdigit():  # Si es un número, empilar
            stack.append(e)
        else:  # Misma idea que en mostrar_pre, pero este caso para formar expresión postfija
            b = stack.pop()
            a = stack.pop()
            # Añadir paréntesis (si es necesario) para mantener la precedencia
            if precedence(e) > precedence('+'):
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
        # Verificar si la acción es EVAL o MOSTRAR
        if action.startswith("EVAL") or action.startswith("MOSTRAR"):
            acc, order, *expr = action.split()
            # Verificar la validez de los elementos en la expresión
            error_expr = False
            for e in expr:
                if not e.isdigit() and e not in ['+', '-', '*', '/']:
                    print(f"Error: se ingresó un elemento ({e}) inválido en la expresión")
                    error_expr = True
                    break
            # Si se encontró un error en la expresión, pasar a la siguiente iteración del bucle
            if error_expr:
                continue
            # Manejar acciones EVAL y MOSTRAR
            match acc:
                case "EVAL":
                    match order:
                        case "PRE":
                            print(eval_pre(expr))
                        case "POST":
                            print(eval_post(expr))
                        case _:
                            print(f"Error: orden ingresado {order} inválido")
                case "MOSTRAR":
                    match order:
                        case "PRE":
                            print(mostrar_pre(expr))
                        case "POST":
                            print(mostrar_post(expr))
                        case _:
                            print(f"Error: orden ingresado {order} inválido")
        
        # Si la acción es SALIR
        elif action == "SALIR":
            print("Saliendo")
            break
        
        # Si la acción no es correcta
        else:
            print("Error: no se reconoce la acción")

if __name__ == "__main__":
    main()
