"""
#1
num=int(input("Introduce un número: "))
fct=1
for i in range(1,num+1):
    fct *= i
print("El factorial de",num,"es:",fct)
"""
#2
num=int(input("Introduce un número: "))
a=0
b=1
print(a,b,end=", ")
for i in range(num):
    i += i
    print(i,end=", ")