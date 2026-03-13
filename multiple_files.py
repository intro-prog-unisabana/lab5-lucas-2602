import utils
entrada = input("Please type your message\n")
reverso = utils.flip(entrada)
menaje_codificado = utils.count_letters(reverso, "a")
print(f"Your encoded message is: {reverso}{menaje_codificado}")