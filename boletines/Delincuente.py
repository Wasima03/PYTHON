class Delincuente:
    __delitos=[]
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
        self.__delitos=[]
    def getNombre(self):
        return self.__nombre
    def __getEdad(self):
        return self.__edad
    def añadir_delito(self, delito):
        self.__delitos.append(delito)
    def mostrarExpediente(self):
        print("Edad:" ,self.__getEdad())
        print("Antecedentes penales:")
        for d in self.__delitos:
            print(d)