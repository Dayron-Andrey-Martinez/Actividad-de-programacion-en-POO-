

class Olla:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.contenido = []

    def agregar(self, ingrediente):
        if len(self.contenido) < self.capacidad:
            self.contenido.append(ingrediente)
            print(f"{ingrediente} agregado a la olla ")
        else:
            print(" La olla está llena.")

    def ver_contenido(self):
        return f"Contenido actual: {len(self.contenido)} elementos"