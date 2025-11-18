import re

#1
#CODIGO POSTAL
cp = input("Introduce el código postal: ")
pt=r"28[0-9]{3}"
if re.fullmatch(pt,cp):
    print("Código postal válido.")
else:
    print("Código postal no válido.")
    
#2
tlf=input("Introduce un teléfono válido: ")
pt=r"91[0-9]{6}"
if re.fullmatch(pt,tlf):
    print("Teléfono válido.")
else:
    print("Teléfono no váldio.")

#3
tlf=input("Introduce un teléfono válido: ")
pt=r"[678][0-9]{8}"
if re.fullmatch(pt,tlf):
    print("Teléfono válido.")
else:
    print("Teléfono no váldio.")

#4
#TELEFONO 
tlf=input("Introduce un teléfono válido: ")
pt=r"\+[0-9]{2} [0-9]{9}"
if re.fullmatch(pt,tlf):
    print("Teléfono válido.")
else:
    print("Teléfono no váldio.")

#5
pl=input("Introduce dos palabras: ")
pt=r"[A-Z]{1}[a-zA-Z]+\s[A-Z]{1}[a-zA-Z]+"
if re.fullmatch(pt,pl):
    print("Palabras válidas.")
else:
    print("Palabras no válidas.")

#6
cl=input("Introduce una clave: ")
pt=r"[A-Z]{2}[0-9]{2}-[a-z]{2}[A-Z]-[0-9]{2}"
if re.fullmatch(pt,cl):
    print("Clave válida.")
else:
    print("Clave no válida.")

#7
#TARJETA
tc=input("Introduce tu tarjeta de crédito: ")
pt=r"[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4} (0[1-9]|1[0-2])/[0-9]{2}"
if re.fullmatch(pt,tc):
    print("Tarjeta valida.")
else:
    print("Tarjeta no valida")

#8
#ISBAN
tc=input("Introduce tu tarjeta de crédito: ")
pt=r"ES[0-9]{2} [0-9]{4} [0-9]{4} [0-9]{2} [0-9]{10}"
if re.fullmatch(pt,tc):
    print("Tarjeta valida.")
else:
    print("Tarjeta no valida")

#9
tc=input("Introduce el numero: ")
pt=r"[0-9]{4,8}"
if re.fullmatch(pt,tc):
    print("Numero valido.")
else:
    print("Numero no valido")

#IP
#10
ip=input("Introduec una IP válida: ")
pt=r"192\.168\.[0-9]{2}\.[0-9]{2}"
if re.fullmatch(pt,ip):
    print("IP valida.")
else:
    print("IP no valida")

#EXTRAS
#CORREO
ce=input("Introduce un correo válido: ")
pt=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]"
if re.fullmatch(pt,ce):
    print("Correo valido.")
else:
    print("Correo no valido")

#PASSWORD
contraseña = input("Introduce tu contraseña: ")
if len(contraseña) < 8:
    print("Contraseña demasiado corta.")
else:
    if not re.search(r"[A-Z]", contraseña):
        print("Debe contener al menos una letra mayúscula.")
    elif not re.search(r"[a-z]", contraseña):
        print("Debe contener al menos una letra minúscula.")
    elif not re.search(r"[0-9]", contraseña):
        print("Debe contener al menos un número.")
    elif not re.search(r"[!@#$%^&*()_+=\-]", contraseña):
        print("Debe contener al menos un carácter especial.")
    else:
        print("Contraseña válida y segura.")

#GPS
coord = input("Introduce coordenadas GPS (latitud, longitud): ")
patron = r"^-?\d{1,2}(\.\d+)?\s*,\s*-?\d{1,3}(\.\d+)?$"

if re.fullmatch(patron, coord):
    lat, lon = map(float, coord.split(","))
    if -90 <= lat <= 90 and -180 <= lon <= 180:
        print("Coordenadas válidas.")
    else:
        print("Coordenadas fuera de rango.")
else:
    print("Formato inválido.")


