class Vehiculo:
    def __init__(self,nombre):
        self.nombre=nombre

    def num_ruedad(self):
        pass

class Motochicleta(Vehiculo):
    def __init__(self):
        super().__init__("MOTOCICLETA")
    
    def num_ruedad(self):
        return 2

moto=Motochicleta()
print("NUMERO DE RUEDAS")
print(moto.num_ruedad())