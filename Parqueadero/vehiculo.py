class Vehiculo:

    def __init__(self, placa, tipo_carro, color):
        self.__placa = placa
        self.__tipo_carro = tipo_carro
        self.__color = color

    def get_placa(self):
        return self.__placa

    def get_tipo_carro(self):
        return self.__tipo_carro

    def get_color(self):
        return self.__color