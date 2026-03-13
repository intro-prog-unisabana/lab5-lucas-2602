def obtener_precio_usuario():
    """Convierte el numero ingresado por el usuario, a un flotante"""
    entrada = input("Enter the item's price:\n")
    return float(entrada)
precio = obtener_precio_usuario()
print(precio)