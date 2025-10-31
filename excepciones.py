from zope.interface.common.interfaces import IValueError
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