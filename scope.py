int_value = None
str_value = None
def set_globals(some_int = None, some_str = None):
    global int_value
    int_value = (some_int)
    global str_value
    str_value = str(some_str)
def get_globals():
    return (int_value, str_value)

print(get_globals())       # Salida: (None, None)
set_globals(10, "Hello")
print(get_globals())       # Salida: (10, "Hello")