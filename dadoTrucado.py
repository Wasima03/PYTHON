#1
import random

veces = int(input("Cuantos dados vamos a tirar: "))
contador = 0
todosIguales = False
while todosIguales==False:
    tirada = []
    # cuento el número de tiradas
    contador = contador + 1
    for i in range (veces):
        tirada.append(random.randint(1,6))
    # convierto la lista a string y hago los replaces necesarios para que sea como me la piden
    salida = str(tirada)
    salida = salida.replace("[","")
    salida = salida.replace("]", "")
    salida = salida.replace(", ", " - ")
    print(salida)
    # si lo que sale en el primer dado se repite tantas veces como dados hay es que son todos iguales
    if(tirada.count(tirada[0]) == veces):
        todosIguales = True;
print("He tenido que tirar los dados", contador, "veces para que salgan todos iguales")



#2
import random

veces = int(input("Cuantos dados vamos a tirar: "))
contador = 0
todosIguales = False
estadistica =[0,0,0,0,0,0]
while todosIguales==False:
    tirada = []
    contador = contador + 1
    for i in range (veces):
        dado = random.randint(1,6)
        tirada.append(dado)
        # acumulo en la lista de estadisticas los dados que salen de cada número.
        # en la posición 0 de la lista irá el número de veces que sale el dado 1, etc.
        estadistica[dado - 1] += 1
    salida = str(tirada)
    salida = salida.replace("[","")
    salida = salida.replace("]", "")
    salida = salida.replace(", ", " - ")
    print(salida)
    if(tirada.count(tirada[0]) == veces):
        todosIguales = True;
# necesito el total de dados para los porcentajes. Será igual al número de tiradas por los dados que tiro en cada una
totalDados = contador * veces
for i in range (len(estadistica)):
    # para calcular las estadisticas calculo el porcentaje de veces que ha salido cadad dado
    print("El número", i+1, "ha salido el ", round(estadistica[i]*100/totalDados,2), "% de las veces")
print("He tenido que tirar los dados", contador, "veces para que salgan todos iguales")


#3

import random

veces = int(input("Cuantos dados vamos a tirar: "))
contador = 0
todosIguales = False
estadistica =[0,0,0,0,0,0]
while todosIguales==False:
    tirada = []
    contador = contador + 1
    for i in range (veces):
        # Para simular que el dado está trucado imagino un dado de 8 caras pero siempre que sale un 7 o un 8
        # lo contabilizo como si fuese un 6. Así este número tiene el triple de posibilidades de salir
        dado = random.randint(1,8)
        if dado == 7 or dado == 8:
            dado = 6
        tirada.append(dado)
        estadistica[dado - 1] += 1
    salida = str(tirada)
    salida = salida.replace("[","")
    salida = salida.replace("]", "")
    salida = salida.replace(", ", " - ")
    print(salida)
    if(tirada.count(tirada[0]) == veces):
        todosIguales = True;
totalDados = contador * veces
for i in range (len(estadistica)):
    print("El número", i+1, "ha salido el ", round(estadistica[i]*100/totalDados,2), "% de las veces")
print("He tenido que tirar los dados", contador, "veces para que salgan todos iguales")
