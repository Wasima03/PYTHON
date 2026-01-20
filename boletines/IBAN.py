class Iban:
    def __init__(self,codigo):
        self.__pais=codigo[:2]
        self.__dc:codigo[2:4]
        self.__entidad:codigo[4:8]
        self.__sucursal:codigo[8:12]
        self.__numCuenta:codigo[13:]

    def __getPais(self):
        return self.__pais
    def __getDc(self):
        return self.__getDc()
    def __getEntidad(self):
        return self.__getEntidad()
    def __getSucursal(self):
        return self.__getSucursal()
    def __getNumCuenta(self):
        return self.__getNumCuenta()
    def __mostrar(self):
        cod= f"""
            Pais: {self.__getPais()}
            DC: {self.__getDc()}
            Entidad: {self.__getEntidad()}
            Sucursal: {self.__getSucursal()}
            Número de cuenta: {self.__getNumCuenta()}
        """
        print(cod)

