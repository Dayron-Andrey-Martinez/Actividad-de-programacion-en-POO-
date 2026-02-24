from datetime import datetime

class Calculadora:

    def __init__(self, tipo_operacion, usuario):
        self.__tipo_operacion = tipo_operacion
        self.__usuario = usuario
        self.__resultado = None
        self.__fecha = datetime.now()

    def get_tipo_operacion(self):
        return self.__tipo_operacion

    def get_fecha(self):
        return self.__fecha

    def realizar_operacion(self, num1, num2):

        if self.__tipo_operacion == "suma":
            self.__resultado = num1.get_valor() + num2.get_valor()

        elif self.__tipo_operacion == "resta":
            self.__resultado = num1.get_valor() - num2.get_valor()

        elif self.__tipo_operacion == "multiplicacion":
            self.__resultado = num1.get_valor() * num2.get_valor()

        elif self.__tipo_operacion == "division":
            if num2.get_valor() != 0:
                self.__resultado = num1.get_valor() / num2.get_valor()
            else:
                return "Error: division por cero"

        return self.__resultado

    def mostrar_info(self):
        return f"""
Usuario: {self.__usuario.get_nombre()}
Cedula: {self.__usuario.get_cedula()}
Operacion: {self.__tipo_operacion}
Resultado: {self.__resultado}
Fecha: {self.__fecha}
"""