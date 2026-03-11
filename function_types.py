def list_shift(datos: float, number: float):
    """Una lista de flotantes, en la cual se le suma un valor flotante, a cada elemento de la lista"""
    for i in range(len(datos)):
        datos[i] = datos[i] + number 
def calc_avg(datos):
    """Hallar el promedio de la lista de flotantes"""
    promedio = sum(datos)/len(datos)
    return promedio
def print_normalized(datos):
    """Imprimir la lista de flotantes"""
    return print(datos)

datos = [2.0, 4.0, 6.0, 8.0]
prom = calc_avg(datos)         # 5.0
list_shift(datos, -prom)       # datos se convierte en [-3.0, -1.0, 1.0, 3.0]
print_normalized(datos)        # imprime [-3.0, -1.0, 1.0, 3.0]