#1-2-3
"""
def mostrarDatos(diccionario):
    for clave,valor in diccionario.items():
        print(clave.replace(",",""), "(", valor, ")")

def nuevoCliente(diccinario,nombre,apellido,edad):
    clave=apellido+", "+nombre

    aux=diccinario.get(clave,"None")
    if aux == "None":
        diccinario[clave] = edad
        print("Cliente añadido")
    else:
        print("La clave ya existe")
        opc=input("Desea sobreescribir la edad(S/N): ")
        if opc=="S":
            diccinario[clave]=edad
            print("Edad sobreescrita")
        else:
            print("Edad no sobreescrita")

def cumpleCliente(diccionario,nombre,apellido):
    clave=apellido+", "+nombre
    valor=diccionario[clave]
    diccionario[clave]=valor+1
    print("Edad actualizada")



clientes = {"Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }
print("edad",clientes["Chuletón, José"])
mostrarDatos(clientes)
print()
#nuevoCliente(clientes, "Felpie", "Lotas", 76)
mostrarDatos(clientes)
#nuevoCliente(clientes, "Felpie", "Lotas", 70)
mostrarDatos(clientes)
cumpleCliente(clientes, "José", "Chuletón")
print(clientes)
print(clientes["Chuletón, José"])


#4
texto= input("Introduce tu texto: ")
palabras=texto.split(" ")
diccionario=dict()
for i in palabras:
   diccionario[i]=texto.count(i)
print(diccionario)
"""
#5
diccionario={"Aguacate":4.35,"Mandarina":2.60,"Kiwi":3.75,"Naranja":1.80}
print(diccionario.get("rg", False))

fruta=""
while(True):
    fruta=input("¿Qúe fruta quieres comprar? ")   #.strip().lower() #para limpiar los espacios en blanco y ponerlos en minusucula
    if fruta=="fin" or fruta=="FIN" or fruta=="Fin":
        break
    precio=diccionario.get(fruta)
    if precio is None:
        print("Lo siento mucho pero no vendemos esa fruta")
    else:
        try:
            kilos =float(input("¿Cuántos kilos quieres? "))
            print(kilos,"de",fruta,"cuestan",precio*kilos)
        except ValueError:
            print("No has introducido bien la cantidad que quieres")














