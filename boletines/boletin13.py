from abc import ABCMeta

class Persona(metaclass=ABCMeta):
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido

class Alumno(Persona):
    menorEdad=False
    def __init__(self,nombre,apellido,edad):
        super().__init__(nombre,apellido)
        self.__edad = edad
        if(edad>=18):
            self.menorEdad=False

    def getEdad(self):
        return self.__edad

class Profesor(Persona):
    departamentos ={"Informatica","Empresa","Ingles"}
    def __init__(self,nombre,apellido,departamento):
        super().__init__(nombre,apellido)
        if departamento in self.departamentos:
            self.__departamento = departamento
        else:
            self.__departamento = "Informática"

    def getDepartamento(self):
        return self.__departamento

class Modulo():
    def __init__(self,nombre,anyo,horas,optativo):
        self.__nombre = nombre
        if anyo != 1 or anyo !=2:
            self.__anyo=1
        else:
            self.__anyo=anyo
        self.__horas=horas
        if optativo ==True or optativo ==False:
            self.__optativo=False
        else:
            self.__optativo=optativo

    def getNombre(self):
        return self.__nombre
    def getAnyo(self):
        return self.__anyo
    def getHoras(self):
        return self.__horas
    def getOptativo(self):
        aux=""
        if(self.__optativo):
            aux= "Optativo"
        return aux

class Ciclo:
    grados ={"Medio","Superior"}
    def __init__(self,nombre,grado):
        self.__nombre = nombre
        if grado in self.grados:
            self.__grado = grado
        else:
            self.__grado="Medio"
        self.__modulosPrimero = []
        self.__modulosSegundo = []

    def getNombre(self):
        return self.__nombre
    def getGrado(self):
        return self.__grado
    def getModulosPrimero(self):
        return self.__modulosPrimero
    def gerModulosSegundo(self):
        return self.__modulosSegundo
    def addModulo(self,modulo):
        if modulo.getAnyo()==1:
            self.__modulosPrimero.append(modulo)
        else:
            self.__modulosSegundo.append(modulo)

class Grupo:
    listaAlumnos=[]
    tutor=None
    def __init__(self,nombre,ciclo,curso,numAlumnos):
        self.__nombre = nombre
        self.__ciclo = ciclo
        if curso!=1 or curso !=2:
            self.__curso=1
        else:
            self.__curso = curso
        self.__numAlumnos = numAlumnos

    def setAlumnos(self,alumno):
        self.listaAlumnos.append(alumno)
    def eliminarAlumno(self,alumno):
        if alumno in self.listaAlumnos:
            self.listaAlumnos.remove(alumno)
            print("Alumno eliminado")
        else:
            print("Alumno no encontrado")

    def setTutor(self,tutor):
        self.tutor=tutor

    def getTutor(self):
        return self.tutor.getNombre() + " " + self.tutor.getApellido()

    def getAlumnos(self):
        lista=""
        for i in self.listaAlumnos:
            lista+=i.getNombre()+" "+i.getApellido()+"\n"+"\t"
        return lista

    def addAlumno(self,alumno):
        self.listaAlumnos.append(alumno)
    def eliminarAlumno(self,alumno):
        esta=False
        for i in self.listaAlumnos:
            if(i.getNombre()==alumno.getNombre()):
                self.listaAlumnos.remove(alumno)
        if(esta):
            print("Alumno no encontrado")
        else:
            print("Alumno eliminado")
    def getModulos(self):
        aux=""
        if self.__curso==1:
            for i in self.__ciclo.getModulosPrimero():
                aux+=i.getNombre()+" "+i.getOptativo()+"\n"+"\t"
        else:
            for i in self.__ciclo.getModulosSegundo():
                aux+=i.getNombre()+" "+i.getOptativo()+"\n"+"\t"
        return aux

    def getInfoGrupo(self):
        informe = f"""
    Grupo {self.__nombre}
    =========================
    Ciclo: {self.__ciclo}
    Curso: {self.__curso}
    Tutor: {self.getTutor()}
    Número Alumnos: {self.__numAlumnos}
    Módulos:
    {self.getModulos()}
    Alumnos:
    {self.getAlumnos()}
    =========================
                """
        print(informe)





