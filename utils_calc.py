from math import pow, fmod, floor, fabs

def add(num1, num2):
    if isinstance(num1, int) and (num2, int):
        suma = num1 + num2
        return print(int(suma))
    else:
        suma = num1 + num2
        return print(float(suma))
def sub(num1, num2):
    if isinstance(num1, int) and (num2, int):
        resta = num1 - num2
        return print(int(resta))
    else:
        resta = num1 - num2
        return print(float(resta))
if __name__ == "__main__":
    add(3, 5)      # 8 (resultado entero)
    add(3.5, 5)     # 8.5 (resultado decimal)
    sub(10, 4)      # 6 (resultado entero)
    sub(10.0, 4.5)  # 5.5 (resultado decimal)

def multiply(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        multiplicación = num1 * num2
        return print(int(multiplicación))
    else:
        multiplicación = num1 * num2
        return print(multiplicación)
def divide(num1, num2):
    if num2 != 0:
        división = num1 / num2
        return print(división)
    else:
        división = print("Error: Division by zero is not allowed.")
        return división
if __name__ == "__main__":
    multiply(3, 4)    # 12 (resultado entero)
    multiply(3.5, 4)  # 14.0 (resultado decimal)
    divide(10, 2)     # 5.0 (resultado decimal, la división siempre retorna decimal)
    divide(7, 3)      # 2.3333333333333335 (resultado decimal)
    divide(4, 0)      # "Error: Division by zero is not allowed." (resultado cadena de texto)

def exponent(base, exp):
    if isinstance(base, int) and isinstance(exp, int):
        exponenciación = pow(base, exp)
        return print(int(exponenciación))
    else:
        exponenciación = pow(base, exp)
        return print(exponenciación)
def modulo(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        if num2 != 0:
            residuo = int(fmod(num1, num2))
            return print(residuo)
        else:
            return print("Error: Modulo by zero is not allowed.")
    else:
        if num2 != 0:
            residuo = fmod(num1, num2)
            return print(residuo)
        else:
            return print("Error: Modulo by zero is not allowed.")
if __name__ == "__main__":
    exponent(2, 3)    # 8 (resultado entero)
    exponent(2.0, 3)  # 8.0 (resultado decimal)
    modulo(10, 3)     # 1 (resultado entero)
    modulo(10.5, 3)   # 1.5 (resultado decimal)
    modulo(10, 0)     # "Error: Modulo by zero is not allowed." (resultado cadena de texto)

def floor_divide(num1, num2):
    if num2 != 0:
        if isinstance(num1, int) and isinstance(num2, int):
            dividir = num1/num2
            entero_mas_grande = floor(dividir)
            return print(entero_mas_grande)
        else:
            dividir = num1/num2
            entero_mas_grande = floor(dividir)
            return print(float(entero_mas_grande))
    else:
        return print("Error: Division by zero is not allowed.")
def absolute(num):
    if isinstance(num, int):
        valor_absoluto = fabs(num)
        return print(int(valor_absoluto))
    else:
        valor_absoluto = fabs(num)
        return print(valor_absoluto)
if __name__ == "__main__":
    floor_divide(10, 3)   # 3 (resultado entero)
    floor_divide(10.5, 3) # 3.0 (resultado decimal)
    floor_divide(5, 0)    # "Error: Division by zero is not allowed." (resultado cadena de texto)
    absolute(-5)          # 5 (resultado entero)
    absolute(-5.5)        # 5.5 (resultado decimal)