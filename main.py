abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","-"]

listaImpar = ["E17", "L8", "H23", "P2", "F13", "525", "Q28", "W19", "T1", "N21", "Z12", "O4", "Y3", "G10", "J15", "V9", "M7", "X11", "A5", "D14", "I26", "E16", "R24", "U20", "K18", "B22", " "]

listaPar = ["K16", "B3", "J25", "W20", "C2", "L9", "Y24", "M8", "R17", "N4", "O22", "X15", "A1", "P10", "V19", "G6", "S11", "D7", "U14", "I12", "N21", "Z13", "Q5", "F18", "E26", "T23", " "]


entrada = input("Tu texto a cifrar: ")
palabras = entrada.split()
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

def cifrado(serie, palabras):
    print(serie)
    cifradoText = ""
    posiciones = []
    palabrasWithSpace = [val for sublist in [[item, '-'] for item in palabras] for val in sublist]
    palabrasWithSpace.pop() 

    for palabra in palabrasWithSpace:
        palabra.upper()
        letras = list(palabra.upper())
        
        for caracter in letras:
            if caracter in abecedario:
                posicion = abecedario.index(caracter)
                posiciones.append(posicion)
            else:
                print(f"La letra '{caracter}' no está en la lista.")

    index = 0
    print(serie)
    for pos in posiciones:
        try:
            if listaImpar[pos] == " ":
                index += 1
                
                cifradoText += listaImpar[pos]
            
            else:
                newIndex = serie[index]
                
                cifradoText += listaImpar[pos+newIndex]

        except IndexError:
            print(f"el valor de indice es {index}")
            print(f"el valor de la serie es {newIndex}")
            print(f"el valor de la lado es {pos+newIndex}")
            indiceForNewList = (pos+newIndex) - 26
            print(f"el valor de la lado es {indiceForNewList}")
            print("¡Error: El índice está fuera de rango!")

        
             
    # print(cifradoText)
    return cifradoText


print(cifrado(serie, palabras))