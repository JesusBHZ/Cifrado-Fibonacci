lista = [7, 12, 26, 34, 32, 26]
resultado = []
sublista = []

for elemento in lista:
    if elemento == 26:
        if sublista:
            resultado.append(sublista)
        sublista = []
    else:
        sublista.append(elemento)

if sublista:
    resultado.append(sublista)

print(resultado)
