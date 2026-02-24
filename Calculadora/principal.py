from usuario import Usuario
from numero import Numero
from calculadora import Calculadora
from calculadora_cientifica import CalculadoraCientifica

print("=== DATOS DEL USUARIO ===")
nombre = input("Nombre: ")
cedula = input("Cedula: ")

usuario = Usuario(nombre, cedula)

print("\n=== TIPO DE CALCULADORA ===")
tipo = input("Normal / Cientifica: ")

if tipo.lower() == "normal":

    print("\nOperaciones: suma, resta, multiplicacion, division")
    operacion = input("Operacion: ")

    n1 = Numero(float(input("Numero 1: ")))
    n2 = Numero(float(input("Numero 2: ")))

    calc = Calculadora(operacion, usuario)

    resultado = calc.realizar_operacion(n1, n2)

    print("Resultado:", resultado)
    print(calc.mostrar_info())

elif tipo.lower() == "cientifica":

    print("\nEjemplos:")
    print("area circulo, perimetro cuadrado, volumen cilindro...")
    operacion = input("Operacion: ")

    calc = CalculadoraCientifica(operacion, usuario)

    resultado = calc.operaciones_cientificas()

    print("Resultado:", resultado)
    print("Fecha:", calc.get_fecha())
    print("Operacion:", calc.get_tipo_operacion())

else:
    print("Tipo no valido")