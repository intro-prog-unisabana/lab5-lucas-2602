def obtener_precio_usuario():
    """Convierte el numero ingresado por el usuario, a un flotante"""
    resultad = input("Enter the item's price:\n")
    return float(resultad)
precio = obtener_precio_usuario()
print(precio)