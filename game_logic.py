import secret_number
from response import input_response
entrada = input("Enter a seed number: ")
secret_number.seed_secret_numbers(entrada)
numero_generado = secret_number.generate_secret_number(1, 100)
user_input = 0
while True:
    if user_input != numero_generado:
        user_input = int(input("What is your guess: "))
        input_response(numero_generado, user_input)
        continue
    else:
        break