import pickle
#pickle.load---deserializa un texto binario a objeto otra vez
#pickle.dump ---- serializa objeto a texto binario
#ab-----escribe en fichero pero no borra append

def Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def ver(self):
        print(self.nombre+"("+str(self.edad)+")")

p1 = Persona("Pepe",45)
p2 = Persona("Ana",52)
lista=[p1,p2]

#p1.ver()

try:
    fichero=open("personas.bin","wb")
    pickle.dump(lista,fichero)
    fichero.close()
    p1 = Persona("Pepe", 45)

    fichero=open("personas.bin","rb")
    lista=pickle.load(fichero)
    for elemento in lista:
        elemento.ver()
    fichero.close()

except:
    print("Error.")