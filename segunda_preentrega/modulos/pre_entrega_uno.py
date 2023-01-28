from pre_entrega_dos import client
import json

# Funcion que crea nuevos usuarios.
def signup():
    try:
        newuser = {"user": None, "email": None, "password": None, "delivery": None}
        newuser['email'] = input('Ingrese su correo electronico: ')
        newuser['user'] = input('Ingrese un nombre de usuario: ')    
        while not valid_user(newuser['user']):
            newuser['user'] = input('Ingrese un nombre de usuario distinto: ')
        else:
            pass
        newuser['delivery'] = input('Ingrese un direccion: ')
        newuser['password'] = input('Ingrese un contraseña: ')
        re_password = input('Verificacion de contraseña: ')
        while newuser['password'] != re_password:
            newuser['password'] = input('Ingrese un contraseña: ')
            re_password = input('Verificacion de contraseña: ')
        else:
            global clt
            clt = client(newuser['user'], newuser['email'], newuser['password'], newuser['delivery'])
            newuser['id'] = clt.get_id()
            writeUser(newuser)
    except Exception as error:
        print(f'problema en la carga de usuario: {error}')
    return newuser

# Funcion que realiza el login de usuario por nombre de usuario.
def signin():
    try:
        user = input('Ingrese su usuario: ')
        while valid_user(user):
            print('Usuario no registrado')
            user = input('Ingrese su usuario: ')
        else:
            password = input('Ingrese su contraseña: ')
            while valid_pass(password):
                print('Contraseña incorrecta')
                password = input('Ingrese su contraseña: ')
    except Exception as error:
        print(f'problema en el logueo de usuario: {error}')
    return searchUser(user)

# Funcion para validar que no existe en nombre de usuario al crear un nuevo registro de usuario.
def valid_user(user):
    try:
        data = readFile()
        for use in (data['prueba']):
            if use['user'] == user:
                return False            
    except Exception as error:
        print('Problemas en el validador de usuario: ', error)
    return True 

# Funcion para validar la password cuando el usuario se loguea.
def valid_pass(password):
    try:
        data = readFile()        
        for use in data['prueba']:            
            if use['password'] == password:
                return False            
    except Exception as error:
        print('Problemas en el validador de usuario', error)
    return True 


# Funcion que realiza la busqueda del usuario dentro del diccionario.
def searchUser(user):
    try:
        data = readFile()
        for users in data['prueba']:
            if users['user'] == user:
                return users
    except Exception as error:
        print('\n problemas en buscar usuario', error) 



# Funcion de lectura de archivo.
def readFile():
    try:
        ruta = 'c:\Development\Python\Clase\segunda_preentrega\modulos'
        with open(ruta + '\prueba.json', 'r') as file:            
            leer = json.load(file)       
        return (leer) 
    except Exception as error:
        print('\n problemas de lectura', error)

# Funcion de esctritura de archivo.
def writeUser(user):
    try:
        ruta = 'c:\Development\Python\Clase\segunda_preentrega\modulos'
        data = readFile()
        data['prueba'].append(user)     
        with open(ruta + '\prueba.json', 'w') as file:
            json.dump(data, file, indent=4) 
    except Exception as error:
        print('problema en escritura', error)
    else:
        print('Se guardo el usuario')

# Funcion de saludo al usuario.
def wellcome(user):
    name = user['user']
    print(f'Hola {name}, ya estas logueado.')


# Funcion principal de login o creacion de usuario.
def start():
    try:
        print('Bienvenidos \n Seleccione una acceder si tiene cuenta o crear cuenta si no tienes una.')
        select = int(input('Seleccione una opcion: \n 1_Ingresar cuenta \n 2_Crear cuenta: '))
        if select == 1:
            wellcome(signin())
        elif select == 2:
            signup()
            print(clt.__str__())
        else:    
            print('¡Ingreso una opcion incorrecta!')
            start()
    except Exception as error:
        print('Problema en la app, se genero el siguiente error: \n', error)

#start()