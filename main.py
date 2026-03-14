from utils_calc import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute
while True:
    entrada = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n")
    if entrada == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        add(num1, num2)
        continue
    elif entrada == "subtract":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        res = sub(num1, num2)
        print(f"The result is: {res}")
        continue
    elif entrada == "multiply":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        res = multiply(num1, num2)
        print(f"The result is: {res}")
        continue
    elif entrada == "divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        res = divide(num1, num2)
        print(f"The result is: {res}")
        continue
    elif entrada == "exponent":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        res = exponent(num1, num2)
        print(f"The result is: {res}")
        continue
    elif entrada == "modulo":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        res = modulo(num1, num2)
        print(f"The result is: {res}")
        continue
    elif entrada == "floor_divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        res = floor_divide(num1, num2)
        print(f"The result is: {res}")
        continue
    elif entrada == "absolute":
        num1 = float(input("Enter the number: "))
        res = absolute(num1)
        print(f"The result is: {res}")
        continue
    elif entrada == "exit":
        break
    else:
        print("Invalid option!")
        continue