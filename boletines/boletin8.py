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