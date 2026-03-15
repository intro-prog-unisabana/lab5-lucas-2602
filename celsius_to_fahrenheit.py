def celsius_to_fahrenheit(temp: float):
    farenheit = (temp * 9/5) + 32
    return float(farenheit)

print(celsius_to_fahrenheit(0))    # Salida esperada: 32.0
print(celsius_to_fahrenheit(100))  # Salida esperada: 212.0
print(celsius_to_fahrenheit(-40))  # Salida esperada: -40.0