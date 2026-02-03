#EJERCICIO 1

try:
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



#EJERCICIO 13
nombre=input("Introduce el nombre: ")
password = input("Introduce la contraseña: ")
try:
    with open('usuarios.txt', 'r') as f:
        d=dict()
        usuarios=[]
        contraseñas=[]
        lineas=f.readlines()
        if len(lineas)>0:
            for i in lineas:
                datos=i.strip().split(":")
                usuarios.append(datos[0])
                contraseñas.append(datos[1])
            for i in range (len(usuarios)):
                d[usuarios[i]]=contraseñas[i]

            userEncontrado=False
            for clave,valor in d.items():
                if clave==nombre:
                    userEncontrado=True
                    if valor==password:
                        print("Usuario y contraseña válidos.")
                    else:
                        print("Contraseña no válida.")
            if(userEncontrado==False):
                    print("Usuario no encontrado.")
        else:
            print("Fichero vacío.")
except:
        print("Fichero inexistente o imposible acceder a él.")

#EJERCICIO 14
def grabarCuenta(user, password):
    try:
        with open("usuarios.txt",'a') as f:
            f.write("\n"+user+":"+password)
    except:
        print("Fichero inexistente o imposible acceder a él.")

nombre = input("Introduce el usuario: ")
password1=input("Introduce la contraseña: ")
password2=input("Vuelve a introduce la contraseña: ")

if password1==password2:
    print("Cuenta de usuario grabada correctamente.")
    grabarCuenta(nombre,password1)
else:
    print("Las contraseñas no son iguales. No se puede grabar la nueva cuenta.")

from boletines.Consideraciones import Consideraciones

#EJERCICIO 15
try:
    with open("usuarios.txt",'r') as f:
        lineas = f.readlines()
        for i in lineas:
            c=Consideraciones(i)
            print("Nombre:",c.getUser())
            print("Contraseña:",c.getPassword())
            print("Fortaleza de la contraseña:",c.getSolidez(),"\n")
except:
    print("Fichero inexistente o imposible acceder a él.")

from boletines.Consideraciones import Consideraciones

#EJERCICIO 16
try:
    with open("usuarios.txt",'r') as f:
        listaObjetos=[]
        lineas = f.readlines()
        for i in lineas:
            c=Consideraciones(i)
            listaObjetos.append(c)
    with open("login.bin","wb") as f2:
        print("Fichero origen: ",f)
        print("Fichero destino:",f2)
        print("Número:",len(listaObjetos))
        print("Listado: ")

        for i in listaObjetos:
            cadena=("Nombre:"+i.getUser()+"\n"+"Contraseña:"+i.getPassword()+"\n"+"Fortaleza de la contraseña:"+i.getSolidez()+"\n"+"\n")
            f2.write(cadena.encode())
    with open("login.bin","rb") as f3:
        contenido=f3.read().decode()
        print(contenido)
except:
    print("Fichero inexistente o imposible acceder a él.")

#EJERCICIO 17
import re
try:
    patron=re.compile(r"^"
    r"([A-Za-z]+(?: [A-Za-z]+)*), "
    r"([A-Za-z]+(?: [A-Za-z]+)*)"
    r";"
    r"([A-Za-z0-9 ]+)"
    r";"
    r"(\d+(?:\.\d+)?)"
    r"$")

    with open("trabajadores.txt","r",encoding="UTF-8") as f:
        lineas = f.readlines()
    with open("trabajadoresValidos.txt","w+") as f2:
        for i in lineas:
            i=i.strip()
            if re.fullmatch(patron,i):
                f2.write(i+"\n")
            else:
                print(i)
except:
    print("Fichero inexistente o imposible acceder a él.")

#EJERCICIO 18
try:
    with open("trabajadoresValidos.txt", "r",encoding="UTF-8") as f:
        lineas = f.readlines()
    with open("trabajadoresValidos.txt","a") as f2:
        for i in lineas:
            i = i.strip().split(";")
            datos=i[0].split(",")
            nombre=datos[0]
            apellido=datos[1]

            while(True):
                edad= int(input(nombre + "," + apellido + ".Edad: "))
                if edad > 18 and edad < 67:
                    break;
            f2.write(";"+str(edad))

except:
    print("Fichero inexistente o imposible acceder a él.")


#ALTERNATIVA PARA QUE LAS EDADES SE AÑADAN AL FINAL DE CADA LINEA Y NO AL FINAL DEL FICHERO
#HAY QUE LEER, MODIFICAR Y LUEGO SOBREESCRIBIR

try:
    with open("trabajadoresValidos.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    nuevas_lineas = []

    for linea in lineas:
        linea = linea.strip()
        partes = linea.split(";")

        datos = partes[0].split(",")
        apellido = datos[0].strip()
        nombre = datos[1].strip()

        while True:
            edad = int(input(nombre + " " + apellido + ". Edad: "))
            if 18 < edad < 67:
                break
            else:
                print("Edad no válida (19-66).")

        nuevas_lineas.append(linea + ";" + str(edad) + "\n")

    # Sobrescribimos el fichero
    with open("trabajadoresValidos.txt", "w", encoding="utf-8") as f:
        f.writelines(nuevas_lineas)

except FileNotFoundError:
    print("Fichero inexistente o imposible acceder a él.")
except ValueError:
    print("La edad debe ser un número.")

from boletines.Empleado import Empleado

#EJERCICIO 19
try:
    with open("trabajadoresValidos.txt","r",encoding="UTF-8") as f:
        lineas=f.readlines()
        for i in lineas:
            i=i.strip()
            e = Empleado(i)
            print(e.mostrar())

except FileNotFoundError:
    print("Fichero inexistente.")

#EJERCICIO 20
import pickle
from boletines.Empleado import Empleado
def grabarEmpleado(fichero,empleado):
    try:
        with open(fichero,"ab") as f:
            pickle.dump(empleado,f)
        with open(fichero,"rb") as f:
            try:
                while(True):
                    objeto=pickle.load(f)
                    print(objeto.mostrar())
            except EOFError: #END OF FILE
                pass
    except FileNotFoundError:
        print("Fichero inválido.")

e=Empleado("Wasima, El Ouastani Aznag; Programadora Junior; 3450;20")
grabarEmpleado("nuevo.bin",e)

#EJERCICIO 21
import re
entrada="pokemon_in.txt"
salida="pokemon_out.txt"
validos=0
patron=r"^[A-Za-z .]+$"
try:
    pokemons=[]
    with open(entrada,"r") as f:
        lista=f.readlines()
    with open(salida,"w") as f2:
        for i in lista:
            pokemons=i.strip().split("; ")
            if len(pokemons) >3:
                print("Número de pokemons excedido en linea:",i)
            else:
                for p in pokemons:
                    datos=p.split(" ")
                    num=datos[0]
                    nombre=datos[1]
                if int(num) >1 and int(num)<151:
                    if re.fullmatch(patron,nombre):
                        f2.write(i)
                        validos+=1
                    else:
                        print("El nombr del pokemon no es válido en linea: ",i)
                else:
                    print("Número de pokemon no válidoen linea: ",i)
        print("Pokemons correctos: ",validos)
except FileNotFoundError:
    print("Error fichero.")

#EJERCICIO 22
# Fichero de entrada
entrada = "pokemon_in.txt"

# Diccionario principal: clave = número o nombre en minúsculas
pokedex = {}

# Leer el fichero y construir la pokedex
with open(entrada, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea:
            continue

        pokemons = []
        partes = linea.split("; ")
        for idx, p in enumerate(partes):
            num_str, nombre = p.split(" ", 1)
            num = int(num_str)
            # Evoluciona de y evoluciona en
            de = None if idx == 0 else partes[idx-1]
            en = None if idx == len(partes)-1 else partes[idx+1]

            # Guardar info en diccionario
            info = {"num": num, "nombre": nombre, "de": de, "en": en}
            # Clave por número
            pokedex[num] = info
            # Clave por nombre en minúsculas
            pokedex[nombre.lower()] = info

# Función para mostrar la información de un Pokémon
def mostrar_pokemon(entrada_usuario):
    # Determinar si es número o nombre
    if entrada_usuario.isdigit():
        clave = int(entrada_usuario)
    else:
        clave = entrada_usuario.lower()

    if clave in pokedex:
        p = pokedex[clave]
        print(f"{p['nombre']}. Su número de la Pokedex es {p['num']}")
        # Evoluciona de
        if p["de"]:
            num_de, nombre_de = p["de"].split(" ", 1)
            print(f"Evoluciona de {nombre_de} ({num_de})", end=". ")
        else:
            print("No evoluciona de ningún otro.", end=". ")
        # Evoluciona en
        if p["en"]:
            num_en, nombre_en = p["en"].split(" ", 1)
            print(f"Evoluciona en {nombre_en} ({num_en})")
        else:
            print("No evoluciona a ningún otro")
    else:
        print("Ese Pokemon no está registrado en la pokedex")

# Interacción con el usuario
while True:
    entrada_usuario = input("Introduce el pokemon en el que estás interesado: ").strip()
    if entrada_usuario.lower() == "exit":
        print("Gracias por consultar la pokedex")
        break
    # Validar entrada
    if entrada_usuario.replace(" ", "").replace(".", "").isalpha() or entrada_usuario.isdigit():
        mostrar_pokemon(entrada_usuario)
    else:
        print("Eso no parece corresponder a un nombre de pokemon o código de la pokedex")

from boletines.Pokemon import Pokemon

#EJERCICIO 23
# Crear pokemons
pokemon1 = Pokemon(10, "Caterpie")
pokemon2 = Pokemon(11, "Metapod")
pokemon3 = Pokemon(12, "Butterfree")

# Definir evoluciones
pokemon1.evoluciona(pokemon2)
pokemon2.evoluciona(pokemon3)

# Definir tipos
pokemon1.tipo("Bicho")
pokemon2.tipo("Bicho")
pokemon3.tipo("Bicho")
pokemon3.tipo("Volador")

# Mostrar información
pokemon1.mostrar()
pokemon2.mostrar()
pokemon3.mostrar()

#EJERCICIO 24
import pickle
import os

def grabarFichero(fichero, *pokemons):
    lista_total = []

    # Leer el fichero si existe y tiene contenido
    if os.path.exists(fichero) and os.path.getsize(fichero) > 0:
        try:
            with open(fichero, "rb") as f:
                lista_total = pickle.load(f)
        except:
            print("Error: fichero inválido o corrupto")
            return

    # Añadir los nuevos Pokémon
    lista_total.extend(pokemons)

    # Guardar todo de nuevo
    with open(fichero, "wb") as f:
        pickle.dump(lista_total, f)

import random

def combate(fichero):
    # Comprobar existencia y contenido
    if not os.path.exists(fichero):
        print("Error: fichero no encontrado")
        return

    try:
        with open(fichero, "rb") as f:
            lista = pickle.load(f)
    except:
        print("Error: contenido inválido")
        return

    if len(lista) < 4:
        print("Error: se necesitan al menos 4 pokemons para el combate")
        return

    # Elegir 4 Pokémon distintos
    seleccionados = random.sample(lista, 4)

    jugador1 = seleccionados[:2]
    jugador2 = seleccionados[2:]

    print(f"El jugador 1 combate con {jugador1[0]} y {jugador1[1]}")
    print(f"El jugador 2 combate con {jugador2[0]} y {jugador2[1]}")



