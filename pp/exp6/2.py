# creating tuple and adding elements in it

tup = ()

ls = list(tup)

no_of_elements = int(input("enter the no. of elements that you want to enter :\t"))

for _ in range(no_of_elements):
    element = int(input("enter the element:\t"))
    ls.append(element)

tup = tuple(ls)

# concatenation

tup1 = (2, 3, 4, 5, 6)

ls2 = list (tup1)
ls+= ls2
tup = tuple(ls)

print(f"tup after concatenating it with tup1 :\t {tup}")

# using functions

print(f"the max element in tup is {max(ls)}")

print(f"the min element in tup is {min(ls)}")

print(f"the sum element in tup is {sum(ls)}")

print(f"the len of tup is {len(tup)}")

