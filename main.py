abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","-"]

listaImpar = ["E17", "L8", "H23", "P2", "F13", "S25", "Q28", "W19", "T1", "N21", "Z12", "O4", "Y3", "G10", "J15", "V9", "M7", "X11", "A5", "D14", "I26", "E16", "R24", "U20", "K18", "B22", " "]

listaPar = ["K16", "B3", "J25", "W20", "C2", "L9", "Y24", "M8", "R17", "N4", "O22", "X15", "A1", "P10", "V19", "G6", "S11", "D7", "U14", "I12", "N21", "Z13", "Q5", "F18", "E26", "T23", " "]


entrada = input("Tu texto a cifrar: ")
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
                # print(posiciones)
            else:
                print(f"La letra '{caracter}' no está en la lista.")

    indexFibonacci = 0
    # print(serie)

    contador = 0
    for pos in posiciones:
        try:
            if listaImpar[pos] == " ":
                # print(f"agrego un espacio {pos}")
                indexFibonacci += 1
                cifradoText += listaImpar[pos]
                contador += 1
            else:
                newIndex = serie[indexFibonacci]
                if newIndex >= 34:                    
                    del posiciones[:contador]
                    cifradoText = cifradoWithTwoLists(serie, cifradoText, posiciones)
                    break
                
                # print(f"agrego {abecedario[pos]}")
                if (pos+newIndex) == 26:
                    pos = 0
                    newIndex = 0 

                
                sumaIndex = pos+newIndex
                # print(f"que es {listaImpar[pos+newIndex]} wii con la posicion {sumaIndex}")    
                cifradoText += listaImpar[sumaIndex]
                contador += 1

        except IndexError:
            # print("upp")
            indiceForNewList = (pos+newIndex) - 26
            cifradoText += listaImpar[indiceForNewList]
            contador += 1
             
    # print(cifradoText)
    return cifradoText

def cifradoWithTwoLists(listaFibonacci, cifradoText, newPositions):
    del listaFibonacci[:9]

    resultado = []
    sublista = []

    for elemento in newPositions:
        if elemento == 26:
            if sublista:
                resultado.append(sublista)
            sublista = []
        else:
            sublista.append(elemento)

    if sublista:
        resultado.append(sublista)

    for sublista in resultado:
        desfase = listaFibonacci.pop(0) / 26  # Utiliza un valor de listaFibonacci y elimínalo
        # print(f"este es el desfase {desfase}")
        entero = int(desfase)
        # print(f"hoiii {entero}")
        decimal = desfase - int(desfase)
        # print(f"este es el número 1 {decimal:.2f}")  # Asegura dos decimales

        # Formatea 'decimal' con dos decimales y luego extrae 'decimales_str' con los dos dígitos decimales
        decimal_formateado = "{:.2f}".format(decimal)
        decimales_str = decimal_formateado[-2:]
        # print(f"este es el STR {decimales_str}")
    
        multiplicacion = int(decimales_str[0]) * int(decimales_str[1]) if decimales_str else 0        

        if entero % 2 == 0:
            cifradoText = cifradoText + " "
            cifradoText = cifradoPar(multiplicacion, cifradoText, sublista)
        else:
            cifradoText = cifradoText + " "
            cifradoText = cifradoImpar(multiplicacion, cifradoText, sublista)
            

    return cifradoText

def cifradoPar(multiplicacion, cifradoText, newPosition):
    # print("ListaPar")
    # print(newPosition)
    #for lista in newPosition:
        # print(abecedario[lista])
    for lista in newPosition:
        # print(f"El índice es {lista}")
        # print(f"la pos seria: {lista + multiplicacion} por que la mult es {multiplicacion}")
        
        extraIndice = lista + multiplicacion
        if extraIndice == 26:
            extraIndice = 0
        if extraIndice > 26:
            # print(f"el extraindice vale {extraIndice}")
            extraIndice = extraIndice % 26
            # print(f"el modulo de extraindice  vale {extraIndice}")

        # print(f"Agrego: {abecedario[lista]} que es {listaPar[lista]} con un desfase de: {multiplicacion} lo cual se traduce como: {listaPar[extraIndice]}")
        cifradoText = cifradoText + listaPar[extraIndice]

    # print(f"La lista va así: {cifradoText}")
    return cifradoText

def cifradoImpar(multiplicacion, cifradoText, newPosition):
    # print("ListaImpar")
    # print(newPosition)
    # for lista in newPosition:
        #print(abecedario[lista])


    for lista in newPosition:
        # print(f"El índice es {lista}")
        # print(f"la pos seria: {lista + multiplicacion} por que la mult es {multiplicacion}")
        
        extraIndice = lista + multiplicacion
        if extraIndice == 26:
            extraIndice = 0
        if extraIndice > 26:
            # print(f"el extraindice vale {extraIndice}")
            extraIndice = extraIndice % 26
            # print(f"el modulo de extraindice  vale {extraIndice}")

        # print(f"Agrego: {abecedario[lista]} que es {listaImpar[lista]} con un desfase de: {multiplicacion} lo cual se traduce como: {listaImpar[extraIndice]}")
        cifradoText = cifradoText + listaImpar[extraIndice]

    # print(f"La lista va así: {cifradoText}")
    return cifradoText


print(f"Tu texto cifrado: {cifrado(serie, palabras)}")

# Hola buenas tardes como esta usted espero que se encuentre bien usted y su familia
#   1   2       3     4    5    6     7      8   9    10      11    12  13 14  15

