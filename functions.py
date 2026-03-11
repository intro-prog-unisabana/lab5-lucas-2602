calificaciones = []
def promedio_estudiante(calificaciones):
    """Calcula el promedio notas, si no hay ninguna nota, el promedio es cero"""
    if not calificaciones:
        return 0.0
    promedio = (sum(calificaciones))/(len(calificaciones))
    return float(promedio)
print(promedio_estudiante([45, 32, 18]))