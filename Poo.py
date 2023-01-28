""" class perro:
    # Constante de la clase
    especie = 'Mamifero'

    #Constructor de clase
    def __init__(self, nombre, raza):
        self.__uno = nombre
        self.dos = raza
    
    #Método especial __str__ (para definir como se muestra la clase instanciada y que no muestre la direccion de memoria)
    def __str__(self):
        return "\nNombre:" +self.__uno +",  Raza:" +self.__raza +",  Especie:" +self.especie
    

    #metodos comunes de la clase
    def get_nombre(self):
        return self.__uno, self.dos

    def set_nombre(self, nombre, raza):
        self.__uno = nombre
        self.__raza = raza """

        

#perro1 = perro('pucca', 'Rottwailer')
#print(perro1.get_nombre())
#print(perro1.raza)
#perro1.set_nombre('Tyson', 'Labrador')
#perro1.set_raza('Labrador')
#print(perro1.get_nombre())
#print(perro1._class__uno)

#------------------------------------------------------

""" class Mamifero:

    def __init__(self, CantMamas, EspVida):
        self.CantidadMamas = CantMamas
        self.EsperanzaVida = EspVida
    
    def mamar(self):
        print('Forma de alimentar a sus crias')

    def nacer(self):
        print('Nacen en el vientre materno')

class AnimalMarino:
    
    def __init__(self, TieneBranq, Especie):
        self.ConBranq = TieneBranq
        self.Especie = Especie

    def nadar(self):
        print('Foram en la que se mueven')

class Cetaceo(Mamifero, AnimalMarino):

    def __init__(self, notas, viveEn, peso):
        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso
    
    #def nacer():
    #    pass
    
    #def nadar():
    #    pass   

    def accion(self):
        print('Salto por afuera del agua')


def hacer(algo):
    algo.accion()


BallenaAzul = Cetaceo('Animal mas grande del mundo', 'Oceanos', 110000)
BallenaFrancaPigmea = Cetaceo('Misticetos mas pequeño', 'Oceano', 3000)

BallenaAzul.nacer()

BallenaFrancaPigmea.nadar()

BallenaAzul.accion()

hacer(BallenaAzul) """

#-------------------------------------------------------------------

class Alumno:
    
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f'Mi nombre es {self.nombre} y tengo una nota de {self.nota}')

