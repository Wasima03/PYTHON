
class Tarea:
    def __init__(self,id,titulo,prioridad,realizada=False):
        self.__id = id
        self.__titulo = titulo
        if prioridad not in [1,2,3,4,5,6,7,8,9]:
            self.__prioridad=9
        else:
            self.__prioridad=prioridad
        if realizada is True or realizada is False:
            self.__realizada = realizada
        else:
            self.__realizada = False
    def getId(self):
        return self.__id
    def getTitulo(self):
        return self.__titulo
    def getPrioridad(self):
        return self.__prioridad
    def setRealizda(self,realizada):
        self.__realizada = realizada

class gestionTareas:
    def __init__(self):
        self.__diccTareas=dict()
        self.__listaTareas=list()
    def agregarTareas(self,tarea):
        aux=self.__diccTareas.get(tarea.getId)
        if aux is not None:
            print("Error:","ID",tarea.getId(),"ya existente")
        else:
            print("Tarea","'",tarea.getTitulo(),"'","(ID:",tarea.getId(),") añadida")
            self.__diccTareas[tarea.getId]=tarea.getTitulo()
            self.__listaTareas.append(tarea)
    def eliminarTareas(self,tarea):
        aux=self.__diccTareas.get(tarea.getId)
        if aux is not  None:
            print("Tarea con ID",tarea.getId(),"('",tarea.getTitulo(),"') eliminada")
            self.__diccTareas.pop(tarea.getId())
            self.__listaTareas.remove(tarea)
        else:
            print("Error: No se encontró una tarea con ID",tarea.getId())
    def marcarComoCompletada(self,id):
        aux = self.__diccTareas.get(id)
        if aux is not None:
            for clave,valor in self.__diccTareas.items():
                print("Tarea ID",id,"'",valor,"' marcada como completada")
                for i in self.__listaTareas:
                    if i.getId() == id:
                        i.setRealizada(True)
        else:
            print("Error: No se encontró una tarea con ID",id)

    def mostrarTareas(self):
        print("-LISTADO DE TAREAS:")
        if len(self.__diccTareas)==0:
            print("No hay tareas no completadas")
        else:
            for clave,valor in self.__diccTareas.items():
                for i in self.__listaTareas:
                    if i.getId() == clave and i.getRealizada()==False:
                        print("[",clave,"]",valor," (Prioridad:", i.getPrioridad,")")

    def mostrarTareasNoCompletadas(self):
        pass

g = gestionTareas()
t1=Tarea("D055","Completar retos de Duolingo",2)
t2=Tarea("P15","Aprender Python",1)
g.agregarTareas(t1)
g.agregarTareas(t2)
g.mostrarTareas()
g.mostrarTareas()
g.marcarComoCompletada("P15")
g.mostrarTareas()














