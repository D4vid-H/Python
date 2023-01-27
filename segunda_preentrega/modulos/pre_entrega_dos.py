import random
from datetime import datetime

class persona:

    def __init__(self):
        self.__name = None
        self.__last_name = None
        self.__age = None

    def __str__(self):
        print(f'Me presento, soy {self.__name}, {self.__last_name} y tengo {self.__age} años.')    

    #Se generan metodos get PUBLICOS, para leer los atributos.
    def get_name(self):
        return self.__name
    def get_last_name(self):
        return self.__last_name
    def get_age(self):
        return self.__age

    #Se generan metodos set PUBLICOS, para modificar los atributos.
    def set_name(self, name):
        self.__name = name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def set_age(self, age):
        self.__age = age 

class cliente(persona):

    def __init__(self, user, email, password, delivery):
        self.__user = user
        self.__email = email
        self.__password = password
        #self.__timestamp = datetime.now()
        self.__delivery = delivery
    
    def __str__(self):
       return f'Cliente {self.__user}, email {self.__email}.'
    
    #Se generan metodos get PUBLICOS, para leer los atributos.
    def get_user(self):
        return self.__user
    def get_email(self):
        return self.__email
    def __get_passwordl(self):
        return self.__password
    def get_times(self):
        return self.__timestamp
    def get_delivery(self):
        return self.__delivery

    #Se generan metodos set PUBLICOS, para modificar los atributos.
    def set_user(self, user):
        self.__user = user
    def set_email(self, email):
        self.__email = email
    def set_password(self, password):
        self.__password = password
    def get_delivery(self, delivery):
        self.__delivery = delivery

    