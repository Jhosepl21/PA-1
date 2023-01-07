
from random import randint


num_secreto = randint(0, 10) + 1
print("Adivine el numero (de 1 a 10):")
num_ingresado = int(input())
while num_secreto != num_ingresado:
  if num_secreto > num_ingresado:
    print("Muy bajo")
  else:
    print("Muy alto")

  num_ingresado = float(input())
if num_secreto == num_ingresado:
  print("Exacto! Usted adivino ")
else:
  print("El numero era: ", num_secreto)