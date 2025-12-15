#1

matriz=[[1,2],[3,4],[5,6]]
traspuesta=[]

print(len(matriz))
print(len(matriz[1]))
print(matriz[0])
print(matriz[1])
print(traspuesta)

for i in range (len(matriz)):
    for j in range (len(matriz[0])):
        traspuesta.append(matriz[j][i])
print(traspuesta)

#2
valida=False
min=False
may=False
num=False
simbolo=False
simbolos = {"_","-", "!", "?", "*"}

while(not valida):
    pasword = input("Introduce una contrseña")
    for i in pasword:
        if i.islower():
            min=True
        elif i.isupper():
            may=True
        elif i.isdigit():
            num=True
    if len(set(pasword) & simbolos)>=1:
        simbolo=True
    if (8 <= len(pasword) <= 20):
        if (min and may and num and simbolo):
            valida=True
            print("Contrseña valida")


#3
mensaje = input("Escribe tu mensaje secreto: ")

cifrado = ""
inicio = 0
fin = len(mensaje) - 1

while inicio <= fin:
    cifrado += mensaje[fin]
    if inicio != fin:
        cifrado += mensaje[inicio]
    inicio += 1
    fin -= 1

print(cifrado)

#4

import random

mensaje = input("Escribe tu mensaje secreto: ")

cifrado = ""
inicio = 0
fin = len(mensaje) - 1

while inicio <= fin:
    # Carácter del final
    caracter = mensaje[fin]
    if caracter.isalpha():
        if random.choice([True, False]):
            caracter = caracter.upper()
        else:
            caracter = caracter.lower()
    cifrado += caracter

    # Carácter del inicio (si no es el mismo)
    if inicio != fin:
        caracter = mensaje[inicio]
        if caracter.isalpha():
            if random.choice([True, False]):
                caracter = caracter.upper()
            else:
                caracter = caracter.lower()
        cifrado += caracter

    inicio += 1
    fin -= 1

print("Mensaje cifrado:", cifrado)


#5

mensaje_cifrado = input("Introduce el mensaje cifrado: ")

resultado = [""] * len(mensaje_cifrado)
inicio = 0
fin = len(mensaje_cifrado) - 1
i = 0

while inicio <= fin:
    # Carácter que venía del final
    resultado[fin] = mensaje_cifrado[i]
    i += 1

    # Carácter que venía del principio (si existe)
    if inicio != fin:
        resultado[inicio] = mensaje_cifrado[i]
        i += 1

    inicio += 1
    fin -= 1

mensaje_descifrado = "".join(resultado).upper()

print("Mensaje descifrado:", mensaje_descifrado)

#6
# Leer la frase
frase = input("Introduce un texto: ")

# Construir la frase limpia sin espacios y en minúsculas
frase_limpia = ""
for caracter in frase:
    if caracter != " ":
        frase_limpia += caracter.lower()

# Comprobar si es palíndromo
if frase_limpia == frase_limpia[::-1]:
    print("El texto introducido es un palíndromo")
else:
    print("El texto introducido NO es un palíndromo")


#7

# Lectura del número desde teclado
numero = int(input("Introduce un número: "))

# Convertimos el número a cadena para poder contar dígitos y recorrerlos
numero_str = str(numero)
num_digitos = len(numero_str)

# Calculamos la suma de cada dígito elevado al número de dígitos
suma = 0
for digito in numero_str:
    suma += int(digito) ** num_digitos

# Comprobamos si la suma coincide con el número original
if suma == numero:
    print(f"El número {numero} es narcisista")
else:
    print(f"El número {numero} no es narcisista")




