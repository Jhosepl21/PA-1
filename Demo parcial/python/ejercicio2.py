estado=True
acum = 0
while(estado):
  print("Ingrese un numero")
  n = int(input())
  acum = acum + n
  print("Desea agregar otro numero,si o no?")
  resp=str(input())
  if resp=="si":
    estado=True
  else:
    estado=False
   
print("La suma de los numeros es:",acum)   