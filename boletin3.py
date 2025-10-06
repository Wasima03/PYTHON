#1-2
"""
p1=input("Introduce la contrasña: ")
p2=input("Vuelve a introducir la contraseña: ")
ct=0
while (not p1.__eq__(p2)):
    print("Las contraseñas no coinciden.")
    p1 = input("Introduce la contrasña: ")
    p2 = input("Vuelve a introducir la contraseña: ")
    ct += 1
print("Las contraseñas coinciden.")
print("Número de intentos:",ct)

#3
nombre=input("Introduce tu nombre: ")
apellido=input("Introduce tus apellidos: ")

print(apellido,",",nombre)

#4
cd=input("Introduce una cadena de texto: ")
n=0
for i in cd:
    if i.__eq__(" "):
        n+=1

print("Número de espacios en blanco:",n)
print(cd.replace(" ",""))

#5
cd=input("Introduce una cadena de texto: ")
for i in cd[::-1]:   #for i in range (len(cd)-1,-1, -1):
    print(i,end="")


#6
cd=input("Introduce una cadena de texto: ")
par=""
impar=""
for i in range(0,(len(cd))):
    if i%2==0:
        par += cd[i]
    else:
        impar+=cd[i]
print("Cadena par:",par)
print("Cadena impar:",impar)
"""

#7
cd=input("Introduce una cadena: ")

for i in cd:
    if i.__eq__("a"):
        i="4"
    elif i.__eq__("e"):
        i="3"
print(cd)