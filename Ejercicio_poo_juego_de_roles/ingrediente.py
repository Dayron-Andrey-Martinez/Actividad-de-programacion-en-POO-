

class Ingrediente:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        
    def get_nombre(self):
        return self.nombre

    def get_vida(self):
        return self.vida

    def set_vida(self, nueva_vida):
        if nueva_vida < 0:
            self.vida = 0
        else:
            self.vida = nueva_vida

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha sido completamente procesado ")

    def ver_info(self):
        return f"Ingrediente: {self.nombre}  Vida: {self.vida}%"