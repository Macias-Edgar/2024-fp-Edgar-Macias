# Definir la matriz 3x3 con valores numéricos
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def buscar_valor_en_matriz(matriz, valor_buscado):
    # Recorre la matriz usando índices para filas y columnas
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas de cada fila
            if matriz[i][j] == valor_buscado:  # Comprueba si el valor en la posición actual es el buscado
                return f"Valor {valor_buscado} encontrado en la posición ({i}, {j})"

    # Si no se encuentra el valor, devuelve un mensaje indicándolo
    return f"Valor {valor_buscado} no encontrado en la matriz"


# Definir el valor que se desea buscar
valor_buscado = 5

# Llamar a la función y mostrar el resultado
resultado = buscar_valor_en_matriz(matriz, valor_buscado)
print(resultado)
