""""
def mifuncion():
    otroTexto="Hola mundo cruel"
    texto="Hola otra vwz"
    print("Dentro de la funcion",texto)
    return otroTexto


texto="Hola mundo"
print("Valor devuelto",mifuncion())
print("Desde fuera de la funcon",texto)


def mifuncion(parametro,parametro2):
    for i in range(0,parametro2):
        print(parametro)
    otroTexto="Hola otra vez"
    print(otroTexto)

otroTexto="Hola mundo cruel"
mifuncion("Hola mundo",3)

def mifuncion(t,l,n):
    t="Hola mundo cruel"
    n=4.4
    lista[1]=111


texto ="Hola mundo"
numero=5.5
lista=[44,2,13]
mifuncion(texto,lista,numero)
print(texto,"-",numero,"-",lista)


#ejercicio 6/boletin 4:
import math
def mifuncion(numero):
    primo=True
    for i in range (2,int(math.sqrt(numero))+1):
        if numero%i==0:
            primo=False
    return primo
contador=0
for i in range(3,100,2):
    while(contador!=50):
        primo=mifuncion(i)
        if primo:
            print(i, "Raiz cuadrada:", math.sqrt(i), "Cuadrado:", i * i, "Cubo:", (i * i * i))
            contador+=1

#ejercicio 7 /boletin 4
for i in range (51,70,2):
    if(mifuncion(i)==True and mifuncion(i+1)==True):
        print("Pareja:",i,"y",(i+1))


#funcion con argumentos por defecto
def saludo(nombre,mensaje="hola",despedida="Hasta la vista"):  #si no ponemos nada, mensaje toma el valor por defecto puesto ahi, siempre van al final
    print(mensaje,nombre,despedida)
saludo("Jose María","Bienvenido")
saludo("Jose María",)
saludo("Wasima",despedida="Adiós")#tenemos que especificar que argumento es (despedida=)

def argumentosVariables(nombre,*titulos): #con el asterisco se recogen los atributos en una tupla
    for titulo in titulos:
        print(titulo,end=" ")
    print(nombre)
argumentosVariables("Wasima","Sra")
argumentosVariables("Wasima","Sra","Excelentisima","Doña") #puedo meter cualquier numero de argumentos y de tipos
argumentosVariables("Wasima") #si no se pone nada funciona

def muestraDatos(nombre,edad):
    print("Nombre:",nombre,"Edad:",edad)
muestraDatos("Wasima",19)
datos=["Pepe",32]
muestraDatos(*datos) #meto como parametro una tupla o lista con un * (parametro empaquetado)

def devuelveTresEnteros():
    return 14,17,24

num1,num2,num3=devuelveTresEnteros()
print(num1,num2,num3,sep=" - ")
"""









































