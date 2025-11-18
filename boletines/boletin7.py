import math
import random

#1-2
from importlib.util import source_hash

def sumar(num1, num2):
    print("La suma de",num1,"y",num2,"es:",(num1+num2))

def restar(num1, num2):
    print("La resta de",num1,"y",num2,"es:",(num1-num2))

def multiplicar(num1, num2):
    print("La multiplicacion de", num1,"y", num2, "es:", (num1 * num2))

def dividir(num1, num2):
    try:
        print("La división de", num1,"y", num2, "es:", (num1 / num2))
    except ZeroDivisionError:
        print("No se puede dividir entre cero")

def raizCuadrada(num1, num2):
    print("La raíz cuadrada de",num1,"es: ",math.sqrt(num1))
    print("La raíz cuadrada de",num2,"es: ",math.sqrt(num2))

def cubo(num1, num2):
    print("El cubo de",num1,"es:",math.pow(num1,3)) #num1 ** 3
    print("El cubo de",num2,"es:",math.pow(num2,3))


try:
    num1 = int(input("Introduce el número 1: "))
    num2 = int(input("Introduce el número 2: "))
    op=input("Introduce la operación (S/R/M/D/RC/C)")

    match op.upper():
        case "S":
            sumar(num1,num2)
        case "R":
            restar(num1,num2)
        case "M":
            multiplicar(num1,num2)
        case "D":
            dividir(num1,num2)
        case "RC":
            raizCuadrada(num1,num2)
        case "C":
            cubo(num1,num2)
        case _:
            print("Operacion no válida")

except ValueError:
    print("Datos introducidos no válidos.")

#3
try:
    num=int(input("Introduce un número: "))
    match num:
        case 1:print("Enero")
        case 2:print("Febrero")
        case 3: print("Marzo")
        case 4:print("Abril")
        case 5:print("Mayo")
        case 6:print("Junio")
        case 7:print("Julio")
        case 8:print("Agosto")
        case 9:print("Septiembre")
        case 10:print("Octubre")
        case 11:print("Noviembre")
        case 12:print("Diciembre")
        case _:print("El número no corresponde a ningún mes.")
except ValueError:
    print("Numero introducido no identificado")

#4
try:
    nota=int(input("Introduce una nota"))
    match nota:
        case n if n>0 and n<3: print("Muy deficiente")
        case n if n>2 and n<5 : print("Insuficiente")
        case 5: print("Suficiente")
        case 6: print("Bien")
        case n if n>6 and n<9: print("Notable")
        case n if n>8 and n<11: print("Sobresaliente")
        case _:print("Nota no válida")
except ValueError:
    print("Datos introducidos no válidos")

#5
num=int(input("Introduce un número: "))
array=[]
total=0
for i in range(num):
    valor=random.randint(10,1000)
    array.append(valor)
    total += valor

print("Maximo: ",max(array))
print("Mínimo: ",min(array))
print("Media aritmética:",round((total/num),2))
max=max(array)
min=min(array)

for i in range(0,len(array)):
    if array[i]==max:
        print("El maximo se encuentra en la pos",i)
    elif array[i]==min:
        print("El minimo se encuentra en la pos",i)

#7
num=int(input("Introduce un numero: "))
array=[]
for i in range (num):
    array.append(random.randint(10,1000))
try:
    pos=int(input("Introduce una posicion: "))
    if pos<0: raise Exception("No se pueden poner posiciones negativas")
    print(array[pos])

except IndexError:
    print("Posicion no válida")

#8
for i in range(0,5):
    print(random.randint(0,1), end=" ")
    for j in range(0,5):
        print(random.randint(0,1),end=" ")
    print()
