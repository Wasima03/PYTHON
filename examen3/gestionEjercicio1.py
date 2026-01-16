from examen3.ejercicio1 import Vehiculo, Coche, Moto, Conductor

conductor1=Conductor("Wasima El Ouastani Aznag","49998076K",2006,2024,10)
coche = Coche("6310nxb",2024,conductor1)
coche.getVehiculo()
coche.getConductor()
coche.getSeguroTodoRiesgo()
coche.getSeguroTerceros()

moto = Moto("6310nxb",2024,conductor1)
moto.getVehiculo()
moto.getConductor()
moto.getSeguroTodoRiesgo()
moto.getSeguroTerceros()