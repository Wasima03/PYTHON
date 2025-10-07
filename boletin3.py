"""
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
"""

#12
m=input("Introduce una matrícula válida:  ")
cd=["A","E","I","O","U","Ñ","Q"]
cd=str(cd)
esta=True
if m[:4].isdigit() and m[4:].isalpha() and m.isupper():

    for i in m[4:]:
        if i in cd:
            esta=True
        else:
            esta=False
    if not esta:
        print("MATRÍCULA VÁLIDA.")
    else:
        print("MATRÍCULA NO VÁLIDA.")
else:
    print("MATRÍCULA NO VÁLIDA.")
