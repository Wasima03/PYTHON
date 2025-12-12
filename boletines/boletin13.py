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
    def __init__(self,nombre,apellido,edad):
        super().__init__(nombre,apellido)
        self.__edad = edad

    def getEdad(self):
        return self.__edad

class Profesor(Persona):
    departamentos ={"Informática","Empresa","Inglés"}
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
        if optativo != "S" or optativo != "N":
            self.__optativo="N"
        else:
            self.__optativo=optativo

    def getNombre(self):
        return self.__nombre
    def getAnyo(self):
        return self.__anyo
    def getHoras(self):
        return self.__horas
    def getOptativo(self):
        return self.__optativo

class Ciclo:
    grados ={"Medio","Superior"}
    def __init__(self,nombre,grado,*modulos):
        self.__nombre = nombre
        if grado in self.grados:
            self.__grado = grado
        else:
            self.__grado="Medio"
        self.__modulos=modulos

    def getNombre(self):
        return self.__nombre
    def getGrado(self):
        return self.__grado
    def getModulos(self):
        return self.__modulos

class Grupo:
    listaAlumnos=[]
    def __init__(self,nombre,ciclo,curso,tutor,numAlumnos):
        self.__nombre = nombre
        self.__ciclo = ciclo
        if ciclo!=1 or ciclo !=2:
            self.__ciclo=1
        else:
            self.__curso = curso
        self.__tutor = tutor
        self.__numAlumnos = numAlumnos

    def setAlumnos(self,alumno):
        self.listaAlumnos.append(alumno)
    def eliminarAlumno(self,alumno):
        if alumno in self.listaAlumnos:
            self.listaAlumnos.remove(alumno)
            print("Alumno eliminado")
        else:
            print("Alumno no encontrado")

    def setModulo(self):

    def getAlumnos(self):
        return self.listaAlumnos

    def getNombre(self):
        return self.__nombre
    def getCiclo(self):
        return self.__ciclo
    def getCurso(self):
        return self.__curso
    def getTutor(self):
        return self.__tutor
    def getNumAlumnos(self):
        return self.__numAlumnos
    def getAlumnos(self):
        return self.__alumnos





