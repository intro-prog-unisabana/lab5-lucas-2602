def input_response(generate_value, user_input):
    while True:
        user_input = input("What is your guess: ")
        if user_input < generate_value:
            print("Too low! Try a higher number.")
        elif user_input > generate_value:
            print("Too high! Try a lower number.")
        else:
            print("Correct! You guessed the number!")
            break
