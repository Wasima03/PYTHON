import re
def validar(num):
    patron=r"[0-9]+"
    valido=False
    if re.fullmatch(patron,num):
        valido=True
    return valido

def esconderPin(pin):
    numeros=[]
    linea="XXXXXXXXXX"
    lista=[]
    for i in pin:
        numeros.append(i)
    for num in numeros:
        match num:
            case "1": lista.append("0XXXXXXXXX")
            case "2": lista.append("X0XXXXXXXX")
            case "3": lista.append("XX0XXXXXXX")
            case "4": lista.append("XXX0XXXXXX")
            case "5": lista.append("XXXX0XXXXX")
            case "6": lista.append("XXXXX0XXXX")
            case "7": lista.append("XXXXXX0XXX")
            case "8": lista.append("XXXXXXX0XX")
            case "9": lista.append("XXXXXXXX0X")
            case "0": lista.append("XXXXXXXXX0")
    tupla=tuple(lista)
    return tupla

pin="6240"
valido=validar(pin)
if(valido):
    tupla=esconderPin("6240")
    for i in tupla:
        if(i!="(" or i!=")" or i!="'"):
            print(i,end=" ")
            print()
else:
    print("Número no válido")
