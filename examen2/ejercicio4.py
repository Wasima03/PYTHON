import re
from sympy import false
try:
    ip=input("Introduce una dirección IP: ")
except ValueError:
    print("Error al introducir datos")
patron=r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
valido=False
#VALIDACIÓN DE LA IP
if re.fullmatch(patron, ip):
    valido=True
else:
    print("Formato de dirección no válido")
if(valido):
    primerByte=""
    for i in ip:
        if(i!="."):
            primerByte+=i
        else:
            break
    primerByte=int(primerByte)
    match primerByte:
        case primerByte if primerByte>=0 and primerByte <=127:
            print(ip,"/8")
        case primerByte if primerByte >= 128 and primerByte <= 191:
            print(ip, "/16")
        case primerByte if primerByte >= 192 and primerByte <= 223:
            print(ip, "/24")
        case primerByte if primerByte >= 224 and primerByte <= 225:
            print("Dirección reservada")
        case _:
            print("Dirección no válida")

