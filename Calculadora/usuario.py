class Usuario:

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

  
    def get_nombre(self):
        return self.nombre

    def get_cedula(self):
        return self.cedula

   
    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre != "":
            self.nombre = nuevo_nombre
        else:
            print("Nombre invalido")

    def set_cedula(self, nueva_cedula):
        if nueva_cedula != "":
            self.cedula = nueva_cedula
        else:
            print("Cedula invalida")