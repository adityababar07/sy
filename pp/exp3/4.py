# Find the largest number from 50 randomly generated numbers

from random import randint as rd

num_50 = []

# Generate 50 random numbers and store them in a list
for _ in range(50):
    num_50.append(rd(0, 87956))

# Find the maximum number in the list using the max() function
print(f"Largest number in the 50 numbers is {max(num_50)}.")
