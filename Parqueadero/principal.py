from usuario import Usuario
from vehiculo import Vehiculo
from parqueadero import Parqueadero

registros = []  

print(" PARQUEADERO ")

while True:

    print("\n 1. Registrar Entrada")
    print("2. Registrar Salida")
    print("3. Ver Tabla")
    print("4. Salir")

    op = input("Opción: ")

    if op == "1":
        
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        tipo_usuario = input("Tipo Usuario: ")
        usuario = Usuario(cedula, nombre, tipo_usuario)

        
        placa = input("Placa: ")
        tipo_carro = input("Tipo Carro: ")
        color = input("Color: ")
        vehiculo = Vehiculo(placa, tipo_carro, color)

       
        puesto = input("Puesto: ")

        registro = Parqueadero(usuario, vehiculo, puesto)
        registros.append(registro)

        print(" Entrada registrada")

    elif op == "2":
        placa_buscar = input("Placa para salida: ")

        for r in registros:
            if r.mostrar_fila()[3] == placa_buscar:
                r.registrar_salida()
                print(" Salida registrada")

    elif op == "3":
        print("\n--- TABLA ---")
        for r in registros:
            print(r.mostrar_fila())

    elif op == "4":
        break