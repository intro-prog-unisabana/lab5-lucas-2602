def obtener_precio_usuario():
    """Convierte el numero ingresado por el usuario, a un flotante"""
    print("Enter the item's price:\n")
    result = input()
    return float(result)
precio = obtener_precio_usuario()
print(precio)