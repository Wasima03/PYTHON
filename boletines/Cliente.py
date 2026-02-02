class Cliente:
    def __init__(self,nombre,apellido,dni):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
    def __getNombre(self):
        return self.__nombre
    def __getApellido(self):
        return self.__apellido
    def __getDni(self):
        return self.__dni
    def mostrarCliente(self):
        cliente=f"""{self.__getDni()} - {self.__apellido} , {self.__getNombre()}"""
        print(cliente)
