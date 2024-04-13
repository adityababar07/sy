# create tuple

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)

mixed_tuple = (2, "hello", 3.67, 'g', (), (1, 4, 5, 7))

empty_tuple = ()

# accessing elements in tuple
print(f"accessing the 5th element in tuple using index 4: {tuple1[4]}")

# slicing operator
print(f"\nafter slicing the tuple, the result is:- {tuple1[3:7]}")

# removing empty tuple from nested tuple
print(f"\nmixed tuple : {mixed_tuple}")

for i in mixed_tuple:
    if type(i) == tuple:
        if len(i) == 0:
            ls = list(mixed_tuple)
            ls.remove(i)
            mixed_tuple = tuple(ls)

print(f"\nmixed_tuple after removing empty tuple :\t{mixed_tuple}")
