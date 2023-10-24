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
    series = []
    for serie, letras in zip(serie, segunda_seccion):
        if serie < 34:
            # print(f'Variable 1: {serie}, Variable 2: {letras}')
            for caracter in letras:
                if caracter in listaImpar:
                    posicion = listaImpar.index(caracter)

                    if posicion == 0:
                        if posicion == 0 and serie == 0:
                            posiciones.append(0)
                            # print(f'Caso 0: Posicion de listaImpar: {posicion}, desfase: {serie} eso es igual a {abecedario[0]}')
                        else:    
                            newPosition = 26 - serie
                            # print(f'Caso 0 0: Posicion de listaImpar: {posicion}, desfase: {serie} eso es igual a {abecedario[newPosition]}')
                            posiciones.append(newPosition)
                    else:
                        posicionNegativa = posicion-serie
                        if posicionNegativa < 0:
                            # print(f'Caso more Megativo: Posicion de listaImpar: {posicion}, desfase: {serie} eso es igual a {abecedario[posicionNegativa-1]} o {posicion-serie}')
                            posiciones.append(posicionNegativa-1)
                        else:
                            # print(f'Caso more: Posicion de listaImpar: {posicion}, desfase: {serie} eso es igual a {abecedario[posicion-serie]} o {posicion-serie}')
                            posiciones.append(posicion-serie)

                else:
                    print(f"La letra '{caracter}' no está en la lista.")
            posiciones.append(26)    
        else:
            series.append(serie)

    for pos in posiciones:
        try:
            descifrado_text += abecedario[pos]
            # print(abecedario[pos])
        except IndexError:
            print("upp")
            #indiceForNewList = (pos+newIndex) - 26
            #cifradoText += listaImpar[indiceForNewList]
            #contador += 1
    del segunda_seccion[:9]
    
    for serie, letras in zip(series, segunda_seccion):
        # print(f'Variable 1: {serie}, Variable 2: {letras}')
        # print()
        desfase = serie/26
        # print(f"este es el desface: {desfase}")
        entero = int(desfase)
        print(f"El entero {entero}")
        decimal = desfase - int(desfase)
        # print(f"este es el número 1: {decimal:.2f}")  # Asegura dos decimales
        # Formatea 'decimal' con dos decimales y luego extrae 'decimales_str' con los dos dígitos decimales
        decimal_formateado = "{:.2f}".format(decimal)
        decimales_str = decimal_formateado[-2:]
        # print(f"este es el STR {decimales_str}")
        
        multiplicacion = int(decimales_str[0]) * int(decimales_str[1]) if decimales_str else 0  
        # print(f"este es la multiplicacion {multiplicacion}")

        if entero % 2 == 0:
            descifrado_text = descifrado_text + " "
            descifrado_text = desCifradoPar(multiplicacion, descifrado_text, letras)
        else:
            descifrado_text = descifrado_text + " "
            descifrado_text = desCifradoImpar(multiplicacion, descifrado_text, letras)

    return descifrado_text           



def desCifradoPar(multiplicacion, descifrado_text, letras):
    # print("lista par")
    try:
        posiciones = []
        for letra in letras:
            if letra in listaPar:
                    posicion = listaPar.index(letra)
                    posiciones.append(posicion)
        
        print(posiciones)
        for pos in posiciones:
            desfase = pos-multiplicacion
            # print(f"desfase : {desfase} con una multiplicacion de : {multiplicacion}")
            if desfase >= 0:
                descifrado_text = descifrado_text + abecedario[desfase]
            elif desfase < 0:
                des = 26 + (desfase)
                if des >= 0:
                    descifrado_text = descifrado_text + abecedario[des]
                else:
                    desfasePositivo = -1 * des
                    desfasePositivoSegundoOrden = 26 - desfasePositivo
                    descifrado_text = descifrado_text + abecedario[desfasePositivoSegundoOrden]

    except IndexError:
        print(f"upps {desfase}")
    
    return descifrado_text


def desCifradoImpar(multiplicacion, descifrado_text, letras):
    # print("lista impar")
    try:
        posiciones = []
        for letra in letras:
            if letra in listaImpar:
                    posicion = listaImpar.index(letra)
                    posiciones.append(posicion)

        print(posiciones)
        for pos in posiciones:
            desfase = pos-multiplicacion
            # print(f"desfase : {desfase} con una multiplicacion de : {multiplicacion}")
            if desfase >= 0:
                descifrado_text = descifrado_text + abecedario[desfase]
            elif desfase < 0:
                des = 26 + (desfase)
                if des >= 0:
                    descifrado_text = descifrado_text + abecedario[des]
                else:
                    desfasePositivo = -1 * des
                    desfasePositivoSegundoOrden = 26 - desfasePositivo
                    descifrado_text = descifrado_text + abecedario[desfasePositivoSegundoOrden]

    except IndexError:
        print(f"upps {desfase}")
    
    return descifrado_text


print(f"Tu texto descifrado: {cifrado(serie, segunda_seccion)}")

# W19J15O4E17 H23E16S25J15L8D14 I26L8A5F13S25D14 F13M7J15M7 W19E16R24P2 B22U20K18N21T1 Y3E17U20Y3B22R24 P2W19X11 G10B22  W19M7S25U20W19M7R24I26W19 W20O22Y24G6 H23E17L8Y3O4 A5 N21Q5 L9K16A1R17X15R17K16