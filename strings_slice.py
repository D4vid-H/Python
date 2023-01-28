palabra = input('Ingrese una palabra:')

letra = input('Ingrese una letra para modificar la palabra: ')
posicion = int(input('Ingrese con numero entero la posicion a cambiar: '))

print('la longitud total de la palabra es: ', len(palabra))

print('La palabra es :', palabra)


nueva_palabra = palabra[0:posicion:1] + letra + palabra[(posicion + 1):]

print('La nueva palabra es: ', nueva_palabra)

