# Escritura de archivo de texto
# Abrimos un archivo llamado 'my_notes.txt' en modo escritura
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Hoy aprendí cómo manipular archivos en Python.\n")
    file.write("Practicar la lectura y escritura en archivos de texto es útil.\n")
    file.write("Recuerda siempre cerrar el archivo después de las operaciones.\n")

# Lectura de archivo de texto
# Abrimos el archivo 'my_notes.txt' en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # .strip() elimina espacios y saltos de línea adicionales
