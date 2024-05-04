import re

def simple_eval(expr):
    try:
        # Convertir la expresión a una lista de tokens
        tokens = re.findall(r"\d+|[+*/()%^-]", expr)
        # Inicializar una pila para los operandos
        operand_stack = []

        # Definir la precedencia de operadores
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '(': 0}
        valid_operators = set(precedence.keys())

        # Convertir la expresión infija a postfija
        output = []
        operator_stack = []
        for token in tokens:
            if token.isnumeric():
                output.append(int(token))
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Sacar el '(' de la pila
            elif token in valid_operators:
                while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence[token]:
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                return f"Error: Token inválido - {token}"

        while operator_stack:
            output.append(operator_stack.pop())

        # Evaluar la expresión postfija
        for token in output:
            if type(token) is int:
                operand_stack.append(token)
            else:
                right_operand = operand_stack.pop()
                left_operand = operand_stack.pop()
                if token == '+':
                    operand_stack.append(left_operand + right_operand)
                elif token == '-':
                    operand_stack.append(left_operand - right_operand)
                elif token == '*':
                    operand_stack.append(left_operand * right_operand)
                elif token == '/':
                    operand_stack.append(left_operand / right_operand)
                elif token == '%':
                    operand_stack.append(left_operand % right_operand)
                elif token == '^':
                    operand_stack.append(left_operand ** right_operand)

        return operand_stack[0]
    except Exception as e:
        return f"Error al evaluar la expresión: {e}"

# Ejemplo de uso
expresion_usuario = input("Ingresa una expresión matemática: ")
print(f"El resultado de la expresión es: {simple_eval(expresion_usuario)}")