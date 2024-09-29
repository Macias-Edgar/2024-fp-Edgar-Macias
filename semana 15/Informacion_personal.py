# Función para crear un diccionario dinámico de información personal
def crear_informacion_personal():
    # Solicitar información al usuario
    nombre = input("Ingrese el nombre: ")
    try:
        edad = int(input("Ingrese la edad: "))  # Validamos que la edad sea un número
    except ValueError:
        print("Error: La edad debe ser un número. Se asignará 0 como valor predeterminado.")
        edad = 0  # Si no se ingresa un número, se asigna 0 como valor predeterminado
    ciudad = input("Ingrese la ciudad: ")
    profesion = input("Ingrese la profesión: ")

    # Crear el diccionario con la información ingresada
    informacion_personal = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "profesion": profesion
    }

    return informacion_personal

# Función para modificar la ciudad en el diccionario
def modificar_ciudad(informacion):
    nueva_ciudad = input(f"La ciudad actual es {informacion['ciudad']}. Ingrese una nueva ciudad: ")
    informacion["ciudad"] = nueva_ciudad
    print(f"Ciudad modificada a {nueva_ciudad}.\n")

# Función para modificar o agregar la profesión
def modificar_profesion(informacion):
    nueva_profesion = input(f"La profesión actual es {informacion['profesion']}. Ingrese una nueva profesión: ")
    informacion["profesion"] = nueva_profesion
    print(f"Profesión actualizada a {nueva_profesion}.\n")

# Función para verificar y agregar un número de teléfono si no existe
def agregar_telefono_si_no_existe(informacion):
    if "telefono" not in informacion:
        telefono = input("No se ha encontrado un número de teléfono. Ingrese un número de teléfono: ")
        informacion["telefono"] = telefono
        print(f"Teléfono agregado: {telefono}\n")
    else:
        print(f"El teléfono ya está registrado: {informacion['telefono']}.\n")

# Función para eliminar la edad
def eliminar_edad(informacion):
    if "edad" in informacion:
        informacion.pop("edad")
        print("Clave 'edad' eliminada.\n")
    else:
        print("La clave 'edad' no está presente.\n")

# Función principal para ejecutar todas las operaciones
def ejecutar_operaciones():
    # Crear el diccionario
    informacion_personal = crear_informacion_personal()

    # Modificar la ciudad
    modificar_ciudad(informacion_personal)

    # Modificar o agregar la profesión
    modificar_profesion(informacion_personal)

    # Verificar si la clave "telefono" existe, si no, agregarla
    agregar_telefono_si_no_existe(informacion_personal)

    # Eliminar la clave "edad"
    eliminar_edad(informacion_personal)

    # Imprimir el diccionario final
    print("Diccionario final actualizado:", informacion_personal)

# Ejecutar el programa
if __name__ == "__main__":
    ejecutar_operaciones()
