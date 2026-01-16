try:
    fichero = open('quijote.txt', 'r+')
    # a-modo para añadir y leer    #con r,w- el cursr se situa al principio, si añade machaca lo primero, lo borra y añade otra cosa
    """
    print("Posición:", fichero.tell())
    print(fichero.readline())
    print("Posición:", fichero.tell())
    fichero.seek(10,1)           #seek(offset,origen)   origen-----0(inicio), 1(posicion actual), 2(final)
    print("Posición:",fichero.tell())           #dice la posicion
    """
    print(fichero.tell())
    fichero.write("\nUna nueva linea")
    fichero.seek(0)
    print(fichero.read())


    fichero.close()
except:
    print("Error, el fichero no existe")