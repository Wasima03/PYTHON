#EJERCICIO 1
from sympy.parsing.sympy_parser import null

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


"""for i in range (len(lista)):
    if i==0 or i%2==0:
        if lista[i] == 'Hombre':
            hombres+=1
        else:
            mujeres+=1
    else:
        t=float(lista[i])
        t+=altura
"""

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
"""
for i in cuentasValidas:
    codigosV+=1
    print("País: ",i[:2])
    print("DC: ",i[2:4])
    print("Entidad: ",i[4:8])
    print("Sucursal: ",i[8:12])
    print("Número de cuenta: ",i[13:])
print("Hay ",codigosV," correctos y ",codigos-codigosV," codigos incorrectos")
"""
#EJERCICIO 4
















