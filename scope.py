int_value = None
str_value = None
def set_globals(some_int, some_str):
    global int_value
    int_value = int(some_int)
    global str_value
    str_value = str(some_str)
def get_globals():
    return (int_value, str_value)

if __name__ == "__main__":
    print(get_globals())       # Salida: (None, None)
    set_globals(10, "Hello")
    print(get_globals())       # Salida: (10, "Hello")