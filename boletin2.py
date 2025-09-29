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
"""
#9






