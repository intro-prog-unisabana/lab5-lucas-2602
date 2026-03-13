import os
import math
directory = ""
num = 0
def directorio():
    directorio_actual = os.getcwd()
    print(f"Directorio actual: {directorio_actual}")
def logaritmo():
    num = int(input("Enter an integer: "))
    log = math.log2(num)
    print(f"Log base 2 of {num} is: {log}")

directorio()
logaritmo()


