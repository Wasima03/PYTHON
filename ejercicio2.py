import random
lista=[]
pares=0
impares=0
print("10 números entre el 1 y el 1000")
for i in range(0,10):
    ale=random.randint(1,1000)
    lista.append(ale)
for i in range (0,len(lista)):
    if i==len(lista)-1:
        print(lista[i],end="")
    else:
        print(lista[i],end=",")

for i in lista:
    if i%2==0:
        pares+=1
    else:
        impares+=1

print()
print("He generado",pares,"números pares y",impares,"números impares")
print("El número mayor ha sido el",max(lista),"y el menor el",min(lista))
