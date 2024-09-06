import random

# Definir ciudades, días de la semana y semanas
ciudades = ["Quininde", "La Concordia", "Esmeraldas"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear una matriz 3D de 3 ciudades, 4 semanas, y 7 días por semana
temperaturas = [[[random.randint(15, 35) for _ in range(7)] for _ in range(4)] for _ in range(3)]

# Mostrar las temperaturas generadas
for ciudad_idx in range(3):
    print(f"\nTemperaturas para {ciudades[ciudad_idx]}:")
    for semana_idx in range(4):
        print(f"  Semana {semana_idx + 1}:")
        for dia_idx in range(7):
            print(f"    {dias_semana[dia_idx]}: {temperaturas[ciudad_idx][semana_idx][dia_idx]}°C")

# Calcular el promedio de temperaturas por ciudad para cada semana
promedios_semanales = [[0 for _ in range(4)] for _ in range(3)]  # Inicializar la lista de promedios

for ciudad_idx in range(3):  # Itera sobre las ciudades
    for semana_idx in range(4):  # Itera sobre las semanas
        suma_temperaturas = sum(temperaturas[ciudad_idx][semana_idx])  # Suma de temperaturas de la semana
        promedio = suma_temperaturas / 7  # Calcular el promedio
        promedios_semanales[ciudad_idx][semana_idx] = promedio

# Mostrar los promedios semanales por ciudad
for ciudad_idx in range(3):
    for semana_idx in range(4):
        print(f"\nEl promedio de temperaturas para {ciudades[ciudad_idx]} en la semana {semana_idx + 1} es: {promedios_semanales[ciudad_idx][semana_idx]:.2f}°C")
