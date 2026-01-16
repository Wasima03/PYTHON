import re
try:
    with open("telefonos.txt","rt+") as fichero:
        lineas=fichero.readlines()

        patron=r"[678][0-9]{8}-[678][0-9]{8}-[0-9]+"
        patron2=r"[678][0-9]{8}-00[0-9]{11}-[0-9]+"

        factura = open("facturas.txt","wt")

        for i in range(len(lineas)):
            lineas[i] = lineas[i].replace('\n', '')
            if(re.fullmatch(patron,lineas[i])) or (re.fullmatch(patron2,lineas[i])):
                factura.write(lineas[i]+"\n")
except:
    print("Error, el fichero no existe")
