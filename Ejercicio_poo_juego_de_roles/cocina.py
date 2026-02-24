

from tomate import Tomate
from cebolla import Cebolla
from cuchillo import Cuchillo
from olla import Olla
from pasta import Pasta


class Cocina:
    def __init__(self):
        self.cebolla = Cebolla("Cebolla", 100, True)
        self.tomate = Tomate("Tomate", 100, "Crudo")
        self.cuchillo = Cuchillo(100, "Imuxa")
        self.olla = Olla(5)
        self.pasta = Pasta()

    def iniciar(self):

        print(" Bienvenido a la Estación de Batalla: Cocina ")

        
        while self.cebolla.esta_vivo():
            opcion = input("1.Cortar Cebolla  2.Afilar: ")

            if opcion == "1":
                self.cuchillo.cortar(self.cebolla)
            elif opcion == "2":
                self.cuchillo.afilar()

    
        while self.tomate.esta_vivo():
            opcion = input("1. Cortar Tomate  2. Afilar: ")

            if opcion == "1":
                self.cuchillo.cortar(self.tomate)
            elif opcion == "2":
                self.cuchillo.afilar()

        print(" Ingredientes listos. Pasando a la olla...")

        self.olla.agregar("Cebolla")
        self.olla.agregar("Tomate")

        print(" Comienza el hervvir ")

        
        while not self.pasta.esta_lista():
            decision = input("¿Deseas seguir hirviendo? (si/no|): ")

            if decision.lower() == "si":
                self.pasta.hervir()
            else:
                print(" La pasta quedó cruda.")
                return

        print(" ¡Combate culinario finalizado! Pasta servida con éxito.")