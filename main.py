from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute
while True:
    entrada = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n")
    if entrada == "add":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num1.is_integer():
            num1 = int(num1)
        else:
            num1 = num1
        if num2.is_integer():
            num2 = int(num2)
        else:
            num2 = num2
        add(num1, num2)
        continue
    elif entrada == "subtract":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num1.is_integer():
            num1 = int(num1)
        else:
            num1 = num1
        if num2.is_integer():
            num2 = int(num2)
        else:
            num2 = num2
        sub(num1, num2)
        continue
    elif entrada == "multiply":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        multiply(num1, num2)
        continue
    elif entrada == "divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num1.is_integer():
            num1 = int(num1)
        else:
            num1 = num1
        if num2.is_integer():
            num2 = int(num2)
        else:
            num2 = num2
        divide(num1, num2)
        continue
    elif entrada == "exponent":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        exponent(num1, num2)
        continue
    elif entrada == "modulo":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        modulo(num1, num2)
        continue
    elif entrada == "floor_divide":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        floor_divide(num1, num2)
        continue
    elif entrada == "absolute":
        num1 = float(input("Enter the number: "))
        absolute(num1)
        continue
    elif entrada == "exit":
        break
    else:
        print("Invalid option!")
        continue