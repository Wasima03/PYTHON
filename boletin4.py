"""
#1
num=int(input("Introduce un número: "))
fct=1
for i in range(1,num+1):
    fct *= i
print("El factorial de",num,"es:",fct)

#2
num=int(input("Introduce un número: "))
a=0
b=1
print(a,b,end=", ")
for i in range(num):
    i += i
    print(i,end=", ")


#2
lista=[0,1]
num=int(input("Introduce un núemro: "))
if num==1:
    lista.pop()
elif num==0:
    lista=[]

else:
    for _ in range(2,num):
        nuevo=lista[-1] + lista[-2]
        lista.append(nuevo)
print(lista)


#3
lista=[0,1]
num=int(input("Introduce un núemro: "))
final=[]
if num==1:
    lista.pop()
elif num==0:
    lista=[]

else:
    for _ in range(2,num):
        nuevo=lista[-1] + lista[-2]
        lista.append(nuevo)
for i in lista:
    if i<=num:
        final.append(i)

print(final)

#4
num=input("Introduce un número: ")
print("Número de cifras: ",len(num))

#5
num=input("Introduce un número: ")
num2=""
for i in num[::-1]:
    num2 += i

if num==num2:
    print("El número es capicúa")
else:
    print("El número no es capicúa")
"""
#6
import math
primos=[]
primo=False
for i in range(3,51,2):
    for j in (2,math.sqrt(i)+1):
        if i%j!=0:
            primo=True
            break
    if primo:
        primos.append(i)

for i in primos:
    print(i,"Raiz cuadrada:",math.sqrt(i),"Cuadrado:",i*i,"Cubo:",(i*i*i))
    print(" ")





