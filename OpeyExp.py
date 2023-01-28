
""" expresiones = [False == True, 10 >= 2*4, 33/3 == 11, True > False, True*5 == 2.5*2]

print(expresiones) """

""" expresiones = [not False, not 3==5, 33/3 ==11 and 5>2, True or False, True*5 == 2.5 or 123>= 23, 12>7 and True<False]

print(expresiones) """

""" Nombre = input('Ingrese un nombre: ')
edad = int(input('Ingrese su edad: '))

cumple = (Nombre != '****') and ( 20 > edad > 5) and (8 >= len(Nombre) >= 4) and (edad * 3 > 35)

print(cumple) """

""" num1 = int(input('ingrese un numero: '))
num2 = int(input('ingrese un numero: '))

print('los numeros son iguales?: ', (num1 == num2))
print('los numeros son distintos?: ', (num1 != num2))
print('el numero 1 es mayor?: ', (num1 > num2))
print('el numero 2 es mayor o igual?: ', (num1 <= num2)) """

""" cadena = input('ingrese una frase: ')

valor = 10 > len(cadena) >= 3 

print(valor) """

numero_magico = 12345679
print('Numero Magico: ', numero_magico)

otro_numero = int(input('Ingrese un numero entre 1 y 9: '))

otro_numero *= 9
numero_magico *= otro_numero

print('el numero magico es: ', numero_magico)