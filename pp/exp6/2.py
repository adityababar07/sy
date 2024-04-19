# Creating a tuple and adding elements to it

tup = ()

ls = list(tup)

no_of_elements = int(input("Enter the number of elements that you want to enter:\t"))

for _ in range(no_of_elements):
    element = int(input("Enter the element:\t"))
    ls.append(element)

tup = tuple(ls)

# Concatenation
tup1 = (2, 3, 4, 5, 6)
ls2 = list(tup1)
ls += ls2
tup = tuple(ls)

print(f"Tuple after concatenating it with tup1:\t{tup}")

# Using functions
print(f"The maximum element in tup is {max(ls)}")
print(f"The minimum element in tup is {min(ls)}")
print(f"The sum of elements in tup is {sum(ls)}")
print(f"The length of tup is {len(tup)}")
