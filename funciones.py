""" nombre = input('Ingresa tu nombre: ')

def saludo(nom):
    bien = print('¡Hola, bienvenido! tu nombre es: {}'.format(nom))
    return bien

saludo(nombre)
 """
#---------------------------------------------------------------

""" lista = []

for ini in range(0,6):
    lista.append(int(input('Ingrese un numero: ')))

def media(param):
    aux = 0
    for lis in param:
        aux += lis
    print(aux)
    print(len(param))
    medi = aux/len(param)
    mostrar = print('La media es: {}'.format(medi))
    return mostrar

media(lista)
 """

#----------------------------------------------------------------

""" arreglo = [ [3],
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12]]

def diagonalDifference(arr):
    # Write your code here
    dato1 = 0
    dato2 = 0
    aux = 0
    aux2 = -1
    for fila in arr:
        if len(fila) <= 1:
            continue
        for col in range(0, len(fila)):
            if col == aux:
                dato1 += fila[col]
                if (col == (len(fila) + aux2)):
                    dato2 += fila[col]
            elif col == (len(fila) + aux2):
                dato2 += fila[col]
            else:
                pass
        aux += 1
        aux2 += -1
    
    return abs(dato1 - dato2)

print(diagonalDifference(arreglo)) """

#---------------------------------------------------------------

""" anio = int(input('Ingrese un AÑo: '))

def bisiesto(anio):
    if (anio % 4 == 0):
        if ((anio % 100 == 0) and (anio % 400 == 0)):
            print(f'Este año "{anio}" es Bisiesto')
        else:
            print(f'Este año "{anio}" es NO Bisiesto')        
    else:
        print(f'Este año "{anio}" es NO Bisiesto')

bisiesto(anio) """

#---------------------------------------------------------------
""" arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    cero = 0
    for num in arr:
        if (num>0):
            pos += 1
        elif (num<0):
            neg += 1
        else:
            cero += 1
    print(format((pos/len(arr)), '.6f'))
    print(format((neg/len(arr)), '.6f'))
    print(format((cero/len(arr)), '.6f'))
    return


plusMinus(arr) """

#---------------------------------------------------------

""" def staircase(n):
    aux = 1
    for row in range(0, n):
        cadena = str()
        for col in range(0, n):
            if col < (len(range(0, n)) - aux):
                cadena += str(' ')
            elif col >= (len(range(0, n)) - aux):
                cadena += str('#') 
        print(cadena)   
        aux +=1
    return()

staircase(9) """

#---------------------------------------------------------

arr = [1,2,3,4,5]

def miniMaxSum(arr):
    aux = 0
    for ini in arr:
        print('hola')
    
miniMaxSum(arr)
#---------------------------------------------------------






