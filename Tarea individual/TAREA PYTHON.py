acum=0
sumapar=0
i=1
print("INGRESE LA CANTIDAD NUMEROS PARA SUMAR")
n=int(input())
while(i<=n):
    print("INGRESE EL,",i," NUMERO")
    num=int(input())
    acum=acum+num
    if num%2==0:
        sumapar=sumapar+num
    i=i+1
print("LA SUMA TOTAL ES:",acum)
print("LA SUMA TOTAL DE PARES  ES:",sumapar)
