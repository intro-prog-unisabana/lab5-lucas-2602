def obtener_precio_usuario():
    """Convierte el numero ingresado por el usuario, a un flotante"""
    resut = input("Enter the item's price:\n")
    return float(resut)
precio = obtener_precio_usuario()
print(precio)