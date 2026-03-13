import os
import math
log = 0
def directorio():
    directorio_actual = os.getcwd()
    print(f"Current working directory: {directorio_actual}")
def logaritmo():
    num = int(input("Enter an integer: "))
    global log
    log = math.log2(num)
    print(f"Log base 2 of {num} is: {log}")
def piso_logaritmo():
    piso = math.floor(log)
    print(f"Floor: {piso}")
def techo_logaritmo():
    techo = math.ceil(log)
    print(f"Ceiling: {techo}")
directorio()
logaritmo()
piso_logaritmo()
techo_logaritmo()


