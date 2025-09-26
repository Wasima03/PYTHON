texto ="Hola mundo"
print(len(texto))
print(texto[3:8])
print(texto[:8])
print(texto[3:])
print(texto[-2])

cadena = str(3456.5)
print(cadena)

print(texto.upper())
texto=texto.upper()
print(texto.lower())
print(texto.swapcase())
texto="Hola mundo"

print(texto[2:].find("o"))
print(texto.count("o"))
print(texto.count("x"))
print(texto.replace("o","x"))
print(texto.replace("do","x"))
print(texto.replace("o","x"))
print(texto.replace("o","x",1))
texto=texto[0:2] + texto[2:].replace("o","x")
print(texto)



#for c in texo:
 #print(c)

 #for i in range (0,len(texto)):
  #   print(i,"-",texto[i])


