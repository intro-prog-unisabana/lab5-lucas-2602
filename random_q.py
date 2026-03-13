import random
random.seed(123)
inicio = int(input("Enter the start value:\n"))
final = int(input("Enter the end value:\n"))
random_number = random.randint(inicio, final)
print(f"Generated random number: {random_number}")