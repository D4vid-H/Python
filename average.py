print("Bienvenido a la app de puntos de campeonato de 20 partidos")
ganados  = int(input("Ingresar partidos ganados del eqipo: "))
empatados = int(input("Ingresar partidos ganados del eqipo: "))
perdidos = int(input("Ingresar partidos ganados del eqipo: "))

cantidad = ganados + empatados + perdidos

if cantidad == 20:
    puntos = ganados * 3 + empatados * 1 
    print("Los puntos del equipos son: ", puntos)

else :
    print("Cantidad de partidos incorrecto")