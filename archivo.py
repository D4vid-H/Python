""" ruta = 'c:\Development\Python\Clase'

f = open(ruta + '/texto.txt', 'a')

f.write(' Hello WORLD \n ')
f.close()

f = open(ruta + '/texto.txt', 'r')

leer = f.read()

print(leer)

f.close()
 """
#---------------------------------

""" ruta = 'c:\Development\Python\Clase'

f = open(ruta + '/texto.txt', 'a')

f.write(' Hello WORLD \n ')
f.close()

f = open(ruta + '/texto.txt', 'r')

leer = f.readline()

print(leer)

f.close() """

#-----------------------------------------

""" ruta = 'c:\Development\Python\Clase'

f = open(ruta + '/texto.txt', 'a')

f.write(' Hello WORLD \n ')
f.close()

f = open(ruta + '/texto.txt', 'r')

leer = f.readlines()

print(leer)

f.close() """

#--------------------------------------------
""" 
ruta = 'c:\Development\Python\Clase'

f = open(ruta + '/texto.txt', 'a')

f.write(' Hello WORLD \n ')
f.close()

f = open(ruta + '/texto.txt', 'r')

f.seek(56)

print(f.read())

f.close() """

#-------------------------------------------