from abc import ABCMeta, abstractmethod

class Conductor():
    def __init__(self,nombre,nif,anyoNacimiento,anyoCarnet,puntosCarnet):
        self.__nombre = nombre
        self.__nif = nif
        self.__anyoNacimiento = anyoNacimiento
        self.__anyoCarnet = anyoCarnet
        self.__puntosCarnet = puntosCarnet
        self.__anyoActual=2025
    def getNombre(self):
        return self.__nombre
    def getNif(self):
        return self.__nif
    def getEdad(self):
        return self.__anyoActual - self.__anyoNacimiento
    def getAnyosCarnet(self):
        return self.__anyoActual - self.__anyoCarnet
    def getPuntosCarnet(self):
        return self.__puntosCarnet

class Vehiculo(metaclass=ABCMeta):
    def __init__(self,matricula,anyoVenta):
        self.__matricula = matricula
        self.__anyoVenta = anyoVenta
        self.__anyoActual=2025

    def getMatricula(self):
        return self.__matricula
    def getAnyoVenta(self):
        return self.__anyoVenta
    def getAntiguedad(self):
        return self.__anyoActual-self.__anyoVenta
    def getAnyoActual(self):
        return self.__anyoActual
    @abstractmethod
    def getSeguroTodoRiesgo(self):
        pass
    @abstractmethod
    def getSeguroTerceros(self):
        pass
    @abstractmethod
    def getVehiculo(self):
        pass

class Moto(Vehiculo):
    def __init__(self,matricula,anyoVenta,conductor):
        super().__init__(matricula,anyoVenta)
        self.__conductor = conductor

    def getSeguroTodoRiesgo(self):
        print("Precio del seguro a todo riesgo: No se hacen seguros a todo riesgo de motos")


    def getSeguroTerceros(self):
        precio=200
        if self.__conductor.getPuntosCarnet()<8:
            precio=precio+150
        if self.__conductor.getEdad() <24:
            precio=precio+24
        if self.__conductor.getAnyosCarnet()<2:
            precio=precio+50
        print( "Precio del seguro a terceros: "+str(precio)+"€")
    def getConductor(self):
        conductor= f"""
Conductor: {self.__conductor.getNombre()}. Edad: {self.__conductor.getEdad()}. Años de carnet: {self.__conductor.getAnyosCarnet}. Puntos: {self.__conductor.getPuntosCarnet()}"""
        print(conductor)
    def getVehiculo(self):
        vehiculo= f"""
Vehiculo: moto. Matrícula: {self.getMatricula()}. Año de compra: {self.getAnyoVenta()}"""
        print(vehiculo)



class Coche(Vehiculo):
    def __init__(self,matricula,anyoVenta,conductor):
        super().__init__(matricula,anyoVenta)
        self.__conductor = conductor

    def getSeguroTodoRiesgo(self):
        precio = 0
        if self.getAnyoVenta() == self.getAnyoActual():
            precio = precio + 400
        elif self.getAnyoVenta() == self.getAnyoActual()+1:
            precio = precio + 500
        elif self.getAnyoVenta() == self.getAnyoActual()+2:
            precio = precio + 700
        elif self.getAnyoVenta() > 3:
            precio = self.getAntiguedad() * 250

        if self.__conductor.getPuntosCarnet() < 8:
            precio = precio + 100
        print( "Precio del seguro a todo riesgo:" +str(precio)+"€")

    def getSeguroTerceros(self):
        precio=250
        if self.__conductor.getPuntosCarnet()<8:
            precio=precio+100
        if self.__conductor.getEdad() <24:
            precio=precio+50
        if self.__conductor.getAnyosCarnet()<2:
            precio=precio+75
        print("Precio del seguro a terceros: "+str(precio)+"€")
    def getConductor(self):
        conductor= f"""
Conductor: {self.__conductor.getNombre()}. Edad: {self.__conductor.getEdad()}. Años de carnet: {self.__conductor.getAnyosCarnet}. Puntos: {self.__conductor.getPuntosCarnet()}"""
        print(conductor)
    def getVehiculo(self):
        vehiculo= f"""
Vehiculo: coche. Matrícula: {self.getMatricula()}. Año de compra: {self.getAnyoVenta()}"""
        print(vehiculo)



