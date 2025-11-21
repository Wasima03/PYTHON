"""
class Perro:

    def __init__(self,secreto,secretisimo,nombre="Booby"): #valor del parámetro por defecto
        self.nombre=nombre
        self._secreto=secreto
        self.__secretisimo=secretisimo

    def llamar(self):
        return ("Ey "+ self.nombre+" ven aquí")

mascota2 = Perro("Cuchi cuchi","cariñito mio","Sultán")
print(mascota2.llamar())
mascota2._secreto="Engendro del demonio"
print(mascota2._secreto)
mascota2._Perro__secretisimo="Rata azmiclera"
print(mascota2._Perro__secretisimo)
"""
class Perro:
    numPerros=0
    def __init__(self, nombre="Bobby"):
        self.nombre=nombre
        Perro.numPerros+=1

    def llamar(self):
        return ("Ey " + self.nombre + " ven aquí")

    @classmethod
    def cuantosPerros(cls):
        return (cls.numPerros) #no se puede acceder a atributos de instancia(perro) solo de clase son cls

    @staticmethod
    def ladrar():
        return "Guau"

    def sobrecargargada(self,atributo):
        if isinstance(atributo,int):
            print("Estoy trabjando con un entero")
        elif isinstance(atributo,float):
            print("Estoy trabjando con un float")
        elif isinstance(atributo, str):
            print("Estoy trabjando con un string")
        elif isinstance(atributo, list):
            print("Estoy trabjando con una lista")
        else:
            print("Estoy trabjando con otra cosa")

    def sobrecargargada2(self, *atributo):
        if(len(atributo)==1):
            print("Recibo un parámetro")
        elif(len(atributo)==2):
            print("Recibo dos parámetros")
        else:
            print("Recibo tres o más parámetros")




mascota2=Perro()
mascota1= Perro("Sult")
mascota3 = Perro("Tobby")

print(Perro.cuantosPerros())
print(Perro.ladrar())
Perro.numPerros=10
print(mascota2.numPerros)
mascota3.sobrecargargada("Hola")
mascota3.sobrecargargada([1,2,3])
mascota3.sobrecargargada2(1,"hola")