#no admiten duplicados
#no tienen posiciones
#funciones que comparan dos conjuntos

profesPrimero={"Ana","Juan Carlos","Sacho","Natalia"}
print(profesPrimero)
profesSegundo = set(["Agustin","Ana","Javier","Natalia"])
print(profesSegundo)
conjuntoVacio=set()

if "Ana" in profesPrimero:
    print("Ana da clase en primero")
if "Javier" not in profesPrimero:
    print("Javier no da clase en primero")

for i in profesSegundo:
    print(i)

print(len(profesPrimero))


for i in range(0,len(profesPrimero)):
    #print(profesPrimero[i]) no se puede hacer bucles con indices
    print("hola")


profesPrimero.add("Jose Maria")
print(profesPrimero)
profesPrimero.remove("Jose Maria")
print(profesPrimero)
profesPrimero.discard("Jose Maria") #si se elimina un elemento que no existe, no da error, con remove si
print(profesPrimero)
profe=profesPrimero.pop()#extre el primer elemento del conjunto y lo elimina del principal
print(profe)
print(profesPrimero)
#profesPrimero.clear()#elimina todos los elementos
print(profesPrimero)



conjunto1=set((1,2,3,1,2,5,4,5)) #elimina los duplicados
print(conjunto1)
conjunto2=set("Hola mu ndo")
print(conjunto2)
lista = list(profesPrimero)
print(lista)
tupla = tuple(profesPrimero)
print(tupla)
texto = str(profesPrimero)
print(texto)



print(profesPrimero | profesSegundo) #union, muestran los elementos de uno y otro sin duplicados
print(profesPrimero & profesSegundo) #interseccion, muestran los elementos que tienene en comun los dos
print(profesPrimero - profesSegundo) #diferencia, aparecen los elementos de uno u oto sin los comunes, el orden afecta al resultadp
print(profesSegundo-profesPrimero)
#print(profesPrimero )

print(profesPrimero.union(profesSegundo))
print(profesPrimero.intersection(profesSegundo))
print(profesPrimero.difference(profesSegundo))
print(profesPrimero.symmetric_difference(profesSegundo))
print(profesPrimero.union(profesSegundo))



