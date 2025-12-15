import boletin13
from boletines.boletin13 import Persona,Alumno, Profesor,Modulo,Ciclo,Grupo

a1 = Alumno("Ana","Sanchez",20)
a2=Alumno("Pepe","Cruz",24)
p1 = Profesor("Lorena","Peña","Informatica")
m1 = Modulo("Acceso a datos",1,100,"N")
m2 = Modulo("Python",2,200,"S")
c1 = Ciclo("Grado","Superior")
g1 = Grupo("DAM2",c1,2,10)
c1.addModulo(m1)
c1.addModulo(m2)
g1.addAlumno(a1)
g1.addAlumno(a2)
g1.setTutor(p1)

g1.getInfoGrupo()

