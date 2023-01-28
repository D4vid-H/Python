""" lista1 = []
lista2 = []
lista5 = [1,2,2,5,7,8,7,5,4,6,3,9,1,4,2,3,6,4,8,5,2,1,6,6,8,4,3,2,1]

lista1.append(456789)
lista1.append("Hola Mundo")

print("lista N°: 1", lista1)

lista2.append("Hola y Adios")
lista2.append(5555)
lista2.append(5566)

lista3 = lista1.pop()

lista4 = lista2[1 : len(lista2) - 1]

print("lista N°: 1", lista1)
print("lista N°: 2", lista2)
print("lista N°: 3", lista3)
print("lista N°: 4", lista4)

print("lista N°: 5", lista5)

print('Se muestra la funcion Count(5): ', lista5.count(5))

print('Se muestra la funcion Index(9): ', lista5.index(9)) """

#-------------------------------------------------------------------------------------
""" tupla = (8,15,4,39,5,89,87,19,7,-755,88,123,2,11,15,9,355)

# -1 El ultimo ítem de tupla
print('El ultimo items: ', tupla[-1])

# -2 El numero de items dento de tupla
print('El numero de items: ', len(tupla))

# -3 La posicion del item 87
print('El item 87 esta en: ', tupla.index(87))

# -4 Una listra con los ultimos 3 items
print('Una lista con los ultimos 3 items: ', list(tupla[-3:]))

# -5 Item en la posicion 8
print('Items en la posicion 8: ', tupla[7])

# -6 Veces que el 7 se repite
print('Veces que el 7 se repite: ', tupla.count(7)) """

#-------------------------------------------------------------------------------------
""" nota1 = float(input('ingrese el valos de la 1° nota:'))
nota2 = float(input('ingrese el valos de la 2° nota:'))
nota3 = float(input('ingrese el valos de la 3° nota:'))

n1 = 0.15
n2 = 0.35
n3 = 0.5

nota_media = float((nota1 + nota2 + nota3) / 3)
print('el valor de la nota media: ', nota_media)

print('el valos de la 1° nota: ', (nota_media * n1))
print('el valos de la 2° nota: ', (nota_media * n2))
print('el valos de la 3° nota: ', (nota_media * n3)) """

#-------------------------------------------------------------------------------------
""" matriz = [[1,5,1], [2,1,2], [3,0,1], [1,4,4]]

print('La matriz es: ', matriz)

nueva_matriz = []

nueva_matriz.append(matriz[0])
nueva_matriz[0].append(sum(matriz[0]))
nueva_matriz.append(matriz[1])
nueva_matriz[1].append(sum(matriz[1]))
nueva_matriz.append(matriz[2])
nueva_matriz[2].append(sum(matriz[2]))
nueva_matriz.append(matriz[3])
nueva_matriz[3].append(sum(matriz[3]))
print(nueva_matriz) """

#------------------------------------------------------------------

""" num_lot = []

for num in range(0,6,1):
    num_lot.append(int(input('Ingrese los numeros ganadores de la loteria: ')))
print('Gracias por ingresar sus numeros')

print(num_lot)
num_lot.sort()
print(num_lot)
 """
#----------------------------------------------------

""" lista = []

for num in range(0,10):
    lista.append(num+1)
    print(lista)
print(lista)
lista.reverse()
print(lista)
print(type(lista)) """

#-----------------------------------------------

""" materias = ['matematica','lengua', 'biologia', 'geografia', 'fisica', 'historia']
aprob = 6
rendir = []
fin = len(materias)
for mater in range(0,fin):
    print(fin)
    nota = int(input(f'Ingrese la nota de {materias[mater]}:'))
    if nota >= aprob :
        print(f'La materia {materias[mater]} fue aprobada')
    elif nota < aprob:
        print(f'La materia {materias[mater]} NO fue aprobada')
        rendir.append(materias[mater])

print('Tenes que rendir las siguientes materias: ')

for mat in rendir:
    print(f'La materia {mat}')
 """
#------------------------------------------------------

""" abcd = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

aux = []
for letra in range(0, len(abcd)):
    if letra % 3 == 0:
        print(abcd[letra])
    else:
        aux.append(abcd[letra])
print(aux) """

#-------------------------------------------------------

""" palabra = input('Ingrese una palabra: ')

if palabra == palabra[::-1]:
  print("La palabra es un palíndromo")
else:
  print("La palabra no es un palíndromo") """

#-------------------------------------------------

""" palabra = input('Ingrese una palabra: ')

print('Cantidad de a: ', palabra.count('a'))
print('Cantidad de e: ', palabra.count('e'))
print('Cantidad de i: ', palabra.count('i'))
print('Cantidad de o: ', palabra.count('o'))
print('Cantidad de u: ', palabra.count('u')) """

#---------------------------------------------------

""" precios = [50, 75, 46, 22, 80, 65, 8]
precios.sort()
print(precios[0])
precios.sort(reverse=True)
print(precios[0]) """

#------------------------------------

""" vec1 = [1,2,3]
vec2 = [-1,0,2]

prod_esc = (vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2])

print(prod_esc) """

#-----------------------------------------------

