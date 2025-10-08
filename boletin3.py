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

#7
cd = input("Introduce una cadena de texto: ")
cd=cd.replace("a","4")
cd=cd.replace("A","4")
cd=cd.replace("e","3")
cd=cd.replace("E","3")
cd=cd.replace("i","1")
cd=cd.replace("I","1")
cd=cd.replace("o","0")
cd=cd.replace("O","0")

print(cd)


#8
cd=input("Introduce una cadena de texto: ")
for i in cd:
    if i.__eq__("a") or i.__eq__("e") or i.__eq__("i") or i.__eq__("o") or i.__eq__("u"):
        cd=cd.replace(i,"")
print(cd)

#9
dst=input("Elige uno de estos 4 destinos(Francia,Italia,Chile,Japón); ")
if dst=="Francia":
    print("La capital de tu destino es: París.")
elif dst=="Italia":
    print("La capital de tu destino es: Roma.")
elif dst=="Chile":
    print("La capital de tu destino es: Santiago de Chile.")
elif dst=="Japon":
    print("La capital de tu destino es: Tokio.")
else:
    print("Destino no reconocido.")


#10-11
dni=input("Introduce tu DNI o NIF: ")
valido=False
if len(dni)==9 and dni[8::].isalpha():
    if dni[0:8].isdigit() :
        print("DNI VÁLIDO.")
    elif (dni[:1]=="X" or dni[:1]=="Y" or dni[:1]=="Z" or dni[:1]=="x" or dni[:1]=="y" or dni[:1]=="z"
          and dni[1:8].isdigit()):
        print("NIF VÁLIDO.")
    else:
        print("DNI o NIF NO válido.")

else:
    print("DNI O NIF NO válido.")


#12-13
m=input("Introduce una matrícula válida:  ")
cd=["A","E","I","O","U","Ñ","Q"]
esta=False

if (len(m)==7 and m[:4].isdigit() and m[4:].isalpha() and m.isupper()
        or (len(m)==8 and m[4]==" ") or (len(m)==8 and m[4]=="-")):
    for i in m[4:]:
        if i in cd:
            esta=True
            break
    if not esta:
        print("MATRÍCULA VÁLIDA.")
    else:
        print("MATRÍCULA NO VÁLIDA.")
else:
    print("MATRÍCULA NO VÁLIDA.")

#14
dni=input("Introduce tu DNI o NIF: ")
valido=False
letrasNIF=["y","Y","Z","X","z","x"]
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
suma=0



if len(dni)==9 and dni[8::].isalpha():
    if dni[0:8].isdigit():
        resto=int(dni[0:8]) % 23
        if dni[8::] ==letras[resto]:
            print("DNI VÁLIDO.")
        else:
            print("DNI NO VÁLIDO")
    elif (dni[:1] in letrasNIF and dni[1:8].isdigit()):
        print("NIF VÁLIDO.")
    else:
        print("DNI o NIF NO válido.")

else:
    print("DNI O NIF NO válido.")


#15
fecha=input("Introduce una fecha válida: ")

if len(fecha)==10 and fecha[2:3]=="/" and fecha[5:6]=="/" and fecha.replace("/","").isdigit():
    if int(fecha[:2]) >=1 and int(fecha[:2])<=31 and int(fecha[3:5])>=1 and int(fecha[3:5])<=12 and int(fecha[6:])>=1900:
        if int(fecha[:2])==28 and int(fecha[3:5])==2 and int(fecha[6:])%4==0:
            print("FECHA VÁLIDA")
        else:
            print("FECHA NO VÁLIDA")

"""