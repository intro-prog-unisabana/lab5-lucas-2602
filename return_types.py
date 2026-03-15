def obtener_precio_usuario():
    """Convierte el numero ingresado por el usuario, a un flotante"""
    result = input("Enter the item's price:\n")
    return float(result)
precio = obtener_precio_usuario()
print(precio)