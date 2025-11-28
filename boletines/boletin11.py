class Pokemon:

    lista={"Normal","Agua","Fuego","Planta","Volador","Lucha","Veneno","Eléctrico","Tierra","Roca","Psíquico","Hielo","Bicho","Fantasma","Dragón"}
    def __init__(self,codigo,nombre,tipos):
        if codigo>=1 or codigo <=151:
            self.codigo=codigo
        else:
            self.codigo=1
        self.nombre=nombre
        if len(lista | tipos)>=1 or len(lista | tipos)<=2:
            self.tipos=tipos


