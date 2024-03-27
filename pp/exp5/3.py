from random import randint as rd

a = []

for i in range(20):
    num = rd(10, 100)
    a.append(num)

a.sort()
print(a)

for i in a:
    if i > 20 and i < 50:
        a.remove(i)

print(a)
