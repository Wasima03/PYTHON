class Empleado:
    def __init__(self,linea):
        datos=linea.split(";")
        nombreApellido=datos[0]
        self.__puesto=datos[1]
        self.__sueldo=datos[2]
        self.__edad=datos[3]

        nombreApellido=nombreApellido.split(",")
        self.__nombre=nombreApellido[0]
        self.__apellido=nombreApellido[1]

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getPuesto(self):
        return self.__puesto
    def getEdad(self):
        return  self.__edad
    def edadRestante(self):
        return 67-int(self.__edad)
    def getSalario(self):
        return round(float(self.__sueldo )* 14,2)
    def mostrar(self):
        cadena=f"""
        Empleado: {self.getNombre()} {self.getApellido()}
        Cargo: {self.__puesto}
        Años hasta su jubilación: {self.edadRestante()}
        Salario neto anual: {self.getSalario()}
        """
        return cadena
