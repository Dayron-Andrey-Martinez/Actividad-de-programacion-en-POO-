

class Pasta:
    def __init__(self):
        self.coccion = 0

    def get_coccion(self):
        return self.coccion

    def hervir(self):
        self.coccion += 25
        if self.coccion > 100:
            self.coccion = 100

        print(f" Cocción actual: {self.coccion}%")

    def esta_lista(self):
        return self.coccion >= 100