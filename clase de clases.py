class Personaje:
    def __init__(self, nombre, hp, dano, habilidades):
        self.nombre = nombre
        self.hp =hp
        self.dano= dano
        self.habilidades = habilidades

    
    def saludar(self):
        print(f"hola, mi nombre es {self.nombre} y puedo: {self.habilidades}")

orco = Personaje("orco", 100, 20, ("salto", "ataque especial", "curacion", "metamorfosis"))

orco.saludar()