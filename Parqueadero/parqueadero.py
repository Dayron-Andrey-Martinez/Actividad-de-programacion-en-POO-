from datetime import datetime

class Parqueadero:

    def __init__(self, usuario, vehiculo, puesto):
        self.__usuario = usuario
        self.__vehiculo = vehiculo
        self.__puesto = puesto
        self.__fecha_entrada = datetime.now().strftime("%Y-%m-%d")
        self.__hora_entrada = datetime.now().strftime("%H:%M")
        self.__hora_salida = ""
        self.__estado = "Entrada"

    def registrar_salida(self):
        self.__hora_salida = datetime.now().strftime("%H:%M")
        self.__estado = "Salida"

    def mostrar_fila(self):
        return [
            self.__usuario.get_cedula(),
            self.__usuario.get_nombre(),
            self.__usuario.get_tipo_usuario(),
            self.__vehiculo.get_placa(),
            self.__vehiculo.get_tipo_carro(),
            self.__vehiculo.get_color(),
            self.__puesto,
            self.__fecha_entrada,
            self.__hora_entrada,
            self.__hora_salida,
            self.__estado
        ]