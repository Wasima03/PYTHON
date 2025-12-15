#1

def mostrarDatos(diccionario):
    for clave,valor in diccionario.items():
        print(clave.replace(",",""), "(", valor, ")")

def addCliente(diccinario,nombre,apellido,edad):
    pass




clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }
print(clientes["Chuletón, José"])
mostrarDatos(clientes)

