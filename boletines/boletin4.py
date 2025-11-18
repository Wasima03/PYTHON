
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

#6
import math
primos=[]

for i in range(3,51,2):
    primo=True
    for j in range (2,int(math.sqrt(i))+1):
        if i%j==0:
            primo=False
            break
    if primo:
        primos.append(i)

for i in primos:
    print(i,"Raiz cuadrada:",math.sqrt(i),"Cuadrado:",i*i,"Cubo:",(i*i*i))
    print(" ")

#7
import math
primos=[]
pareja=[]
contador=0

for i in range (51,70,2):
    primo=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            primo=False
            break
    if primo:
        primos.append(i)

for n in range (len(primos)-1):
    if primos[n+1]-primos[n]==2:
        print("Pareja:",primos[n],primos[n+1])
        contador+=1
        break

#8
num=(input("Introduce una cifra: "))
sumaPares=0
sumaImpares=0
for i in range(len(num)):
    if i%2==0:
        sumaPares+=int(num[i])
    else:
        sumaImpares+=int(num[i])

print("Suma pares:",sumaPares)
print("Suma impares:",sumaImpares)


#9
cadena=input("Introduce una cadena: ")
caracter=input("Introduce un caracter:")
posiciones=[]

for i in range(len(cadena)):
    if cadena[i]==caracter:
        posiciones.append(i)

print("El caracter",caracter,"aparece",cadena.count(caracter),"veces")
print("En las posiciones:",posiciones)


#10

cadena=input("Introduce una cadena: ")
num=[]
num2=""
for i in range(len(cadena)):
    if cadena[i].isdigit():
        num2+=cadena[i]
print(num2)


#11
frase=input("Introduce una frase: ")
for i in range(len(frase)):
    if frase[i]==" " or i==len(frase)-1 or frase[i+1]==" "  :
        print(frase[i],end=" ")
    else:
        print(frase[i],"-" ,end=" ")


#12
year=int(input("Introduce un año: "))
if year%4==0 and ((year%100!=0) or year%400==0):
    print("El año introducido es bisiesto")
else:
    print("El año introducido no es bisiesto")


#13
num=int(input("Introduce un número: "))
caracter=input("introduce un caracter: ")

for i in range(num):
    for j in range(num):
        print(caracter, end="")
    print()

#14
hora=input("Introduce una hora: ")

if hora[0:2].isdigit() and hora[3:5].isdigit() and hora[2]==":":
    if int(hora[0:2])>0 and int(hora[0:2])<24 and int(hora[3:5])>0 and int(hora[3:5])<60:
        if int(hora[0:2])>6 and int(hora[0:2])<12:
            print("Es por la mañana.")
        elif 12 <= int(hora[0:2]) <= 19:
            print("Es por la tarde.")
        elif int(hora[0:2])>=20 and int(hora[0:2])<=23:
            print("Es por la noche.")
        elif int(hora[0:2])>=0 and int(hora[0:2])<=5:
            print("Es por la madrugada.")

    else:
        print("Las horas o minutos no son válidos.")

else:
    print("El formato no es válido.")






