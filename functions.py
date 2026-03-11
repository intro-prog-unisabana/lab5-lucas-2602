calificaciones = []
def promedio_estudiante(calificaciones):
    """Calcula el promedio de 3 notas"""
    if not calificaciones:
        return 0.0
    promedio = (sum(calificaciones))/(len(calificaciones))
    return float(promedio)
print(promedio_estudiante([45, 32, 18]))