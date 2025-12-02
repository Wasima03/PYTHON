import random
from random import randint

class Pokemon:
    #lista de tipos disponibles
    lista={"Normal","Agua","Fuego","Planta","Volador","Lucha","Veneno","Eléctrico","Tierra","Roca","Psíquico","Hielo","Bicho","Fantasma","Dragón"}
    valido=False
    def __init__(self,codigo,nombre,*tipos):

        #si el codigo no está entre 1 y 151, se pone 1 por defecto
        if(1<= codigo <=151):
            self.__codigo=codigo
        else:
            self.__codigo=1

        #validación de tipos, si tiene entre 1 y 2 tipos y todos coinciden con alguno de la lista de tipos posibles son validos
        # si no, se pone por defecto el tipo Normal
        tipos=set(tipos)
        if(1<= len(tipos) <=2 and len(tipos & self.lista)==len(tipos) ):
            self.__tipos=tipos
        else:
            self.__tipos="Normal"

        self.__nombre=nombre
        self.__evolucion=None  #variable no inicializada
        self.__puntos=random.randint(50,100) #asignar puntos de vida de manera aleatoria


    def setEvolucion(self,pokemon): #asignar a un pokemon que evoluciona a otro
        self.__evolucion=pokemon

    def mostrar(self):
        print(self.__nombre)

    def getPuntos(self):
        return (self.__puntos)

    def getTipos(self):
        return (self.__tipos)

    def evoluciona(self):
        if self.__evolucion==None:
            print("Este pokemon no sabe evolucionar") #si no se ha asignado un pokemon al que evoluciona
            evo=self
        else:
            print("Sabe evolucionar")
            evo=self.__evolucion
        return evo
    #si el pokemomn no sabe evolucionar se devuelove el mismo pokemon, si sabe evolucionar devuelve una referencia al otro pokemon y el p1 se convierte en p2


    def setCombate(self,pokemon):
        while(self.__puntos>0 or pokemon.__puntos>0):
            ataque=randint(25,50)  #ataque aleatorio
            self.__puntos=self.__puntos - ataque #el ataque se resta a los puntos de vida
            print("Ataque -",ataque,"puntos")
            contraataque=randint(25,50)
            pokemon.__puntos=pokemon.__puntos-contraataque
            print("Contraataque -",contraataque,"puntos")

        if(self.__puntos<=0):
            print("Pokemon",self.__nombre,"derrotado")
        else:
            print("Pokemon",pokemon.__nombre,"derrotado")

"""p1 = Pokemon("Bulbasaur")
p2 = Pokemon("Vensasaur")
p1.setEvolucion(p2)
p1.mostrar()
p2.mostrar()
p2=p2.evoluciona()
p1= p1.evoluciona()
p1.mostrar()  #p1 ha evolucionado y se ha convertido en p2
p2.mostrar()

print(p2.getPuntos())
p2.setCombate(p1)

p3=Pokemon("Pikachu")
print(p3.getPuntos())
p3.setCombate(p1)
print(p3.getPuntos())
"""
p4 = Pokemon(1,"Pikachu","Agua","ww")
print(p4.getTipos())
p5 = Pokemon(2,"Pikachu","Agua","Fuego")
print(p5.getTipos())


