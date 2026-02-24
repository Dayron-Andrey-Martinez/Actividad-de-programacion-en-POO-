

class Cuchillo:
    def __init__(self, filo, marca):
        self.filo = filo
        self.marca = marca

    def get_filo(self):
        return self.filo

    def esta_afilado(self):
        return self.filo > 0

    def afilar(self):
        self.filo = 100
        print(" El cuchillo ha sido afilado al 100%")

    def cortar(self, ingrediente):
        if not self.esta_afilado():
            print(" El cuchillo está inútil. Debes afilarlo.")
            return

        nueva_vida = ingrediente.get_vida() - 50
        ingrediente.set_vida(nueva_vida)

        self.filo -= 25
        if self.filo < 0:
            self.filo = 0

        print(f"Cortando   Filo actual: {self.filo}%")

        if not ingrediente.esta_vivo():
            ingrediente.morir()