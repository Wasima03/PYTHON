import re
def matriculasValidas(*matriculas):
    validas=0
    noValidas=0
    patron=r"([0-9]{4}[^[AEIOUaeiouQ_]\w{3})|([0-9]{4} [^[AEIOUaeiouQ_]\w{3})|([0-9]{4}-[^[AEIOUaeiouQ_]\w{3})"
    for matricula in matriculas:
        if re.fullmatch(patron,matricula):
            print(matricula,"es válida")
            validas+=1
        else:
            print(matricula, "no es válida")
            noValidas+=1
    print()
    print("Matrículas válidas:",validas)
    print("Matriculas no válidas:",noValidas)
matriculasValidas("22CDR","7521-MXP","1224MN","1234ADF","3456BAC","1224qnd","1234 SDF")
