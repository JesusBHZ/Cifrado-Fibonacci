import re

abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]

listaImpar = ["E17", "L8", "H23", "P2", "F13", "S25", "Q28", "W19", "T1", "N21", "Z12", "O4", "Y3", "G10", "J15", "V9", "M7", "X11", "A5", "D14", "I26", "E16", "R24", "U20", "K18", "B22", " "]

listaPar = ["K16", "B3", "J25", "W20", "C2", "L9", "Y24", "M8", "R17", "N4", "O22", "X15", "A1", "P10", "V19", "G6", "S11", "D7", "U14", "I12", "N21", "Z13", "Q5", "F18", "E26", "T23", " "]


import re

entrada = input("Tu texto cifrado: ")
caracteres_no_deseados = [';', ',', '-', 'ñ']
texto_limpio = ''.join(char for char in entrada if char not in caracteres_no_deseados)

palabras = texto_limpio.split()
cantidad_de_palabras = len(palabras)

def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci_recursivo(n - 1)
        siguiente = fib[-1] + fib[-2]
        fib.append(siguiente)
        return fib

n = cantidad_de_palabras
serie = fibonacci_recursivo(n)

segunda_seccion = [] 
posiciones = []


for seccion in palabras:
    partes = re.findall(r'[A-Z]\d+', seccion)
    segunda_seccion.append(partes)


def cifrado(serie, segunda_seccion):
    descifrado_text = ""

    for serie, letras in zip(serie, segunda_seccion):
        if serie < 34:
            print(f'Variable 1: {serie}, Variable 2: {letras}')
            for caracter in letras:
                if caracter in listaImpar:
                    posicion = listaImpar.index(caracter)

                    if posicion == 0:
                        newPosition = 26 - serie
                        print(f'Posicion de listaImpar: {posicion}, desfase: {serie} eso es igual a {abecedario[newPosition]}')
                        posiciones.append(newPosition)
                    else:
                        print(f'Posicion de listaImpar: {posicion}, desfase: {serie} eso es igual a {abecedario[posicion-serie]}')
                        posiciones.append(posicion-serie)

                else:
                    print(f"La letra '{caracter}' no está en la lista.")
            posiciones.append(26)    
        else:
            # print(f'Variable 1: {serie}, Variable 2: {valor2}')
            pass

    print(posiciones)

    for pos in posiciones:
        try:
            descifrado_text += abecedario[pos]
            # print(abecedario[pos])
        except IndexError:
            print("upp")
            #indiceForNewList = (pos+newIndex) - 26
            #cifradoText += listaImpar[indiceForNewList]
            #contador += 1

    return descifrado_text           

# print(serie)
# print(segunda_seccion)

print(f"Tu texto descifrado: {cifrado(serie, segunda_seccion)}")

# W19J15O4E17 H23E16S25J15L8D14 I26L8A5F13S25D14 F13M7J15M7 W19E16R24P2 B22U20K18N21T1 Y3E17U20Y3B22R24 P2W19X11 G10B22  W19M7S25U20W19M7R24I26W19 W20O22Y24G6 H23E17L8Y3O4 A5 N21Q5 L9K16A1R17X15R17K16