frase= input("Introduce una frase: ")
letra=input("Letra  a mantener: ")
resultado1=[]


for i in range (len(frase)):
    if frase[i]==letra:
        resultado1.append(frase[i])
    elif frase[i]==" ":
        resultado1.append(" ")
    else:
        resultado1.append("*")
print("Resultado: ",end="")
for i in resultado1:
    print(i,end="")

print()
letra2=input("Introduce una letra: ")
contador=0
resultado2=[]

for i in range (len(frase)):
    if frase[i]==letra:
        resultado2.append(frase[i])
    elif frase[i]==letra2:
        resultado2.append(frase[i])
        contador+=1
    elif frase[i]==" ":
        resultado2.append(" ")
    else:
        resultado2.append("*")

print("La letra",letra2,"aparece en",contador,"ocasiones")
print("Resultado: ",end="")
for i in resultado2:
    print(i,end="")


