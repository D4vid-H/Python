""" nacio = int(input('ingrese su año de nacimiento: '))

if nacio < 1920:
    print('No existe generacion asociada')
elif 1940 >= nacio >= 1920:
    print('Generacion Silenciosa')
elif 1964 >= nacio >= 1946:
    print('Generacion Baby Boomer')
elif 1979 >= nacio >= 1965:
    print('Generacion X')
elif 2000 >= nacio >= 1980:
    print('Generacion Y')
elif nacio >= 2001:
    print('Generacion Z') """

#-------------------------------------------------

""" edad = int(input('Ingrese su edad: '))
antiguedad = float(input('ingrese la antiguedad en S.F.: '))
salario = float(input('ingrese su salario: '))


if edad > 18:
    if antiguedad >= 3 and salario > 2500:
        print('Prestamo Aprobado')
    elif salario > 4000:
        print('Prestamo Aprobado')
    else:
        print('Prestamo Desaprobado')
else :
    print('Ud es menor de 18 años') 
 """
#--------------------------------------------------------------------

""" nombre = input("¿Cómo te llamas? ")

genero = input("¿Cuál es tu preferencia (M o C)? ")

if genero == "M":
   if nombre < "m":
       print('grupo = "A"')
   else:
       print('grupo = "B"')
elif genero == "C":
   if nombre > "n":
      print('grupo = "A"')
   else:
       print('grupo = "B"') """

#----------------------------------------------------------------------

""" contra = 'A123456'

user_pass = input('Ingrese su contraseña: ')

if contra.lower() == user_pass.lower():
    print('las contraseñas coinciden')
else:
    print('las contraseñas no coinciden')
 """
#--------------------------------------------------------------

""" r_a = int(input('Ingrse su renta anual: '))

if r_a < 10000:
    print('El tipo Impositivo es 5%')
elif 10000 < r_a < 20000:
    print('El tipo Impositivo es 15%')
elif 20000 < r_a < 35000:
    print('El tipo Impositivo es 20%')
elif 35000 < r_a < 60000:
    print('El tipo Impositivo es 30%')
elif 60000 < r_a :
    print('El tipo Impositivo es 45%') """

#-----------------------------------------------------------

""" vegi = ('Pimiento','Tofu')

novegi = ('Pepperoni', 'Jamon', 'Salmon')

print('Menu:  Vegetariano -1-  No Vegetariano -2-')
elec = int(input('Ingrese que tipo de Menu desea: '))

if elec == 1:
    print('La Pizza elegida es Vegetarian y contiene: *Pimiento, *Tofu y *Salsa de Tomate')
elif elec == 2:
    print('Eleccin de Pizza: 1- Pepperoni 2- Jamon 3- Salmon')
    ing = int(input('Ingrese su eleccin: '))
    if ing == 1:
        print('La Pizza elegida es No Vegetarian y contiene: *Salsa de Tomate, *Muzzarela y *Pepperoni')
    elif ing == 2:
         print('La Pizza elegida es No Vegetarian y contiene: *Salsa de Tomate, *Muzzarela y *Jamon')
    else:
         print('La Pizza elegida es No Vegetarian y contiene: *Salsa de Tomate, *Muzzarela y *Salmon')
else:
     print('La seleccion no es correcta')
 """

#-----------------------------------------------------------

""" cobro = ('Free', '$5', '$10')

print('Wellcome to VicioCity')

edad = int(input('Ingrese su edad: '))

if edad < 4 :
    print('Se le debe cobrar: ', cobro[0])
elif  4 <= edad <= 18:
    print('Se le debe cobrar: ', cobro[1])
else:
    print('Se le debe cobrar: ', cobro[2]) """

#-----------------------------------------------------------
""" 
tarifa = 800

mes = 22

nominal = tarifa * mes

h_extra = 1.35 * (tarifa/8)

impuestos = 0.2

trabajo = int(input('Ingrese la cantidad de horas trabajadas: '))

if trabajo <= (mes * 8) :
    if nominal > 20000:
        cobrar = (nominal - (nominal * impuestos))
        print('Ud debe cobrar con impuestos: $', cobrar)
    else:
        print('Ud debe cobrar: $', nominal)
elif trabajo > (mes * 8) :
    print('Ud tiene horas extras: ', (trabajo % (mes*8)))
    dif_h = (trabajo % (mes*8)) * h_extra
    cobrar = dif_h + nominal
    if cobrar < 20000:
        print('Ud debe cobrar: $', cobrar)
    else:
        print('Ud debe cobrar con impuestos: $', cobrar - (cobrar*impuestos))
else: 
    print('Chau!!') """

#----------------------------------------------------------------
