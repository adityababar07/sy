
list1 = [1, 2, 3, 'apple', 'banana', 'orange']

list2 = ['jackfruit', 'cherry']

# concatenation

list3 = list1 + list2
print(f"After concatenation {list3}")

# indexing

print(f"\nindex of jackfruit is {list3.index('jackfruit')}")

#accessing

print(f"\nThe element at index 3 in list3 is {list3[3]}")

#pop()

print(f"\nusing the pop function on index 1 , result is :- {list3.pop(1)}")

#insert()

list3.insert(3,"mango")
print(f"list3 after inserting 'mango' :\t {list3}")

# remove()

list3.remove("mango")
print(f"list3 after removing 'mango' :\t {list3}")

# reverse()

list3.reverse()
print(f"list3 after reversing :\t {list3}")

# append()

list3.append("mango")
print(f"list3 after appending 'mango' :\t {list3}")

# sort()

list3.sort()
print(f"list3 after sorting in ascending order :\t {list3}")

list3.sort(reverse=True)
print(f"list3 after sorting in descending order :\t {list3}")

# merge()

list1.merge(list2)
print(f"list1 after merging with list2 :\t {list1}")
