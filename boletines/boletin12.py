
class gestionNotas():
    def __init__(self,lista):
        self.__lista=lista
        pass
    def crearNota(self,titulo, descripcion, color, fecha):
        colores = {"amarillo","verde","blanco","cyan"}
        if len(set(color) & colores) == 1:
            c=color
        else:
            c="amarillo"
        nota= Notas(titulo,descripcion,color, fecha)
        self.__lista.append(nota)
        print("Nota creada")

    def listarNota(self):
        for i in self.__lista:
            nota = f"""
                    Informe Nota
                    ==========================
                    Título: {i.getTitulo()}
                    Descripción: {i.getDescripcion()}
                    Color: {i.getColor()}
                    Fecha: {i.getFecha()}
                    ==========================
                    """
            print(nota)


    def eliminarNota(self,titulo):
        esta=False
        for i in self.__lista:
            if i.getTitulo()==titulo:
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




l=[]
g=gestionNotas(l)
g.crearNota("Interfaces","Notable","10-12-2025","21-12-12")
g.crearNota("Acceso a Datos","Notable","vg","15-12-2025")
g.listarNota()
g.eliminarNota("Interfaces")
g.listarNota()




#g=gestionNotas(l).listarNota()