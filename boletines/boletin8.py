#1
"""
matriz=[[1,2],[3,4],[5,6]]
traspuesta=[]

print(len(matriz))
print(len(matriz[1]))
print(matriz[0])
print(matriz[1])
print(traspuesta)

for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        traspuesta.append(matriz[j][i])
print(traspuesta)

#2
valida=False
min=False
may=False
num=False
simbolo=False
simbolos = {"_","-", "!", "?", "*"}

while(not valida):
    pasword = input("Introduce una contrseña")
    for i in pasword:
        if i.islower():
            min=True
        elif i.isupper():
            may=True
        elif i.isdigit():
            num=True
    if len(set(pasword) & simbolos)>=1:
        simbolo=True
    if (8 <= len(pasword) <= 20):
        if (min and may and num and simbolo):
            valida=True
            print("Contrseña valida")
"""

#3
mensaje = input("Escribe tu mensaje secreto")
cifrado=""
for i in mensaje:
    cifrado += i
    for j in mensaje(-1,-1,-1):
        cifrado +=j
print(cifrado)



