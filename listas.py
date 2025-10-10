"""
lista=[]
lista2=list()
lista3=[2,5,6.5,7,8,12,7,12,5,5]
lista4=["Jorge","Pepe","Ana"]
lista3.sort(reverse=True)
print(lista3)

lista3.extend(lista4)   # Otra manera----lista5=lista3+lista4
print(lista3)
lista3.append(14)
print(lista3)
lista3.insert(-1,20) #Inserta un elemento antes de la posicion escrita
print(lista3)

print(lista3.count(5))
print(lista3.index(12))

texto=str(lista3)
print(texto)
texto=texto.replace("[","")
texto=texto.replace("]","")
print(texto)
texto2="Hola mundo"
texto5 =list(texto2)
print(texto5)


matriz=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz[1][0])

print(lista3)
print(lista3[:5])
print(lista3[2:5])
print(lista3[5:])
print(lista3[2:-2])
print(lista3[::-1])

print(" ")

import random
lista6=["Jorge","Pepe","Ana","Manoli","Roberto","Pilar"]
print(random.choice(lista6))
print(random.sample(lista6,3))  #elige tres elementos diferentes
random.shuffle(lista6) #no se puede meter en el print, porque no devuelve nada
print(lista6)
"""




