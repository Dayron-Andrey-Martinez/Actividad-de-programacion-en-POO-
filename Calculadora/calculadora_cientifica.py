from calculadora import Calculadora
import math

class CalculadoraCientifica(Calculadora):

    def __init__(self, tipo_operacion, usuario):
        super().__init__(tipo_operacion, usuario)

    def operaciones_cientificas(self):

        op = self.get_tipo_operacion()

        # AREAS
        if op == "area circulo":
            r = float(input("Radio: "))
            return math.pi * r**2

        elif op == "area rectangulo":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            return b * h

        elif op == "area triangulo":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            return (b * h) / 2

        elif op == "area cuadrado":
            l = float(input("Lado: "))
            return l**2

        # PERIMETROS
        elif op == "perimetro circulo":
            r = float(input("Radio: "))
            return 2 * math.pi * r

        elif op == "perimetro rectangulo":
            b = float(input("Base: "))
            h = float(input("Altura: "))
            return 2 * (b + h)

        elif op == "perimetro triangulo":
            a = float(input("Lado 1: "))
            b = float(input("Lado 2: "))
            c = float(input("Lado 3: "))
            return a + b + c

        elif op == "perimetro cuadrado":
            l = float(input("Lado: "))
            return 4 * l

        # VOLUMEN
        elif op == "volumen esfera":
            r = float(input("Radio: "))
            return (4/3) * math.pi * r**3

        elif op == "volumen cubo":
            l = float(input("Lado: "))
            return l**3

        elif op == "volumen cilindro":
            r = float(input("Radio: "))
            h = float(input("Altura: "))
            return math.pi * r**2 * h

        elif op == "volumen prisma":
            l = float(input("Largo: "))
            a = float(input("Ancho: "))
            h = float(input("Altura: "))
            return l * a * h

        else:
            return "Operacion no valida"