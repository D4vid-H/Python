
""" i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) """

""" n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
    print('n vale' , n) """

""" n = 0
while n < 10:
    n += 1
    if n == 2:
        pass
        print('n vale' , n) """

#-------------------------------------------------------

""" texto = 'Hola Mundo, estoy usando for en Python'
#for letra in texto:
#    print(letra)

texto2 = ''
for letra in texto:
    texto2 = letra * 2
print(texto2) """

#-------------------------------------------------------

""" edad = int(input('Ingrese su edad: '))

if edad >= 18:
  print('Es mayor de edad')
else:
  print('Es menor de edad') """

#-------------------------------------------------------

""" clave = input('Ingrese una contraseña: ')

confirmar = input('Confirmar contraseña: ')

if clave.lower() == confirmar.lower():
  print('Ingreso correcto de contraseña')
else:
  print('La contraseña no coincide') """

#-------------------------------------------------------

""" divid = int(input('Ingrese un numero a dividir: '))
divis = int(input('Ingrese un numero como divisor: '))

if divis == 0:
  print('Error: El divisor no puede ser 0')
else:
  print('El resultado es:', divid/divis)
 """
#-------------------------------------------------------

""" num = int(input('Ingrese un numero: '))

if num == 0:
  print('El numero es cero')
elif num % 2 == 0:
  print('El numero es par')
else:
  print('El numero es impar') """

#-------------------------------------------------------

""" edad = int(input('Ingrese su edad: '))

ingresos = float(input('Ingrese sus ingresos: '))

if edad >= 16:
  if ingresos >= 1000:
    print('Ud. Debe Tributar')
  else:
    print('No debe tributar porque no supera los ingresos')
else:
  print('No cumple con la edad')
 """
#-------------------------------------------------------

""" nombre = input('Ingrese su nombre: ')
sexo = int(input('Ingrese su opcion: 1-Mujer  2-Varon'))

if sexo == 1:
  if nombre < 'M':
    print('Ud esta en el grupo A')
  elif nombre > 'M':
    print('Ud esta en el grupo B')
elif sexo == 2:
  if nombre > 'N':
    print('Ud esta en el grupo A')
  elif nombre < 'N':
    print('Ud esta en el grupo B') """

#-------------------------------------------------------

arr = [1,3,5,7,9]

def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0
    leng = len(arr)
    for i,j in enumerate(arr):
        if (i == (leng - 1)):
          min += j
        
        print(f'la i es: {i}, la j es: {j}')
    
miniMaxSum(arr)
#-------------------------------------------------------


#-------------------------------------------------------



#-------------------------------------------------------


#-------------------------------------------------------



#-------------------------------------------------------


#-------------------------------------------------------

