acum=0
acumu=0
contapa=0
contaimpa=0
for i in range(10):
    print("Ingrese un numero ",i+1,": ")
    num=int(input())
    if num%2:
        acum+=num
        contapa=contapa+1
    else:
        acumu+=num
        contaimpa=contaimpa+1

print("Media de los pares: ",acum/contapa)
print("Media de los impares: ",acumu/contaimpa)