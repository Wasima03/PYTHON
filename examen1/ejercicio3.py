cadenaOriginal=input("Escribe un texto: ")
cadena2=list()
espacios=0
vocSupr=0
resultado=""
vocales=("a","e","i","o","u","A","E","I","O","U")
#bucle para quitar espacios en blanco
for i in cadenaOriginal:
    if i!=" ":
        cadena2+=i
    else:
        espacios+=1
#bucle para quitar vocales
for i in cadena2[0:]:
    for j in vocales:
        if i==j:
            vocSupr+=1
            cadena2.remove(i)

print("Sin vocales ni espacios: ",end="")
#bucle para mostrar resultado en formato pedido
for i in cadena2:
    print(i,end="")
print()
print("Vocales suprimidas:",vocSupr)
print("Espacios en blanco suprimidos: ",espacios)


