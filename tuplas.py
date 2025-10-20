#no se puede cambiar

tupla = (1,2,3,4,5)
print(tupla)
tupla2=("María","Hola","Pepe")
tupla3=(23,"Adios",False,(1,2,3),44.5,[1,2,3])
print(tupla3)
tupla4 = ("Sevilla",) #hay que poner una coma al final de la tupla si quiero meter un soloo elemento
print(tupla4)

for i in tupla4:
    print(i)
for i in range(0,len(tupla4)):
    print(i,"-", tupla4[i])

lista = list(tupla2)
print(lista)
lista.append(1)
print(lista)
texto = str(tupla2)
print(texto)
tupla6 = tuple([1,2,3,4,5])
print(tupla6)
tupla7 = tuple("Hola mundo")
print(tupla7)

tupla8 = "Pepe","Juan",tupla6,"Ana"
print(tupla8)

print(tupla3[5])
tupla3[5][1]=4
print(tupla3)


if 4 in tupla:
    print("El 4 está en la tupla")
if 9 not in tupla:
    print("El 9 no está en la tupla")

profesor=("Jose Maria","Morales",57,False,True)
nombre,apellidos,edad,alumno,profe=profesor
print(nombre,alumno)








