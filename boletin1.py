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


if (n1<n2) and (n1<n3):
    print(n1)
elif ()



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
div=0
n=0
while not primo:
    n=random.randint(10000000,50000000)
    for i in range(2,n):
        if n % i == 0:
            div += 1
    if div == 0:
        primo = True
        print(n)
    else:
        primo=False

#23
import math
div=0
for i in range(1,10):
    n=int(math.sqrt(i))
    for j in range(2,n):
        if n%j == 0:
            div += 1
    if div == 0 :
        print(i)
"""




