frase= input("Introduce una frase: ")
letra=input("Letra  a mantener: ")
resultado=[]

for i in range (len(frase)):
    if frase[i]==letra:
        resultado.append(frase[i])
    elif frase[i]==" ":
        resultado.append(" ")
    else:
        resultado.append("*")
print("Resultado: ",end="")
for i in resultado:
    print(i,end="")