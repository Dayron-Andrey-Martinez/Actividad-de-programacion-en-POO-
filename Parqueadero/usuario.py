class Usuario:

    def __init__(self, cedula, nombre, tipo_usuario):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__tipo_usuario = tipo_usuario

    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre

    def get_tipo_usuario(self):
        return self.__tipo_usuario