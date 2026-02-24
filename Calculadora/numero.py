class Numero:
    def __init__(self, valor):
        self.valor = valor   

   
    def get_valor(self):
        return self.valor

   
    def set_valor(self, nuevo_valor):
        if isinstance(nuevo_valor, (int, float)):
            self.alor = nuevo_valor
        else:
            print("Error: Debe ingresar un numero valido")