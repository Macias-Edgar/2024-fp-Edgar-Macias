# Definir la matriz 3x3 con valores numéricos
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def bubble_sort(lista):
    # Implementación del algoritmo de ordenación Bubble Sort
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Intercambia los elementos si están en el orden incorrecto
                lista[j], lista[j+1] = lista[j+1], lista[j]

def ordenar_fila(matriz, fila_index):
    # Ordena una fila específica utilizando Bubble Sort
    fila = matriz[fila_index]  # Obtiene la fila de la matriz
    bubble_sort(fila)  # Ordena la fila
    matriz[fila_index] = fila  # Actualiza la fila ordenada en la matriz

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definir el índice de la fila que se desea ordenar
fila_a_ordenar = 1

# Ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
