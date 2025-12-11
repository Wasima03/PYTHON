def cuadrado (x):
    return x**2
print(cuadrado(5))

cuadradoLambda = lambda x: x**2  #lo que genera la funcion es lo que devuelve
print(cuadradoLambda(5))

media = lambda *lista: sum(lista)/len(lista) #el sum suma todos los valores de la lista
print(media(2,5,6,7))
print(media(9,8,7,5))
l=(1,2,3)
print(sum(l))

cuadradoMayorQue10 = lambda x: True if x**2>10 else False #como operador ternario
print(cuadradoMayorQue10(2))
print(cuadradoMayorQue10(10))