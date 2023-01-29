class Animal(object):
    
    def ENombre(self,nombre):
        self.nombre=nombre
    
    def Rnombre(self):
        return self.nombre
    
animal=Animal()
animal.ENombre("GATO")
print(animal.Rnombre())