#1
import random
num=int(input("Introduce un número de dados: "))
contador=0
dados=set()
dados2=[]

while len(dados)!=1:
    dados=set()
    for i in range(num):
        ale=random.randint(1,6)
        dados.add(ale)
        dados2.append(ale)
        print(ale,end=" - ")
    print()
    contador+=1
print("Numero de tiradas: ",contador)
total=num*contador
ct=0
for i in range(1,7):
    ct = 0
    for j in dados2:
        if j==6 and i==6:
            ct+=3
        elif i==j:
            ct+=1
    print("El número",i,"ha salido el",round((ct/total)*100,2),"%")





