import random
a=[]
b=[]
for i in range(1,11):
    x=random.randint(1,99)
    a.append(x)
print(a)
print(" en orden inverso:")
for i in reversed(a):
 b.append(i)   
print(b)