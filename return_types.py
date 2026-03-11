def obtener_precio_usuario():
    """Convierte el numero ingresado por el usuario, a un flotante"""
    resultado = float(input("Enter the item's price:\n"))
    return resultado
precio = obtener_precio_usuario()
print(precio)