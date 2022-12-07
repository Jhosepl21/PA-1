print("Ingrese la cantidad de datos:")
n=int(input())
acum=0
for i in range(1,n+1):
    print("INGRESA LOS NUMEROS PARA EL PROMEDIO")
    dato=int(input())
    acum=acum+dato
prom=acum/n

print("EL PROMEDIO ES",prom)