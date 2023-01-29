class Carro(object):
    #primer metodo
    def setColor(self,color):
        self.color=color
    
    def getColor(self):
        return self.color

VEHI=Carro()
VEHI.setColor("AMARIILLO")
print(VEHI.getColor())
