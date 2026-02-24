
from ingrediente import Ingrediente

class Cebolla(Ingrediente):
    def __init__(self, nombre, vida, lagrimas):
        super().__init__(nombre, vida)
        self.__lagrimas = lagrimas

    def ver_info(self):
        return super().ver_info() + f"  Lagrimas: {self.__lagrimas}"