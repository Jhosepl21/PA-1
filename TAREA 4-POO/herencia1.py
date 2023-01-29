class Coche:
    def __init__(self):
        print("CONSTRUIR COCHE")

    def acelerar(self):
        print("ACELERAR")

    def frenar(self):
        print("FRENAR")
class CocheRojo(Coche):
    def __init__(self):
        print("Construyendo carro rojo")

objecto=Coche()
objecto.acelerar()
objecto.frenar()

objecto_coche_rojo=CocheRojo()
objecto_coche_rojo.acelerar()
objecto_coche_rojo.frenar()
