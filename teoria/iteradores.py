profesores =["Agustín", "Natalia", "Javier"]
iterador = iter(profesores)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador,"NO HAY MÁS PROFES")) #cuando llegamos al final de la lista, si no hay más, podemos poner un mensaje y no salta error

class DiasDeLaSemana:
    def __init__(self,dia):
        self.dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
        self.indice=dia  #registro del dia actual
        
        
        #ATAJO PARA PONER GETTER---prop
        #ATAJO PARA PONER GETTER Y SETTER----props
        
        @property
        def indice(self):
            return 
        
        @indice.setter
        def indice(self, value):
            pass
        
        
    def mostrarDia(self):
        print(self.dias[self.indice])

    def __iter__(self): #iterador creado
        return self
    def __next__(self):
        #if self.indice>=len(self.dias):
         #   raise StopIteration
        dia_actual = self.dias[self.indice]

        if(self.indice==len(self.dias)-1):
            self.indice=0
        else:
            self.indice+=1
        return dia_actual

dia = DiasDeLaSemana(2)
#dia.mostrarDia()

iterador = iter(dia)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))