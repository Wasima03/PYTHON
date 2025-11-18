import math
import re
def toDecimal(numero):
    patron=r"[10]+"
    valor=-1
    v=0
    if re.fullmatch(patron,numero):
        for i in range(0,len(numero)):
            if numero[i]=="1":
                valor += math.pow(2,i)
    return valor

print(toDecimal("10110"))
print(toDecimal("345"))
print(toDecimal("hola"))
print()








