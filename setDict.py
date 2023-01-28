""" uno = {1,2,3,4,5,6}
print(type(uno))
print(uno)

dos= set()
print(type(dos))

tres = set(['uno', 'dos', 'tres'])
print(type(tres))
print(tres)

uno.add(7)
print(uno)

print(3 in uno)

primer = uno.pop()
print(primer)

dos.update({1, 'dos', 3})
print(dos)

tres.discard('cuatro')
print(tres)

uno.remove(2)
print(uno) """

#-------------------------------------------------------------

""" colores = {'Rojo', 'Blanco', 'Azul'}

colores.update(['Violeta', 'Dorado'])

print(colores)

colores.discard('Celeste')
colores.discard('Blanco')
colores.discard('Dorado')

print(colores) """

#---------------------------------------------------------------

""" copa_mundiales = {'Alemania': 1990, 'Brasil': 1994, 'Francia': 1998, 'Brasil': 2002, 'Italia': 2006, 'España': 2010, 'Alemania': 2014, 'Francia': 2018, 'Argentina': 2022}

print(copa_mundiales) """

#-----------------------------------------------

paises = set(['Inglaterra', 'USA', 'Mexico'])
print(paises)
paises.update(['Islandia', 'Italia', 'Argentina', 'Portugal', 'USA'])
print(paises)
x = paises.discard('Chile')
y = paises.discard('Italia')

print(y)

#----------------------------------------------------------------------

""" user = {'nombre': 0, 'edad': 0, 'direccion': 0}

user['nombre'] = (input('Ingrese su nombre: '))
user['edad'] = (input('Ingrese su edad: '))
user['direccion'] = (input('Ingrese su direccion: '))

print(user['edad'])
print('Mi nombre es',{user['nombre']} 'tengo ',{user['edad']} 'años, y vivo en ',{user['direccion']}) """