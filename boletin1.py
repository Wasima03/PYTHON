"""
#1
for i in range(0,10):
    print(i)

#2
for i in range(0,50,2):
    print(i)

#3
num=int(input("Introduce un número: "))
for i in range(1,6):
    print(num*i)

#4
for i in range(0,1000):
    if (i%7 == 0):
        print(i)

# 5
n=int(input("Introduce un número: "))
if n%2 == 0 :
   print(n,"es un número par")
else:
   print(n,"es un número impar")

#6
n=int(input("Introduce un número: "))
if n%3 == 0:
    print(n,"es divisible por 3")
else:
    print(n,"no es divisible por 3")

#7
p=float(input("Introduce el precio: "))
print(((p*0.21)+p),"€")

#8
c=float(input("Introduce la cantidad: "))
m=int(input("Introduce los meses: "))
print(round((c/m),2),"€")

#9
import random
print(random.randint(0,50))

#10
import random
print(random.randint(1,6))
print(random.randint(0,6))

#11
import random
d1=0
d2=1
ct=0
while d1 != d2:
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    ct += 1
print("Se han lanzado los dados",ct,"veces")


#12
import random
d=int(input("Introduce el núemro de dados: "))
c=int(input("Introduce el número de caras: "))
ct=0
while ct != d:
    print(random.randint(1,c))
    ct += 1


#13
import random
ct=0
c=1
d = int(input("Introduce el núemro de dados: "))
while c%2 != 0:
    c=int(input("Introduce el número de caras: "))

while ct != d:
        print(random.randint(1,c))
        ct += 1
"""
import math

#14
"""
import random
print("Introduce dos números, el primero debe ser menor.")
n1=int(input("Introduce el número 1: "))
n2= int(input("Introduce el número 2: "))
print(random.randint(n1,n2))

#15
import random
aux=0
n1=int(input("Introduce el número 1: "))
n2= int(input("Introduce el número 2: "))
if (n1>n2):
    aux=n1
    n1=n2
    n2=aux
print(random.randint(n1,n2))

#16
import random
for i in range (0,6):
    print(random.randint(1,49))

#17
import random
for i in range(0,15):
    n=random.randint(1,3)
    if (n==3):
        print("X")
    else:
        print(n)

#18
import random
n=0
ct=0
while n != 666 :
    n=random.randint(1,1000)
    print(n)
    ct += 1
print("Faltan",ct,"días para que se acabe todo!")


#19
n=int(input("Introduce un número: "))
for i in range(1,n):
    if n%i == 0:
        print(i)


#20
n1=int(input("Introduce un núemro: "))
n2=int(input("Introduce un núemro: "))
n3=int(input("Introduce un núemro: "))

numeros =[n1,n2,n3]
numeros.sort()

for i in numeros:
    print(i)


#21
div=0
n=int(input("Introduce un número: "))
for i in range(1,n):
    if(n%i == 0):
        div += 1
if(div <= 1):
    print("El número",n,"es primo")
else:
    print("El número",n,"no es primo")


#22
import random
primo=False
n=0
while not primo:
    n=random.randint(10000000,50000000)
    p=True
    if n<2 or n%2==0 or n==2:
        p=False
    else:
        for i in range (3,int(math.sqrt(n))+1):
            if i % n == 0:
                p=False
                break
    if p:
        primo=True
        print("Número primo: ", n)

#23
import math
for i in range(3,101,2):
    for j in (i,int(math.sqrt(i))):
        primo = False
        if i % j != 0:
            primo = True
            break
    if primo:
        print(i)



#24
import math
n1=int(input("Introduce un número: "))
n2=int(input("Introduce otro número: "))
primo = False
for i in range(n1,(n2+1)):
    if i<2:
        primo=False
    else:
        primo=True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)



#25
n=float(input("Introduce un número: "))
while n > 1:
    n= n / 2
    print(round(n,2))
"""




