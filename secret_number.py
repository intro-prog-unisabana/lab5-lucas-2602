import random
start = 0
end = 0
seed = 0
def seed_secret_numbers(seed):
    random.seed(6)
    generate_secret_number(1, 100)
def generate_secret_number(start, end):
    resu = random.randint(start, end)
    return resu
print(generate_secret_number(start, end))