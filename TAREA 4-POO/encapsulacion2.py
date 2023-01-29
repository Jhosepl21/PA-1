class Encapsulamiento:
    variables_1=1  #accsesible
    _varianle_2=2  #cercado o protegido
    __variables_3=3 #privado

    def __init__(self):
       print(self.variables_1)
       print(self._varianle_2)
       print(self.__variables_3)
    
objecto_encapsulamiento=Encapsulamiento()
print(objecto_encapsulamiento.variables_1)
print(objecto_encapsulamiento._varianle_2)
print(objecto_encapsulamiento.__variables_3)