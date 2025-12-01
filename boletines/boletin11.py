class Pokemon:

    lista={"Normal","Agua","Fuego","Planta","Volador","Lucha","Veneno","Eléctrico","Tierra","Roca","Psíquico","Hielo","Bicho","Fantasma","Dragón"}
    def __init__(self,codigo,nombre,tipos,evolucion):
        if 1<= codigo <=151:
            self.codigo=codigo
        else:
            self.codigo=1

        self.nombre=nombre

        if 1<= len(self.lista & set(tipos)) <=2:
            self.tipos=tipos
        else:
            self.tipos="Normal"
        self.evolucion=evolucion

    def getCodigo(self):
        return (self.codigo)
    def getNombre(self):
        return (self.nombre)
    def getTipos(self):
        return(self.tipos)
    def evoluciona(self):
        return (self.evolucion)

pokemon = Pokemon(1, "Bulbasaur", ["Planta", "Veneno", "Fuego", "Magia"],"jo")
print(pokemon.getTipos())
pokemon2 = Pokemon(2, "Bulbasaur", ["Fuego", "Agua"],pokemon.getCodigo())
print(pokemon2.getTipos())
print(pokemon2.getNombre())
print(pokemon2.getCodigo())
print(pokemon2.evoluciona())

class Manga:
    genero={"shonen", "shojo", "seinen", "josei", "kodomo", "yuri", "spokon", "isekai" , "hentai"}
    def __init__(self,autor,genero,numero,*titulos):
        self.autor=autor
        self.numero=numero
        if(1<=len(titulos)<=2):
            self.titulos=titulos
        if(len(self.genero & set(genero))==1):
            self.genero=genero

    def getAutor(self):
        return (self.autor)
    def getGenero(self):
        return (self.genero)
    def getNumero(self):
        return (self.numero)
    def getTitulos(self):
        return (self.titulos)
    def setNumero(self,num):
        self.numero=num
    def __add__(self, titulo):
        self.titulos=self.titulos+titulo




