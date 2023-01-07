estado = True
while (estado):
  print("Ingrese su codigo")
  x = int(input())
  if (x == 1024):
    print("Codigo Correcto")
    estado = False

  else:
    print("Codigo Incorrecto")
    estado = True
estado2=True
while (estado2):
  print("Ingrese su contraseña")
  y = int(input())
  if (y == 4567):
    print("Contraseña Correcta")
    estado2 = False

  else:
    print("Contraseña Incorrecto")
    estado2 = True
