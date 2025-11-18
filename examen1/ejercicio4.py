fraccion=input("Escribe tu fracción: ")
sinBarra=fraccion.replace("/","")
numeros=[]
if (fraccion[0]=="/" or fraccion[len(fraccion)-1]=="/"  or fraccion[len(fraccion)-1]=="0"
        or fraccion.count("/")!=1 or not sinBarra.isdigit()):
    print("Fracción introducida no válida")
else:
    numeros=fraccion.split("/")
    print("EL valor de tu fracción es",round(int(numeros[0])/int(numeros[1]),3))
