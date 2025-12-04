class Manga:
    listaGeneros={"shonen", "shojo", "seinen", "josei","kodomo", "yuri", "spokon", "isekai", "henta"}
    numeros=list()
    def __init__(self,autor,titJap,genero,numero,titEsp=None):
        self.__autor=autor
        self.__titJap=titJap
        self.__titEsp=titEsp
        self.__ultimoNumero=numero

        if genero in self.listaGeneros:
            self.__genero=genero
        else:
            self.__genero="Shonen"

        self.__numeros=()

    #GETTERS
    def getAutor(self):
        return self.__autor
    def getTitJap(self):
        return self.__titJap
    def getTitEsp(self):
        return self.__titEsp
    def getNumero(self):
        return self.numeros
    def getGenero(self):
        return self.__genero

    #SETTERS
    def setTitEsp(self,titulo):
        if(self.__titEsp==None):
            self.__titEsp=titulo

    def setNumeros(self,*num):
        for n in num:
            self.__numeros=self.numeros.append(n)
            self.numeros.sort()

    def completarColeccion(self):
        nums=list()
        for i in range (1,self.__ultimoNumero+1):
            if i not in self.numeros:
                nums.append(i)
        return nums

    def eliminarNumero(self,num):
        esta=False
        for i in self.numeros:
            if i==num:
                self.numeros.remove(num)
                esta=True
        if(esta):
            print("Numero eliminado de la coleccion")
        else:
            print("No se ha encontrado el número a eliminar")


m=Manga("e","d","cw",10)
m.setNumeros(1,2,3)
print(m.completarColeccion())
print(m.getNumero())
print(m.getTitJap())
print(m.getTitEsp())
m.setTitEsp("f")
print(m.getTitEsp())
m.eliminarNumero(6)
m.eliminarNumero(1)

