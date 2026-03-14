contador = 0
def input_response(generate_value, user_input):
    global contador
    contador = contador + 1
    número = contador
    if user_input < generate_value:
        print("Too low! Try a higher number.")
    elif user_input > generate_value:
        print("Too high! Try a lower number.")
    else:
        print("Correct! You guessed the number!")
        print(f"It took you {número} tries!")
