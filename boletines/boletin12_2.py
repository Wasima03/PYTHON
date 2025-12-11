from abc import abstractmethod
from abc import ABCMeta
class gestionNotas(metaclass=ABCMeta):
    def _init__(self,lista):
        self.__lista=lista
        pass
    def crearNota(self,titulo, descripcion, color, fecha):
        colores = {"amarillo","verde","blanco","cyan"}
        nota=""
        if len(set(color) & colores) == 1:
            c=color
        else:
            c="amarillo"
        if c== "rojo":
            nota=notaUrgente(titulo,descripcion,fecha)
        else:
            nota = Notas(titulo,descripcion,c,fecha)
        self.__lista.append(nota)
        print("Nota creada")


    @abstractmethod
    def listarNota(self):
        for i in self.__lista:
            i.listarNota


    def eliminarNota(self,titulo):
        esta=False
        for i in self.__lista:
            if i.getTitulo==titulo:
                self.__lista.remove(i)
                esta=True
        if(esta):
            print("Nota eliminada")
        else:
            print("Nota no encontrada")



class Notas(gestionNotas):
    def __init__(self,titulo,descripcion,color,fecha):
        self.__titulo=titulo
        self.__descripcion=descripcion
        self.__color=color
        self.__fecha=fecha

    def getTitulo(self):
        return self.__titulo

    def getDescripcion(self):
        return self.__descripcion

    def getColor(self):
        return self.__color

    def getFecha(self):
        return self.__fecha
    def listarNota(self):
        nota = f"""
                    Informe Nota
                    ==========================
                    Título: {self.__titulo}
                    Descripción: {self.__descripcion}
                    Color: {self.__color}
                    Fecha: {self.__fecha}
                    ==========================
                    """
        print(nota)

class notaUrgente(gestionNotas):
    def __init__(self,titulo,descripcion,fecha):
        self.__titulo=titulo
        self.__descripcion=descripcion
        self.__color="rojo"
        self.__fecha=fecha

    def getTitulo(self):
        return self.__titulo

    def getDescripcion(self):
        return self.__descripcion

    def getColor(self):
        return self.__color

    def getFecha(self):
        return self.__fecha

    @abstractmethod
    def listarNota(self):
        nota = f"""
            Informe Nota *URGENTE*
            ==========================
            Título: {self.__titulo}
            Descripción: {self.__descripcion}
            Color: {self.__color}
            Fecha: {self.__fecha}
            ==========================
            """
        print(nota)

l=[]
g=gestionNotas(l)
g.crearNota("Interfaces","Notable","10-12-2025")
"""g.crearNota("Acceso a Datos","Notable","vg","15-12-2025")
g.listarNota()
g.eliminarNota("Interfaces")
g.listarNota()"""