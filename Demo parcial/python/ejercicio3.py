print("Cuantos numeros pares desea sumar:")
n = int(input())
sum, cad = 0, ""
for i in range(2, 2 * n + 2, 2):
  cad = cad + " " + str(i)
  sum = sum + i
print(cad)
print(str(sum))