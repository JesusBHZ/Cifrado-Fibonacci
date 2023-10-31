from cryptography.fernet import Fernet

# Genera una clave aleatoria
clave = Fernet.generate_key()

# Crea un objeto Fernet con la clave generada
fernet = Fernet(clave)

# Datos que quieres cifrar
mensaje_original = b"Ejemplo de mensaje a cifrar"

# Cifra el mensaje
mensaje_cifrado = fernet.encrypt(mensaje_original)

print("Mensaje cifrado:", mensaje_cifrado)

# Descifra el mensaje
mensaje_descifrado = fernet.decrypt(mensaje_cifrado)

print("Mensaje descifrado:", mensaje_descifrado.decode())
