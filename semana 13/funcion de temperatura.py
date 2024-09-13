import random


def calcular_promedio_temperatura_general(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante todo el período de tiempo,
    así como el promedio de cada semana.

    Parámetros:
    temperaturas (list): Una matriz 3D que contiene las temperaturas diarias de múltiples ciudades,
                          semanas y días. La estructura es [ciudades][semanas][días].

    Retorna:
    tuple: Una tupla que contiene dos listas:
           - Promedios semanales por ciudad.
           - Promedios generales por ciudad.
    """

    # Obtener el número de ciudades, semanas y días
    num_ciudades = len(temperaturas)
    num_semanas = len(temperaturas[0])
    num_dias = len(temperaturas[0][0])

    # Inicializar listas para almacenar los promedios semanales y generales
    promedios_semanales = [[0 for _ in range(num_semanas)] for _ in range(num_ciudades)]
    promedios_generales = [0 for _ in range(num_ciudades)]

    # Iterar sobre cada ciudad
    for ciudad_idx in range(num_ciudades):
        suma_total_temperaturas = 0  # Para calcular el promedio general
        num_dias_totales = 0  # Contador de días para calcular el promedio general

        # Iterar sobre cada semana
        for semana_idx in range(num_semanas):
            # Calcular la suma de las temperaturas de la semana para la ciudad actual
            suma_temperaturas = sum(temperaturas[ciudad_idx][semana_idx])
            # Calcular el promedio de las temperaturas de la semana
            promedio_semanal = suma_temperaturas / num_dias
            # Almacenar el promedio en la lista de promedios semanales
            promedios_semanales[ciudad_idx][semana_idx] = promedio_semanal

            # Acumulación para el promedio general
            suma_total_temperaturas += suma_temperaturas
            num_dias_totales += num_dias

        # Calcular el promedio general para la ciudad actual
        promedio_general = suma_total_temperaturas / num_dias_totales
        promedios_generales[ciudad_idx] = promedio_general

    return promedios_semanales, promedios_generales


# Datos de ejemplo: temperaturas de 3 ciudades durante 4 semanas y 7 días por semana
ciudades = ["Quininde", "La Concordia", "Esmeraldas"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear una matriz 3D con temperaturas aleatorias
temperaturas = [[[random.randint(15, 35) for _ in range(7)] for _ in range(4)] for _ in range(3)]

# Llamar a la función para calcular los promedios
promedios_semanales, promedios_generales = calcular_promedio_temperatura_general(temperaturas)

# Mostrar los promedios semanales y generales
for ciudad_idx in range(len(ciudades)):
    print(f"\nPromedios de temperaturas para {ciudades[ciudad_idx]}:")

    # Promedios semanales
    for semana_idx in range(len(promedios_semanales[0])):
        print(f"  Semana {semana_idx + 1}: {promedios_semanales[ciudad_idx][semana_idx]:.2f}°C")

    # Promedio general
    print(
        f"\nEl promedio general de temperaturas para {ciudades[ciudad_idx]} es: {promedios_generales[ciudad_idx]:.2f}°C")
