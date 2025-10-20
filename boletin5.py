#1
"""
import random
lista=set()

while(not len(lista)==6):
    lista.add(random.randint(1,49))
print(lista)

#2
num1=int(input("Introduce el numero 1: "))
num2=int(input("Introduce el número 2: "))

lista1=set()
lista2=set()

for i in range(1,num1):
    if num1%i==0:
        lista1.add(i)
for i in range(1,num2):
    if num2%i==0:
        lista2.add(i)

print(lista1)
print(lista2)
print(lista1 & lista2)

#3
frase=input("Introduce una frase: ")
palabras=1
for i in range (0,len(frase)-1): #palabras=frase.split
    if frase[i]==" " and frase[i+1]!=" ":
        palabras+=1
print("Número de palabras:",palabras)


#4
cadena=input("Introduce una cadena: ")
contador=0
cadena=cadena.lower()
vocales={"a","e","i","o","u"}
palabras=set(cadena.split())

for i in palabras:
    aux=set(i)&vocales
    if len(aux) >=4:
        contador+=1
print(contador)


#5
import math
import random
num=[]
veces=[]
for i in range(1,101):
    num.append(random.randint(1,50))
print("Mayor:",max(num))
print("Menor:",min(num))
for i in num:
    veces.append(num.count(i))
print("Numero que mas se repite:",veces.index(max(veces)))
print("Veces:",max(veces))
"""

#6
num=(input("Introduce un número: "))
veces=set()

for i in num:
    if i not in veces:
        print("Número",i,":",num.count(i))
        veces.add(i)









