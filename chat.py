def limpiar_entrada(texto):
    # Crear una función que elimine caracteres no deseados y devuelva la entrada limpia
    texto_limpio = ''.join(char for char in texto if char.isalpha() or char.isspace() or char == '-')
    return texto_limpio

# Solicitar entrada al usuario y limpiarla
entrada = input("Tu texto a cifrar: ")
entrada_limpia = limpiar_entrada(entrada)

if entrada != entrada_limpia:
    print("Se han eliminado caracteres no válidos de la entrada.")

# Dividir la entrada limpia en palabras
palabras = entrada_limpia.split()
cantidad_de_palabras = len(palabras)

# Realizar el cifrado aquí
