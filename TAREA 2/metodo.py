def saludar():
    print("hola mundo")
def CalcularDoble(num):
    res=num*2
    print(res)
def Triplicar(num):
    res=num*3
    print(res)
print("Llamada a la funcion Saludar:")
print("Ingrese un valor numérico para x:")
num=int(input())
print("Llamada a la función CalcularDoble (pasaje por valor)")
print( "El doble de ",num," es ", CalcularDoble(num))
print( "El valor original de x es ",num)
print("Llamada a la función Triplicar (pasaje por referencia)")
print( "El triple es  Triplicar")
Triplicar(num)
print( "El nuevo valor de x es ", num)

	
