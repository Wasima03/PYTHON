"""class ClaseA:
    def __init__(self):
        self.nombre= "Clase A"

     #funcion normal de getter
    def nombre(self):
        return (self.nombre)

class ClaseB(ClaseA): #clase padre dentro de ()
    def __init__(self,subclase):
        super()
        self.subclase= "Clase B" #redefinir costructor


    def getNombre(self):
        return (self.nombre)

    #COMO TIENE LOS DOS SUBRAYADOS, NO SE PUEDE REDEFINIR EL CONSTRUCTOR SIN PONER EL PROPERTY Y EL GETTER



objetoA= ClaseA()
objetoB=ClaseB()
print(objetoA.nombre)
print(objetoB.nombre)
print(objetoB.getNombre())
-----------------------------------------------------------
"""




"""class ClaseA:
    def __init__(self):   #constructor
        self.nombre="Clase A"
        self.codigo=55

    def cambiarNombre(self,nuevoNombre): #existe también en la clase hija
        self.nombre=nuevoNombre



class ClaseB(ClaseA):
    def __init__(self):
        super().__init__() #invoca a la funcion de la clase padre
        self.subclase = "Clase B" #añade un nuevo atributo

    def incrementaCodigo(self): #existe en la clse hija pero no en la del padres
        self.codigo+=1


objetoa=ClaseA()
objeetob=ClaseB()
print(objetoa.nombre)
print(objeetob.nombre)
print(objeetob.subclase)
"""



#HERENCIA MÚLTIPLE

class ClaseA:
    def __init__(self):   #constructor
        self.nombre="Clase A"
        self.codigo=55

    def queSoy(self):
        print("Soy clase A")

class ClaseB():
    def __init__(self):
        self.nombre = "Clase B"

    def queSoy(self):
        print("Soy clase B")

class ClaseC(ClaseA,ClaseB):  #como ponemos la clase a primero, si hay atributos iguales, se va a coger el de la primera clase
    def queSoy(self):
        print("Y además soy clase B")
    pass
class ClaseD(ClaseB,ClaseA): #como d se pone primero, coge el nombre de la clase b
    pass

objetoa = ClaseA()
objeetob = ClaseB()
print(objetoa.nombre)
print(objeetob.nombre)
objetoc=ClaseC()
print(objetoc.nombre)
print(objetoc.codigo)
objetod=ClaseD()
print(objetod.nombre)
objetoc.queSoy()
objetod.queSoy()