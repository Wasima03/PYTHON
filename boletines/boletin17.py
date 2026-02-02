#EJERCICIO 1

"""try:
    def compararFicheros(fichero1,fichero2):
        igual=False
        f1=open(fichero1)
        f2=open(fichero2)

        texto1=f1.read()
        texto2=f2.read()

        if texto1==texto2:
            igual=True
        return igual

except:
    print("Error, el fichero no es correcto")
# EJERCICIO 2

fichero= open('estadisticas.txt','r+')
lista = fichero.readlines()
hombres=0
mujeres=0
altura=0
for i in lista:

    if i=='Hombre\n':
        hombres+=1
    elif i=='Mujer\n':
        mujeres+=1
    else:

        t=float(i)
        altura=altura+t

print("Hombres: ", hombres)
print("Mujeres: ", mujeres)
print("Estatura media: ", round((altura / (hombres + mujeres)),2))


for i in range (len(lista)):
    if i==0 or i%2==0:
        if lista[i] == 'Hombre':
            hombres+=1
        else:
            mujeres+=1
    else:
        t=float(lista[i])
        t+=altura


#EJERCICIO 3-4

import re
from boletines.IBAN import Iban

cuentas=open('codigos.txt','r+')
cuentasValidas=[]
codigos=0
codigosV=0
patron=r"[A-Z]{2}[0-9]{22}"

while True:
    linea=cuentas.readline()
    linea=linea.replace(" ","")
    codigos+=1
    if re.fullmatch(patron, linea[:-1]):
        print(linea)
        cuentasValidas.append(linea)
        iban = Iban(linea)
    if linea=="":
        break
#EJERCICIO 3

for i in cuentasValidas:
    codigosV+=1
    print("País: ",i[:2])
    print("DC: ",i[2:4])
    print("Entidad: ",i[4:8])
    print("Sucursal: ",i[8:12])
    print("Número de cuenta: ",i[13:])
print("Hay ",codigosV," correctos y ",codigos-codigosV," codigos incorrectos")

import random
from random import shuffle


#EJERCICIO 4

#EJERCICIO 5
import random

from boletines.Cliente import Cliente


def barajarDatos(fichero):
    nombres=[]
    apellidos=[]
    dnis=[]
    lista=[]
    try:
        with open(fichero,'r',encoding="UTF-8") as f: #PARA QUE SE LEEAN Y ESCRIBAN BIEN LAS TILDES
            datos=f.readlines()

            for i in range (len(datos)):
                datos[i]=datos[i].replace("\n","")
                lista=datos[i].split(" ")
                nombres.append(lista[0])
                apellidos.append(lista[1])
                dnis.append(lista[2])
                cliente = Cliente(lista[0],lista[1],lista[2])
                cliente.mostrarCliente()

            random.shuffle(nombres)
            random.shuffle(apellidos)
            random.shuffle(dnis)
        with open(fichero,'w', encoding="UTF-8") as fi:
            for i in range(len(nombres)):
                fi.write(nombres[i]+" "+apellidos[i]+" "+dnis[i]+"\n")


    except FileNotFoundError:
        print("Error, el fichero no es correcto")

barajarDatos("clientes.txt")


from boletines.Delincuente import Delincuente


#EJERCICIO 7
def delitos(n,fichero):
    lineas=[]
    lista=[]

    try:
        with open(fichero,'r',encoding="UTF-8") as f:
            lineas=f.readlines()

            i=0
            while i< len(lineas):
                linea=lineas[i].strip()
                if linea[0]=="-":
                    datos=linea[2:].split(",")
                    nombre=datos[0]
                    edad=datos[1]
                    d=Delincuente(nombre,edad)
                    lista.append(d)
                    i+=1
                    #SI LA LINEA NO EMPIEZA POR - Y "I" ESTA DENTRO DE LOS RANGOS,
                    #SE LEE OTRA LINEA Y SE AÑADE A DELITOS
                    while(i<len(lineas) and not lineas[i].startswith("-")):
                        d.añadir_delito(lineas[i].strip())
                        i+=1
                else:
                    i+=1
        #SI EL NOMBRE COINCIDE SE IMPRIME LA LISTA DE DELITOS
        for j in lista:
            if j.getNombre()==n:
                j.mostrarExpediente()
            else:
                print("Sin antecedentes penales")

    except FileNotFoundError:
        print("Error, el fichero no es correcto")

nombre=input("Introduce tu nombre: ")
delitos(nombre,"delincuentes.txt")
import random

#EJERCICO 8
nombres = ["Ash", "Momo", "Monkey", "Naruto", "Nico", "Ken","Roronoa", "Touka"]
apellidos = ["Ketchum", "Ayase", "D. Luffy", "Uzumaki", "Robin","Kaneki", "Zoro", "Kirishima"]

num=0
while(num>8 or num<1):
    num=int(input("Introduce el número de personajes: "))
try:
    with open("personajes.txt", 'w', encoding="UTF-8") as f:
        print("Personajes:")
        for i in range(num):
            personaje= random.choice(nombres)+" "+random.choice(apellidos)+"\n"
            print(personaje,end="")
            f.write(personaje)
except FileNotFoundError:
    print("Error, el fichero no es correcto")

#EJERCICIO 9
try:
    with open("alumnos.txt",'r') as fr:
        lineas = fr.readlines()
        for i in lineas:
            datos=i.split(":")
            nombre=datos[0].strip().replace(",","")
            notas=datos[1].strip().split(",")
            aprobado=True
            total=0
            for j in notas:
                total+=float(j)
                if float(j)<5:
                    aprobado=False
            if(aprobado):
                media=round(total/len(notas),1)
                print(nombre,"-",media)

except FileNotFoundError:
    print("Error, el fichero no es correcto")

#EJERCICIO 10
try:
    with open("redes.txt",'r') as f:
        claseA=[]
        claseB=[]
        claseC=[]
        redes=f.readlines()
        for i in redes:
            red=i.strip().split("/")
            mascara=red[1]
            if mascara == "8":
                claseA.append(i.strip())
            elif (mascara=="16"):
                claseB.append(i.strip())
            else:
                claseC.append(i.strip())
        print("Redes Clase A: ")
        for i in claseA:
            print(i)
        print()
        print("Redes Clase B: ")
        for i in claseB:
            print(i)
        print()
        print("Redes Clase C: ")
        for i in claseC:
            print(i)
except FileNotFoundError:
    print("Error, el fichero no es correcto")

#EJERCICIO 11
def datosValidos(fichero):
    try:
        with open(fichero,'r') as f:
            linea=" "
            validos=[]
            invalidos=0
            total=0
            while(linea!= ""):
                linea=f.readline().strip()
                try:
                    validos.append(float(linea))
                    total+=float(linea)
                except:
                    invalidos+=1
            print("Número de datoa válidos:",len(validos))
            print("Número de datoa inválidos:",invalidos)
            print("Mínimo:",min(validos))
            print("Máximo:",max(validos))
            print("Media aritmética:",total/len(validos))
    except FileNotFoundError:
        print("Error, el fichero no es correcto")

datosValidos("datos.txt")
#EJERCICIO 12
import re
def validarSoluciones(fichero):
    try:
        with open(fichero,'r') as f:
            patron=r"([ABCD], ){9}[ABCD]"
            linea=f.readline().strip()
            if re.fullmatch(patron,linea):
                return True
            else:
                return False
    except FileNotFoundError:
        print("Error, el fichero no es correcto")

def corregirExamen(ficheroSoluciones,ficheroRespuestas):
    if validarSoluciones(ficheroSoluciones):
        try:
            with open(ficheroSoluciones, 'r') as f:
                linea=f.readline().replace(" ","").strip()
                linea=linea.split(",")

            with open(ficheroRespuestas,'r') as fi:
                patron=r"[A-Za-z]+ [A-Za-z]+: ([ABCD], ){9}[ABCD]"
                examen=" "

                while(True):
                    nota=0
                    examen=fi.readline()
                    if examen=="":
                        break
                    examen=examen.strip()
                    if re.fullmatch(patron,examen):
                        examen=examen.split(":")
                        respuesta=examen[1].split(",")
                        for i in range (len(respuesta)):
                            if linea[i]==respuesta[i]:
                                print(respuesta[i])
                                print(linea[i])
                                nota+=1
                            else:
                                nota-=0.2
                        print(examen[0],":",round(nota,2))

        except FileNotFoundError:
            print("Error al abrir fichero")

    else:
        print("Fichero de soluciones no válido.")
corregirExamen("soluciones.txt","respuestas.txt")

"""
#EJERCICIO 13
nombre=input("Introduce el nombre: ")
try:
    with open("usuarios",'r') as f:
        lineas=f.readlines()
        lineas=lineas.strip().split(":")
        usuario=lineas[0]
        contrseña=lineas[1]
        d=dict()
        for i in range (len(usuario)):
            d=(usuario[i]=contrseña[i])


        d=dict(usuario=contraseña)







except:
        print("Fichero de soluciones no válido.")



