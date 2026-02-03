class Pokemon:
    def __init__(self, numero, nombre):
        self.numero = numero
        self.nombre = nombre
        self.de = None        # Pokemon del que evoluciona
        self.en = None        # Pokemon al que evoluciona
        self.tipos = []       # Lista de tipos

    # Método para definir evolución
    def evoluciona(self, otro_pokemon):
        self.en = otro_pokemon
        otro_pokemon.de = self

    # Método para añadir tipos (uno o varios)
    def tipo(self, tipo_nombre):
        if tipo_nombre not in self.tipos:
            self.tipos.append(tipo_nombre)

    # Método para mostrar información
    def mostrar(self):
        print(f"{self.numero}. {self.nombre}")
        if self.de:
            print(f"- Evoluciona de {self.de.nombre}")
        else:
            print("- No se conoce de donde evoluciona")
        if self.en:
            print(f"- Evoluciona en {self.en.nombre}")
        else:
            print("- No se conoce a donde evoluciona")
        print(f"- Tipos: {', '.join(self.tipos)}\n")
