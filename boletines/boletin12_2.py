from abc import abstractmethod, ABC
from abc import ABCMeta

class NotaBase(metaclass=ABCMeta):
    colores = {"amarillo", "verde", "blanco", "cyan"}
    def __init__(self,titulo, descripcion, color, fecha):
        self._titulo = titulo
        self._descripcion = descripcion
        if color not in self.colores:
            self._color="amarillo"
        else:
            self._color = color
        self._fecha = fecha

    @abstractmethod
    def listarNotas(self):
        pass

class gestionNotas():
    listaNormal=[]
    listaUrgente=[]
    listaGlobal=[]
    def __init__(self):

        pass
    def crearNota(self,titulo, descripcion, color, fecha):
        colores = {"amarillo","verde","blanco","cyan"}
        nota=""
        if color== "rojo":
            nota=notaUrgente(titulo,descripcion,fecha)
            self.listaUrgente.append(nota)
        else:
            nota = NotaNormal(titulo,descripcion,color,fecha)
            self.listaNormal.append(nota)
        self.listaGlobal.append(nota)
        print("Nota creada")

    def listarNotas(self):
        for i in self.listaUrgente:
            i.listarNotas()
        for j in self.listaNormal:
            j.listarNotas()

    def eliminarNota(self,titulo):
        esta=False
        for i in self.listaGlobal:
            if i.getTitulo()==titulo:
                self.listaGlobal.remove(i)
                if i.getColor()=="rojo":
                    self.listaUrgente.remove(i)
                else:
                    self.listaNormal.remove(i)
                esta=True
        if(esta):
            print("Nota eliminada")
        else:
            print("Nota no encontrada")



class NotaNormal(NotaBase):
    def __init__(self,titulo,descripcion,color,fecha):
        super().__init__(titulo, descripcion, color, fecha)

    def getTitulo(self):
        return self._titulo

    def getDescripcion(self):
        return self._descripcion

    def getColor(self):
        return self._color

    def getFecha(self):
        return self._fecha
    def listarNotas(self):
        nota = f"""
                    Informe Nota
                    ==========================
                    Título: {self._titulo}
                    Descripción: {self._descripcion}
                    Color: {self._color}
                    Fecha: {self._fecha}
                    ==========================
                    """
        print(nota)

class notaUrgente(NotaBase):
    def __init__(self,titulo,descripcion,fecha):
        super().__init__(titulo,descripcion,"rojo",fecha)

    def getTitulo(self):
        return self._titulo

    def getDescripcion(self):
        return self._descripcion

    def getColor(self):
        return self._color

    def getFecha(self):
        return self._fecha

    def listarNotas(self):
        nota = f"""
                    Informe Nota *URGENTE*
                    ==========================
                    Título: {self._titulo}
                    Descripción: {self._descripcion}
                    Color: {self._color}
                    Fecha: {self._fecha}
                    ==========================
            """
        print(nota)

l=[]
g=gestionNotas()
g.crearNota("Interfaces","Notable","cyan","10-12-2025")
g.crearNota("Acceso a Datos","Notable","vg","15-12-2025")
g.crearNota("Python","Notable","rojo","15-12-2025")
g.listarNotas()
g.eliminarNota("Interfaces")
g.listarNotas()