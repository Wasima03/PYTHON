matriz=[[1,2],[3,4]]
traspuesta=[]

for i in matriz:
    for j in i:
        traspuesta=[[j][i]]
        print("|",j,end=" ")
    print("|")
print(traspuesta)