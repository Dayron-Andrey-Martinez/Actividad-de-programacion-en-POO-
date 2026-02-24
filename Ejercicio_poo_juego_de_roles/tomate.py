

from ingrediente import Ingrediente

class Tomate(Ingrediente):
    def __init__(self, nombre, vida, estado):
        super().__init__(nombre, vida)
        self.estado = estado

    def ver_info(self):
        return super().ver_info() + f" Estado: {self.estado}"