"""
#1
c1=input("Introduce la cadena 1: ")
c2=input("Introduce la cadena 2: ")
c3=input("Introduce la cadena 3: ")
cadenas=[c1,c2,c3]
cadenas.sort()
print(cadenas)

#2
c1=input("Introduce la cadena 1: ")
c2=input("Introduce la cadena 2: ")
c3=input("Introduce la cadena 3: ")
cadenas=[c1,c2,c3]
cadenas.sort(reverse=True)
print(cadenas)


#3
import math
n=float(input("Introduce el precio: "))
print("Total:",round((n-(n*0.21)),2))

#4
n1=float(input("Introduce la nota 1: "))
n2=float(input("Introduce la nota 2: "))

if (n1<0 or n1>10) or (n2<0 or n2>10):
    print("Notas introducidas erróneas")
else:
    print("Media arritmética:", round(((n1+n2)/2)))

#5
n1=float(input("Introduce la nota 1: "))
n2=float(input("Introduce la nota 2: "))
n3=float(input("Introduce la nota 3: "))

print("Nota final con decimales: ", round(((n1*0.05)+(n2*0.15)+(n3*0.8)),2))
print("Nota final sin decimales: ", round(((n1*0.05)+(n2*0.15)+(n3*0.8))))

from os import truncate

#6
import math
n1=float(input("Introduce la nota 1: "))
n2=float(input("Introduce la nota 2: "))
n3=float(input("Introduce la nota 3: "))

n1=n1*0.05
n2=n2*0.15
n3=n3*0.8
t=n1+n2+n3

if t>5:
    print("Nota final:",round(t))
else:
    print("Nota final:",math.trunc(t))  # int(t) es otra manera

#7
n=int(input("Introduce un número: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

#8
import math
n=int(input("Introduce un núemro: "))
div=[]
for i in range (2,n):
    if n%i == 0:
        div.append(i)
print("Divisores del número",n,":",div)


# 9-10-11
c=0
t=0
num=[]
n=" "
while n != "FIN":
    n=input("Introduce un número entre el 1 y el 100: ")
    if n<"0" or n>"100":
        print("Opcion no valida")
    else:
        t =+ int(n)
        num.append(n)
        c =+ 1
print("Número de entradas válidas: ",c-1)
print("Media aritmética: ", t/c)
print("Mayor núemero: ", )



#12
import random
n=random.randint(1,50)
c=0
intento=0
while intento != n:
    intento = int(input("Introduce un núemero: "))

    if intento<n:
        print("Te has quedado corto.")
    else:
        print("Te has pasado.")
    c += 1
    if c>5:
        print("Se han alcanzado un número máximo de intentos.")
        break
if intento ==n:
    print("Enhorabuena, has acertado")

#13
import random
n=random.randint(1,50)
c=0
intento=0
while intento != n:
    intento = int(input("Introduce un núemero: "))

    if intento<n:
        print("Te has quedado corto.")
    else:
        print("Te has pasado.")
    c += 1

print("Enhorabuena, has acertado")
print("Número de intentos:",c)


#14
c = 0
intento = 0
import random
n=random.randint(1,50)

while intento != n:
    intento = int(input("Introduce un núemero: "))

    if intento<n:
        print("Te has quedado corto.")
    else:
        print("Te has pasado.")
    c += 1

print("Enhorabuena, has acertado")
print("Número de intentos:",c)
print()

jugar=input("Quieres volver a jugar?. Escribe 'Y' para jugar o 'N' para cancelar.")
if jugar == "Y":
    c=0
    intento=0
    while intento != n:
        intento = int(input("Introduce un núemero: "))

        if intento < n:
            print("Te has quedado corto.")
        else:
            print("Te has pasado.")
        c += 1

    print("Enhorabuena, has acertado")
    print("Número de intentos:", c)
elif jugar == "N":
    print("Como quieras.")
else:
    print("No te he entendido.")



#15
import random
c = 0
intento = 0

nIntentos=int(input("Indica el número máximo de intentos: "))
nMaximo=int(input("Indica el número máximo: "))
n=random.randint(1,nMaximo)

while intento != n:
    intento = int(input("Introduce un núemero: "))
    c += 1
    if c > 5:
        print("Número de intentos máximo alcanzado.")
        break
    if intento<n:
        print("Te has quedado corto.")
    elif intento>n:
        print("Te has pasado.")
    else:
        print("Enhorabuena, has acertado")


print()

jugar=input("Quieres volver a jugar?. Escribe 'Y' para jugar o 'N' para cancelar.")
if jugar == "Y":
    c=0
    intento=0
    n = random.randint(1, nMaximo)
    while intento != n:
        intento = int(input("Introduce un núemero: "))
        c += 1
        if c > nIntentos:
            print("Número de intentos máximo alcanzado.")
            break
        if intento < n:
            print("Te has quedado corto.")
        elif intento>n:
            print("Te has pasado.")
        else:
            print("Enhorabuena, has acertado")


elif jugar == "N":
    print("Como quieras.")
else:
    print("No te he entendido.")


#16
import math
r=float(input("Introduce el radio de una circuferencia: "))
area=3.14159 * (r*r)
long=2*3.14159*r
print("Área de la circunferencia:",round(area,5))
print("Longitud de la circunferencia",round(long,5))
"""

#17
temp=(input("Introduce la temperatura, indicando la unidad: "))
unidad=temp[len(temp)-1]
cnt=temp[:(len(temp)-1)]
print(unidad,cnt)
if unidad == "C":















