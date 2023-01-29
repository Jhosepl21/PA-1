class Transporteterrestre:
    def __init__(self):
        print("CONSTRUCCION TRANSPORTE TERRESTRE")
 
    def acelerar(self):
        print("ACELAR TRANSPORTE TERRESTRE")

class Coche(Transporteterrestre):
    def __init__(self):
        print("CONSTRUCTOR DE COCHE")

class Bicileta(Transporteterrestre):
    def __init__(self):
        print("CONTRUCOTR DE BICI")
    
    def acelerar(self):
        print("accelear bici")

objeto_transporte_terrestre=Transporteterrestre()
objeto_transporte_terrestre.acelerar

objeto_coche=Coche()
objeto_coche.acelerar()

objeto_bici=Bicileta()
objeto_bici.acelerar()