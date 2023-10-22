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

    indexFibonacci = 0
    print(serie)

    contador = 0
    for pos in posiciones:
        try:
            if listaImpar[pos] == " ":
                indexFibonacci += 1
                cifradoText += listaImpar[pos]
                contador += 1
            else:
                newIndex = serie[indexFibonacci]
                if newIndex >= 34:                    
                    del posiciones[:contador]
                    cifradoText = cifradoWithTwoLists(serie, cifradoText, posiciones)
                    break

                cifradoText += listaImpar[pos+newIndex]
                contador += 1

        except IndexError:
            indiceForNewList = (pos+newIndex) - 26
            cifradoText += listaImpar[indiceForNewList]
            contador += 1
             
    # print(cifradoText)
    return cifradoText

def cifradoWithTwoLists(listaFibonacci, cifradoText,newPositions):
    del listaFibonacci[:9]

    for newSerie, newPosition in zip(listaFibonacci, newPositions):
        print("las posiciones")
        print(newPositions)


        desfase = newSerie/26
        # print(desfase)
        entero = int(desfase)
        decimal = desfase - int(desfase)
        decimales_str = str(decimal)[2:4]
        multiplicacion = int(decimales_str[0]) * int(decimales_str[1])
        newDesfase = multiplicacion + newPosition

        if entero % 2 == 0:
            cifradoText = cifradoPar(multiplicacion, cifradoText, newPosition)
        else:
            cifradoText = cifradoImpar(multiplicacion, cifradoText, newPosition)
    
    return cifradoText


def cifradoPar(multiplicacion, cifradoText, newPosition):
    print("listaPar")
    print(f"el indeice es {newPosition}")
    print(f"agrego: {listaPar[newPosition]} con un desfase de: {multiplicacion}")
    cifradoText = cifradoText + listaPar[newPosition+multiplicacion]

    return cifradoText

def cifradoImpar(multiplicacion, cifradoText, newPosition):
    print("listaImpar")
    print(f"el indeice es {newPosition}")
    print(f"agrego: {listaImpar[newPosition]} con un desfase de: {multiplicacion}")
    cifradoText = cifradoText + listaImpar[newPosition+multiplicacion]

    return cifradoText

print(cifrado(serie, palabras))