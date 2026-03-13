import random
def seed_secret_numbers(seed):
    random.seed(6)
    return seed
def generate_secret_number(start=1, end=100):
    num = random.randint(start, end)
    return num
