from zope.interface.common.interfaces import IValueError
"""
try:
    denominador=int(input("Introduce el denominador:"))
    x=45/denominador
    print(x)
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("No puedo convertirlo a entero")
except:
    print("Excepción no reconocida")
else: #solo se ejecuta cuando no hay excepciones
    print("No ha ocurrido ninguna excepción")

finally:
    print("Haya o no haya excepción")
print("Fin del programa")

n=int(input("Introduce un núemero entero positivo"))
if n<0:
   raise Exception("No es un entero positivo") #forzamos una excepcion nosotros/sale la excepcion pero con el mensaje
print(n)

y=int(input("Introduce un núemero entero positivo"))
#raise ZeroDivisionError("NO has dividido por cero pero yo lo digo")  # lanzo una excepcion que existe pero no ocurre de verdad

x=int(input("Introduce un núemero entero positivo"))
assert (x!=5 and n>0),"El número no es igual a 1" #si no es igual que 1 salta la excepcion(cuando es falso), puedo poner un mensaje o no o parentesiss o no
"""

nombre="Wasima"
edad=19
sueldo=2500.567
ficha=f"""
Ficha de profesor
=================
Nombre: {nombre}
Edad: {edad} años
Sueldo: {sueldo:.2f} euros
=================
"""
print(ficha)



print("Mi nombre es",nombre,"tengo",edad,"años y cobro",sueldo)
print("Mi nombre es %s tengo %d años y cobro %.2f euros" %(nombre,edad,sueldo)) #printf
print(f"Mi nombre es {nombre} tengo {edad} años y cobro {sueldo:.2f} euros") #f-Stringa / el .2f es para redondear
promedio=0.67532
print(f"El porcentaje de aprobados es de {promedio:.4%}") #me hace directamente el porcentaje del número multiplicando por cien
poblacion=1234567890
print(f"La poblacion del pais es de {poblacion:,} habitantes") #separa las cifras segun el signo que pongas(el punto no funciona)




n1=23
n2=456
n3=1
lista=[1,2,3]
def devuelveMINombre():
    return "Wasima"
print(f"Números: \n{n1:04d}\n{n2:04d}\n{n3:04d}")
print(f"Justificado a la izquierda: ***{n1:<20}***") #el < es a la izquierda 20 espacios
print(f"Justificado a la derecha: ***{n1:>20}***") #el > es a la derecha
print(f"Justificado al centro: ***{n1:^20}***")
print(f"Inspeccionano variables {n1=} y {n2=}") #aparece el nobre de la variable y su valor
print(f"Con listas: {lista=}")
print(f"Mi nombre es {devuelveMINombre()}")



print(f"¿n1 es par? {True if n1%2==0 else False}")
print(F"¿n2 es par? {'Si' if n2%2==0 else 'No'}")
nota=10
print(f"Nota: {'Excelente' if nota>8 else 'Suficiente' if nota>5 else 'Suspenso'}")









