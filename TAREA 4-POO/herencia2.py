class Animal:
    def __init__(self):
        print("VIDA DEL PERRO")

    def comer(self):
        print("COMER")
    
    def jugar(self):
        print("JUEGA")

class Animalmanchas(Animal):
    def __init__(self):
        print("PERRO")

objeto=Animal()
objeto.comer()
objeto.jugar()