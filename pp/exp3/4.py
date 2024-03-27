# largest num from 50 numbers

from random  import randint as rd

num_50 = []

for _ in range(50):
    num_50.append(rd(0, 87956))

print(f"Largest no. in the 50 numbers is {max(num_50)}.")
