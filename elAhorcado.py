#1
textoOriginal = input("Introduce una frase: ")
# convertimos a minúsculas por si acaso aunque el enunciado no lo pide
textoOriginal = textoOriginal.lower()
letra = input("Letra a mantener: ")
textoAhorcado="" # En esta string construiremos la frase a mostrar en pantalla
for caracter in textoOriginal:
    if caracter==letra or caracter == " ": #si es igual a la letra a conservar o espacio lo copiamos igual
        textoAhorcado += caracter
    else: # y, si no, ponemos un asterisco
        textoAhorcado += "*"
print("Resultado: ", textoAhorcado)


#2
textoOriginal = input("Introduce una frase: ")
textoOriginal = textoOriginal.lower()
letra = input("Letra a mantener: ")
textoAhorcado=""
for caracter in textoOriginal:
    if caracter==letra or caracter == " ":
        textoAhorcado += caracter
    else:
        textoAhorcado += "*"
print("Resultado: ", textoAhorcado)
# turno del jugador. Le pedimos una letra
letra = input("Introduce una letra: ")
# contamos cuantas veces aparece
veces = textoOriginal.count(letra)
print("La letra", letra, "aparece en", veces, "ocasiones")
if veces!=0: # si la letra que hemos elegido no aparece no hacemos nada
    # textoNuevo será la nueva string a mostrar
    textoNuevo = ""
    for i  in range(0,len(textoOriginal)):
        if textoOriginal[i] == letra: # si la letra nueva aparece la metemos en textoNuevo
            textoNuevo += letra
        else:
            textoNuevo+= textoAhorcado[i] # y, si no, metemos el texto modificado que tendrá un asterisco o la letra a mantener
    print("Resultado:", textoNuevo)


#3
textoOriginal = input("Introduce una frase: ")
# convertimos a minúsculas por si acaso
textoOriginal = textoOriginal.lower()
letra = input("Letra a mantener: ")
textoAhorcado=""
for caracter in textoOriginal:
    if caracter==letra or caracter == " ":
        textoAhorcado += caracter
    else:
        textoAhorcado += "*"
print("Resultado: ", textoAhorcado)
intentos=0
# Necesitamos un bucle para repetir intentos y una variable booleana que nos dirá cuando hemos terminado
acertado=False
while acertado==False:
    letra = input("Introduce una letra: ")
    veces = textoOriginal.count(letra)
    intentos+=1
    print("La letra", letra, "aparece en", veces, "ocasiones")
    if veces!=0:
        textoNuevo = ""
        for i in range(0,len(textoOriginal)):
            if textoOriginal[i] == letra:
                textoNuevo += letra
            else:
                textoNuevo+= textoAhorcado[i]
        asteriscos = 0
        # podríamos haberlo hecho antes, pero lo ponemos en un segundo recorrido para que quede mas claro
        # si quedan asteriscos en el texto es que no hemos terminado
        for c in textoNuevo:
            if c == "*":
                asteriscos+=1
        if asteriscos==0:
            acertado = True
        textoAhorcado = textoNuevo
        print("Resultado:", textoNuevo)
print("Haz ganado. Haz necesitado", intentos, "intentos para completar la frase")

