import random
lista=set()
numero=int(input("Escribe un número:"))
while numero<10:
    print("Número introducido no válido")
    numero=int(input("Vuelve a escribri un número: "))

print("5 números pares aleatorios y diferentes comprendidos entre el 1 y el",numero)

while len(lista)!=5:
    lista=set()
    for _ in range(0,5):
        ale=random.randint(1,numero)
        if ale%2==0:
            lista.add(ale)
for i in lista:
    print(i,sep=" ")


