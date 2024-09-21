# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Retorna el descuento calculado
    return descuento

# Llamada 1: Solo se proporciona el monto total de la compra (descuento por defecto)
monto_total_1 = 250.00
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1

# Llamada 2: Se proporciona tanto el monto total como el porcentaje de descuento
monto_total_2 = 450.00
porcentaje_descuento_2 = 20
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2

# Mostrar los resultados
print(f"Llamada 1: Monto Total: ${monto_total_1:.2f}")
print(f"Descuento (10%): ${descuento_1:.2f}")
print(f"Monto Final a Pagar: ${monto_final_1:.2f}\n")

print(f"Llamada 2: Monto Total: ${monto_total_2:.2f}")
print(f"Descuento ({porcentaje_descuento_2}%): ${descuento_2:.2f}")
print(f"Monto Final a Pagar: ${monto_final_2:.2f}")
