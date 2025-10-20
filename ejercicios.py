"""
#1 JUEGO DE MONEDAS
import random

num=int(input("Introduce el número de monedas: "))
moneda=["cara","cruz"]
resultado=set()
contador=0
cara=0
cruz=0

while len(resultado)!=1:
    resultado=set()
    for i in range(0,num):
        aux=random.choice(moneda)
        if aux =="cara":
            cara+=1
        else:
            cruz+=1
        resultado.add(aux)
        if i==num-1:
            print(aux)
        else:
            print(aux,end="-")

    contador+=1
total=num*contador
print()
print("Se han tenido que lanzar las monedas",contador,"veces")

print("Cara ha salido un porcentaje de:",round(cara/total*100,2),"%")
print("Cruz ha salido un porcentaje de:",round(cruz/total*100,2),"%")
"""


#DADO TRUCADO
import random

num=int(input("Introduce el numero de dados: "))
dados=set()
estadistica=[]
contador=0
while len(dados)!=1:
    dados=set()
    for i in range(1,num+1):
        ale=random.randint(1,6)
        dados.add(ale)
        estadistica.append(ale)
        if i ==num:
            print(ale)
        else:
            print(ale,end="-")
    contador+=1

print("He tenido que lanzar los dados",contador,"veces")
total=num*contador
ctDados=0
for i in range(1,7):
    ctDados=0
    for j in estadistica:
        if i==j:
            ctDados+=1
    print("El número",i,"ha salido un porcentaje de:",round(ctDados*100/total,2))




