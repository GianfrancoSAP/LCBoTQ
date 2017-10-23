import random


def analizar(texto, mostrar = False):
    comando = texto.split()
    tiradas = []
    operaciones = []
    secuencia = []
    numeros = []
    for i in comando:
        if 'd' in i:
            tiradas.append(i)
            secuencia.append('d')
        elif i == '+' or i == '-' or i == '*' or i == '/':
            operaciones.append(i)
            secuencia.append('o')
        else:
            try:
                numero = int(i)
                secuencia.append('n')
                numeros.append(numero)
            except:
                pass
    contadorOperaciones = 0
    contadorTiradas = 0
    contadorNumeros = 0
    calculo = ''
    detalle = ''
    for i in secuencia:
        if i == 'd':
            tirada = tiradas[contadorTiradas]
            contadorTiradas += 1
            pos = tirada.index('d')
            resultado = 0
            total = 0
            det = '('
            for i in range(int(tirada[:pos])):
                resultado = random.randint(1,int(tirada[pos+1:])) 
                total += resultado
                if i == 0:                    
                    det += str(resultado)
                else:
                    det += ' + ' + str(resultado) 
            calculo += str(total)
            detalle += str(total) + det + ')'
        elif i == 'o':
            operador = operaciones[contadorOperaciones]
            contadorOperaciones += 1
            calculo += operador
            detalle += operador
        elif i == 'n':
            num = numeros[contadorNumeros]
            contadorNumeros += 1
            calculo += str(num)
            detalle += str(num)
    if mostrar == True:
        return detalle + ' = ' + str(eval(calculo))
    if mostrar == False:
        return eval(calculo) 
