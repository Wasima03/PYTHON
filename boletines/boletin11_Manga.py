class Manga:
    listaGeneros={"shonen", "shojo", "seinen", "josei","kodomo", "yuri", "spokon", "isekai", "henta"}
    def __init__(self,autor,titJap,genero,numero,titEsp=None):
        self.__autor=autor
        self.__titJap=titJap
        self.__titEsp=titEsp
        self.__numero=numero

        if genero in self.listaGeneros:
            self.__genero=genero
        else:
            self.__genero="Shonen"

        self.__numeros=()

    #GETTERS
    def getAutor(self):
        return (self.__autor)
    def getTitJap(self):
        return (self.__titJap)
    def getTitEsp(self):
        return (self.__titEsp)
    def getNumero(self):
        return (self.__numero)
    def getGenero(self):
        return (self.__genero)

    #SETTERS
    def setTitEsp(self,titulo):
        if(self.__titEsp==None):
            self.__titEsp=titulo
    def setNumeros(self,*numeros):
        for numero in numeros:
            self.__numeros=self.__numeros+numero

m=Manga("e","d","cw",10)
m.setNumeros(1,2,3)